.. _simulating_observations:

=======================
Simulating Observations
=======================

To simulate observations, you must first define the "Observation Simulation Settings," which specify *how* and *when* an observation model should be used.

.. note::
   In Tudat, we distinguish between "Observation Model Settings" (which define the software block that computes the observations) and "Observation Simulation Settings" (which define how to use the model, e.g., at which time, with which reference link end, etc.).

Defining Observation Simulation Settings
=========================================

Basic Settings
--------------

The basic manner in which to define an observation simulation settings object uses the :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings`, specifying the observation times explicitly as follows:

.. code-block:: python

    from tudatpy.estimation import observations_setup
    
    one_way_nno_mex_link_ends = dict()
    one_way_nno_mex_link_ends[transmitter] = observations_setup.links.body_reference_point_link_end_id("Earth", "NNO")
    one_way_nno_mex_link_ends[receiver] = observations_setup.links.body_origin_link_end_id("MeX")
    one_way_nno_mex_link_definition = observations_setup.links.link_definition(one_way_nno_mex_link_ends)
    
    observation_times = [10.0, 20.0, 30.0]
    
    observation_simulation_settings = observations_setup.observations_simulation_settings.tabulated_simulation_settings(
        one_way_range_type,
        one_way_nno_mex_link_definition,
        observation_times
    )

By default, the *reference time* for the one-way range observable is the receiver. This means that the above settings will simulate observations that are *received* by MeX at :math:`t=10`, :math:`t=20`, and :math:`t=30`, respectively.

Reference Link End
------------------

To override this behaviour, we can specify a reference link end manually, which will yield observations *transmitted* at :math:`t=10`, :math:`t=20`, and :math:`t=30` by NNO:

.. code-block:: python

    observation_simulation_settings = observations_setup.observations_simulation_settings.tabulated_simulation_settings(
        one_way_range_type,
        one_way_nno_mex_link_definition,
        observation_times,
        reference_link_end=observations_setup.links.LinkEndType.transmitter
    )

Multiple Observables
--------------------

As an extension of the above, you can also use :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings_list`. This function contains a list of objects, for any number of observable types and link ends (stored together in the ``link_definitions_per_observable`` below):

.. code-block:: python

    observation_simulation_settings_list = observations_setup.observations_simulation_settings.tabulated_simulation_settings_list(
        link_definitions_per_observable,
        observation_times
    )

.. note::
   The :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings` is the simplest manner in which to define the times (and other settings) at which to simulate observations. By adding observation constraints (see below), this list of times may be filtered during the observation simulation process to only retain those times at which specific conditions are met (e.g. target above the horizon). For many practical cases, it is desirable to have continuous tracking passes of a given length that are not interrupted by such constraints. The :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.continuous_arc_simulation_settings` can be used to achieve such behaviour.

.. _additional_observation_settings:

Defining Additional Settings
=============================

In addition to defining the observable type, link ends, observation times and (optionally) reference link ends for simulating an observation, you can (or, in some cases, need to) define a number of additional settings to be taken into account:

- **Ancillary settings**: Some observables may or must get additional quantitative data that influences the ideal value of the observable. Examples are the integration time for averaged Doppler observables, and retransmission times for n-way observables.
- **Constraints**: You can define settings such that an observation is only simulated if certain conditions (elevation angle, no occultation, *etc.*) are (not) met.
- **Noise levels**: You can define functions which adds (random) noise to the simulated observations. This noise is typically, but not necessarily, Gaussian.
- **Additional output**: Similarly to the state propagation framework, you can define a wide range of *dependent variables* to be calculating during the simulation of observations. Note that the *type* of variables you can choose from is distinct from those available during state propagation.

