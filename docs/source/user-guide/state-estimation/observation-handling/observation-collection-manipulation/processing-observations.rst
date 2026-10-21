.. _processing_observations:

=======================
Processing Observations
=======================

This page describes how to filter, split, and remove observation sets from an :class:`~tudatpy.estimation.observations.ObservationCollection`.

.. _filtering_observations:

Filtering Observations
======================

Observations can be filtered out of an observation collection using different types of filtering conditions.
The observation filters generally act on the observation *value*, its timetag, residual or dependent variable.
For an exhaustive list, see the :class:`~tudatpy.estimation.observations.observations_processing.ObservationFilterType` enum in the API documentation.

.. hint::

    If you would like to select a subset of the observation collection based on the metadata of the observation set (e.g., the observable type, link ends or ancillary settings), see the user guide on :ref:`observation collection parsing <observation_collection_parser>`.

Creating a Filter
-----------------

The creation of an observation filter object is done by specifying the type of filtering to apply and the filter value, here demonstrated for the ``residual_filtering`` option:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import (
        observation_filter,
        ObservationFilterType,
    )

    # Create a filter to remove observations with residuals greater than cutoff_value
    filter_obj = observation_filter(
        ObservationFilterType.residual_filtering, cutoff_value, use_opposite_condition=False
    )

The (optional) ``use_opposite_condition`` argument allows the user to revert the filtering condition as it is described above for each type of filtering. For instance, while using ``residual_filtering`` nominally cuts off all observations with residuals **higher** than the specified limit value, reverting the filtering condition implies that residuals **lower** than the limit will be removed.

Available Filter Types
----------------------

Tudat supports several types of filters, which are accessible as values from the :class:`~tudatpy.estimation.observations.observations_processing.ObservationFilterType` enum:

- **residual_filtering**: Remove observations with residuals exceeding a threshold
- **absolute_value_filtering**: Remove observations whose absolute value exceeds a threshold
- **epochs_filtering**: Remove observations at specific time epochs
- **time_bounds_filtering**: Remove observations outside a specified time range
- **dependent_variable_filtering**: Remove observations based on dependent variable values (e.g., elevation angle too low)

Applying a Filter
-----------------

Once the filter object has been defined, one must call the :meth:`~tudatpy.estimation.observations.ObservationCollection.filter_observations` method of the observation collection object to apply the filtering:

.. code-block:: python

    # Apply the filter in-place (modifies observation_collection directly)
    observation_collection.filter_observations(filter_obj)

The above directly modifies the content of the ``observation_collection`` object. Alternatively, it is also possible to create a new observation collection that would only contain the post-filtering observations:

.. code-block:: python

    from tudatpy.estimation.observations import create_filtered_observation_collection
    
    # Create a new filtered collection
    filtered_observation_collection = create_filtered_observation_collection(
        observation_collection,
        filter_obj
    )

The :func:`~tudatpy.estimation.observations.create_filtered_observation_collection` function can also take an optional observation parser object as input. In this case, the filter is only applied to the single observation sets meeting the parsing conditions.

Saving and Retrieving Filtered Observations
-------------------------------------------

When filtering out some observations, it is possible to make sure that they are saved such that the user can still access them, or such that they can be re-introduced at a later stage. A good use case would be if some observations are initially filtered out due to too high residuals, but those residuals go down in subsequent iterations of the estimation.

For each single observation set, the filtered observations are stored within a separate, nested observation set. By default, filtered-out observations are saved within each :class:`~tudatpy.estimation.observations.SingleObservationSet`.

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import (
        observation_filter,
        ObservationFilterType,
    )

    residual_threshold = 0.1  # Define the threshold for residual filtering

    # Create a filter for all residuals > 0.1
    residual_filter = observation_filter(
        ObservationFilterType.residual_filtering, residual_threshold, filter_out=True
    )

    # Filter out the outliers, and save the filtered observations (default behavior)
    observation_collection.filter_observations(
        residual_filter, save_filtered_observations=True
    )

    # For each observation set, get the number of filtered observations and retrieve them as separate observation set objects
    nb_filtered_obs_per_set = list()
    filtered_obs_sets = list()
    for obs_set in observation_collection.get_single_observation_sets():
        nb_filtered_obs_per_set.append(obs_set.number_filtered_observations)
        filtered_obs_sets.append(obs_set.filtered_observation_set)

    # ... Later, re-introduce the filtered observations
    residual_filter_back = observation_filter(
        ObservationFilterType.residual_filtering, residual_threshold, filter_out=False
    )
    observation_collection.filter_observations(residual_filter_back)

The input argument ``filter_out``, by default set to ``True``, is the one that defines whether the filter is applied to remove observations from the collection (``filter_out=True``) or to re-introduce previously filtered observations (``filter_out=False``).

