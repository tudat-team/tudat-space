.. _extracting_observation_information:

===============================
Extracting Information
===============================

The :class:`~tudatpy.estimation.observations.ObservationCollection` provides numerous methods to retrieve observation data. This page describes how to access the observations and their associated metadata.

.. _observation_collection_parser:

Observation Collection Parser
==============================

To access, manipulate, and retrieve specific subsets of an :class:`~tudatpy.estimation.observations.ObservationCollection`, you can use an observation collection parser.
A parser is a user-created object that defines criteria for selecting specific :class:`~tudatpy.estimation.observations.SingleObservationSet` objects based on the metadata of the observation set.
The :func:`~tudatpy.estimation.observations.observations_processing.observation_parser` function is overloaded, which means that the function is able to accept different types of input arguments to create the desired parser.

Here is a simple example of how to create and use a parser to retrieve specific observations:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType
    
    # Create a parser to select only 'one_way_range' observations
    range_parser = observation_parser(ObservableType.one_way_range_type)
    
    # Use the parser to get the concatenated observation times for the selected sets
    range_times = observation_collection.get_concatenated_observation_times(range_parser)

.. hint::

    If you would like to select a subset of the observation collection based on the observation value, its timetag, or residual, see the user guide on :ref:`observation collection filtering <filtering_observations>`.


Parser Types
------------

You can create parsers to select :class:`~tudatpy.estimation.observations.SingleObservationSet` objects based on the following criteria:

**Observable Type**

Only targets single observation sets of the specified observation type:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType
    
    # Create a parser for a single observable type
    parser = observation_parser(ObservableType.dsn_n_way_averaged_doppler_type)
    
    # Create a parser for a list of observable types (selects sets with EITHER type)
    obs_type_list = [ObservableType.dsn_n_way_averaged_doppler_type, ObservableType.one_way_range_type]
    parser = observation_parser(obs_type_list)

**Link Ends**

Only targets single observation sets with the specified link ends:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup import links
    
    # Create a parser for a specific set of link ends
    link_ends_graz = dict()
    link_ends_graz[links.transmitter] = links.body_reference_point_link_end_id("Earth", "Graz")
    link_ends_graz[links.receiver] = links.body_origin_link_end_id("LRO")
    parser = observation_parser(link_ends_graz)

A few variants of this link ends-based parsing exist, allowing the user to provide only part of the link ends information instead of the full link ends:

- By the name of a body or reference point:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    
    parser = observation_parser("Graz", is_reference_point=True)

- By the ID of a link end:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    
    parser = observation_parser(("Earth", "Graz"))

- By the type of a link end:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.links import LinkEndType
    
    parser = observation_parser(LinkEndType.receiver)

- By specifying one of the link ends (both link end ID and type):

.. code-block:: python

    from tudatpy.estimation.observable_models_setup.links import (
        LinkEndType,
        body_reference_point_link_end_id,
    )
    from tudatpy.estimation.observations.observations_processing import observation_parser

    parser = observation_parser(
        (LinkEndType.receiver, body_reference_point_link_end_id("Earth", "Graz"))
    )

**Time Bounds**

Selects sets where **all** observation times are within the specified bounds:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    
    min_time = ...  # Start time in seconds since J2000
    max_time = ...  # End time in seconds since J2000
    parser = observation_parser((min_time, max_time))

**Ancillary Settings**

Only targets single observation sets matching the specified ancillary settings:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observations_setup.ancillary_settings import doppler_ancillary_settings
    
    # Example: Create a parser for observations with specific integration time
    ancillary_set = doppler_ancillary_settings(integration_time=60.0)
    parser = observation_parser(ancillary_set)

**Multi-Type Parser**

Combine multiple parsers. This allows you to combine any number of the above parsing conditions. The input argument ``combine_conditions`` then defines whether the union or intersection of the different conditions should be used (e.g., all sets with ``one_way_range`` **or** the Graz station as receiver, or ``one_way_range`` **and** Graz station as receiver):

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType
    from tudatpy.estimation.observable_models_setup.links import LinkEndType, body_reference_point_link_end_id
    
    parser_list = []
    parser_list.append(observation_parser(ObservableType.one_way_range_type))
    parser_list.append(observation_parser((LinkEndType.receiver, body_reference_point_link_end_id("Earth", "Graz"))))
    
    # Combine with OR logic (union) - default behavior
    parser = observation_parser(parser_list, combine_conditions=False)
    
    # Combine with AND logic (intersection)
    parser_and = observation_parser(parser_list, combine_conditions=True)

Lists of Arguments
^^^^^^^^^^^^^^^^^^

For each of the parser types mentioned above (with the notable exception of the multi-type one), the function creating a parser of a given type can either be called with a single argument or a list of arguments:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType

    obs_type_list = [
        ObservableType.dsn_n_way_averaged_doppler_type,
        ObservableType.one_way_range_type,
    ]
    parser = observation_parser(obs_type_list)

In the above code snippet, the parser will target all observation sets containing either ``dsn_n_way_averaged_doppler`` **or** ``one_way_range`` observations.

