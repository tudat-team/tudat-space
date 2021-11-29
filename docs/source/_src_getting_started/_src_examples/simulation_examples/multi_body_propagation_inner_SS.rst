.. _propagating_a_multi_body_system:

Propagating the Inner Solar System Bodies using Multi-Body Propagation
========================================================================

In this example, we will demonstrate a multi-body propagation of a simplified inner solar system model.
Multi-body propagations become necessary when one or more propagated bodies cannot be treated as quasi-massless.
Through their non-negligible mass, the bodies mutually exert accelerations on each other and thereby affecting each
others' future states. In order to consistently simulate the evolution of such a system, the equations of motion of all
massive bodies have to be propagated concurrently in a multi-body propagation.

The code for this example can be found on `github <https://github.com/tudat-team/tudatpy-examples/blob/master/propagation/solar_system_propagation.py>`_.

Import Statements and Setup
###########################

The first lines of code in your script should always be the tudatpy import statements. These import statements allow you to use the tools in tudatpy.

.. code-block:: python

    from tudatpy.util import result2array
    from tudatpy.kernel import constants
    from tudatpy.kernel import numerical_simulation
    from tudatpy.kernel.interface import spice_interface
    from tudatpy.kernel.numerical_simulation import environment_setup, environment
    from tudatpy.kernel.numerical_simulation import propagation_setup, propagation


Important first steps to take are to load the spice kernels and to set the start- and end epochs of your simulation. In Tudat, J2000 is t = 0, with all times given in seconds. Here the simulation is set up to cover 5 Julian years, starting from an arbitrary epoch (1.0e7 s after J2000).

.. code-block:: python

    spice_interface.load_standard_kernels()

    simulation_start_epoch = 1.0e7
    simulation_end_epoch = 1.0e7 + 5.0 * constants.JULIAN_YEAR


Environment Setup
#################

Let's create the environment for the simulation. This setup covers the creation of the major celestial bodies that constitute the inner Solar System.

Create bodies
-------------

Bodies can be created by making a list of strings with the bodies you want to include in your simulation. The default body settings (such as atmosphere, body shape, rotation model) are taken from spice. These settings can be adjusted to your preference, see :ref:`available_environment_models` for more detail. Finally, the system of bodies is created using your settings and stored into the variable ``body_system``.

.. code-block:: python

    bodies_to_create = bodies_to_propagate = [
        "Moon",
        "Earth",
        "Mars",
        "Venus",
        "Mercury",
        "Sun",
    ]

    body_settings = environment_setup.get_default_body_settings(bodies_to_create)
    body_system = environment_setup.create_system_of_bodies(body_settings)



Propagation Setup
#################

Now that the environment is created, the propagation setup has to be defined.
This includes the choice of central bodies. Central bodies are the bodies with respect to which the state of the respective propagated bodies is defined.
In this example we want to demonstrate two variants of setting up the central bodies in a multi-body propagation.
Using a ``for`` statement, we will loop over the simulation setup twice - once for each propagation variant:
In the first variant all bodies are propagated about the same central point, which is chose to be the Solar System Barycentre ("SSB").
The second variant uses a "hierachical" central-body setup, in which each body is propagated around its vicinal "parent body".

.. code-block:: python
    results = {}
    for propagation_variant in ["barycentric", "hierarchical"]:


- **Define Accelerations**

Before tending to the central body setups, we create the acceleration settings.
We use a nested dictionary in which each propagated body ``body_i`` is undergoing ``point_mass_gravity()`` acceleration
from each massive body ``body_j`` so long as ``body_i`` != ``body_j``.

.. code-block:: python

        acceleration_dict = {}
        for body_i in bodies_to_create:
            current_accelerations = {}
            for body_j in bodies_to_create:
                if body_i != body_j:
                    current_accelerations[body_j] = [
                        propagation_setup.acceleration.point_mass_gravity()
                    ]
            acceleration_dict[body_i] = current_accelerations



