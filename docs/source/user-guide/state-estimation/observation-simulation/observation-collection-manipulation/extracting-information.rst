.. _extracting_observation_information:

===============================
Extracting Information
===============================

The :class:`~tudatpy.estimation.observations.ObservationCollection` provides numerous methods to retrieve observation data. This page describes how to access the observations and their associated metadata.

Observation Collection Parser
==============================

To access, manipulate, and retrieve specific subsets of an :class:`~tudatpy.estimation.observations.ObservationCollection`, you can use an observation collection parser. A parser is a user-created object that defines criteria for selecting specific :class:`~tudatpy.estimation.observations.SingleObservationSet` objects. The :func:`~tudatpy.estimation.observations.observation_parser` function is overloaded to accept different types of input to create the desired parser.

Here is a simple example of how to create and use a parser to retrieve specific observations:

.. code-block:: python

    from tudatpy.estimation import observations
    
    # Create a parser to select only 'one_way_range' observations
    range_parser = observations.observation_parser(one_way_range)
    
    # Use the parser to get the concatenated observation times for the selected sets
    range_times = observation_collection.get_concatenated_observation_times(range_parser)

Parser Types
------------

You can create parsers to select :class:`~tudatpy.estimation.observations.SingleObservationSet` objects based on the following criteria:

**Observable Type**

Only targets single observation sets of the specified observation type:

.. code-block:: python

    # Create a parser for a single observable type
    observable_type = dsn_n_way_averaged_doppler
    parser = observations.observation_parser(observable_type)
    
    # Create a parser for a list of observable types (selects sets with EITHER type)
    obs_type_list = [dsn_n_way_averaged_doppler, one_way_range]
    parser = observations.observation_parser(obs_type_list)

**Link Ends**

Only targets single observation sets with the specified link ends:

.. code-block:: python

    # Create a parser for a specific set of link ends
    link_ends_graz = dict()
    link_ends_graz[transmitter] = observations.body_reference_point_link_end_id("Earth", "Graz")
    link_ends_graz[receiver] = observations.body_origin_link_end_id("LRO")
    parser = observations.observation_parser(link_ends_graz)

A few variants of this link ends-based parsing exist, allowing the user to provide only part of the link ends information instead of the full link ends:

- By the name of a body or reference point:

.. code-block:: python

    parser = observations.observation_parser("Graz", is_reference_point=True)

- By the ID of a link end:

.. code-block:: python

    parser = observations.observation_parser(("Earth", "Graz"))

- By the type of a link end:

.. code-block:: python

    parser = observations.observation_parser(observations.receiver)

- By specifying one of the link ends (both link end ID and type):

.. code-block:: python

    parser = observations.observation_parser((observations.receiver, ("Earth", "Graz")))

**Time Bounds**

Selects sets where **all** observation times are within the specified bounds:

.. code-block:: python

    min_time = ...  # Start time in seconds since J2000
    max_time = ...  # End time in seconds since J2000
    parser = observations.observation_parser((min_time, max_time))

**Ancillary Settings**

Only targets single observation sets matching the specified ancillary settings:

.. code-block:: python

    # Example: Create a parser for a specific frequency band
    ancillary_settings = observations.ancillary_settings(frequency_band='X')
    parser = observations.observation_parser(ancillary_settings)

**Multi-Type Parser**

Combine multiple parsers. This allows you to combine any number of the above parsing conditions. The input argument ``combine_conditions`` then defines whether the union or intersection of the different conditions should be used (e.g., all sets with ``one_way_range`` **or** the Graz station as receiver, or ``one_way_range`` **and** Graz station as receiver):

.. code-block:: python

    parser_list = []
    parser_list.append(observations.observation_parser(one_way_range))
    parser_list.append(observations.observation_parser((observations.receiver, ("Earth", "Graz"))))
    
    # Combine with OR logic (union) - default behavior
    parser = observations.observation_parser(parser_list, combine_conditions=False)
    
    # Combine with AND logic (intersection)
    parser_and = observations.observation_parser(parser_list, combine_conditions=True)

Lists of Arguments
^^^^^^^^^^^^^^^^^^

For each of the parser types mentioned above (with the notable exception of the multi-type one), the function creating a parser of a given type can either be called with a single argument or a list of arguments:

.. code-block:: python

    obs_type_list = [dsn_n_way_averaged_doppler, one_way_range]
    parser = observations.observation_parser(obs_type_list)

In the above code snippet, the parser will target all observation sets containing either ``dsn_n_way_averaged_doppler`` **or** ``one_way_range`` observations.

Inverting Parser Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   It is also possible to "invert" the parsing condition (e.g., retrieving observations of all types but the one specified, etc.) by setting the ``use_opposite_condition`` input argument to ``True`` (default is ``False``):

   .. code-block:: python

       parser = observations.observation_parser(observable_type, use_opposite_condition=True)

.. tip::
   Having a clear overview of which observable type, link ends, etc. are present in the observation collection one is working with can be difficult, especially if the collection was created by :ref:`loading real observations <loading_real_data>` from e.g., ODF or IFMS files. This can make the use of a parser more difficult. The :meth:`~tudatpy.estimation.observations.ObservationCollection.print_observation_sets_start_and_size` method can be very useful in that respect, as it prints a summary of all observation sets in the collection (see :ref:`Inspecting Observation Collections <observationSimulation>`).

Retrieving Observation Data
============================

The :class:`~tudatpy.estimation.observations.ObservationCollection` provides numerous methods to retrieve observation data. A complete list can be found in the `API Reference <https://py.api.tudat.space>`_. These methods can optionally take a parser object to retrieve data from a specific subset of the collection.

Here are some examples:

.. code-block:: python

    from tudatpy.estimation import observations
    
    # Create a parser for Doppler observations from the 'DSS-14' station
    doppler_parser = observations.observation_parser([
        observations.observation_parser(dsn_n_way_averaged_doppler),
        observations.observation_parser("DSS-14", is_reference_point=True)
    ], combine_conditions=True)
    
    # Get the concatenated residuals for this specific subset
    residuals = observation_collection.get_concatenated_residuals(doppler_parser)
    
    # Get the observation times and values for the same subset
    times, values = observation_collection.get_observations_and_times(doppler_parser)

Data is always returned in a fixed, sorted order to ensure deterministic and reproducible results.

Retrieving Metadata
===================

You can also retrieve metadata about the collection, which is useful for creating parsers:

.. code-block:: python

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
- :meth:`~tudatpy.estimation.observations.ObservationCollection.sorted_observation_sets`: Get the nested dictionary of :class:`~tudatpy.estimation.observations.SingleObservationSet` objects

All of these methods can optionally accept a parser to filter the results to a specific subset of observations.
