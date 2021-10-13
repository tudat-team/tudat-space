.. _propagating_variational_equations:

Propagating Variational Equations
===========================================

In this example, we will propagate variational equations. Furthermore, we demonstrate how to calculate changes to the vehicle's state.

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

    bodies.get( "Delfi-C3").set_constant_mass( 400.0 )

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
              propagation_setup.acceleration.cannonball_radiation_pressure(),
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
              propagation_setup.acceleration.cannonball_radiation_pressure(),
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
      
    earth_gravitational_parameter = bodies.get( "Earth" ).gravitational_parameter

    initial_state = conversion.keplerian_to_cartesian(
        gravitational_parameter = earth_gravitational_parameter,
        semi_major_axis = 7500.0E3,
        eccentricity = 0.1,
        inclination = np.deg2rad(85.3),
        argument_of_periapsis = np.deg2rad(235.7),
        longitude_of_ascending_node = np.deg2rad(23.4),
        true_anomaly = np.deg2rad(139.87)
    )

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

Create list of parameters
-------------------------

Now we will create a list of parameters for which the variational equations are to be propagated. For the following example we will add the gravitational parameter of Earth, the drag coefficient of the spacecraft (Delfi-C3) and the radiation pressure coefficient of the spacecraft.

.. code-block:: python

  parameter_settings = estimation_setup.parameter.initial_states( propagator_settings, bodies )
  
  parameter_settings.append( estimation_setup.parameter.gravitational_parameter( "Earth" ) )
  parameter_settings.append( estimation_setup.parameter.constant_drag_coefficient( "Delfi-C3" ) )
  parameter_settings.append( estimation_setup.parameter.radiation_pressure_coefficient( "Delfi-C3" ) )

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

Let's simulate our vehicle for the given epochs. This is done by creating a variational equations solver with your bodies, integrator- and propagator settings and the parameter settings.

Create dynamics simulator
-------------------------

.. code-block:: python
      
    variational_equations_solver = estimation_setup.SingleArcVariationalSimulator(
    bodies, integrator_settings, propagator_settings, estimation_setup.create_parameters_to_estimate( parameter_settings, bodies ),
    integrate_on_creation=1 )

.. note::

  The ``integrate_on_creation=1`` argument is given to ensure that equations are being integrated once the ``variational_equations_solver`` object is constructed. If you use ``integrate_on_creation=0``, you will have to call the integration of the variational equations manually.

Retrieve result
---------------

You can retrieve the states, state transition matrices and sensitivity matrices at each time step in your simulation by using ``.state_history``, ``.state_transition_matrix_history`` and ``sensitivity_matrix_history``, respectively, on the variational equations solver object.

.. code-block:: python
      
    states = variational_equations_solver.state_history
    state_transition_matrices = variational_equations_solver.state_transition_matrix_history
    sensitivity_matrices = variational_equations_solver.sensitivity_matrix_history


The state transition matrix and sensitivty matrix are the start and end can be requested as follows:

.. code-block:: python

    print(
      f"""
        Initial State Transition Matrix: \n{
            sensitivity_matrices[list(sensitivity_matrices.keys())[0]]}
        Initial Sensitivity Matrix: \n{
            state_transition_matrices[list(state_transition_matrices.keys())[0]] }

        Final State Transition Matrix \n{
            state_transition_matrices[list(state_transition_matrices.keys())[-1]] }
        Final Sensitivity Matrix \n{
            sensitivity_matrices[list(sensitivity_matrices.keys())[-1]] }
      """
    )

Which results in the following print statement:

