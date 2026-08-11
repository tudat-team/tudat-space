.. _observation_handling:

====================
Observation Handling
====================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   observation-handling/observation-collection-creation
   observation-handling/observation-collection-manipulation

In Tudat, observations, whether real or simulated, are stored in an :class:`~tudatpy.estimation.observations.ObservationCollection` object. This class manages the storage of all observations in a sorted manner and handles all related bookkeeping.

A single observation is defined by the following quantities:

- Its **type**, which also defines the size of the observation (e.g., a range observation has a size of 1, while an angular position has a size of 2).
- Its **link ends**, which define the transmitter, receiver, and any transponders involved in the observation.
- The actual **observable value**.
- The **time** of the observation. While original data may be time-tagged in any scale (e.g., UTC), all times are converted to and stored in the Barycentric Dynamical Time (TDB) scale within Tudat.
- The **weight** assigned to the observation, used during least-squares estimation to account for observation uncertainty (defaults to 1).
- Any **dependent variables** calculated for the observation.
- The **observation residual**, computed as the difference between the observed and simulated values. This value is only available after being explicitly computed.
- Optional **ancillary settings** required for the simulation of an observation, such as the integration time of a Doppler observation.

Within an :class:`~tudatpy.estimation.observations.ObservationCollection`, observations are not stored individually but are grouped into :class:`~tudatpy.estimation.observations.SingleObservationSet` objects.
:class:`~tudatpy.estimation.observations.SingleObservationSet` objects store any number of observations that share:

- the same observable type
- the same link ends
- the same ancillary settings

Each :class:`~tudatpy.estimation.observations.SingleObservationSet` contains vectors of observation times, values, and weights. Residuals and dependent variables are also stored here once they are computed. The :class:`~tudatpy.estimation.observations.ObservationCollection` acts as a container for these :class:`~tudatpy.estimation.observations.SingleObservationSet` objects, organizing them in an internal data structure.

.. note::
   The internal dictionary structure of the :class:`~tudatpy.estimation.observations.ObservationCollection` is a low-level implementation detail that is typically not needed for most user interactions.


Working with Observations: A Workflow Guide
-------------------------------------------

The following sections of this guide will walk you through the workflow of working with observations in Tudat. We will cover:

- :ref:`Creating an Observation Collection <creating_observations>`: How to generate observations by :ref:`simulation <simulating_observations>` or :ref:`load them from real tracking data files <loading_real_data>`, as well as how to create :ref:`pseudo-observations from external ephemerides <pseudo_observations>`.
- :ref:`Interaction with an Observation Collection <observation_collection_manipulation>`: How to manipulate and interact with an existing :class:`~tudatpy.estimation.observations.ObservationCollection`, including filtering, splitting, and retrieving auxiliary quantities.
