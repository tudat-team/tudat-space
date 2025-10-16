.. _processing_observations:

=======================
Processing Observations
=======================

This page describes how to filter, split, and remove observation sets from an :class:`~tudatpy.estimation.observations.ObservationCollection`.

Filtering Observations
======================

Filtering allows you to remove unwanted observations from your collection, for instance, to discard outliers with high residuals or to focus on a specific time period.

Creating a Filter
-----------------

First, create a filter object specifying the filtering criterion:

.. code-block:: python

    from tudatpy.estimation import observations
    
    # Create a filter to remove observations with residuals greater than 0.1
    residual_filter = observations.observation_filter(
        observations.residual_filtering,
        0.1
    )

Available Filter Types
----------------------

Tudat supports several types of filters:

- **Residual filtering**: Remove observations with residuals exceeding a threshold
- **Time filtering**: Remove observations outside a specified time range
- **Dependent variable filtering**: Remove observations based on dependent variable values (e.g., elevation angle too low)

Applying a Filter
-----------------

Then, apply the filter to the collection. You can either modify the collection in-place or create a new, filtered collection:

.. code-block:: python

    # Apply the filter in-place
    observation_collection.filter_observations(residual_filter)
    
    # Or create a new filtered collection
    filtered_collection = observations.create_filtered_observation_collection(
        observation_collection,
        residual_filter
    )

By default, filtered-out observations are saved within each :class:`~tudatpy.estimation.observations.SingleObservationSet`.

.. note::
   Saved filtered observations are excluded from all subsequent calculations, such as residual computation, unless they are explicitly reintroduced into the main collection.

Splitting Observation Sets
===========================

You can split :class:`~tudatpy.estimation.observations.SingleObservationSet` objects into multiple, smaller sets. This can be useful to isolate data around specific events, like maneuvers or antenna swaps.

.. code-block:: python

    from tudatpy.estimation import observations
    
    # Create a splitter to divide sets at specific times
    splitter = observations.observation_set_splitter(
        observations.time_tags_splitter,
        [epoch1, epoch2]
    )
    
    # Apply the splitter in-place
    observation_collection.split_observation_sets(splitter)

After splitting, the :class:`~tudatpy.estimation.observations.ObservationCollection` will contain more :class:`~tudatpy.estimation.observations.SingleObservationSet` objects, each covering a subset of the original time range.

Removing Observation Sets
==========================

You can remove entire :class:`~tudatpy.estimation.observations.SingleObservationSet` objects from the collection using a parser.

.. code-block:: python

    from tudatpy.estimation import observations
    
    # Remove all one_way_range observations
    range_parser = observations.observation_parser(one_way_range)
    observation_collection.remove_single_observation_sets(range_parser)
    
    # Remove any sets that have become empty after filtering
    observation_collection.remove_empty_observation_sets()

Common Use Cases
================

Outlier Removal
---------------

.. code-block:: python

    # Compute initial residuals
    observations_setup.observations_wrapper.compute_residuals_and_dependent_variables(
        observation_collection,
        observation_simulators,
        bodies
    )
    
    # Remove observations with residuals > 3 sigma
    residual_threshold = 3.0 * observation_noise_level
    residual_filter = observations.observation_filter(
        observations.residual_filtering,
        residual_threshold
    )
    observation_collection.filter_observations(residual_filter)

Data Quality Assessment
-----------------------

.. code-block:: python

    # Filter by elevation angle (keep only observations above 10 degrees)
    elevation_settings = observations_setup.dependent_variable.elevation_angle_dependent_variable(
        link_end_type=transmitter
    )
    observation_collection.add_dependent_variable_settings(elevation_settings, bodies)
    
    observations_setup.observations_wrapper.compute_residuals_and_dependent_variables(
        observation_collection,
        observation_simulators,
        bodies
    )
    
    elevation_filter = observations.observation_filter(
        observations.dependent_variable_filtering,
        elevation_settings,
        min_value=np.deg2rad(10.0)
    )
    observation_collection.filter_observations(elevation_filter)

Time Range Selection
--------------------

.. code-block:: python

    # Keep only observations in a specific time window
    time_filter = observations.observation_filter(
        observations.time_filtering,
        start_time=start_epoch,
        end_time=end_epoch
    )
    
    filtered_collection = observations.create_filtered_observation_collection(
        observation_collection,
        time_filter
    )
