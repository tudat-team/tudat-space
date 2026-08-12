.. _observation_dependent_variables_usage:

=============================
Using Dependent Variables
=============================

Observation dependent variables (e.g., elevation angle, range distance) can be calculated and stored alongside observations. These dependent variables are calculated when the observations are computed, and are stored alongside the observation values and epochs. They can be especially useful to gain insight into the observation geometry and thus facilitate the residual and estimation analyses. A list of available dependent variable types is given on our `API documentation <https://py.api.tudat.space/en/latest/estimation/observations_setup/observations_dependent_variables.html>`_.

Adding Dependent Variables
===========================

Most of these factory functions take some link ends information as (optional) inputs, more precisely the type and link end ID of both ends of the link. However, to limit the overhead on the user's side, an observation dependent variable settings can be created without specifying anything about which link end(s) to consider. For a given single observation set, multiple settings will then be automatically created for all possible link ends combinations.

Defining Settings for All Link Ends
------------------------------------

As an example, let us assume that an observation collection only contains observations matching the following three-way link ends with "Station1" as transmitter and "Station2" as receiver:

.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links
    
    link_ends = dict()
    link_ends[links.LinkEndType.transmitter] = links.body_reference_point_link_end_id("Earth", "Station1")
    link_ends[links.LinkEndType.reflector1] = links.body_origin_link_end_id("MRO")
    link_ends[links.LinkEndType.receiver] = links.body_reference_point_link_end_id("Earth", "Station2")

We will now illustrate two different ways to define dependent variable settings, taking the elevation angle as an example. In the first approach, the user does not specify anything about which link end(s) to focus on:

.. code-block:: python

    from tudatpy.estimation.observations_setup import observations_dependent_variables
    
    observation_collection = ...

    elevation_angle_settings_1 = observations_dependent_variables.elevation_angle_dependent_variable()
    observation_collection.add_dependent_variable(elevation_angle_settings_1, bodies)

Since no particular link ends information is given, the above lines of code will ultimately lead to the automatic creation of two elevation angle settings:

- The elevation angle of MRO as seen from Station1, at transmitter time
- The elevation angle of MRO as seen from Station2, at receiver time

Defining Settings for Specific Link Ends
-----------------------------------------

Alternatively, the user can explicitly specify for which link end the elevation angle should be computed, as follows:

.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links
    from tudatpy.estimation.observations_setup import observations_dependent_variables
    
    elevation_angle_settings_2 = observations_dependent_variables.elevation_angle_dependent_variable(
        link_end_type=links.LinkEndType.transmitter
    )
    # or
    elevation_angle_settings_2 = observations_dependent_variables.elevation_angle_dependent_variable(
        link_end_id=links.body_reference_point_link_end_id("Earth", "Station1")
    )

Both options above lead to the creation of a single elevation dependent variable (elevation of MRO as seen by the transmitting station "Station1").

Adding Settings to the Observation Collection
----------------------------------------------

Once the observation dependent variable settings are defined, they need to be added to the observation collection:

.. code-block:: python

    observation_collection = ...

    elevation_angle_parser = observation_collection.add_dependent_variable(elevation_angle_settings, bodies)

Within the observation collection, the :meth:`~tudatpy.estimation.observations.ObservationCollection.add_dependent_variable` method will add the desired dependent variable to all single observation sets for which it can be defined. It must be noted that this method returns an observation parser that defines for which single observation set the specified dependent variable could be created. This can be useful to isolate the observation sets for which elevation angle values will be available:

.. code-block:: python

    # Retrieve the single observation sets for which the elevation angle will be defined
    elevation_angle_sets = observation_collection.get_single_observation_sets(elevation_angle_parser)

The :meth:`~tudatpy.estimation.observations.ObservationCollection.add_dependent_variable` method can also take a parser as an additional input. If provided, this implies that the dependent variable settings will only be added to the observation sets for which they can be defined (as already mentioned above) but which also fulfill the parsing condition. As an example:

