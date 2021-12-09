.. _observationSimulation:

Observation Simulation
======================

Having defined the :ref:`observation models <_observationModelSetup>`, you can now simulate actual observations to use in your analysis. If you are using Tudat for analysis or real data, you can skip this part, and move to TODO

.. _observationTypes:

Defining observation simulation settings
----------------------------------------

There are various manner in which to define how to simulate observations. The most straightforward approach is to define a list of times at which an observation is to be simulated, which is the case that will be considered on this page, for the purpose of showcasing the various addititonal options available to define observations to be simulated.

The following block of code defines settings to define a single set of observations

.. code-block:: python
                
    one_way_nno_mex_link_ends = dict( );
    one_way_nno_mex_link_ends[ transmitter ] = ( "Earth", "NNO" );
    one_way_nno_mex_link_ends[ receiver ] = ( "MeX", "" );
    
    observation_times = list( )
    observation_times = ...
    
    observation_simulation_settings = observation_setup.tabulated_settings( 
       one_way_range_type
       one_way_nno_mex_link_ends,
       observation_times )
       
Which will define a settings object to simulate a one-way range observable, with the given link ends (uplink from NNO Earth-based station to MeX spacecraft), at the list of time specified by ``observation_times``. By default, the reference time for the one-way range observable is the ''receiver''. This means that, if we would have ``observation_times = [10.0, 20.0, 30.0]``, these settings will simulate observations which are *received* by MeX at t=10, t=20, and t=30, respectively. To override this behaviour, we can specify a reference link end manually:

.. code-block:: python
    
    observation_simulation_settings = observation_setup.tabulated_settings( 
       one_way_range_type
       one_way_nno_mex_link_ends,
       observation_times,
       reference_link_end = observation_setup.transmitter )

which will yield observations *transmitted* at t=10, t=20, and t=30 by NNO. Note that the choice of reference link ends also influences the formulation of the partial derivatives used in the estimation. 

As an extension of the above, you can also use:

.. code-block:: python
    
    observation_simulation_settings_list = observation_setup.tabulated_settings_list( 
       link_ends_per_observable,
       observation_times )
 
where the ``link_ends_per_observable`` is TODO. Instead of creating a single object to simulate observations, it contains a list of objects, for any number of observable types and link ends.

Defining additional settings
----------------------------

In addition to defining the observable type, link ends, observation times and (optionally) reference link ends for simulating an observation, you can define a number of additional settings to be taken into account:

- **Constraints**: You can define settings such that an observation is only simulated if certain conditions (elevation angle, no occultation, *etc.*) are met
- **Noise levels**: You can define a functions which adds (random) noise to the simulated observations. This noise is typically, but not necesarilly, Gaussian
- **Defining additional output**: Similarly to the state propagation framework, you can define a wide range of *dependent variables* to be calculating during the simulation of observations. Note that the *type* of variables you can choose from is distinct from those available during state proagation.

Typically, these settings are defined and added to the observation simulation settings *after* the nominal settings have been defined. To this end, there are several functions available in Tudat, which take a list of observation simulation settings objects (such as those returned by the :func:`~tudatpy.tabulated_settings_list` function), and you can add additional setting of the above type to:

- Each ``ObservationSimulationSettings`` object in the list
- Each ``ObservationSimulationSettings`` object in the list which contains settings for a given :func:`~tudatpy.ObservableType`
- Each ``ObservationSimulationSettings`` object in the list which contains settings for a given :func:`~tudatpy.ObservableType` and a given set of link ends.

Defining observation constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In many cases, you will not have the full list of observation times *a priori*. Instead, the observation times could be a function of the states of the link ends, and depend on a number of constraints that must be satisfied for an observation to be possible. We have termed such constraints 'observation viability settings', and we have currently implemented the following types:

- **Minimum_elevation_angle**: Minimum elevation angle at a ground station: target must be at least a certain elevation above the horizon.
- **Body avoidance angle**: the line-of-sight vector from a link end to a given third body must have an angle w.r.t. the line-of-sight between link ends that is sufficiently large. This constraint is typically used to prevent the Sun from being too close to the field-of-view of the telescope(s).
- **Body occultation**: the link must not be obscured by a given third body. For instance: the Moon occulting a link between Earth and Mars.

As an example, 

.. code-block:: python
    
    station_id = [ "Earth", "NNO" ];
    
    single_viability_settings = observation_setup.elevation_angle_viability( 
       station_id,
       np.deg2rad( 15 ) )
 
 
elevation_angle_viability

Defining noise levels
^^^^^^^^^^^^^^^^^^^^^

If no noise is defined, the observations are simulated according to the determininistic model that has been defined in the :ref:`observationModelSetup`. We stress that this 'noise-free' observation can contain a simulated bias, if such a bias is included in the observation model settings. By adding noise settings, a user can add random noise to the simulations of the observations. We currently have two interfaces for this:

- **Gaussian noise**: By specifying the standard deviation, you can add uncorrelated, zero-mean Gaussian noise to the observations
- **Generic noise**: By specifying an arbitrary function that generates noise (as a function of time), a user can add noise from any type of distribution to the simulated observations


Defining additional output
^^^^^^^^^^^^^^^^^^^^^^^^^^

As is the case with the state propagation (add link TODO), you can define any number of dependent variable to be saved along with the observations. These include distances between link ends, angles between link ends, and a variety of other options. Note that this functionality is relatively new, and the list of implemented dependent variables is currently limited. A full list of options can be found in TODO