Inverting Parser Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is also possible to "invert" the parsing condition (e.g., retrieving observations of all types but the one specified, etc.) by setting the ``use_opposite_condition`` input argument to ``True`` (default is ``False``):

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType
    
    parser = observation_parser(ObservableType.one_way_range_type, use_opposite_condition=True)

.. tip::
   Having a clear overview of which observable type, link ends, etc. are present in the observation collection one is working with can be difficult, especially if the collection was created by :ref:`loading real observations <loading_real_data>` from e.g., ODF or IFMS files. This can make the use of a parser more difficult. The :meth:`~tudatpy.estimation.observations.ObservationCollection.print_observation_sets_start_and_size` method can be very useful in that respect, as it prints a summary of all observation sets in the collection (see :ref:`Inspecting Observation Collections <observation_handling>`).

Retrieving Observation Data
============================

The :class:`~tudatpy.estimation.observations.ObservationCollection` provides numerous methods to retrieve observation data. A complete list can be found in the `API Reference <https://py.api.tudat.space>`_. These methods can optionally take a parser object to retrieve data from a specific subset of the collection.

Here are some examples:

.. code-block:: python

    from tudatpy.estimation.observations.observations_processing import observation_parser
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType

    observation_collection = ...

    # Create a parser for Doppler observations from the 'DSS-14' station
    doppler_parser = observation_parser(
        [
            observation_parser(ObservableType.dsn_n_way_averaged_doppler_type),
            observation_parser("DSS-14", is_reference_point=True),
        ],
        combine_conditions=True,
    )

    # Get the concatenated residuals for this specific subset
    residuals = observation_collection.get_concatenated_residuals(doppler_parser)

    # Get the observation times and values for the same subset
    values, times = observation_collection.get_observations_and_times(doppler_parser)

Data is always returned in a fixed, sorted order to ensure deterministic and reproducible results.

Retrieving Metadata
===================

You can also retrieve metadata about the collection, which is useful for creating parsers:

.. code-block:: python

    observation_collection = ...

    # Get all observable types in the collection
    observable_types = observation_collection.get_observable_types()
    
    # Get names of all bodies involved in link ends
    body_names = observation_collection.get_bodies_in_link_ends()
    
    # Get names of all reference points
    reference_points = observation_collection.get_reference_points_in_link_ends()

Common Retrieval Methods
=========================

The following methods are commonly used to extract data from an :class:`~tudatpy.estimation.observations.ObservationCollection`:

- :meth:`~tudatpy.estimation.observations.ObservationCollection.get_concatenated_observations`: Get all observation values
- :meth:`~tudatpy.estimation.observations.ObservationCollection.get_concatenated_observation_times`: Get all observation times
- :meth:`~tudatpy.estimation.observations.ObservationCollection.get_concatenated_weights`: Get all observation weights
- :meth:`~tudatpy.estimation.observations.ObservationCollection.get_concatenated_residuals`: Get all observation residuals (after computation)
- :meth:`~tudatpy.estimation.observations.ObservationCollection.get_observations_and_times`: Get both observations and times together
- :attr:`~tudatpy.estimation.observations.ObservationCollection.sorted_observation_sets`: Get the nested dictionary of :class:`~tudatpy.estimation.observations.SingleObservationSet` objects

All of these methods can optionally accept a parser to filter the results to a specific subset of observations.

Example: Complete Workflow
===========================

Here's a complete example showing how to extract and analyze specific observations:

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    from tudatpy.estimation.observable_models_setup import links
    from tudatpy.estimation.observable_models_setup.model_settings import ObservableType
    from tudatpy.estimation.observations.observations_processing import observation_parser

    observation_collection = ...

    # Print overview of all observation sets
    observation_collection.print_observation_sets_start_and_size()

    # Create parser for specific Doppler observations from a ground station
    parser_list = [
        observation_parser(ObservableType.dsn_n_way_averaged_doppler_type),
        observation_parser(
            (
                links.LinkEndType.transmitter,
                links.body_reference_point_link_end_id("Earth", "DSS-14"),
            )
        ),
    ]
    doppler_parser = observation_parser(parser_list, combine_conditions=True)

    # Extract data
    times = observation_collection.get_concatenated_observation_times(doppler_parser)
    observations = observation_collection.get_concatenated_observations(doppler_parser)
    residuals = observation_collection.get_concatenated_residuals(doppler_parser)
    weights = observation_collection.get_concatenated_weights(doppler_parser)

    # Convert times to hours since start
    times_hours = (np.array(times) - times[0]) / 3600.0

    # Plot residuals
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(times_hours, observations, "b.", markersize=2, label="Observations")
    plt.ylabel("Doppler [Hz]")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(times_hours, residuals, "r.", markersize=2, label="Residuals")
    plt.xlabel("Time since start [hours]")
    plt.ylabel("Residuals [Hz]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Compute statistics
    rms_residual = np.sqrt(np.mean(residuals**2))
    print(f"RMS residual: {rms_residual:.6e} Hz")
    print(f"Number of observations: {len(observations)}")