.. note::
   Saved filtered observations are excluded from all subsequent calculations, such as residual computation, unless they are explicitly reintroduced into the main collection. The filtering can also be performed at the :class:`~tudatpy.estimation.observations.SingleObservationSet` level.

Splitting Observation Sets
===========================

It is also possible to split a single observation set into multiple ones, which can be useful to take specific events into account (e.g., switch between two antennas, maneuvers, etc.). This is a way to make sure that nothing unusual occurs in the middle of an observation set, and that the observations within that set are obtained under the same conditions (e.g., same antenna as reference point). It can also allow the user to split an observation set if it spans over a long period of time, or limits the number of observations per set.

Available Splitter Types
------------------------

Any of the following conditions can be used to specify where the splitting should be applied:

- **time_tags_splitter**: Takes a list of epochs as input and splits the observation set(s) at these epochs
- **time_interval_splitter**: Takes as input a float value representing the maximum time interval between two consecutive observations, and splits the set accordingly
- **time_span_splitter**: Takes as input a float value representing the maximum time span of a single observation set, and splits the set(s) accordingly
- **nb_observations_splitter**: Takes as input an integer denoting the maximum number of observations per set above which the set(s) should be split

Applying a Splitter
-------------------

The splitting is performed as follows:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import (
        observation_set_splitter,
        ObservationSetSplitterType,
    )

    # Define splitting epochs
    splitting_epochs = [epoch1, epoch2, epoch3]

    # Create a splitter to divide sets at specific times
    splitter = observation_set_splitter(
        ObservationSetSplitterType.time_tags_splitter, splitting_epochs
    )

    # Apply the splitter in-place
    observation_collection.split_observation_sets(splitter)

Note that the splitting does not change the observation content of the observation collection, and only redefines the number and size of the observation sets contained within that collection.
After splitting, the :class:`~tudatpy.estimation.observations.ObservationCollection` will contain more :class:`~tudatpy.estimation.observations.SingleObservationSet` objects, each covering a subset of the original time range.

Similarly to the filtering functionality, the splitting can either be applied to modify the content of an existing observation collection (as shown above), or a new, post-splitting observation collection can be created (without altering the original one):

.. code-block:: python

    from tudatpy.estimation.observations import split_observation_collection
    
    # Create a new post-splitting collection
    post_split_collection = split_observation_collection(
        observation_collection,
        splitter
    )

The :func:`~tudatpy.estimation.observations.split_observation_collection` function can also take an optional observation parser object as input, in which case the splitting is only applied to the single observation sets that match the parsing condition.

Removing Observation Sets
==========================

At the observation collection level, it is also possible to remove entire single observation sets altogether. This can be done using the :meth:`~tudatpy.estimation.observations.ObservationCollection.remove_single_observation_sets` method. It takes an observation parser as input and removes from the observation collection all sets meeting the parsing condition.

Removing Sets by Criteria
--------------------------

As an example, the following lines of code would remove all ``one_way_range`` data from the observation collection:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType
    
    # Remove all one_way_range observations
    range_parser = observation_parser(ObservableType.one_way_range_type)
    observation_collection.remove_single_observation_sets(range_parser)

Removing Empty Sets
-------------------

It is also possible to parse all single observation sets and remove those that are empty. This can for instance be part of a post-filtering processing, as the filtering only removes observations from the :class:`~tudatpy.estimation.observations.SingleObservationSet` objects, but does not delete those objects if empty. This can be done as follows:

.. code-block:: python

    # Remove any sets that have become empty after filtering
    observation_collection.remove_empty_observation_sets()

Common Use Cases
================

Outlier Removal
---------------

.. code-block:: python

    from tudatpy.estimation.observations import compute_residuals_and_dependent_variables
    from tudatpy.estimation.observations.observations_processing import (
        ObservationFilterType,
        observation_filter,
    )

    # Compute initial residuals
    compute_residuals_and_dependent_variables(
        observation_collection, observation_simulators, bodies
    )

    # Remove observations with residuals > 3 sigma
    residual_threshold = 3.0 * observation_noise_level
    residual_filter_obj = observation_filter(
        ObservationFilterType.residual_filtering, residual_threshold
    )
    observation_collection.filter_observations(residual_filter_obj)

Data Quality Assessment
-----------------------

