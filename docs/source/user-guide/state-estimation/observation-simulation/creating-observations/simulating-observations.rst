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

    from tudatpy.estimation.observations_setup import observations_simulation_settings
    from tudatpy.estimation.observable_models_setup import links
    
    one_way_nno_mex_link_ends = dict()
    one_way_nno_mex_link_ends[links.transmitter] = links.body_reference_point_link_end_id("Earth", "NNO")
    one_way_nno_mex_link_ends[links.receiver] = links.body_origin_link_end_id("MeX")
    one_way_nno_mex_link_definition = links.link_definition(one_way_nno_mex_link_ends)
    
    observation_times = [10.0, 20.0, 30.0]
    
    observation_simulation_settings = observations_simulation_settings.tabulated_simulation_settings(
        links.one_way_range_type,
        one_way_nno_mex_link_definition,
        observation_times
    )

By default, the *reference time* for the one-way range observable is the receiver. This means that the above settings will simulate observations that are *received* by MeX at :math:`t=10`, :math:`t=20`, and :math:`t=30`, respectively.

Reference Link End
------------------

To override this behaviour, we can specify a reference link end manually, which will yield observations *transmitted* at :math:`t=10`, :math:`t=20`, and :math:`t=30` by NNO:

.. code-block:: python

    observation_simulation_settings = observations_simulation_settings.tabulated_simulation_settings(
        links.one_way_range_type,
        one_way_nno_mex_link_definition,
        observation_times,
        reference_link_end=links.transmitter
    )

Multiple Observables
--------------------

As an extension of the above, you can also use :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings_list`. This function contains a list of objects, for any number of observable types and link ends (stored together in the ``link_definitions_per_observable`` below):

.. code-block:: python

    observation_simulation_settings_list = observations_simulation_settings.tabulated_simulation_settings_list(
        link_definitions_per_observable,
        observation_times
    )

.. note::
   The :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings` is the simplest manner in which to define the times (and other settings) at which to simulate observations. By adding observation constraints (see below), this list of times may be filtered during the observation simulation process to only retain those times at which specific conditions are met (e.g. target above the horizon). For many practical cases, it is desirable to have continuous tracking passes of a given length that are not interrupted by such constraints. The :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.continuous_arc_simulation_settings` can be used to achieve such behaviour.

.. _additional_observation_settings:

Defining Additional Settings
=============================

In addition to defining the observable type, link ends, observation times and (optionally) reference link ends for simulating an observation, you can (or, in some cases, need to) define a number of additional settings to be taken into account:

- **Ancillary settings**: Some observables may require additional data that influences the calculation of the observation (integration time, frequency band, transponder delay, etc.). See the :ref:`tudatpy:ancillary_settings` module for details and options to create/add ancillary settings.
- **Constraints**: You can define settings such that an observation is only simulated if certain conditions (elevation angle, no occultation, *etc.*) are (not) met. See the :ref:`tudatpy:viability` module for details and options to create/add observation constraints.
- **Noise levels**: You can define functions which adds (random) noise to the simulated observations. This noise is typically, but not necessarily, Gaussian. See the :ref:`tudatpy:random_noise` module for details and options to add noise models to observation simulation settings.
- **Additional output**: Similarly to the state propagation framework, you can define a wide range of *dependent variables* to be calculating during the simulation of observations. Note that the *type* of variables you can choose from is distinct from those available during state propagation. See the :ref:`tudatpy:observations_dependent_variables` module for options to add additional outputs to observation simulation settings. A more detailed description on how to extract the computed dependent variables after observation simulation can be found :ref:`here <observation_dependent_variables_usage>`

Typically (but not necessarily), these settings are defined and added to the observation simulation settings *after* the nominal settings have been defined (in the process outlined above). To efficiently achieve this, there are several functions available in Tudat, which take a list of :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` objects (such as those returned by the :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings_list` function), and add settings for one of the above options to any number of observation simulation settings.

For each of the above type of (optional) settings, three separate functions are provided to modify the list of observation simulation settings (see module-level documentation links above for details):

- One function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list (for instance: regardless of the type or link end of the observation, always save the light-time as dependent variable)
- One function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list which contains settings for a given :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType` (for instance: regardless of link ends, use 1 mm/s random noise for all two-way Doppler observables)
- One function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list which contains settings for a given :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType` **and** a given link definition (for instance: for all one-way range observables between New Norcia ground station and Mars Express, only simulate an observation if Mars Express is at least 15 degrees above the horizon).

Creating the Observations
==========================

.. _observation_simulation:

Simulating the Observations
----------------------------

Having fully defined the list of observation simulation settings ``observation_simulation_settings``, as well as the ``observation_simulators`` (see :func:`~tudatpy.estimation.observable_models_setup.create_observation_simulators`), the actual observations can be simulated as follows:

.. code-block:: python

    from tudatpy.estimation.observations_setup.observations_wrapper import simulate_observations
    
    simulated_observations = simulate_observations(
        observation_simulation_settings,
        observation_simulators,
        bodies
    )

where ``bodies`` is the usual :class:`~tudatpy.dynamics.SystemOfBodies` object that defines the physical environment (see :ref:`environment_setup` for details on creation and usage). The :func:`~tudatpy.estimation.observations_setup.observations_wrapper.simulate_observations` function returns an object of the :class:`~tudatpy.estimation.observations.ObservationCollection`.