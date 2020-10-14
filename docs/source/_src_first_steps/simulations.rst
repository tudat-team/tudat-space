********************************
Getting Started with Simulations
********************************

Setting up basic simulations in the ``tudat`` API can be summarised into the
three fundamental procedural steps:

1. `Environment Setup`_
2. `Propagation Setup`_
3. `Simulator Usage`_

.. note::
    More advanced simulations that involve parameter estimation are not covered
    entirely by the following guide.

Propagating a Spacecraft with Perturbations
===========================================

Import Statements and Setup
###########################

The first lines of code in your script should always be the (``tudatpy``) import statements. These import statements allow you to use the tools in ``tudatpy``.

.. code-block:: python

    import numpy as np
    from tudatpy.kernel import constants
    from tudatpy.kernel.interface import spice_interface
    from tudatpy.kernel.simulation import environment_setup
    from tudatpy.kernel.simulation import propagation_setup
    from tudatpy.kernel.astro import conversion

Important first steps to take are to (1) load the spice kernels, and (2) to set the start- and end epochs of your simulation. In ``tudat``, J2000 is t = 0, with all times given in seconds. The simulation end epoch is set to be one Julian day, which equals 86400 s.

.. code-block:: python

    spice_interface.load_standard_kernels()

    simulation_start_epoch = 0.0
    simulation_end_epoch = constants.JULIAN_DAY



Environment Setup
#################

Let's create the environment for your simulation. This setup covers the creation of (celestial) bodies, vehicle(s), and environment interfaces.

Create bodies
-------------

Bodies can be created by making a list of strings with the bodies you want to include in your simulation. The default body settings (such as atmosphere, body shape, rotation model) are taken from spice. These settings can be adjusted to your preference, see :ref:`available_environment_models` for more detail. Finally, the system of bodies is created using your settings and stored into the variable ``bodies``. 

.. code-block:: python
  
    bodies_to_create = ["Sun", "Earth", "Moon", "Mars", "Venus"]

    body_settings = environment_setup.get_default_body_settings(
        bodies_to_create,
        simulation_start_epoch,
        simulation_end_epoch,
        "Earth","J2000")

    bodies = environment_setup.create_system_of_bodies(body_settings)


Create vehicle
--------------

Now it's time to create your vehicle. In the following code, a vehicle named *Delfi-C3* is made, with a body mass of 400 kg.

.. code-block:: python
  
    bodies.create_empty_body( "Delfi-C3" )

    bodies.get_body( "Delfi-C3").set_constant_mass( 400.0 )

Create interfaces
-----------------

Interfaces define the interaction of the environment on the vehicle. This step is important for later defining accelerations that are dependent on
parameters defining the nature of the interaction. Below the aerodynamics coefficients interface and the radiation pressure interface are defined. For all the options, visit :ref:`available_environment_models`.

- **Aerodynamic Coefficients**
  


  .. code-block:: python
    
      reference_area = 4.0
      drag_coefficient = 1.2

      aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
          reference_area,[drag_coefficient,0,0],
          are_coefficients_in_aerodynamic_frame=True,
          are_coefficients_in_negative_axis_direction=True
      )

      environment_setup.add_aerodynamic_coefficient_interface(
                  bodies, "Delfi-C3", aero_coefficient_settings )


- **Radiation Pressure**

  .. code-block:: python

      reference_area_radiation = 4.0
      radiation_pressure_coefficient = 1.2
      occulting_bodies = ["Earth"]
      radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
          "Sun", reference_area_radiation, radiation_pressure_coefficient, occulting_bodies
      )

      environment_setup.add_radiation_pressure_interface(
                  bodies, "Delfi-C3", radiation_pressure_settings )


Propagation Setup
#################

Now that the environment is created, the propagation setup is defined. First, the bodies to be propagated and the central bodies will be defined, as given below.

.. code-block:: python

    bodies_to_propagate = ["Delfi-C3"]

    central_bodies = ["Earth"]

Create acceleration models
--------------------------

This is the place to define the accelerations acting on your vehicle, and create the acceleration models for propagation. For our vehicle, the *Delfi-C3*, we want the cannonball radiation pressure and aerodynamic accelerations as given by the interfaces defined above. Furthermore, gravitational accelerations are also defined; a spherical harmonic gravity exerted by Earth up to degree and order 5, and a point mass (central) gravity for the other celestial bodies.

