.. _specific_environment_considerations:

=======================
Specific Considerations
=======================

On this page, we give an overview of some aspects of the environment models that may be useful for a user to select and understand their choice of environment models.
This page is meant to supplement the API documentation, and is *not* a comprehensive overview of all environment models (which can be found there). 

Rotation models
===============

Tudat has a broad range of rotation models available. In principle, these models can be assigned to both celestial bodies and natural bodies. 
However, a subset of these models is typically only applied to natural *or* artificial bodies. Rotation models have a wide range of, sometimes indirect, influences on the dynamics

* A spherical harmonic acceleration exerted by a central body is first evaluated in a body-fixed frame, and the transformed to an inertial frame. Consequently, the central body's rotation has a fundamental influence on the exerted spherical harmonic acceleration
* A thrust acceleration in Tudat is calculated from two models: (1) an engine model, which defined the body-fixed direction of the thrust, and the magnitude of the thrust (2) the orientation of the body in space, defined by its rotation model
* For a non-spherical central body, the current orientation of a body has an indirect influence on the altitude at which a vehicle with a given *inertial* state is located

Two rotation models, which are typically used for vehicles under thrust, and/or vehicles in an atmosphere, are the following:

* The rotation model :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`, which calculates the body's rotation based on the angle of attack, sideslip angle and bank angle. Note that these angles are definend w.r.t. the relative wind. This model is typical when using, for instance, a re-entry simulation. It imposes these three angles, and calculates the body orientation by combination with the latitude, longitude, heading angle, flight path angles. There is a related model, :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.zero_pitch_moment_aerodynamic_angle_based`, that uses the same setup, but does not impose the angle of attack, but caculates by imposing aerodynamic pitch trim (zero pitch moment).
* The rotation model :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_inertial_direction_based`, which is typical when calcualting dynamics of a vehicle under thrust. It is based on linking a body-fixed  direction (now limited to the body-fixed x-axis) to an arbitrary inertial direction. This allows the thrust (assuming that this is aligned with this same body-fixed direction) to be guided in an inertial direction determined by a user-defined model. 

Ephemeris models
================

An ephemeris is arguably the most fundamental of the environment models: it defines *where* a body is located in space. 

Use of Spice
------------

For many typical applications, natural body ephemerides will be calculated from Spice kernels. In some cases, a user may find that the default Spice kernels are insufficient for their purposes, due to one of two reasons:

* The body for which the state is required *is* in the ephemeris Spice kernel, but the time at which the state is neede lies outside of the bounds for which the Spice kernel has data
* The body for which the state is required *is not* in the ephemeris Spice kernel

In both cases, a user should load additional Spice kernels. This can be done using the :func:`~tudatpy.interface.spice.load_kernel`. Spice kernels for many bodies may be found in a number of places. The 'goto' place for Spice kernels for ephemerides is the NAIF website (developers of Spice), which you can find `here <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/>`_.

Use of scaled models
--------------------

For a sensitivity analysis (among others) it may be useful to modify the ephemeris of a body, for instance to emulate the influence of a 1 km offset in the state provided by the nominal ephemeris. Unlike most other environment models, this cannot be achieved (at least not for most types of ephemerides) by modifying a single defining parameter of the model. Instead, we provide the functions 
:func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector` and :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector_function`, which take nominal ephemeris settings, and add a user-defined variation (constant or time-varying; absolute or relative) to the inertial Cartesian state elements produced by the ephemeris.

Gravity fields
==============

There are two options in Tudat for creating either a spherical harmonic gravity field, and a point mass gravity field:

* Point mass: defining the gravitational parameter manually (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central`) or requiring the gravitional parameter to be extracted from Spice (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central_spice`).
* Spherical harmonics: defining all the settings manually (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic`) or calculating the spherical harmonic coefficients (up to a given degree) based on an ellipsoidal homogeneous mass distribution (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic_triaxial_body`)

Wind models
===========

Wind models may be added to an atmosphere model by using the :attr:`~tudatpy.numerical_simulation.environment_setup.atmosphere.AtmosphereSettings.wind_settings` attribute of the atmosphere settings, as in the following example:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/adding_wind.py
             :language: python

Here, a wind vector in the positive z-direction of the vertical frame (downward) of 10 m/s is added, using the :attr:`~tudatpy.numerical_simulation.environment_setup.atmosphere.constant_wind_model`.
            
By default, an atmosphere has 'zero wind', which means that the atmosphere corotates with the body. A user may add a wind model to this atmosphere model, which will modify the freestream velocity that a vehicle in the atmosphere experiences/