- **Central Body Setup**

Now to the central body setup. For the "barycentric" variant the procedure is straightforward.
"SSB" is the central body for the propagation of each body and can thus be assigned to every index in the ``central_bodies`` list:

.. code-block:: python

        if propagation_variant == "barycentric":Create acceleration models
            central_bodies = ["SSB"] * len(bodies_to_create)



For the "hierarchical" variant the procedure can be implemented by assigning a pre-selected body to a given index in the ``central_bodies`` list.
Note that with this setup all bodies except the Sun are propagated w.r.t. to a reference body that undergoes propagation itself!

.. code-block:: python

        elif propagation_variant == "hierarchical":
            central_bodies = []
            for body_name in bodies_to_create:
                if body_name == "Moon":
                    central_bodies.append("Earth")
                elif body_name == "Sun":
                    central_bodies.append("SSB")
                else:
                    central_bodies.append("Sun")


- **Create acceleration models**

  With the acceleration settings and the central bodies defined, the acceleration models are created by the code given below.

  .. code-block:: python

        acceleration_models = propagation_setup.create_acceleration_models(
            body_system=body_system,
            selected_acceleration_per_body=acceleration_dict,
            bodies_to_propagate=bodies_to_propagate,
            central_bodies=central_bodies
        )


Define Initial System State
---------------------------

At the beginning of your script, you have defined a simulation start epoch, but you also need to define the initial state of your system.
The ``propagation`` module offers a convenient interface with the ``environment`` module, which allows us to retrieve the initial state of our system using the ``get_initial_state_of_bodies`` function:


.. code-block:: python

        system_initial_state = propagation.get_initial_state_of_bodies(
            bodies_to_propagate=bodies_to_propagate,
            central_bodies=central_bodies,
            body_system=body_system,
            initial_time=simulation_start_epoch)



Create propagator settings
--------------------------

We have defined all the ingredients for the propagator settings. Let's create translational propagator settings for this case. For more details, also for other propagator dynamics, visit :ref:`simulation_propagator_setup`.

.. code-block:: python

        termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)

        propagator_settings = propagation_setup.propagator.translational(
            central_bodies,
            acceleration_models,
            bodies_to_propagate,
            system_initial_state,
            termination_condition,
        )


Create integrator settings
--------------------------

The simulator also required an integrator to be defined. The integrator settings for a Runge-Kutta 4 integrator can be defined as given below. We have chosen to use a step size of 3600.0 s, you might want to change that for your simulation, depending on the type of integrator and propagation time. For more integrator settings, please visit :ref:`simulation_integrator_settings`.

.. code-block:: python

        fixed_step_size = 3600.0
        integrator_settings = propagation_setup.integrator.runge_kutta_4(
            simulation_start_epoch, fixed_step_size
        )

Simulator Usage
###############

Let's simulate our system for the given propagation settings. This is done by creating a dynamics simulator with your bodies, integrator- and propagator settings.
By default, the equations of motion are propagated upon creation of the dynamics simulator. This means that in the very next line the propagation results are accessible through the attributes of the simulator object.

Create dynamics simulator
-------------------------

.. code-block:: python

        dynamics_simulator = numerical_simulation.SingleArcSimulator(
            body_system, integrator_settings, propagator_settings)


Retrieve result
---------------

In our example we are interested in the propagated state history of our system, we retrieve it from the simulator and store it in a dictionary.

.. code-block:: python
      
        results[propagation_variant] = dynamics_simulator.state_history


.. _visualize_results:

Visualize results
#################

Let's make some plots to visualize our simulation results.
We are going to generate two figures, for each propagation variant we will plot the trajectory of each body over the propagation time.
Note that in the hierarchical case the raw output of the propagation cannot be visualised in a single plot,
since some bodies have their propagated state defined w.r.t different bodies.
The results of the hierarchical propagation are therefore split over multiple subplots.

