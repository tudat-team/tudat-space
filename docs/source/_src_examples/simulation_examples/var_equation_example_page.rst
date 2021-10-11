.. _propagating_variational_equations:

Propagating Variational Equations
===========================================


In this example, we will propagate variational equations and show how to use the resulting state transition & sensitivity matrices to propagate variations through the orbiter's state.


Basic Setup
###########################
Again, we are considering the Delfi-C3 Earth orbiter.
The basic setup of the problem is therefore identical to that of the first minimal usecase of :ref:`propagating_a_spacecraft_with_perturbations`:

*  Import Statements and Setup

    - import tudatpy kernels
    - setting up spice kernels

*  Environment Setup

    - creating bodies
    - creating vehicles
    - creating interfaces

*  Propagation Setup

    - creating acceleration models
    - defining initial system state
    - setting dependent variables to save
    - creating propagator settings
    - creating integrator setting


After the basic problem setup, we will add the extensions that are specific to the variational equations use case.
Instead of a dynamics simulator, a variational equations solver object is used for the propagation of the orbiter state and the variational equations w.r.t the user-defined variational parameters.
Next, the history of state transition & sensitivity matrices is retrieved from the variational equations solver object.
At last they are used to propagate variations of selected parameters and to assess their impact on the orbiter's trajectory.


Simulator Usage
###########################


Setting variational parameters
------------------------------

Now we will create a list of parameters for which the variational equations are to be propagated.
First, the initial state(s) of the propagated object(s) are set as "parameters". This is done via the ``.initial_states( )`` method, which constructs the corresponding variational equations from the ``propagator_settings`` and ``bodies``.
The propagation of the variational equations w.r.t the initial state(s) results in the history of a state transition matrix.
The gravitational parameter of Earth and the drag coefficient of the spacecraft (Delfi-C3) are added to that same ``parameter_settings`` list.
The propagation w.r.t. these parameters will result in the history of a sensitivity matrix.


.. code-block:: python

    parameter_settings = estimation_setup.parameter.initial_states( propagator_settings, bodies )

    parameter_settings.append( estimation_setup.parameter.gravitational_parameter( "Earth" ) )
    parameter_settings.append( estimation_setup.parameter.constant_drag_coefficient( "Delfi-C3" ) )

Create dynamics simulator
-------------------------

The dynamics simulator in this use case is a ``SingleArcVariationalSimulator`` object.
It propagates the variational equations specified by ``estimation_setup.create_parameters_to_estimate()`` alongside the dynamics of the orbiter as specified in ``propagator_settings``.

.. code-block:: python

    variational_equations_solver = numerical_simulation.SingleArcVariationalSimulator(
        bodies, integrator_settings, propagator_settings, estimation_setup.create_parameters_to_estimate( parameter_settings, bodies ),
        integrate_on_creation=1 )

.. note::

  The ``integrate_on_creation=1`` argument is given to ensure that equations are being integrated once the ``variational_equations_solver`` object is constructed. If you use ``integrate_on_creation=0``, you will have to call the integration of the variational equations manually.


Retrieve results
----------------

You can retrieve the states, state transition matrices and sensitivity matrices at each time step in your simulation by using ``.state_history``, ``.state_transition_matrix_history`` and ``sensitivity_matrix_history``, respectively, on the variational equations solver object.

.. code-block:: python

    states = variational_equations_solver.state_history
    state_transition_matrices = variational_equations_solver.state_transition_matrix_history
    sensitivity_matrices = variational_equations_solver.sensitivity_matrix_history




Propagating Variations
###########################

Define variations
-------------
Before putting the state transition / sensitivity matrices to work, you have to create the variation of the vehicle state and available parameters that you want to assess.
In this example we will chose an initial state variation in x-position and x-velocity. We define this variation in a vector of the same size as the vehicle state, such that it is compatible with the state transition matrix.
We will also create vectors for the variation of the two available parameters - Earth standard gravitational parameter and vehicle drag coefficient.
Since we want to assess the variations independently from one another, we define them in separate vectors which match the parameter indices in the sensitivity matrix.

.. code-block:: python

    initial_state_variation = [1, 0, 0, 1.0E-3, 0, 0]
    earth_standard_param_variation = [-2.0E+5, 0.0]
    drag_coeff_variation = [0.0, 0.05]


