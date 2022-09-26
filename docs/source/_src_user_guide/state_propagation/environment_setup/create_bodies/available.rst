
.. _environment_model_overview:

==================
Environment Models
==================

On this page, we provide an overview of the categories of environment models that are available (with links to API documentation), as well as some general notes on their usages, typical pitfalls, hints, etc.

.. _available_environment_models:

Available Model Types
=====================

The complete list of available environment model settings can be found on our API documentation. Below is a list with the different categories of models, and a link to the corresponding Tudatpy module

* `Aerodynamic coefficients <https://py.api.tudat.space/en/latest/aerodynamic_coefficients.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.aerodynamic_coefficient_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. 

   * These models provide various ways in which to define aerodynamics force (and if required, moment) coefficients of a body.

* `Atmosphere models <https://py.api.tudat.space/en/latest/atmosphere.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.atmosphere_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  

   * These models provide various ways in which to define atmospheric properties of a body. For state propagation, the density will typically be the most important one. However, many of the models here include outputs of temperature, density, etc. as well. Depending on the model, the atmospheric properties may be only altitude-dependent, or fully time- and position-dependent. Note that the atmosphere settings can include wind settings (default: none)

* `Ephemeris models <https://py.api.tudat.space/en/latest/ephemeris.html>`_, , to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.ephemeris_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  
  
   * These models provide various ways in which to define predetermined (e.g. not coming from a Tudat propagation) translational states of bodies in the solar system
  
* `Gravity field models <https://py.api.tudat.space/en/latest/gravity_field.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.gravity_field_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  

   * These models provide various ways in which to define the gravitational field of solar system bodies. Note: the mass associated with these gravitational field is the gravitational mass, which does *not* need to be equal to its inertial mass.
  
* `Gravity field variation models <https://py.api.tudat.space/en/latest/gravity_field_variation.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.gravity_field_variation_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. Note: this attribute is a list, and any number of variation models may be added.  

   * These models provide various ways in which to define the time-variability of a body's (spherical harmonic) gravitaty field.
  
* `Rotation models <https://py.api.tudat.space/en/latest/rotation_model.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.rotation_model_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. 

   * These models provide various ways in which to define the orientation of a body w.r.t. inertial space, and produces a quaternion/rotation matrix, and angular velocity vector/rotation matrix derivative. Note that Tudat can also produce such models by numerical propagation of the Euler equations (see :ref:`rotational_dynamics`).
  
* `Shape models <https://py.api.tudat.space/en/latest/shape.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.shape_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. 

   * These models provide various ways in which to define the exterior of a *natural* body and is typically used to calculate (for instance) altitude, ground station position, etc. Note: the exterior shape of an artificial body, from which aerodynamic and radiation pressure properties can be evaluated, uses a different interface, which is currently under development

* `Radiation pressure <https://py.api.tudat.space/en/latest/radiation_pressure.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.rotation_model_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. Note: this attribute is a dictionary, with one radiation pressure model per source body. 

   * These models provide various ways in which to define the response of a body to incident radation pressure.

.. _specific_environment_considerations:


Points of attention
===================

On this page, we give an overview of some specifica aspects of the environment models that may be useful for a user to
know, in order to properly select and understand their choice of environment models.
This page is meant to supplement the API documentation, and is *not* a comprehensive overview of all environment models.


Aerodynamic coefficients
------------------------

See the section on :ref:`aerodynamic coefficients during the propagation <aerodynamics_during_propagation>`
concerning a number of points of attention regarding the aerodynamic coefficients, concerning the frame in which
they are defined.


Ephemeris models
----------------

**Spice-based models** For many typical applications, natural body ephemerides will be calculated from :ref:`Spice kernels <spice_in_tudat>`.
In some cases, a user may find that the default Spice kernels are insufficient for their purposes, due to one of two reasons:

* The body for which the state is required *is* in the ephemeris Spice kernel, but the time at which the state is needed lies outside of the bounds for which the Spice kernel has data
* The body for which the state is required *is not* in the ephemeris Spice kernel

In both cases, a user should load additional Spice kernels. This can be done using the :func:`~tudatpy.interface.spice.load_kernel`. Spice kernels for many bodies may be found in a number of places.
The 'goto' place for Spice kernels for ephemerides is the NAIF website (developers of Spice), which you can find
`here <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/>`_.

**Use of scaled models** For a sensitivity analysis (among others) it may be useful to modify the ephemeris of a body, for instance
to emulate the influence of a 1 km offset in the state provided by the nominal ephemeris. Unlike most other environment models,
this cannot be achieved (at least not for most types of ephemerides) by modifying a single defining parameter of the model.
Instead, we provide the functions
:func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector` and
:func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector_function`,
which take nominal ephemeris settings, and add a user-defined variation (constant or time-varying; absolute or relative) to the
inertial Cartesian state elements produced by the ephemeris.


Gravity fields
--------------

Unlike most other environment model options in Tudat, there are multiple options for creating either a spherical harmonic gravity field, and a point mass gravity field:

* Point mass: defining the gravitational parameter manually (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central`) or requiring the gravitational parameter to be extracted from Spice (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central_spice`).
* Spherical harmonics: defining all the settings manually (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic`), loading a pre-defined model for a soalr system body (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.from_file_spherical_harmonic`) or calculating the spherical harmonic coefficients (up to a given degree) based on an ellipsoidal homogeneous mass distribution (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic_triaxial_body`)

