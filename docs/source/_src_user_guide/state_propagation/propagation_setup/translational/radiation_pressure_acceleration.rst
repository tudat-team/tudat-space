.. _radiation_pressure_acceleration:

================================
Radiation pressure acceleration
================================

Radiation pressure arises from the exchange of momentum between electromagnetic radiation and the spacecraft.
In Tudat, radiation pressure accelerations require models for sources (how radiation is emitted) and targets
(how the spacecraft is accelerated depending on the incident radiation). Here, the 'source' may also be a body
that reflects light from another body (e.g. albedo). Both sources and targets may be defined in any number of ways.
Regardless of how the source and target models are defined, creating the acceleration model for them is always done
in the same manner, using the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.radiation_pressure`,
which takes the source model of the body exerting the acceleration, and the target model of the body undergoing the
acceleration, and links these models to set up the specific acceleration model.
For extensive details on the mathematical
models, see `this paper <http://resolver.tudelft.nl/uuid:8a82400a-2233-4a84-98be-ed37f7eeb620>`_.

.. contents:: Contents:
    :depth: 3




Radiation source models
========================
In most orbits, there are two sources of radiation: direct solar radiation, and albedo + thermal radiation of the
central body (particularly in low orbits). Both require different treatment. Therefore, there are two source models in Tudat.
Settings for a body are defined in the ``radiation_source_settings`` attribute of the :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` class


Isotropic point source
------------------------
The radiation due to an isotropic (point) source depends only on the distance from the source, not on the relative latitude/longitude
If the source is far away, all rays hitting the target are virtually parallel. This is, for example, the case for solar radiation at 1 AU.
The default source model for the Sun is such a point source with a luminosity of 3.828 × 10\ :sup:`26` W. Defining settings for an
isotropic source model is done using the :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.isotropic_radiation_source`
function, which requires a luminosity model. These may be defined by one of the following models:

  * User-defined constant luminosity: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.constant_luminosity`
  * User-defined time-variable luminosity: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.time_variable_luminosity`
  * User-defined constant irradiance at a reference distance (e.g., as total solar irradiance at 1 AU).: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.irradiance_based_constant_luminosity`
  * User-defined time-variable irradiance at a reference distance: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.irradiance_based_time_variable_luminosity`

Defining the second to last option, for a solar irradiance of 1367 W/m:sup:`2` at 1 AU, the settings for the body called 'Sun' would be modified as follows:

.. code-block:: python

    solar_luminosity_settings = radiation_pressure.irradiance_based_constant_luminosity( 1367.0, constant.AU )
    body_settings.get( "Sun" ).radiation_source_settings = radiation_pressure.isotropic_radiation_source( solar_luminosity_settings )


Extended source
------------------------
Planetary radiation is generally not isotropic and the spacecraft is relatively close to the surface.
Therefore, the central body is modeled as an extended source, which is discretized into panels.
This model was described by Knocke et al. [Knocke1988]_. Each panel emits radiation as defined by a radiosity model.
Typically, these include albedo radiation (reflected solar radiation) and/or thermal radiation (due to surface heating).

The following options are supported for defining surface radiosity models:

  * Globally constant radiosity: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.constant_radiosity`
  * Radiosity due to a globally constant albedo: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.constant_albedo_surface_radiosity`
  * Radiosity due to an albedo that varies over the surface (requires a surface distribution model, see below): :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.variable_albedo_surface_radiosity`
  * Radiosity due to thermal radiation from an isotropically heated source with constant emissivity: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.thermal_emission_blackbody_constant_emissivity`
  * Radiosity due to thermal radiation from an isotropically heated source with an emissivity that varies over the surface (requires a surface distribution model, see below): :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.thermal_emission_blackbody_constant_emissivity`
  * Radiosity due to thermal radiation from a heated blackbody source with a surface temperature defined from the angle to the sub-solar point (assuming the Sun is the body causing the heating): :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.thermal_emission_angle_based_radiosity`