- **Define Accelerations**

  .. code-block:: python

      accelerations_settings_delfi_c3 = dict(
          Sun=
          [
              propagation_setup.acceleration.cannon_ball_radiation_pressure_(),
              propagation_setup.acceleration.point_mass_gravity()
          ],
          Earth=
          [
              propagation_setup.acceleration.spherical_harmonic_gravity(5, 5),
              propagation_setup.acceleration.aerodynamic()
          ],
          Moon=
          [
              propagation_setup.acceleration.point_mass_gravity()
          ],
          Mars=
          [
              propagation_setup.acceleration.point_mass_gravity()
          ],
          Venus=
          [
              propagation_setup.acceleration.point_mass_gravity()
          ]
          )


  .. note::
    
    A more compact way of adding a point mass gravity of all bodies *except* a small selection, such as Earth in this case, can be done using the ``.difference()`` function in python. The same accelerations can be added in a more elegant manner, as given below:

    .. code-block:: python

        accelerations_settings_delfi_c3 = dict(
          Sun=
          [
              propagation_setup.acceleration.cannon_ball_radiation_pressure_(),
          ],
          Earth=
          [
              propagation_setup.acceleration.spherical_harmonic_gravity(5, 5),
              propagation_setup.acceleration.aerodynamic()
          ]
          )
        
        for other in set(bodies_to_create).difference( { "Earth" } ):
          accelerations_settings_delfi_c3[other] = 
          [
              propagation_setup.acceleration.point_mass_gravity()
          ]


- **Create acceleration models**

  With the accelerations defined, the acceleration models are created by the code given below.

  .. code-block:: python
        
      acceleration_settings = {"Delfi-C3": accelerations_settings_delfi_c3}

      acceleration_models = propagation_setup.create_acceleration_models(
          bodies,
          acceleration_settings,
          bodies_to_propagate,
          central_bodies)


Define Initial System State
---------------------------

At the beginning of your script, you have defined a simulation start epoch, but you also need to define the initial state of your vehicle. For this case, we define a point along a Kepler orbit around Earth to be the initial state of *Delfi-C3*, and subsequently transform it to a Cartesian state using the ``conversion.keplerian_to_cartesian()`` function. Obviously, we need the gravitational parameter of our central body, Earth, which we can retrieve from the ``bodies`` variable.

.. code-block:: python
      
    earth_gravitational_parameter = bodies.get_body( "Earth" ).gravitational_parameter

    initial_state = conversion.keplerian_to_cartesian(
        gravitational_parameter = earth_gravitational_parameter,
        semi_major_axis = 7500.0E3,
        eccentricity = 0.1,
        inclination = np.deg2rad(85.3),
        argument_of_periapsis = np.deg2rad(235.7),
        longitude_of_ascending_node = np.deg2rad(23.4),
        true_anomaly = np.deg2rad(139.87)
    )


Define dependent variables to save
----------------------------------

Apart from the state history, you can specify certain dependent variables to be saved, which you can later use for analysis. For *Delfi-C3*, we want to save the total acceleration, Keplerian state and latitude and longitude, which we will plot later. Here is a list of all the :ref:`available_dependent_variables`.

.. code-block:: python
      
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
        propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" )
        ]



Create propagator settings
--------------------------

We have defined all the ingredients for the propagator settings. Let's create translational propagator settings for this case. For more detailes, also for other propagator dynamics, visit :ref:`simulation_propagator_setup`.

.. code-block:: python
      
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_state,
        simulation_end_epoch,
        output_variables = dependent_variables_to_save
    )


Create integrator settings
--------------------------

The simulator also required an integrator to be defined. The integrator settings for a Runge-Kutta 4 integrator can be defined as given below. We have chosen to use a step size of 10.0 s, you might want to change that for your simulation, depending on the type of integrator and propagation time. For more integrator settings, please visit :ref:`simulation_integrator_settings`.

.. code-block:: python
      
    fixed_step_size = 10.0

    integrator_settings = propagation_setup.integrator.runge_kutta_4(
        simulation_start_epoch,
        fixed_step_size
    )

Simulator Usage
###############

Let's simulate our vehicle for the given epochs. This is done by creating a dynamics simulator with your bodies and integrator- and propagator settings.

Create dynamics simulator
-------------------------

.. code-block:: python
      
    dynamics_simulator = propagation_setup.SingleArcDynamicsSimulator(
        bodies, integrator_settings, propagator_settings)

Retrieve result
---------------

You can retrieve the states and dependent variables at time step in your simulation by using ``.state_history`` and ``.dependent_variable_history``, respectively, on the dynamics simulator object.

.. code-block:: python
      
    states = dynamics_simulator.state_history

    dependent_variables = dynamics_simulator.dependent_variable_history

Visualize results
-----------------
