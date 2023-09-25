.. _radiation_pressure_acceleration:

================================
Radiation pressure acceleration
================================

Radiation pressure arises from the exchange of momentum between electromagnetic radiation and the spacecraft. In Tudat, radiation pressure accelerations require models for sources (how radiation is emitted) and targets (how the spacecraft is accelerated depending on the incident radiation). For more details on the mathematical models, see `this paper <http://resolver.tudelft.nl/uuid:8a82400a-2233-4a84-98be-ed37f7eeb620>`_.

.. contents:: Contents:
    :depth: 3




Radiation source models
========================
In most orbits, there are two sources of radiation: direct solar radiation, and albedo + thermal radiation of the central body (particularly in low orbits). Both require different treatment. Therefore, there are two source models in Tudat.


Isotropic point source
------------------------
The radiation due to an isotropic point source depends only on the distance, not on the spherical position. If the source is far away, all rays are virtually parallel. This is, for example, the case for solar radiation at 1 AU. The default source model for the sun is such a point source with a luminosity of 3.828 × 10\ :sup:`26` W. The luminosity can also be given as irradiance at a given distance (e.g., as total solar irradiance/TSI).

.. tabs::

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/radiation_source_point.cpp
         :language: cpp


Extended source
------------------------
Planetary radiation is generally not isotropic and the spacecraft is relatively close to the surface. Therefore, the central body is modeled as extended source, which is discretized into panels. Each panel emits radiation as defined by a radiosity model. Usually, these include albedo radiation (reflected solar radiation) and thermal radiation (due to surface heating). This model was described by Knocke et al. [Knocke1988]_.

Albedo and thermal radiosity models require an original source, the radiation of which is reflected or re-radiated. Therefore, the Sun body needs to be added if Earth or Moon radiation is used.

.. tabs::

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/radiation_source_extended.cpp
         :language: cpp




Radiation pressure target models
=================================
The spacecraft acceleration due to radiation pressure depends on the cross-section area, optical properties, and mass. The dependence on the area-to-mass ratio is similar to drag. Optical properties are relevant since reflected radiation imparts more momentum than absorbed radiation. There are two target models in Tudat.


Cannonball target
------------------
A cannonball models the spacecraft as isotropic sphere defined by the cross-section area and a radiation pressure coefficient. This model is useful for estimation, but cannot capture changing geometry and orientation, which can have large effects on accelerations.

.. tabs::

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/radiation_pressure_target_cannonball.cpp
         :language: cpp


Paneled target
------------------
A paneled target can account for the spacecraft geometry. The cross-section and optical properties can vary with attitude. This is particularly important for asymmetric spacecraft or when a solar array tracks the Sun. Optical surface properties are given by the specular and diffuse reflectivity coefficients.

.. tabs::

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/radiation_pressure_target_paneled.cpp
         :language: cpp



.. [Knocke1988] Knocke et al., (1988). Earth radiation pressure effects on satellites.
   American Institute of Aeronautics and Astronautics, Astrodynamics Conference, https://doi.org/10.2514/6.1988-4292.