Polyhedron models
-----------------
A polyhedron can be used to define both gravity (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.polyhedron_from_gravitational_parameter`)
and shape (:func:`~tudatpy.numerical_simulation.shape.gravity_field.polyhedron`) models. Since both models tend to be computationally intensive (the gravity
model more so), it is recommended to use polyhedra with the lowest number of facets that allows meeting the desired accuracy. The number of facets of a polyhedron
model can be reduced using any mesh processing software, for example `PyMeshLab <https://pymeshlab.readthedocs.io/en/latest/>`_.
Additionally, different functions to process a polyhedron are available in `Polyhedron utilities <https://py.api.tudat.space/en/latest/polyhedron_utilities.html>`_.

Inertia tensor
--------------

TODO: write documentation

Rotation models
---------------

Tudat has a broad range of rotation models available. In principle, these models can be assigned to both celestial bodies and natural bodies. 
However, a subset of these models is typically only applied to natural *or* artificial bodies. Rotation models have a wide range of,
sometimes indirect, influences on the dynamics

* A spherical harmonic acceleration exerted by a central body is first evaluated in a body-fixed frame, and the transformed to an inertial frame. Consequently, the central body's rotation has a fundamental influence on the exerted spherical harmonic acceleration
* A :ref:`thrust acceleration <thrust_models>` in Tudat is calculated from two models: (1) an engine model, which defined the body-fixed direction of the thrust, and the magnitude of the thrust (2) the orientation of the body in space, defined by its rotation model
* For a non-spherical central body shape models, the current orientation of this central body has an indirect influence on the altitude at which a vehicle with a given *inertial* state is located

Two rotation models, which are typically used for vehicles under :ref:`thrust <thrust_models>`, and/or vehicles undergoing :ref:`aerodynamic forces <aerodynamic_models>`, are the following:

* The rotation model :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`, which calculates the body's rotation based on the angle of attack, sideslip angle and bank angle. Note that these angles are definend w.r.t. the relative wind. This model is typical when using, for instance, a re-entry simulation. It imposes these three angles, and calculates the body orientation by combination with the latitude, longitude, heading angle, flight path angles. There is a related model, :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.zero_pitch_moment_aerodynamic_angle_based`, that uses the same setup, but does not impose the angle of attack, but caculates by imposing aerodynamic pitch trim (zero pitch moment).
* The rotation model :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_inertial_direction_based`, which is typical when calculating dynamics of a vehicle under thrust. It is based on linking a body-fixed  direction (now limited to the body-fixed x-axis) to an arbitrary inertial direction. This allows the thrust (assuming that this is aligned with this same body-fixed direction) to be guided in an inertial direction determined by a user-defined model. 

Wind models
-----------

Wind models may be added to an atmosphere model by using the :attr:`~tudatpy.numerical_simulation.environment_setup.atmosphere.AtmosphereSettings.wind_settings` attribute of the atmosphere settings, as in the following example:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/adding_wind.py
             :language: python

Here, a wind vector in the positive z-direction of the :ref:`vertical frame<aero_frames>` (downward) of 10 m/s is added, using the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.constant_wind_model`.
            
By default, an atmosphere has 'zero wind', which means that the atmosphere corotates with the body. A user may add a wind model to this atmosphere model, which will modify the freestream velocity that a vehicle in the atmosphere experiences