For a number of the above models, a surface distribution of a property has to be defined (e.g. albedo, emissivity). A number of options are available for this:

  * Globally constant surface distribution: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.constant_surface_property_distribution`
  * Surface distribution defined by spherical harmonics: :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.spherical_harmonic_surface_property_distribution`, or :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.predefined_spherical_harmonic_surface_property_distribution`
  * Surface distribution as per Knocke et al. [Knocke1988]_ (degree-two zonal spherical harmonic definition, with time-variable degree-one coefficient): :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.knocke_type_surface_property_distribution`, or :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.predefined_knocke_type_surface_property_distribution`

For each of the above options, the surface
The fidelity increases with the number of panels, which are arranged into rings. Convergence tests are recommended to
find a sufficient number of rings. Commonly used numbers of rings: LAGEOS: 2 rings for Earth; LRO: 5-6 rings for the Moon.

Albedo and thermal radiosity models require an original source, the radiation of which is reflected or re-radiated.
Therefore, the Sun body needs to be added if Earth or Moon radiation is used. Intrinsic sources (e.g., due to tidal
heating or from flux observations) do not require an original source. However, the corresponding class
(``CustomInherentSourcePanelRadiosityModel``) is not exposed yet.

.. tabs::

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/radiation_source_extended.cpp
         :language: cpp



Radiation pressure target models
=================================
The spacecraft acceleration due to radiation pressure depends on the cross-section area, optical properties, and mass.
The dependence on the area-to-mass ratio is similar to drag. Optical properties are relevant since reflected radiation
imparts more momentum than absorbed radiation. There are two target models in Tudat.


Cannonball target
------------------
A cannonball models the spacecraft as isotropic sphere defined by the cross-section area and a radiation
pressure coefficient. This model is useful for parameter estimation, but typically cannot capture changing
geometry and orientation, which can have large effects on accelerations.

.. tabs::

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/radiation_pressure_target_cannonball.cpp
         :language: cpp


Paneled target
------------------
A paneled target can account for the spacecraft geometry. The cross-section and optical properties can vary with attitude.
This is particularly important for asymmetric spacecraft or when a solar array tracks the Sun. Optical surface properties
are given by the specular and diffuse reflectivity coefficients.

.. tabs::

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/radiation_pressure_target_paneled.cpp
         :language: cpp



Dependent variables
=================================
There is a number of dependent variables associated with radiation pressure acceleration:

* ``singleAccelerationDependentVariable(radiation_pressure, "TargetBody", "SourceBody")``: Cartesian vector of acceleration in propagation frame
* ``receivedIrradianceDependentVariable("TargetBody", "SourceBody")``: received irradiance by target due to source (in W/m²)

For point source only:

* ``receivedFractionDependentVariable("TargetBody", "SourceBody")``: received fraction of irradiance, given ny shadow function (between 0 and 1)

For extended source only:

* ``visibleAndEmittingSourcePanelCountDependentVariable("TargetBody", "SourceBody")``: number of source panels contributing to irradiance at target
* ``visibleSourceAreaDependentVariable("TargetBody", "SourceBody")``: total area of source panels contributing to irradiance at target



Assumptions
============================
Some assumptions are made for radiation pressure models:

* The paneled target is much smaller than the extended source and far enough away. Therefore, all target panels receive the same irradiance, from the same direction. The source irradiance is evaluated at the target center.
* The extended source far enough away from the original source (e.g., 1 AU for Earth and Sun). Therefore, the panels of the extended source receive the same irradiance, from the same direction. The original source irradiance is evaluated at the source center.
* The extended source is a perfect sphere, and not an oblate spheroid. Panels are distributed on the perfect sphere.



.. [Knocke1988] Knocke et al., (1988). Earth radiation pressure effects on satellites.
   American Institute of Aeronautics and Astronautics, Astrodynamics Conference, https://doi.org/10.2514/6.1988-4292.