Compute impact on orbiter trajectory
-------------
Using the dot product between state transition / sensitivity matrix and the initial state / parameter variation vector, the change of the orbiter trajectory is computed at every simulation epoch.
The changes are stored in separate dictionaries.

.. code-block:: python

    delta_initial_state_dict = dict()
    earth_standard_param_dict = dict()
    delta_drag_coeff_dict = dict()

    for epoch in state_transition_matrices:
        delta_initial_state_dict[epoch] = np.dot(state_transition_matrices[epoch], initial_state_variation)
        earth_standard_param_dict[epoch] = np.dot(sensitivity_matrices[epoch], earth_standard_param_variation)
        delta_drag_coeff_dict[epoch] = np.dot(sensitivity_matrices[epoch], drag_coeff_variation)


Visualise Impact
###########################

Let's make some plots to visualize our simulation results. In order to make plots in python, import pyplot from matplotlib and adjust some settings for our purposes.

.. code-block:: python

    from matplotlib import pyplot as plt
    font_size = 20
    plt.rcParams.update({'font.size': font_size})



- **Pre-processing**

Now we extract the relevant variables stored in the dictionaries. The times are stored in the keys, and can be extracted using the ``.keys( )`` function.
Using *list comprehensions* in python, you can convert them to more convenient units for your plots.
The actual states (or state deviations) are in the values of the dictionary, and we use ``.values( )`` to extract these, and subsequently stack them vertically using ``np.vstack( )`` in order to select the desired columns.

.. code-block:: python

    time = state_transition_matrices.keys()
    time_hours = [t / 3600 for t in time]

    delta_initial_state = np.vstack(list(delta_initial_state_dict.values()))
    delta_earth_standard_param = np.vstack(list(earth_standard_param_dict.values()))
    delta_drag_coefficient = np.vstack(list(delta_drag_coeff_dict.values()))



- **Magnitude of state deviation**

For each of the three variations, we want to plot the magnitude of the deviation in position and the deviation in velocity.

.. code-block:: python

    # 1 // due to initial state variation
    delta_r1 = np.linalg.norm( delta_initial_state[:, 0:3], axis = 1 )
    delta_v1 = np.linalg.norm( delta_initial_state[:, 3:7], axis = 1 )

    # 2 // due to gravitational parameter variation
    delta_r2 = np.linalg.norm( delta_earth_standard_param[:, 0:3], axis = 1 )
    delta_v2 = np.linalg.norm( delta_earth_standard_param[:, 3:7], axis = 1 )

    # 3 // due to drag coefficient variation
    delta_r3 = np.linalg.norm( delta_drag_coefficient[:, 0:3], axis = 1 )
    delta_v3 = np.linalg.norm( delta_drag_coefficient[:, 3:7], axis = 1 )



- **Create and save figures**

The magnitudes of the state deviations are subsequently plotted as given by the following piece of code (For more details, visit :ref:`visualize_results`).

.. code-block:: python

    # Plot deviations of position
    plt.figure( figsize=(17,5))
    plt.grid()
    plt.plot(time_hours, delta_r1, color='tomato', label='variation initial state')
    plt.plot(time_hours, delta_r2, color='orange', label='variation grav. parameter (Earth)')
    plt.plot(time_hours, delta_r3, color='cyan', label='variation drag coefficient')
    plt.yscale('log')
    plt.xlabel('Time [hr]')
    plt.ylabel('$\Delta r (t_1)$ [m]')
    plt.xlim( [min(time_hours), max(time_hours)] )
    plt.legend()
    plt.savefig(fname='position_deviation.png', bbox_inches='tight')

    # Plot deviations of speed
    plt.figure( figsize=(17,5))
    plt.grid()
    plt.plot(time_hours, delta_v1, color='tomato', label='variation initial state')
    plt.plot(time_hours, delta_v2, color='orange', label='variation grav. parameter (Earth)')
    plt.plot(time_hours, delta_v3, color='cyan', label='variation drag coefficient')
    plt.yscale('log')
    plt.xlabel('Time [hr]')
    plt.ylabel('$\Delta v (t_1)$ [m/s]')
    plt.xlim( [min(time_hours), max(time_hours)] )
    plt.legend()
    plt.savefig(fname='velocity_deviation.png', bbox_inches='tight')

Which results in the following figures:

.. image:: figures/position_deviation.png

.. image:: figures/velocity_deviation.png