.. code-block:: python

    import numpy as np
    from tudatpy.estimation.observable_models_setup import links
    from tudatpy.estimation.observations import compute_residuals_and_dependent_variables
    from tudatpy.estimation.observations.observations_processing import observation_filter
    from tudatpy.estimation.observations_setup import observations_dependent_variables

    # Define elevation angle dependent variable
    elevation_settings = (
        observations_dependent_variables.elevation_angle_dependent_variable(
            link_end_type=links.LinkEndType.transmitter
        )
    )
    observation_collection.add_dependent_variable(elevation_settings)

    # Compute residuals and dependent variables
    compute_residuals_and_dependent_variables(
        observation_collection, observation_simulators, bodies
    )

    # Filter by elevation angle (keep only observations above 10 degrees)
    elevation_filter = observation_filter(
        elevation_settings, np.array([np.deg2rad(10.0)]), use_opposite_condition=True
    )
    observation_collection.filter_observations(elevation_filter)

Time Range Selection
--------------------

.. code-block:: python

    from tudatpy.estimation.observations import create_filtered_observation_collection
    from tudatpy.estimation.observations.observations_processing import (
        ObservationFilterType,
        observation_filter,
    )

    # Keep only observations in a specific time window
    time_filter = observation_filter(
        ObservationFilterType.time_bounds_filtering, start_epoch, end_epoch
    )

    filtered_collection = create_filtered_observation_collection(
        observation_collection, time_filter
    )

Splitting Around Events
-----------------------

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import (
        ObservationSetSplitterType,
        observation_set_splitter,
    )

    # Split observation sets around maneuver epochs
    maneuver_epochs = [maneuver_epoch_1, maneuver_epoch_2, maneuver_epoch_3]

    splitter = observation_set_splitter(
        ObservationSetSplitterType.time_tags_splitter, maneuver_epochs
    )

    observation_collection.split_observation_sets(splitter)

Example: Complete Filtering Workflow
=====================================

Here's a complete example showing how to filter observations based on multiple criteria:

.. code-block:: python

    import numpy as np
    from tudatpy.estimation.observable_models_setup import links
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType
    from tudatpy.estimation.observations import compute_residuals_and_dependent_variables
    from tudatpy.estimation.observations.observations_processing import (
        ObservationFilterType,
        observation_filter,
        observation_parser,
    )
    from tudatpy.estimation.observations_setup import observations_dependent_variables

    # Add elevation angle as dependent variable
    elevation_settings = (
        observations_dependent_variables.elevation_angle_dependent_variable(
            link_end_type=links.LinkEndType.transmitter
        )
    )
    observation_collection.add_dependent_variable(elevation_settings)

    # Compute residuals and dependent variables
    compute_residuals_and_dependent_variables(
        observation_collection, observation_simulators, bodies
    )

    # Filter 1: Remove observations below 15 degrees elevation
    elevation_filter = observation_filter(
        elevation_settings, np.array([np.deg2rad(15.0)]), use_opposite_condition=True
    )
    observation_collection.filter_observations(elevation_filter)

    # Filter 2: Remove observations with high residuals (only for Doppler)
    doppler_parser = observation_parser(ObservableType.dsn_n_way_averaged_doppler_type)
    residual_filter_obj = observation_filter(
        ObservationFilterType.residual_filtering, 3.0 * doppler_noise_level
    )
    observation_collection.filter_observations(
        residual_filter_obj, observation_parser=doppler_parser
    )

    # Remove any empty observation sets
    observation_collection.remove_empty_observation_sets()

    # Print filtering results
    print(
        f"Number of remaining observation sets: {len(observation_collection.get_single_observation_sets())}"
    )
    print(
        f"Total number of observations: {len(observation_collection.get_concatenated_observations())}"
    )

Filtering by Multiple Conditions
=================================

You can apply multiple filters sequentially to progressively refine your observation data:

.. code-block:: python

    from tudatpy.estimation.observations import compute_residuals_and_dependent_variables
    from tudatpy.estimation.observations.observations_processing import (
        ObservationFilterType,
        observation_filter,
    )

    # Step 1: Filter by time range
    time_filter = observation_filter(
        ObservationFilterType.time_bounds_filtering, start_time, end_time
    )
    observation_collection.filter_observations(time_filter)

    # Step 2: Compute residuals
    compute_residuals_and_dependent_variables(
        observation_collection, observation_simulators, bodies
    )

    # Step 3: Filter by residual magnitude
    residual_filter_obj = observation_filter(
        ObservationFilterType.residual_filtering, max_residual_threshold
    )
    observation_collection.filter_observations(
        residual_filter_obj, save_filtered_observations=True
    )

    # Step 4: Remove specific problematic epochs if needed
    problematic_epochs = [epoch1, epoch2, epoch3]
    epochs_filter = observation_filter(
        ObservationFilterType.epochs_filtering, problematic_epochs
    )
    observation_collection.filter_observations(epochs_filter)

    # Clean up
    observation_collection.remove_empty_observation_sets()
