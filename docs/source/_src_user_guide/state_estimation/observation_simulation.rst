.. _observationSimulation:

Observation Simulation
======================

Having defined the :ref:`observation models <_observationModelSetup>`, you can now simulate actual observations to use in your analysis. If you are using Tudat for analysis or real data, go to (TODO create page), and move to :ref:`runningEstimation`

.. _observationTypes:

Defining observation simulation settings
----------------------------------------

In addition to the definition of the observation model, simulating the observations themselves requires a definition of the time(s) at which the observation is to be simulated, as well as a definition of which observation model these are to be simulated from. The basic manner in which to define these uses the :func:`~tudatpy.numerical_simulation.estimation_setup.observation.tabulated_settings`, specifying the observation times explicitly as follows:

.. code-block:: python
                
    one_way_nno_mex_link_ends = dict( );
    one_way_nno_mex_link_ends[ transmitter ] = ( "Earth", "NNO" );
    one_way_nno_mex_link_ends[ receiver ] = ( "MeX", "" );
    one_way_nno_mex_link_definition = estimation_setup.observation.link_definition( one_way_nno_mex_link_ends )
    
    observation_times = list( )
    observation_times = [10.0, 20.0, 30.0]
    
    observation_simulation_settings = observation_setup.tabulated_settings( 
       one_way_range_type
       one_way_nno_mex_link_definition,
       observation_times )
       
where a list of times (:math`t=10,20,30` s) is explicitly specified, and an observation simulation settings object is created, which specifies that a one-way range observation is to be simulated at these times, with the link ends specified by ``one_way_nno_mex_link_definition``.

By default, the reference time for the one-way range observable is the receiver (see TODO). This means that, for th above, these settings will simulate observations which are *received* by MeX at t=10, t=20, and t=30, respectively. To override this behaviour, we can specify a reference link end manually:

.. code-block:: python
    
    observation_simulation_settings = observation_setup.tabulated_settings( 
       one_way_range_type
       one_way_nno_mex_link_ends,
       observation_times,
       reference_link_end = observation_setup.transmitter )

which will yield observations *transmitted* at t=10, t=20, and t=30 by NNO. 

As an extension of the above, you can also use:

.. code-block:: python
    
    observation_simulation_settings_list = observation_setup.tabulated_settings_list( 
       link_definitions_per_observable,
       observation_times )
 
where the ``link_ends_per_observable`` is TODO. Instead of creating a single object to simulate observations, it contains a list of objects, for any number of observable types and link ends.

Defining additional settings
----------------------------

In addition to defining the observable type, link ends, observation times and (optionally) reference link ends for simulating an observation, you can define a number of additional settings to be taken into account:

