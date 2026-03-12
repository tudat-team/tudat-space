.. _manual_observation_collections:

==============================
Manual Observation Collections
==============================

In addition to loading pre-defined file types (such as ODF or IFMS files), or simulating observations within the Tudat environment, users can manually create an :class:`~tudatpy.estimation.observations.ObservationCollection` from external data sources,
such as experimental measurements or pre-processed Python arrays. This allows the use of Tudat's estimation and plotting utilities on user-provided datasets.

Defining Single Observation Sets
================================

The building block of a manual collection is the :class:`~tudatpy.estimation.observations.SingleObservationSet`. This object encapsulates the data for a specific observable type associated with a specific link definition.

To create a single observation set, you must define the link ends, provide the observation times and values, and specify the reference link end.

.. code-block:: python

    from tudatpy.estimation import observations
    from tudatpy.estimation import observable_models_setup
    import numpy as np

    # 1. Define the link ends
    link_ends = {
        observable_models_setup.links.transmitter:
            observable_models_setup.links.body_origin_link_end_id("Starship"),
        observable_models_setup.links.receiver:
            observable_models_setup.links.body_reference_point_link_end_id("Earth", "Goldstone")
    }

    # 2. Prepare the data (times in seconds since J2000, observations in SI units)
    times = np.array([1.0e7, 1.0e7 + 300, 1.0e7 + 600])

    # Angular observations (RA/Dec) must be provided in radians
    obs_values = np.array([
        [np.deg2rad(120.0), np.deg2rad(10.0)],
        [np.deg2rad(120.2), np.deg2rad(10.1)],
        [np.deg2rad(120.4), np.deg2rad(10.2)]
    ])

    # 3. Create the set
    angular_set = observations.create_single_observation_set(
        observable_models_setup.model_settings.angular_position_type,
        link_ends,
        obs_values,
        times,
        observable_models_setup.links.receiver
    )

.. note::
   When creating a manual observation collection, it is recommended to adhere to Tudatpy's default SI units: **meters** for distance, **radians** for angles, and **seconds** for time.