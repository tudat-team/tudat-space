.. _basic_estimation:

Simulated state estimation - basic example
==========================================

In this tutorial, we will show how to simulate tracking observables, and use these observations to estimate the state of a spacecraft, as well as a variety of physical parameters of the environment. The estimation framework in Tudat has a broad variety of features, and we only cover the basic aspects here. A tutorial of more extensive features is given on the page TODO.  The code for this example can be found on `github <https://github.com/tudat-team/tudatpy-examples/blob/master/propagation/perturbed_satellite_orbit.py>`_. TODO update.

The general scenario we use here will be:

* Simulated tracking data: two-way Doppler data from a single ground station located in Delft
* Determination of the dynamics of the Delfi-C3 spacecraft 
* Determination of radiation pressure coefficient and drag coefficient



Environment and State Propagation Settings
##########################################

As you can see in the code, setting up the environment is done in the same manner as the previous tutorials: a set of celestial bodies is created, as well as a vehicle, which is endowed with radiation pressure and aerodynamic properties. In addition, settings for the accelerations, integrator and propagator are defined.

To perform the estimation, we make a single extension to the environment, defining a ground station on Earth. Ground stations serve as reference points from which observations can be performed.

.. code-block:: python

    # Define station coordindates
    station_altitude = 10.0
    delft_latitude =  np.deg2rad( 52.00667 )
    delft_longitude = np.deg2rad( 4.35556 )
    position_element_type = element_conversion.geodetic_position_type
    
    # Create station
    station_name = 'TrackingStation'
    environment_setup.add_ground_station(
        bodies.get_body('Earth'),
        station_name,
        [station_altitude, delft_latitude, delft_longitude],
        position_element_type )

In this instance, the station's position is defined by its geodetic position (altitude, geodetic latitude and longitude). See :func:`~tudatpy.add_ground_station' for alternative options.

Defining parameters to estimate 
###############################

To perform an estimation, we need to define the list of parameters that should be estimated.  Her we consider:

* The spacecraft initial state :math:`\mathbf{x}_{0}`
* The spacecraft drag coefficient :math:`C_{D}`
* The spacecraft radiation pressure coefficient :math:`C_{r}`

Defining these parameters is done as follows:

.. code-block:: python

     # Create list of parameters that are to be estimated
    parameter_settings = estimation_setup.parameter.initial_states( propagator_settings, bodies )
    parameter_settings.append( estimation_setup.parameter.constant_drag_coefficient("Delfi-C3") )
    parameter_settings.append( estimation_setup.parameter.radiation_pressure_coefficient("Delfi-C3") )
    
The first entry defines the estimation of initial states which correspond exactly to the propagator settings. Here, we propagate Delfi-C3 over a single arc, so the above defines that we also *estimate* Delfi-C3 over a single arc. A full list of all parameters that can be estimated is found TODO. An example in which the dynamics is propagated in a multi-arc manner is found in TODO.

Defining observation models
###########################

In this simulation, we'll be limiting ourselves to a single type of observable (one-way Doppler) from a single ground station. We define the settings for this observation as follows:

.. code-block:: python

    # Define upink link ends for one-way observable
    link_ends = dict()
    link_ends[ observations.transmitter ] = ( 'Earth', 'TrackingStation')
    link_ends[ observations.receiver ] = ( 'Delfi-C3', '' )

    # Create observation settings for each link/observable
    observation_settings_list = [ observations.one_way_open_loop_doppler(link_ends) ]
    
Creating the estimation object
##############################

To perform the estimation, we now create an :class:`~tudatpy.Estimator` object.

.. code-block:: python

    estimator = numerical_simulation.Estimator(
        bodies, parameter_set, observation_settings_list, integrator_settings,
        propagator_settings )
        
The ``estimator`` object contains within it an object of type ``VariationalSolver`` (see TODO), and upon creation of the ``estimator``, the dynamics and variational equations automatically get propagated. The objects that propagated the variational equations and dynamics can be extracted by:

.. code-block:: python

    variational_equations_simulator = estimator.variational_solver
    dynamics_simulator = variational_equations_simulator.dynamics_simulator
    
In addition, creating the ``estimator`` also creates objects which can simulate observations, as per the model settings defined in the ``observation_settings_list``. The resulting :class:`~tudatpy.ObservationSimulator` objects can be extracted by:

.. code-block:: python

    observation_simulators = estimator.observation_simulators

These objects are then used in the next step, to simulate the observations 
    
Simulating the observations
###########################

Now, we can simulate the observations, having propagated the dynamics of the spacecraft, and having defined the observation model. For this example, we will simulate an observation once every 60 s, if the spacecraft is more than 10 degrees above the horizon.

To this end, we first create a list of *potential* observation times by:

.. code-block:: python

    # Define observation simulation times for each link
    observation_times = np.arange( simulation_start_epoch, simulation_end_epoch, 60.0 )
    observation_simulation_settings = observations.tabulated_simulation_settings(
        observations.one_way_doppler_type,
        link_ends,
        observation_times )
        
This defines settings to create a one-way Doppler observable from the TrackingStation to Delfi-C3 every 60 seconds. To add the constraint that the tracking station should be visible, we add a so-called 'viability setting':

.. code-block:: python

    # Create viability settings
    viability_setting = observations.elevation_angle_viability( ["Earth", "TrackingStation"], np.deg2rad( 15 ) )
    observations.add_viability_check_to_settings(
        [ observation_simulation_settings ],
        [ viability_setting ]
    )

The observations are then simulated by:

.. code-block:: python

    # Simulate required observation
    simulated_observations = observations.simulate_observations(
        [ observation_simulation_settings ],
        estimator.observation_simulators,
        bodies )
        
Performing the estimation
#########################

What now remains is inputing the simulated observations to the ``estimator``. But, before we do so, we should modify our 'current guess' of the parameters that we want to estimate. Otherwise, our estimation residuals after the first iteration will all be 0!. We can do this in several ways, here we choose to do so directly when creating the :class:`~tudatpy.PodInput` class:

.. code-block:: python

    pod_input = estimation.PodInput(
        simulated_observations, parameter_set.parameter_set_size,
        apriori_parameter_correction = initial_parameter_deviation )
    pod_input.define_estimation_settings(
        reintegrate_variational_equations = False )
        
The second line (calling the ``define_estimation_settings`` function) allows us to modify certain settings of the estimation procedure. Here, we modify a single one: we override the default setting of re-integrating the variational equations after each iteration.

Since we only use a single observable and a single set of link ends, and no *a priori* covariance, we do not need to set any weights for the estimation to properly converge. But, we do need to set weights for the formal error to be properly computed. The one-way Doppler observable is dimensionless in Tudat (velocity divided by speed of light). So, if we assume a noise level of 1 mm/s in range-rate, the observable noise level :math:`sigma_{h}` should be :math:`0.001/c`. Since the diagonals of the weights should be :math:`1/sigma_{h}^{2}`, the weights should be set at:

.. code-block:: python

    # Define weights
    noise_level = 1.0E-3 / constants.SPEED_OF_LIGHT
    weights_per_observable = \
        { estimation_setup.observations.one_way_doppler_type, noise_level ** -2 }
    pod_input.set_constant_weight_per_observable(  weights_per_observable )


Now, we are ready to perform the estimaion:

.. code-block:: python

    pod_output = estimator.perform_estimation( pod_input )





