In order to generate plots in python, we import ``pyplot`` from ``matplotlib``.

.. code-block:: python
      
    from matplotlib import pyplot as plt



The only "pre-processing" step required is the conversion of state history dictionaries to arrays for easier processing:

.. code-block:: python
    barycentric_system_state_array = result2array(results['barycentric'])
    hierarchical_system_state_array = result2array(results['hierarchical'])


Then we define a function ``plot_multi_body_system_state_history()`` that facilitates the setup of the two figures:

  .. code-block:: python
        
      def plot_multi_body_system_state_history(system_state_history_array, propagated_bodies, hierarchical=False):

        if hierarchical:

            fig1 = plt.figure(figsize=plt.figaspect(0.3))
            ax1 = fig1.add_subplot(311, projection='3d')
            ax1.set_title(f'Trajectory of the Sun w.r.t SSB')
            ax1.scatter(0, 0, 0, marker='x', label="Sun")

            ax2 = fig1.add_subplot(312, projection='3d')
            ax2.set_title(f'System state evolution w.r.t Sun')
            ax2.scatter(0, 0, 0, marker='x', label="SSB")

            ax3 = fig1.add_subplot(313, projection='3d')
            ax3.set_title(f'Trajectory of the Moon w.r.t Earth')
            ax3.scatter(0, 0, 0, marker='x', label="Earth")


            for i, body in enumerate(propagated_bodies):

                if body == "Sun":
                    ax1.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                             system_state_history_array[:, 6 * i + 3],
                             label=body)

                elif body != "Sun" and body != "Moon":
                    ax2.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                             system_state_history_array[:, 6 * i + 3],
                             label=body)

                elif body == "Moon":
                    ax3.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                             system_state_history_array[:, 6 * i + 3],
                             label=body)

            axs = [ax1, ax2, ax3]
            ax_lims = [[-2.0E9, 2.0E9], [-2.5E11, 2.5E11], [-4.0E8, 4.0E8]]  # equal axis limit per subplot, [m]

            for ax, ax_lim in zip(axs, ax_lims):
                ax.legend()
                ax.set_xlabel('x [m]')
                ax.set_xlim(ax_lim)
                ax.set_ylabel('y [m]')
                ax.set_ylim(ax_lim)
                ax.set_zlabel('z [m]')
                ax.set_zlim(ax_lim)


        else:  # barycentric case

            fig1 = plt.figure(figsize=(8, 6))
            ax1 = fig1.add_subplot(111, projection='3d')
            ax1.set_title(f'System state evolution of all bodies w.r.t SSB.')


            for i, body in enumerate(propagated_bodies):
                ax1.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                         system_state_history_array[:, 6 * i + 3],
                         label=body)
                ax1.scatter(system_state_history_array[0, 6 * i + 1], system_state_history_array[0, 6 * i + 2],
                            system_state_history_array[0, 6 * i + 3],
                            marker='x')

            ax1.scatter(0, 0, 0, marker='x', label="SSB", color='black')
            ax1.legend()
            ax1.set_xlabel('x [m]')
            ax1.set_xlim([-2.5E11, 2.5E11])
            ax1.set_ylabel('y [m]')
            ax1.set_ylim([-2.5E11, 2.5E11])
            ax1.set_zlabel('z [m]')
            ax1.set_zlim([-2.5E11, 2.5E11])

        return fig1


We call our custom plotting function and obtain the visualisation of our propagated system states:

  .. code-block:: python
    figA = plot_multi_body_system_state_history(barycentric_system_state_array, bodies_to_propagate)
    figB = plot_multi_body_system_state_history(hierarchical_system_state_array, bodies_to_propagate, hierarchical=True)
    plt.tight_layout()
    plt.show()


- **Barycentric Propagation Variant**

  .. image:: figures/multi_body_barycentric.png


- **Hierarchical Propagation Variant**

  .. image:: figures/multi_body_hierarchical.png
  