.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links, model_settings
    from tudatpy.estimation.observations_setup import observations_dependent_variables
    from tudatpy.estimation.observations.observations_processing import observation_parser
    
    observation_collection = ...

    elevation_angle_settings = observations_dependent_variables.elevation_angle_dependent_variable(
        link_end_type=links.LinkEndType.transmitter,
        link_end_id=links.body_reference_point_link_end_id("Earth", "Station1")
    )
    elevation_angle_parser = observation_collection.add_dependent_variable(
        elevation_angle_settings,
        bodies,
        observation_parser(model_settings.ObservableType.one_way_range_type)
    )

In the above lines of code, the elevation angle is only added to observation sets containing ``one_way_range`` data with Station1 as the transmitting station.

Computing Dependent Variable Values
====================================

After adding the dependent variable settings to the observation collection, the dependent variable values have however not been computed yet. This requires the call to the :func:`~tudatpy.estimation.observations.compute_residuals_and_dependent_variables` function. To compute the observation dependent variable values requires accessing the link ends times and states at the required observation epochs and thus simulating the observations, which is what this function performs:

.. code-block:: python

    from tudatpy.estimation.observations import compute_residuals_and_dependent_variables
    
    observation_collection = ...

    compute_residuals_and_dependent_variables(
        observation_collection,
        observation_simulators,
        bodies
    )

When to Add Dependent Variables
--------------------------------

The above describes how to add dependent variable settings to the observation collection and compute their values **after the observation collection has been created**. This is the way to go when creating an observation collection by :ref:`loading real data files <loading_real_data>`.

However, when creating an observation collection from :ref:`simulated data <simulating_observations>`, the desired dependent variable settings can be directly added to the observation simulation settings. The corresponding dependent variable values will then be computed alongside the simulated observations **upon the observation collection creation**:

.. code-block:: python

    from tudatpy.estimation.observations_setup import observations_dependent_variables
    from tudatpy.estimation.observations_setup.observations_wrapper import (
        simulate_observations,
    )

    observation_simulation_settings = ...
    observation_simulators = ...

    # Create list of dependent variable settings
    elevation_angle_settings = ...
    dependent_variables_list = [elevation_angle_settings, ...]

    # Add dependent variable settings to observation simulation settings
    observations_dependent_variables.add_dependent_variables_to_all(
        observation_simulation_settings, dependent_variables_list, bodies
    )

    # When simulating the observations, the dependent variables are automatically calculated too
    observation_collection = simulate_observations(
        observation_simulation_settings, observation_simulators, bodies
    )

Retrieving Dependent Variables
===============================

When retrieving the dependent variable values from an observation collection, two important points should be kept in mind. For given dependent variable settings:

- The dependent variable is not necessarily defined or computed for **all** single observation sets within the collection. This is why most of the functions designed to retrieve the dependent variable values associated with certain settings also return an observation parser object indicating which single observation sets contain this specific dependent variable.
- Multiple dependent variables can match the settings given as input, if those are not fully defined (e.g., lack of information on link ends). This is due to the way dependent variable settings are created (see above).

Using the dependent_variable Method
------------------------------------

To illustrate the above two points, we will take the :meth:`~tudatpy.estimation.observations.ObservationCollection.dependent_variable` method as an example. This method returns a tuple with:

- 1st element = vector of dependent variable matrices, one for each single observation set for which the dependent variable exists
- 2nd element = observation parser indicating which single observation sets contain the required dependent variable(s)

For each observation set :math:`i`, the dependent variable matrix size is :math:`n_{\text{obs},i} \times n_{dv}`, with :math:`n_{\text{obs},i}` the number of observations and :math:`n_{dv}` the size of the dependent variable.

As mentioned above, the following line creates elevation angle settings for all possible link ends (i.e., both the transmitter and the receiver in the case from above) since no link ends information is provided:

.. code-block:: python

    from tudatpy.estimation.observations_setup import observations_dependent_variables
    
    elevation_angle_settings = observations_dependent_variables.elevation_angle_dependent_variable()

Attempting to retrieve the elevation angle values with ``dependent_variable(elevation_angle_settings)`` would then fail: within each observation set, multiple variables could match these settings (e.g., the elevation angle either at the transmitter or the receiver). There are two options to resolve this:

**Option 1**: Returning the first dependent variables that match the settings by setting the input argument ``first_compatible_settings`` to ``True``:

.. code-block:: python

    elevation_angle_settings_1 = observations_dependent_variables.elevation_angle_dependent_variable()
    elevation_angle_outputs = observation_collection.dependent_variable(
        elevation_angle_settings_1,
        first_compatible_settings=True
    )

**Option 2**: Providing more specific settings as inputs:

.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links

    elevation_angle_settings_2 = observations_dependent_variables.elevation_angle_dependent_variable(
        link_end_type=links.LinkEndType.transmitter
    )
    elevation_angle_outputs = observation_collection.dependent_variable(elevation_angle_settings_2)

Both of the options above would successfully return the required outputs, which can be unpacked as follows:

.. code-block:: python

    # Get vector of elevation angle matrices
    elevation_angle_values = elevation_angle_outputs[0]
    
    # Get elevation angle parser
    elevation_angle_parser = elevation_angle_outputs[1]
    
    # The elevation_angle_parser allows to access the single observation sets for which the elevation angle is computed
    elevation_angle_sets = observation_collection.get_single_observation_sets(elevation_angle_parser)

.. tip::

   When a call to :meth:`~tudatpy.estimation.observations.ObservationCollection.dependent_variable`
   fails because the settings are ambiguous (several stored variables match them), the
   :meth:`~tudatpy.estimation.observations.ObservationCollection.compatible_dependent_variable_settings` method can be used
   to list the fully-defined settings that already exist in the collection and that your input could be referring to.

   "Compatible" here means *potentially the same stored variable*. Two settings are compatible when:

   * They have the same dependent-variable type.
   * For each link end (transmitting and receiving), the values are either identical or left blank in either setting. A blank field acts as a wildcard: leaving link ends unspecified matches all of them.
   * For variables that are independent of the link's direction, settings whose two link ends are swapped are also considered compatible.

   The method returns a tuple with:

   * **1st element:** a nested list with one entry per single observation set if it contains a match, in that case it contains the fully-defined settings compatible with the input.
   * **2nd element:** an observation parser selecting the observation sets listed above.

Additional Retrieval Methods
-----------------------------

Besides the :meth:`~tudatpy.estimation.observations.ObservationCollection.dependent_variable` and :meth:`~tudatpy.estimation.observations.ObservationCollection.compatible_dependent_variable_settings` methods introduced above, the dependent variable values can also be retrieved using the :meth:`~tudatpy.estimation.observations.ObservationCollection.concatenated_dependent_variable` method to retrieve all dependent variables concatenated.
The :meth:`~tudatpy.estimation.observations.ObservationCollection.dependent_variable_history` and :meth:`~tudatpy.estimation.observations.ObservationCollection.dependent_variable_history_per_set` methods can be used to retrieve the dependent variable values in the familiar time-history format, i.e., as a dictionary with observation times as keys and the dependent variable values as values.
For more information, take a look at the corresponding API entries.

Example: Plotting Elevation Angle
==================================

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    from tudatpy.estimation.observations import compute_residuals_and_dependent_variables
    from tudatpy.estimation.observable_models_setup import links
    from tudatpy.estimation.observations_setup import observations_dependent_variables

    observation_collection = ...

    # Define elevation angle settings
    elevation_settings = observations_dependent_variables.elevation_angle_dependent_variable(
        link_end_type=links.LinkEndType.transmitter
    )

    # Add to observation collection
    elevation_parser = observation_collection.add_dependent_variable(elevation_settings, bodies)

    # Compute residuals and dependent variables
    compute_residuals_and_dependent_variables(
        observation_collection,
        observation_simulators,
        bodies
    )

    # Retrieve elevation angle values
    elevation_values, elevation_parser = observation_collection.dependent_variable(elevation_settings)
    elevation_times = observation_collection.get_concatenated_observation_times(elevation_parser)

    # Plot elevation angle over time
    plt.figure(figsize=(10, 6))
    plt.plot(elevation_times, np.rad2deg(elevation_values))
    plt.xlabel("Time [s]")
    plt.ylabel("Elevation Angle [deg]")
    plt.title("Ground Station Elevation Angle")
    plt.grid(True)
    plt.show()
