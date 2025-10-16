.. _observationSimulation:

====================
Observation Creation
====================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   observation-simulation/creating-observations
   observation-simulation/observation-collection-manipulation

Observation Collection Overview
================================

In Tudat, observations, whether real or simulated, are stored in an :class:`~tudatpy.estimation.observations.ObservationCollection` object. This class manages the storage of all observations in a sorted manner and handles all related bookkeeping.

Single Observation Structure
-----------------------------

A single observation is defined by the following quantities:

- Its **type**, which also defines the size of the observation (e.g., a range observation has a size of 1, while an angular position has a size of 2).
- Its **link ends**, which define the transmitter, receiver, and any transponders involved in the observation.
- The actual **observable value**.
- The **time** of the observation. While original data may be time-tagged in any scale (e.g., UTC), all times are converted to and stored in the Barycentric Dynamical Time (TDB) scale within Tudat.
- The **weight** assigned to the observation, used during least-squares estimation to account for observation uncertainty (defaults to 1).
- Any **dependent variables** calculated for the observation.
- The **observation residual**, computed as the difference between the observed and simulated values. This value is only available after being explicitly computed.
- **Ancillary settings** (optional).

Single Observation Set
-----------------------

Within an :class:`~tudatpy.estimation.observations.ObservationCollection`, observations are not stored individually but are grouped into :class:`~tudatpy.estimation.observations.SingleObservationSet` objects. These objects store any number of observations that share:

- The same observable type.
- The same link ends.
- The same ancillary settings.

Each :class:`~tudatpy.estimation.observations.SingleObservationSet` contains vectors of observation times, values, and weights. Residuals and dependent variables are also stored here once they are computed. The :class:`~tudatpy.estimation.observations.ObservationCollection` acts as a container for these :class:`~tudatpy.estimation.observations.SingleObservationSet` objects, organizing them in an internal data structure.

.. note::
   The internal dictionary structure of the :class:`~tudatpy.estimation.observations.ObservationCollection` is a low-level implementation detail that is typically not needed for most user interactions.


Working with Observations: A Workflow Guide
============================================

The following sections of this guide will walk you through the workflow of working with observations in Tudat. We will cover:

**Creating an ObservationCollection**: How to generate observations by :ref:`simulation <simulating_observations>` or :ref:`load them from real tracking data files <loading_real_data>`, as well as how to create :ref:`pseudo-observations from external ephemerides <pseudo_observations>`.

**Extracting Information**: How to :ref:`access specific subsets of information <extracting_observation_information>` from the collection using parsers.

**Modifying the Collection**: How to :ref:`adjust the properties <modifying_observation_collections>` of your observations after creation, such as setting weights and defining reference points.

**Using Dependent Variables**: How to :ref:`work with ancillary data <observation_dependent_variables_usage>`, like observation geometry, for deeper analysis.

**Processing Observations**: How to :ref:`refine your data <processing_observations>` by filtering outliers, splitting sets, or removing data.








