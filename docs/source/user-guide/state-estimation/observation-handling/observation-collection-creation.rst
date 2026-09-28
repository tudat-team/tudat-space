.. _creating_observations:

===============================
Observation Collection Creation
===============================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   observation-collection-creation/simulating-observations
   observation-collection-creation/loading-real-data
   observation-collection-creation/pseudo-observations

An :class:`~tudatpy.estimation.observations.ObservationCollection` can be created by simulating observations or by loading them from external files. It's also possible to manually create an :class:`~tudatpy.estimation.observations.ObservationCollection` from a list of :class:`~tudatpy.estimation.observations.SingleObservationSet` objects or to create a new collection after filtering or splitting an existing one.

This section covers the different readily-available methods for creating observation collections in Tudat:

- :ref:`Simulated observations <simulating_observations>`: Generate synthetic observations using observation models
- :ref:`Loading real tracking data <loading_real_data>`: Import observations from external data sources (MPC, ODF, TNF, IFMS, FDETS, ...)
- :ref:`Pseudo-observations from ephemerides <pseudo_observations>`: Create observations from external ephemerides


The following pages provide detailed information on each method.

Manual Creation of Observation Collections
==========================================

In addition to loading observations from pre-defined file types (such as ODF or IFMS files), or simulating observations within the Tudat environment, users can manually create an :class:`~tudatpy.estimation.observations.ObservationCollection` from arbitrary data sources,
such as experimental measurements or pre-processed Python arrays. This allows the use of Tudat's estimation and plotting utilities on user-provided datasets.

Defining Single Observation Sets
--------------------------------

The building block of an observation collection is the :class:`~tudatpy.estimation.observations.SingleObservationSet`. This object encapsulates the data for a specific observable type associated with a specific link definition.

To create a single observation set, you must define the link ends, provide the observation times and values, and specify the reference link end.
The observation collection is then created by passing a list of single observation sets to the :class:`~tudatpy.estimation.observations.ObservationCollection` constructor.

.. code-block:: python

    import numpy as np
    from tudatpy.estimation import observations
    from tudatpy.estimation.observable_models_setup import links, model_settings

    # 1. Define the link ends
    link_ends = {
        links.LinkEndType.transmitter: links.body_origin_link_end_id("Starship"),
        links.LinkEndType.receiver: links.body_reference_point_link_end_id(
            "Earth", "Goldstone"
        ),
    }

    # 2. Prepare the data (times in seconds since J2000, observations in SI units)
    times = np.array([1.0e7, 1.0e7 + 300, 1.0e7 + 600])

    # Angular observations (RA/Dec) must be provided in radians
    obs_values = np.array(
        [
            [np.deg2rad(120.0), np.deg2rad(10.0)],
            [np.deg2rad(120.2), np.deg2rad(10.1)],
            [np.deg2rad(120.4), np.deg2rad(10.2)],
        ]
    )

    # 3. Create the single observation set
    angular_set = observations.create_single_observation_set(
        model_settings.ObservableType.angular_position_type,
        link_ends,
        obs_values,
        times,
        reference_link_end=links.LinkEndType.receiver,
    )

    # 4. Create the observation collection
    observation_collection = observations.ObservationCollection([angular_set])

.. note::
   When creating a manual observation collection, you must adhere to TudatPy's default (SI) units: **meters** for distance, **radians** for angles, and **seconds** for time.