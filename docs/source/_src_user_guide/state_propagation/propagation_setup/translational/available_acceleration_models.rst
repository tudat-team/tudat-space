.. _available_acceleration_models:

===============================
Available Acceleration Models
===============================

In this page, all the acceleration models available in Tudat are explained. Regardless of the type of acceleration
model, the procedure to link such acceleration model to the bodies exerting and undergoing the acceleration is
explained in this page: :ref:`acceleration_models_setup`. Therefore, this information will not be repeated in this
page. Instead, for each model, a reference to the related API documentation entry and the requirements are provided.


.. note::
   In Tudat, acceleration models are defined through factory functions, which define the properties required of
   the accelerations, but do not perform any calculations themselves. These properties are stored through instances
   of the :class:`~tudatpy.numerical_simulation.propagation_setup.acceleration.AccelerationSettings` class or of its 
   derived classes.


.. contents:: List of available acceleration models
   :depth: 1
   :local:

In certain pieces of code, such as when requesting the saving of a single acceleration (see :ref:`dependent_variables`
for saving of dependent variables), you will need to supply an identifier for the type of acceleration you are requesting.
See the list of supported identifier types in the API documentation: :class:`~tudatpy.numerical_simulation.propagation_setup.acceleration.AvailableAcceleration`.

###########################
Gravitational
###########################

Tudat contains a number of different models for gravitational accelerations. In general, the gravitational
acceleration exerted by a body B, with associated potential :math:`U_{B}`, on a body A can be expressed as follows:

.. math::
    \mathbf{a}_{_{BA}}=\nabla U_{_{B}}\left(\mathbf{r}_{_{BA}}\right)

with :math:`\mathbf{r}_{_{BA}}(=\mathbf{r}_{_{B}}-\mathbf{r}_{_{A}})` denoting the relative position vector of body A
with respect to Body B.

There are different gravitational models available in Tudat:

- :ref:`point_mass_acceleration`
- :ref:`spherical_harmonic_acceleration`
- :ref:`mutual_spherical_harmonic_acceleration`
- :ref:`third_body_gravity`

These are explained in more detail below.

.. _point_mass_acceleration:

Point Mass Gravity
##################

| **Description**
| The point-mass gravity acceleration model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.point_mass_gravity`
  factory function.

| **Dependencies**
| 1. Gravity field for body exerting acceleration (see `Gravity field models <https://py.api.tudat.space/en/latest/gravity_field.html>`_ for non-default models).
| 2. Current state of body exerting acceleration, either from a pre-defined ephemeris model (see
     `Ephemeris models <https://py.api.tudat.space/en/latest/ephemeris.html>`_) or from the numerical propagation of the translational dynamics of the body
     exerting the acceleration.


.. _spherical_harmonic_acceleration:

Spherical Harmonic Gravity
##########################

| **Description**
| The spherical harmonic gravity acceleration model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.spherical_harmonic_gravity`
  factory function.

| **Dependencies**
| 1. Spherical harmonic gravity field for the body exerting acceleration. See `Gravity field models <https://py.api.tudat.space/en/latest/gravity_field.html>`_ for
  options on how to define one (if the default gravity field model of the exerting body is not spherical harmonic).
| 2. Rotation model from the inertial frame to the body-fixed frame, either from a pre-defined rotation model
  (`Rotation models <https://py.api.tudat.space/en/latest/rotation_model.html>`_) or from the numerical propagation of the rotational dynamics of the body
  exerting the acceleration (Earth in the above example).
| 3. Current state of body exerting acceleration, either from a pre-defined ephemeris model
  (see `Ephemeris models <https://py.api.tudat.space/en/latest/ephemeris.html>`_) or from the numerical propagation of the translational dynamics of the body
  exerting the acceleration (Earth in the above example).

.. note::
  The spherical harmonic acceleration up to degree N and order M includes the point-mass gravity acceleration
  (which is the degree and order 0 term).

.. _mutual_spherical_harmonic_acceleration:

Mutual Spherical Harmonic Gravity
##############################################


| **Description**
| The mutual spherical harmonic gravity acceleration model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.mutual_spherical_harmonic_gravity`
  factory function. This model is typically only used for detailed propagation of planetary systems. With additional
  parameters, it can
  be used even if the bodies mutually exerting the spherical harmonic gravity acceleration are not the central body.


| **Dependencies**
| 1. Spherical harmonic gravity field for body exerting acceleration and body undergoing acceleration (see
  `Gravity field models <https://py.api.tudat.space/en/latest/gravity_field.html>`_ for non-default models).
| 2. Rotation model from the inertial frame to the body-fixed frame and body undergoing acceleration (see
  `Rotation models <https://py.api.tudat.space/en/latest/rotation_model.html>`_ for non-default models).
| 3. Current state of bodies undergoing and exerting acceleration, either from an Ephemeris model or from the numerical
  propagation (see `Ephemeris models <https://py.api.tudat.space/en/latest/ephemeris.html>`_).


.. _third_body_gravity:

Third Body Gravity vs. Central Gravity
#######################################

| **Description**
| In addition to the three models listed above, which define different models for gravitational interactions between two
  bodies, you can of course define a **third-body acceleration**. In Tudat, however, you do *not* specify directly
  whether an
  acceleration is a 'third-body' acceleration. This is fully defined by what you've chosen as your center of propagation
  (see :ref:`translational_dynamics`), and the bodies exerting and undergoing the acceleration. Similarly, when
  calculating the dynamics of a massive body, a correction is required for expressing the gravitational acceleration
  exerted by the propagation origin (*e.g.* acceleration exerted by Earth on Moon, with Earth as propagation origin).
  We term this the 'central' acceleration.