.. code-block:: 

    Initial State Transition Matrix: 
    [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]
    Initial Sensitivity Matrix: 
      [[1. 0. 0. 0. 0. 0.]
       [0. 1. 0. 0. 0. 0.]
       [0. 0. 1. 0. 0. 0.]
       [0. 0. 0. 1. 0. 0.]
       [0. 0. 0. 0. 1. 0.]
       [0. 0. 0. 0. 0. 1.]]

    Final State Transition Matrix 
    [[ 1.17145804e+02  5.41485791e+01  3.67012126e+01 -2.98224153e+04 -6.02486101e+02  1.42838537e+05]
     [ 6.15826205e+01  2.79502410e+01  1.93683317e+01 -1.60634242e+04 8.48686311e+02  7.49012456e+04]
     [ 1.32896097e+02  6.13560690e+01  4.26745211e+01 -3.33918198e+04 7.93578452e+01  1.63555814e+05]
     [-1.08498064e-01 -4.96323749e-02 -3.35592225e-02  2.81832264e+01 5.50420314e-01 -1.32375020e+02]
     [-3.30846489e-02 -1.59631342e-02 -1.01606433e-02  8.92132366e+00 -2.11974552e-01 -4.05618770e+01]
     [ 1.40311628e-01  6.47611785e-02  4.45610274e-02 -3.58780763e+01 -2.25111499e-02  1.72902539e+02]]
    Final Sensitivity Matrix 
    [[-1.73337573e-06 -1.08193214e+03 -5.23922129e+00]
     [-9.08585461e-07 -5.68109655e+02 -1.66646264e+00]
     [-1.96654984e-06 -1.24318022e+03 -1.29704649e+00]
     [ 1.59705773e-09  9.84074569e-01  3.91340440e-03]
     [ 4.89694722e-10  3.01777330e-01  1.71593373e-03]
     [-2.08675300e-09 -1.28562397e+00 -9.45425963e-04]]


Visualize results
#################

Let's make some plots to visualize our simulation results. In order to make plots in python, import pyplot from matplotlib.

.. code-block:: python
      
    from matplotlib import pyplot as plt


- **Change in state**

  The changes in state for each epoch are calculated using the state transition matrix. We define an initial state deviation of 1 m in x-position and 1 mm/s in x-velocity as follows:

  .. code-block:: python

    initial_state_deviation = [1, 0, 0, 1.0E-3, 0, 0]

  Next, we calculate the change in state for each time by looping over the dictionary entries of ``state_transition_matrices``, and store each result in another dictionary:

  .. code-block:: python 

    delta_states_dict = dict()

    for epoch in state_transition_matrices:

      delta_states_dict[epoch] = np.dot(state_transition_matrices[epoch], initial_state_deviation)


  Now we extract the relevant variables stored in the dictionaries. The times are stored in the keys, and can be extracted using the ``.keys( )`` function. The actual states (or state deviations) are in the values of the dictionary, and we use ``.values( )`` to extract these, and subsequently stack them vertically using ``np.vstack( )`` in order to select the desired columns.



  .. code-block:: python
        
      time = state_transition_matrices.keys( )

      delta_states = np.vstack( list( delta_states_dict.values( ) ) )



  We also convert the time axis to be in the units of hours instead of seconds, which is optional. For this, we make use of *list comprehensions* in python:

  .. code-block:: python

      time_hours = [ t / 3600 for t in time]

  .. note::

    Using

    .. code-block:: python

      time_hours = time / 3600

    will **not** work in python, it will result in an ``TypeError``.

  We want to plot the magnitude of the deviation in position and the deviation in velocity. The ``delta_states`` is used to calculate the magnitude of these vectors.

  .. code-block:: python

    delta_r = np.sqrt( delta_states[:,0] ** 2 + delta_states[:,1] ** 2 + delta_states[:,2] ** 2 )
    delta_v = np.sqrt( delta_states[:,3] ** 2 + delta_states[:,4] ** 2 + delta_states[:,5] ** 2 )

  Which are subsequently plotted as given by the following piece of code (For more details, visit :ref:`visualize_results`.

  .. code-block:: python

      plt.figure( figsize=(17,5))
      plt.grid()
      plt.plot(time_hours, delta_r)
      plt.xlabel('Time [hr]')
      plt.ylabel('$\Delta r (t_1)$ [m]')
      plt.xlim( [min(time_hours), max(time_hours)] )

      plt.figure( figsize=(17,5))
      plt.grid()
      plt.plot(time_hours, delta_v)
      plt.xlabel('Time [hr]')
      plt.ylabel('$\Delta v (t_1)$ [m/s]')
      plt.xlim( [min(time_hours), max(time_hours)] )

  Which results in the following figures:

  .. image:: figures/delta_r.png

  .. image:: figures/delta_v.png












