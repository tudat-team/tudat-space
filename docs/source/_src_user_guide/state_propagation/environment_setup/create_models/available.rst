.. _available_environment_models:

==============================
Available Environment Models
==============================

.. contents:: List of available environment models
   :depth: 2
   :local:


.. _environment_ephemeris_model:

################
Ephemeris
################

Ephemeris model settings are intended to be assigned to the ``ephemeris_settings`` property of a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object.
For code examples and additional (model) information, please follow the links to the API documentation.


| **Direct Spice Ephemeris**
| Spice ephemeris models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.direct_spice` function.


| **Interpolated Spice Ephemeris**
| Interpolated Spice ephemeris models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.interpolated_spice` function.


| **Approximate JPL Ephemeris**
| Approximate planet ephemeris models (from `JPL model <https://ssd.jpl.nasa.gov/planets/approx_pos.html>`_) can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.approximate_jpl_model` function.


| **Constant Ephemeris**
| Constant ephemeris models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.constant` function.


| **Custom Ephemeris**
| Custom ephemeris models from tabulated data can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.custom` function.


| **Kepler Ephemeris**
| Kepler ephemeris models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.keplerian` function.


| **Kepler Ephemeris from Spice**
| Kepler ephemeris models from Spice can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.keplerian_from_spice` function.


| **Scaled Ephemeris**
| Ephemeris models can be scaled via either of the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_constant`, :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector`, :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector_function` functions.


| **Tabulated Ephemeris**
| Ephemeris models from tabulated data can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.tabulated` function.



.. _environment_gravity_field_model:

####################
Gravity Field
####################

Gravity field model settings are intended to be assigned to the ``gravity_field_settings`` property of a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object.
For code examples and additional (model) information, please follow the links to the API documentation.

| **Point Mass Gravity**
| Point-mass gravity field models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central` function.


| **Point Mass Gravity from Spice**
| Point-mass gravity field models using the gravitational parameter from Spice data can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central_from_spice` function.


| **Spherical Harmonics Gravity**
| Spherical harmonics gravity field models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic` function.


| **Spherical Harmonics Gravity - Triaxial body**
| Spherical harmonics gravity field models derived from homogenous, triaxial bodies can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic_triaxial_body` function.



.. _environment_atmosphere_model:

#################
Atmosphere
#################

Atmosphere model settings (which include wind model settings) are to be assigned to the atmosphere_settings property of a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object.
Atmosphere models describe other atmospheric conditions such as local density, temperature and pressure and their settings objects can be matched directly with the ``atmosphere_settings`` property.
Wind models can be used to retrieve local wind vectors and their settings objects must be assigned to the ``wind_settings`` member of the ``atmosphere_settings`` property (i.e. ``BodySettings.atmosphere_settings.wind_settings``)
For code examples and additional (model) information, please follow the links to the API documentation.


| **Constant Wind Model**
| Constant wind models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.constant_wind_model` function.


| **Custom Wind Model**
| Custom wind models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_wind_model` function.


| **Predefined Exponential Atmosphere**
| Exponential atmosphere models from predefined settings can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.exponential_predefined` function.


| **Exponential Atmosphere**
| Exponential atmosphere models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.exponential` function.


| **NRLMSISE-00**
| NRLMSISE-00 atmosphere models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.nrlmsise00` function.


| **Custom Constant Temperature Atmosphere**
| Custom atmosphere models with custom one-dimensional density profile, constant temperature and composition can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_constant_temperature` function.


| **Custom Four-Dimensional Constant Temperature Atmosphere**
| Custom atmosphere models with custom four-dimensional density profile, constant temperature and composition can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_four_dimensional_constant_temperature` function.


| **Scaled Atmosphere Model**
| Atmosphere models can be scaled via either of the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.scaled_by_constant`, :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.scaled_by_function` functions.




.. _environment_shape_model:

#################
Body Shape
#################

Shape model settings are intended to be assigned to the ``shape_settings`` property of a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object.
For code examples and additional (model) information, please follow the links to the API documentation.


| **Spherical Body Shape**
| Spherical body shape models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.shape.spherical` function.


| **Spherical Body Shape from Spice**
| Spherical body shape models can be created from Spice data via the :func:`~tudatpy.numerical_simulation.environment_setup.shape.spherical_spice` function.


| **Oblate Spherical Body Shape**
| Oblate spherical body shape models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.shape.oblate_spherical` function.




.. _environment_rotational_model:

#################
Rotational
#################

Shape model settings are intended to be assigned to the ``rotation_model_settings`` property of a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object.
For code examples and additional (model) information, please follow the links to the API documentation.


| **Simple Rotation Model**
| Simple rotation models (constant rotation rate, fixed rotation axis) can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.simple` function.


| **Simple Rotation Model from Spice**
| Simple rotation models (constant rotation rate, fixed rotation axis) can be created from Spice data via the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.simple_from_spice` function.


| **Synchronous Rotation Model**
| Synchronous rotation models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.synchronous` function.


| **Spice Rotation Model**
| Rotation models (non-simplified) from Spice can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.spice` function.


| **Gcrs to Itrs Rotation Model**
| High-accuracy Earth rotation models (Gcrs to Itrs) can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.gcrs_to_itrs` function.


| **Constant Rotation Model**
| Constant rotation models (single time-invariant rotation matrix) can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.constant` function.




.. _environment_aerodynamic_coefficient_interface:

##################################
Aerodynamic Coefficient Interfaces
##################################

Aerodynamic coefficient settings are intended to be used by the :func:`~tudatpy.numerical_simulation.environment_setup.add_aerodynamic_coefficient_interface` function,
which creates and assigns aerodynamic coefficient interfaces to the specified artificial bodies.
For code examples and additional (model) information, please follow the links to the API documentation.

| **Constant Aerodynamic Coefficient**
| Constant (not a function of any independent variables) aerodynamic coefficient settings can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.constant` function.


| **Custom Aerodynamic Coefficient**
| Custom aerodynamic coefficient settings can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.custom` function.


| **Tabulated Aerodynamic Coefficient**
| Aerodynamic coefficient settings can be created from tabulated data via the :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.tabulated` function.


| **Tabulated Force Only Aerodynamic Coefficient**
| Aerodynamic coefficient settings can be created from tabulated force coefficient data via the :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.tabulated_force_only` function.


| **Scaled Atmosphere Model**
| Aerodynamic coefficient settings can be scaled via either of the :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.scaled_by_constant`, :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.scaled_by_function`, :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.scaled_by_vector_function` functions.



.. _environment_radiation_pressure_interface:

#############################
Radiation Pressure Interfaces
#############################

Radiation pressure interface settings are intended to be used by the :func:`~tudatpy.numerical_simulation.environment_setup.add_radiation_pressure_interface` function,
which creates and assigns radiation pressure interfaces to the specified artificial bodies.
For code examples and additional (model) information, please follow the links to the API documentation.

| **Cannonball Radiation Pressure**
| Radiation pressure interface settings for a cannonball model can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.cannonball` function.


| **Panelled Radiation Pressure**
| Radiation pressure interface settings for a panelled model can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.radiation_pressure.panelled` function.
