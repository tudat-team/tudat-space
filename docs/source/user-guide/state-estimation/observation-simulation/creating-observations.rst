.. _creating_observations:

======================
Creating Observations
======================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   creating-observations/simulating-observations
   creating-observations/loading-real-data
   creating-observations/pseudo-observations

An :class:`~tudatpy.estimation.observations.ObservationCollection` can be created by simulating observations or by loading them from external files. It's also possible to manually create an :class:`~tudatpy.estimation.observations.ObservationCollection` from a list of :class:`~tudatpy.estimation.observations.SingleObservationSet` objects or to create a new collection after filtering or splitting an existing one.

This section covers the different methods for creating observation collections in Tudat(Py):

- :ref:`Simulating observations <simulating_observations>`: Generate synthetic observations using observation models
- :ref:`Loading real tracking data <loading_real_data>`: Import observations from external data sources (MPC, ODF, IFMS, FDETS)
- :ref:`Pseudo-observations <pseudo_observations>`: Create observations from external ephemerides

The following pages provide detailed information on each method.
