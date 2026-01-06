.. _pseudo_observations:

======================================
Pseudo-observations from Ephemerides
======================================

Using some external source (for instance: SPICE kernels) to compute/extract position observables (e.g. using the 3-dimensional Cartesian position of a body at an epoch as an 'observable'), and then fitting these observations to a dynamical model in Tudat can be very useful. In particular, such a procedure allows you to quantify exactly how closely the dynamical model settings used in Tudat can recreate the published orbit. Using such Cartesian positions from an external data source is sometimes termed using 'pseudo-observations'.

External Data Sources
=====================

The source of the Cartesian positions is up to the user, but typical sources are:

- Body positions from SPICE kernels
- Body positions from JPL Horizons
- TLEs propagated in time using an SGP4 propagator, and rotated to an inertial frame
- SP3c files containing tabulated state histories, typically for Earth-orbiting spacecraft

.. note::
   SPICE kernels with spacecraft orbits for a large number of planetary missions can be found on NASA's `Navigation and Ancillary Information Facility <https://naif.jpl.nasa.gov/naif/data.html>`_ website.

Creating Pseudo-observations
=============================

In Tudat Cartesian position (pseudo-)observations are processed using the :func:`~tudatpy.estimation.observable_models_setup.model_settings.relative_cartesian_position` observation model. In addition to creating the :class:`~tudatpy.estimation.observations.ObservationCollection` manually from external data, we provide a function of convenience to generate such pseudo-observations, using the following procedure:

1. Create the body for which the pseudo-observations are to be generated in your environment, using the :ref:`ephemeris<tudatpy:ephemeris>` module. Note that the :func:`~tudatpy.dynamics.environment_setup.ephemeris.tabulated_from_existing` option can be used to turn any ephemeris settings into tabulated ephemeris settings (which is required if using the same bodies in the estimation).

2. Generate relative position observations (and associated observation model settings) using the :func:`~tudatpy.estimation.observations_setup.observations_wrapper.create_pseudo_observations_and_models` function.

The latter function provides both the observations (as an :class:`~tudatpy.estimation.observations.ObservationCollection`), and a list of :class:`~tudatpy.estimation.observable_models_setup.model_settings.ObservationSettings` to be used for simulating the observables. The combination of these two can be used directly for the subsequent steps of defining estimation settings and performing the estimation.

Example
=======

.. code-block:: python

    from tudatpy.dynamics import environment_setup
    from tudatpy.estimation.observations_setup.observations_wrapper import create_pseudo_observations_and_models
    import numpy as np
    
    # Create body with ephemeris from SPICE
    body_settings = environment_setup.get_default_body_settings(
        ["Earth", "Moon", "Sun"],
        "SSB",
        "J2000"
    )
    
    # Convert to tabulated ephemeris for estimation
    body_settings.get("TargetBody").ephemeris_settings = \
        environment_setup.ephemeris.tabulated_from_existing(
            body_settings.get("TargetBody").ephemeris_settings,
            initial_time,
            final_time,
            time_step
        )
    
    bodies = environment_setup.create_system_of_bodies(body_settings)
    
    # Create pseudo-observations and observation model settings
    # This function generates observations from the existing ephemeris in the bodies
    pseudo_observations, observation_settings = create_pseudo_observations_and_models(
        bodies=bodies,
        observed_bodies=["TargetBody"],
        central_bodies=["Sun"],
        initial_time=initial_time,
        final_time=final_time,
        time_step=time_step
    )

For a complete example of using pseudo-observations, see the :ref:`Galilean moon state estimation example <estimation_using_pseudo_observations>`.