.. _observation_collection_manipulation:

=====================================
Observation Collection Manipulation
=====================================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   observation-collection-manipulation/extracting-information
   observation-collection-manipulation/modifying-collections
   observation-collection-manipulation/dependent-variables
   observation-collection-manipulation/processing-observations

Once you have created an :class:`~tudatpy.estimation.observations.ObservationCollection`, whether from simulated or real data, you will often need to access, modify, and process the observations. This section covers the various operations you can perform on observation collections:

- :ref:`Extracting information <extracting_observation_information>`: Learn how to retrieve observation data, times, residuals, and metadata
- :ref:`Modifying collections <modifying_observation_collections>`: Set weights, define reference points, and compute residuals
- :ref:`Using dependent variables <observation_dependent_variables_usage>`: Add and retrieve auxiliary quantities calculated alongside observations
- :ref:`Processing observations <processing_observations>`: Filter, split, and remove observation sets

These tools allow you to prepare your observation data for estimation, analyze results, and ensure data quality.