Typically (but not necessarily), these settings are defined and added to the observation simulation settings *after* the nominal settings have been defined (in the process outlined above). To efficiently achieve this, there are several functions available in Tudat, which take a list of :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects (such as those returned by the :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings_list` function), and add settings for one of the above options to any number of observation simulation settings.

For each of the above type of (optional) settings, three separate functions are provided to modify the list of observation simulation settings:

- One function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list (for instance: regardless of the type or link end of the observation, always save the light-time as dependent variable)
- One function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list which contains settings for a given :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType` (for instance: regardless of link ends, use 1 mm/s random noise for all two-way Doppler observables)
- One function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list which contains settings for a given :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType` **and** a given link definition (for instance: for all one-way range observables between New Norcia ground station and Mars Express, only simulate an observation if Mars Express is at least 15 degrees above the horizon).

.. _ancilliary_settings:

Ancillary Settings
------------------

Some observation models can depend on data in addition to that normally contained in either the observation model of the observation simulation settings to fully determine the value of the observable. In some cases, these data *may* be defined, in other cases they *must* be defined. At present, the following ancillary settings are supported:

- **Integration time**: This is required for each averaged Doppler observable. A value of 60 s is set by default. The integration time defines the time over which the observable is to be averaged.
- **Retransmission delays**: This is optional for each N-way observable. It is undefined by default. The retransmission delays quantify how much time elapses between the reception and retransmission of a signal at one of the retransmitter link ends.

For example, to set a 5s Doppler integration time for every averaged n-way Doppler observable:

.. code-block:: python

    from tudatpy.estimation import observations_setup
    
    integration_time = 5.0
    doppler_ancillary_settings = observations_setup.ancillary_settings(integration_time=integration_time)
    observations_setup.add_ancillary_settings_to_observable(
        observation_simulation_settings_list,
        doppler_ancillary_settings,
        observations_setup.model_settings.dsn_n_way_averaged_doppler
    )

Similar interfaces exist to add ancillary settings to all observations (the :func:`~tudatpy.estimation.observations_setup.ancillary_settings.add_ancillary_settings_to_all` function), or to add the settings to observation simulation settings of a given observable **and** a given link definition (the :func:`~tudatpy.estimation.observations_setup.ancillary_settings.add_ancillary_settings_to_observable_for_link_ends` function).

.. _observation_constraints:

Defining Observation Constraints
---------------------------------

In many cases, whether an observation at a given time should be realized will depend on a number of constraints that must be satisfied. We have termed such constraints 'observation viability settings', and we have currently implemented the following types:

- **Minimum elevation angle**: Minimum elevation angle at a ground station: target must be at least a certain elevation above the horizon (see :func:`~tudatpy.estimation.observations_setup.viability.elevation_angle_viability`).
- **Body avoidance angle**: The line-of-sight vector from a link end :math:`A` to a given third body must have an angle w.r.t. the line-of-sight between link end :math:`A` and any other link ends that it observed that is sufficiently large. This constraint is typically used to prevent the Sun from being too close to the field-of-view of the telescope(s) (see :func:`~tudatpy.estimation.observations_setup.viability.body_avoidance_viability`).
- **Body occultation**: The link must not be obscured by a given third body. For instance: the Moon occulting a link between Earth and Mars (see :func:`~tudatpy.estimation.observations_setup.viability.body_occultation_viability`).

For example, the ``observation_simulation_settings_list`` list created in the example above can be modified such that only observations above a 15 degree elevation angle at New Norcia are accepted:

.. code-block:: python

    station_id = ["Earth", "NNO"]
    viability_settings_list = list()
    viability_settings_list.append(
        observations_setup.viability.elevation_angle_viability(
            station_id,
            np.deg2rad(15.0)
        )
    )
    observations_setup.viability.add_viability_check_to_all(
        observation_simulation_settings_list,
        viability_settings_list
    )

In this case (the :func:`~tudatpy.estimation.observations_setup.viability.add_viability_check_to_all` function), the list of settings in ``viability_settings_list`` is applied to *all* observation simulation settings in ``observation_simulation_settings_list``. To only add the viability settings to observation simulation settings of a given type of observable, or only to those of a given observable **and** a given link definition, use the :func:`~tudatpy.estimation.observations_setup.viability.add_viability_check_to_observable` and :func:`~tudatpy.estimation.observations_setup.viability.add_viability_check_to_observable_for_link_ends` functions, respectively.

To add viability settings directly to a single :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object, use the :attr:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings.viability_settings_list` attribute.

.. _noise_levels:

Defining Noise Levels
---------------------

If no noise is defined, the observations are simulated according to the deterministic model that has been defined in the :ref:`observationModelSetup`. We stress that this 'noise-free' observation can contain a simulated bias, if such a bias has been included in the observation model settings (see :ref:`observationTypes`).

By adding noise settings, a user can add (typically, but not necessarily) random noise to the simulation of the observations. We currently have two types of interfaces for adding noise to an observation:

- **Gaussian noise**: By specifying the standard deviation, you can add uncorrelated, zero-mean Gaussian noise to the observations
- **Generic noise**: By specifying an arbitrary function that generates noise (as a function of time), a user can add noise from any type of distribution to the simulated observations

Adding Gaussian noise to all observations of a given type can be done by:

.. code-block:: python

    noise_level = 0.1
    observations_setup.random_noise.add_gaussian_noise_to_observable(
        observation_simulation_settings_list,
        noise_level,
        observations_setup.model_settings.one_way_range_type
    )

which will add 10 cm random noise to each one-way range observable in the ``observation_simulation_settings_list`` list. In this case (the :func:`~tudatpy.estimation.observations_setup.random_noise.add_gaussian_noise_to_observable` function), the noise is applied to all observations of a given type. To add the noise to observation simulation settings of all observables, or only to those of a given observable **and** a given link definition, use the :func:`~tudatpy.estimation.observations_setup.random_noise.add_gaussian_noise_to_all` and :func:`~tudatpy.estimation.observations_setup.random_noise.add_gaussian_noise_to_observable_for_link_ends` functions, respectively.

Similar interfaces exist to add a generic noise function to the observation:

.. code-block:: python

    def custom_noise_function(current_time):
        return np.array([np.random.lognormal(0.0, 1.0)])
    
    observations_setup.random_noise.add_noise_function_to_observable(
        observation_simulation_settings_list,
        custom_noise_function,
        observations_setup.model_settings.one_way_range_type
    )

where it is important to realize that the noise function *must* have a single float representing time as input, and returns a vector (of the size of a single observation) as output. For many observables (range, Doppler), this size will be 1. For angular position observables, for instance, the size will be 2. The :func:`~tudatpy.estimation.observations_setup.random_noise.add_noise_function_to_all`, :func:`~tudatpy.estimation.observations_setup.random_noise.add_noise_function_to_observable` and :func:`~tudatpy.estimation.observations_setup.random_noise.add_noise_function_to_observable_for_link_ends` functions can be used to add a noise function to a subset of all observation simulation settings.

To add a generic noise function directly to a single :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object, use the :attr:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings.noise_function` attribute.

.. _observation_dependent_variables:

Defining Additional Output
---------------------------

As is the case with the state propagation (see :ref:`here<dependent_variables>`), you can define any number of dependent variable to be saved along with the observations. These include distances between link ends, angles between link ends, and a variety of other options. Note that this functionality is relatively new, and the list of implemented dependent variables is currently limited. A full list of options can be found in the API documentation.

Creating the Observations
==========================

.. _observation_simulation:

Simulating the Observations
----------------------------

Having fully defined the list of observation simulation settings ``observation_simulation_settings``, as well as the ``observation_simulators`` (see :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.create_observation_simulators`), the actual observations can be simulated as follows:

.. code-block:: python

    from tudatpy.estimation import observations_setup
    
    simulated_observations = observations_setup.observations_wrapper.simulate_observations(
        observation_simulation_settings,
        estimator.observation_simulators,
        bodies
    )

where ``bodies`` is the usual :class:`~tudatpy.dynamics.environment.SystemOfBodies` object that defines the physical environment (see :ref:`environment_setup` for details on creation and usage). The :func:`~tudatpy.estimation.observations_setup.observations_wrapper.simulate_observations` function returns an object of the :class:`~tudatpy.estimation.observations.ObservationCollection`.
