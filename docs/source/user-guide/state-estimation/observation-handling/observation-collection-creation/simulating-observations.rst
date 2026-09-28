.. _simulating_observations:

=======================
Simulated Observations
=======================

To create an observation collection with simulated observations, you need to define the "Observation Model Settings" and the "Observation Simulation Settings".
The former define the type of observable to simulate and the observation geometry; the latter specify when and how to simulate observations.
In this section we cover the creation of the observation *simulation* settings, while the setup of the observation model is covered in :ref:`observationModelSetup`.

Defining Observation Simulation Settings
=========================================

Basic Settings
--------------

The basic manner in which to define an observation simulation settings object uses the :func:`~tudatpy.estimation.observations_setup.observations_simulation_settings.tabulated_simulation_settings`, specifying the observation times explicitly as follows:

.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links, model_settings
    from tudatpy.estimation.observations_setup import observations_simulation_settings

    # Define link ends
    one_way_nno_mex_link_ends = {
        links.LinkEndType.transmitter: links.body_reference_point_link_end_id(
            "Earth", "NNO"
        ),
        links.LinkEndType.receiver: links.body_origin_link_end_id("MeX"),
    }
    one_way_nno_mex_link_definition = links.link_definition(one_way_nno_mex_link_ends)

    observation_times = [10.0, 20.0, 30.0]

    observation_simulation_settings = (
        observations_simulation_settings.tabulated_simulation_settings(
            model_settings.ObservableType.one_way_range_type,
            one_way_nno_mex_link_definition,
            observation_times,
        )
    )

By default, the *reference time* for the one-way range observable is the receiver. This means that the above settings will simulate observations that are *received* by MeX at :math:`t=10`, :math:`t=20`, and :math:`t=30`, respectively.

To override this behaviour, we can specify a reference link end manually, which will yield observations *transmitted* at :math:`t=10`, :math:`t=20`, and :math:`t=30` by NNO:

.. code-block:: python

    observation_simulation_settings = (
        observations_simulation_settings.tabulated_simulation_settings(
            model_settings.ObservableType.one_way_range_type,
            one_way_nno_mex_link_definition,
            observation_times,
            reference_link_end_type=links.LinkEndType.transmitter
        )
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

- ``add_***_to_all``: Function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list. For instance,  regardless of the type or link end of the observation, always save the light-time as dependent variable.
- ``add_***_to_observable``: Function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list which contains settings for a given :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType`. For instance, regardless of link ends, use 1 mm/s random noise for all two-way Doppler observables.
- ``add_***_to_observable_for_link_ends``: Function modifying each :class:`~tudatpy.estimation.observations_setup.observations_simulation_settings.ObservationSimulationSettings` object in the list which contains settings for a given :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservableType` **and** a given link definition. For instance, for all one-way range observables between New Norcia ground station and Mars Express, only simulate an observation if Mars Express is at least 15 degrees above the horizon.

.. _observation_simulation:

Simulating the Observations
===========================

Having fully defined the list of observation simulation settings ``observation_simulation_settings``, as well as the ``observation_simulators`` (see the guide on :ref:`observationSimulators`), the actual observations can be simulated as follows:

.. code-block:: python

    from tudatpy.estimation.observations_setup.observations_wrapper import simulate_observations
    
    bodies = ...
    observation_simulators = ...
    observation_simulation_settings = ...

    simulated_observations = simulate_observations(
        observation_simulation_settings,
        observation_simulators,
        bodies
    )

where ``bodies`` is the usual :class:`~tudatpy.dynamics.environment.SystemOfBodies` object that defines the physical environment (see :ref:`environment_setup` for details on creation and usage).
The :func:`~tudatpy.estimation.observations_setup.observations_wrapper.simulate_observations` function returns an object of the :class:`~tudatpy.estimation.observations.ObservationCollection` that can be manipulated further (see :ref:`observation_collection_manipulation`) or used directly in an estimation (see :ref:`estimationSettings`).