| **Dependencies**
| The same for each gravitational acceleration type.

.. seealso::
   For more details: :ref:`third_body_acceleration`.

########################
Aerodynamic
########################

| **Description**
| The aerodynamic acceleration model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.aerodynamic`
  factory function.

| **Dependencies**
| 1. Atmosphere model for body exerting acceleration (see `Atmosphere models <https://py.api.tudat.space/en/latest/atmosphere.html>`_).
| 2. Aerodynamic coefficient interface for body undergoing acceleration (see
  `Aerodynamic coefficients <https://py.api.tudat.space/en/latest/aerodynamic_coefficients.html>`_).
| 3. Mass model for body undergoing acceleration.
| 4. Current state of body undergoing acceleration and body with atmosphere.
| 5. Shape model for the body exerting an acceleration (to allow for the calculation of vehicle altitude)
| 6. Roation model for the body undergoing an acceleration (or numerical propagation of this body's rotational dynamics)

.. note::
   The aerodynamic acceleration is calculated in the vehicles body-fixed or aerodynamic frame. Expressing the
   acceleration in an inertial frame (as required by the propagation) requires the vehicle's orientation to be defined.
   For a simple definition, in which the body’s angle of attack, sideslip angle, and bank angle are all set to 0, see
   :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`.

   More details on aerodynamic guidance can be found on :ref:`this page <aerodynamic_models>`.

#############################
Radiation Pressure
#############################

..
  TODO-RP change to single acceleration model, link to _radiation_pressure_acceleration

There are two different radiation pressure models available in Tudat:

- :ref:`cannonball_radiation_pressure`
- :ref:`panelled_radiation_pressure`

The distinction between them lies in the type of radiation pressure interface that is used for the body undergoing
acceleration (see below).

.. _cannonball_radiation_pressure:

Cannonball Radiation Pressure
#############################

| **Description**
| The cannonball radiation pressure model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.cannonball_radiation_pressure`
  factory function.

| **Dependencies**
| 1. Cannonball radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration), see `Radiation pressure <https://py.api.tudat.space/en/latest/radiation_pressure.html>`_.
| 2. Current state of body undergoing and body emitting radiation.


.. _panelled_radiation_pressure:

Panelled Radiation Pressure
###########################

| **Description**
| The panelled radiation pressure model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.panelled_radiation_pressure`
  factory function.


| **Dependencies**
| 1. Panelled radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration), see `Radiation pressure <https://py.api.tudat.space/en/latest/radiation_pressure.html>`_.
| 2. Current state of body undergoing and body emitting radiation.


####################################
Relativistic Correction
####################################

| **Description**
| The relativistic correction acceleration model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.relativistic_correction`
  factory function. This is a first-order (in 1/c^2) correction to the acceleration due to the influence of relativity
  for a massless body (e.g. spacecraft) orbiting a massive body (e.g. Earth), which in turn orbits a third body (e.g.
  Sun), consisting of three distinct effects: the Schwarzschild, Lense-Thirring and de Sitter accelerations.

| **Dependencies**
| 1. Mass of the orbited body and the third body (de Sitter only)
| 2. Current state of body undergoing acceleration, the orbited body, and the third body (de Sitter only)

- Mass of the orbited body and the third body (de Sitter only)
- Current state of body undergoing acceleration, the orbited body, and the third body (de Sitter only)

#######################
Empirical
#######################

| **Description**
| The empirical acceleration model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.empirical`
  factory function. This is constant/once-per-orbit acceleration, expressed in the RSW frame (see for instance
  :func:`~tudatpy.astro.frame_conversion.inertial_to_rsw_rotation_matrix`), for which the magnitude is determined
  empirically (typically during an orbit determination process).

| **Dependencies**
| 1. Gravity field of the central body (for calculation of true anomaly).

######
Thrust
######

| **Description**
| The thrust acceleration model can be created through one of the factory functions:

  * :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_engine` (use single specific engine)
  * :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_engines` (use multiple specific engines)
  * :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_all_engines` (use all engines)

  Which differ only in the manner in which the user selects the engine model(s) this is(are) to be used for calculating the thrust.
  The details of the model used for the thrust is given on a :ref:`dedicated page <thrust_acceleration_setup>`

| **Dependencies**
| 1. One or more engine models for the body under thrust
| 2. A rotation model for the body under thrust
| 3. Mass of the body under thrust (if the thrust magnitude model for the engine defines a force, and not an acceleration)

##################################
Tidal effect on natural satellites
##################################

| **Description**
| The acceleration accounting for the tidal effect on natural satellites can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.direct_tidal_dissipation_acceleration`
  factory function. It is a rather specialist model, which is only relevant for the dynamics of natural satellites
  themselves. When calculating the dynamics of spacecraft orbiting natural satellites, use gravity field variations
  instead. Two types of accelerations can be computed: acceleration on the satellite due to tide on the planet, or
  acceleration on the satellite due to tide on the satellite.

| **Dependencies**
| 1. Masses of planet and satellite.
| 2. Current state of planet and satellite.
| 3. Spherical harmonic gravity field for body on which the tide is raised (planet or satellite)
| 4. Planet rotation model (only for effect of tide on planet)

#################################
Quasi-Impulsive Shot
#################################

| **Description**
| The acceleration accounting for the tidal effect on natural satellites can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.quasi_impulsive_shots_acceleration`
  factory function. This is a manner in which to incorporate short bursts of thrust into a numerical propagation.
  When using this model, ensure that your integration step is sufficiently small to be able to capture the burst of
  thrust.

| **Dependencies**
| None.