- **Constraints**: You can define settings such that an observation is only simulated if certain conditions (elevation angle, no occultation, *etc.*) are (not) met (using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.tabulated_settings`)
- **Noise levels**: You can define a functions which adds (random) noise to the simulated observations. This noise is typically, but not necesarilly, Gaussian
- **Defining additional output**: Similarly to the state propagation framework, you can define a wide range of *dependent variables* to be calculating during the simulation of observations. Note that the *type* of variables you can choose from is distinct from those available during state proagation.

Typically, these settings are defined and added to the observation simulation settings *after* the nominal settings have been defined (in the process outlined above). To this end, there are several functions available in Tudat, which take a list of ``ObservationSimulationSettings``  objects (such as those returned by the :func:`~tudatpy.tabulated_settings_list` function), and you can add additional setting of the above types to (TODO add examples):

- Each ``ObservationSimulationSettings`` object in the list (for instance: regardless of the type or link end of the observation, always save the light-time as dependent variable)
- Each ``ObservationSimulationSettings`` object in the list which contains settings for a given :func:`~tudatpy.ObservableType` (for instance: regardless of link ends, use 1 mm/s random noise for all two-way Doppler observables)
- Each ``ObservationSimulationSettings`` object in the list which contains settings for a given :func:`~tudatpy.ObservableType` and a given set of link ends (for instance: for all one-way range observables between New Norcia ground station and Mars Express, only simulate an observation if Mars Express is at last 15 degrees abov the horizon.

Defining observation constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In many cases, you will not have the full list of observation times *a priori*. Instead, the observation times could be a function of the states of the link ends, and depend on a number of constraints that must be satisfied for an observation to be possible. We have termed such constraints 'observation viability settings', and we have currently implemented the following types:

- **Minimum_elevation_angle**: Minimum elevation angle at a ground station: target must be at least a certain elevation above the horizon (see :func:`~tudatpy.numerical_simulation.estimation_setup.observation.elevation_angle_viability`).
- **Body avoidance angle**: the line-of-sight vector from a link end to a given third body must have an angle w.r.t. the line-of-sight between link ends that is sufficiently large. This constraint is typically used to prevent the Sun from being too close to the field-of-view of the telescope(s),  (see :func:`~tudatpy.numerical_simulation.estimation_setup.observation.body_avoidance_viability`)
- **Body occultation**: the link must not be obscured by a given third body. For instance: the Moon occulting a link between Earth and Mars (see :func:`~tudatpy.numerical_simulation.estimation_setup.observation.(see :func:`~tudatpy.numerical_simulation.estimation_setup.observation.body_occultation_viability`)`)

For example, the ``observation_simulation_settings`` list created in the example above can be modified such that only observations above a 15 degree elevation angle at New Norcia (for those observations in which New Norcia is a ground station) are accepted:

.. code-block:: python
    
    station_id = [ "Earth", "NNO" ];    
    single_viability_settings = estimation_setup.observation.elevation_angle_viability( 
       station_id,
       np.deg2rad( 15.0 ) )
    observation.add_viability_check_to_settings(
      observation_simulation_settings,
      [single_viability_settings] )

 
Defining noise levels
^^^^^^^^^^^^^^^^^^^^^

If no noise is defined, the observations are simulated according to the determininistic model that has been defined in the :ref:`observationModelSetup`. We stress that this 'noise-free' observation can contain a simulated bias, if such a bias is included in the observation model settings (see :ref:`observationTypes`). By adding noise settings, a user can add random noise to the simulations of the observations. Random noise is defined by a probability distribution, which is used to generate random noise during the propagation. We currently have two interfaces for this:

- **Gaussian noise**: By specifying the standard deviation, you can add uncorrelated, zero-mean Gaussian noise to the observations
- **Generic noise**: By specifying an arbitrary function that generates noise (as a function of time), a user can add noise from any type of distribution to the simulated observations

Adding Gaussian noise to all observations of a given type can be done by:

.. code-block:: python
    
    noise_level = 1.0E-3 / constants.SPEED_OF_LIGHT
    observation.add_gaussian_noise_to_settings(
        observation_simulation_settings,
        noise_level,
        observation.one_way_doppler_type )
        
which will add 1 mm/s random noise to each one-way Doppler observable


Defining additional output
^^^^^^^^^^^^^^^^^^^^^^^^^^

As is the case with the state propagation (see :ref:`here<dependent_variables>`), you can define any number of dependent variable to be saved along with the observations. These include distances between link ends, angles between link ends, and a variety of other options. Note that this functionality is relatively new, and the list of implemented dependent variables is currently limited. A full list of options can be found in TODO

Simulating the observations
---------------------------

Having fully defined the list of observation simulation settings ``observation_simulation_settings``, as well as the ``observation_simulators`` (see :ref:`observationSimulatorCreation`), the actual observations can be simulated as follows:

.. code-block:: python

    simulated_observations = estimation.simulate_observations(
        observation_simulation_settings,
        estimator.observation_simulators,
        bodies)
        
where the ``bodies`` is the usual ``SystemOfBodies`` object that defines the physical environment (see :ref:`environment_setup` for details on creation and usage). The :func:`~tudatpy.numerical_simulation.estimation.observation.simulate_observations` function returns an object of :class:`~tudatpy.numerical_simulation.estimation.observation.ObservationCollection` type, which stores all observations and dependent variables

Analyzing the simulated observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
