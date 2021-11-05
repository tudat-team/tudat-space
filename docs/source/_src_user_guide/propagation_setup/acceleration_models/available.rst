.. _available_acceleration_models:

===============================
Available Acceleration Models
===============================

In this page, all the acceleration models available in TudatPy are explained. Regardless of the type of acceleration
model, the procedure to link such acceleration model to the bodies exerting and undergoing the acceleration is
explained in this page: :ref:`Acceleration Model Setup`. Therefore, this information will not be repeated in this
page. Instead, for each model, a reference to the related API entry and the requirements are provided.


.. note::
   In tudat(py), acceleration models are defined through factory functions, which define the properties required of
   the accelerations, but do not perform any calculations themselves. These properties are stored through instances
   of the
   ``AccelerationSettings`` class (see `API <https://tudatpy.readthedocs.io/en/latest/acceleration.html#tudatpy
   .numerical_simulation.propagation_setup.acceleration.AccelerationSettings>`_) or of its derived classes.


.. contents:: List of available acceleration models
    :depth: 3

###########################
Gravitational accelerations
###########################

Tudat(py) contains a number of different models for gravitational accelerations. In general, the gravitational
acceleration exerted by a body B, with associated potential :math:`U_{B}`, on a body A can be expressed as follows:

.. math::
    \mathbf{a}_{_{BA}}=\nabla U_{_{B}}\left(\mathbf{r}_{_{BA}}\right)

with :math:`\mathbf{r}_{_{BA}}(=\mathbf{r}_{_{B}}-\mathbf{r}_{_{A}})` denoting the relative position vector of body A
with respect to Body B.


.. _point_mass_acceleration:

Point Mass Gravity
##################

The point-mass gravity acceleration model can be created as indicated in the `API <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.point_mass_gravity>`_.
It requires the following environment models to be defined:

- Gravity field for body exerting acceleration (see :ref:`environment_gravity_field_model` for non-default models).
- Current state of body exerting acceleration, either from a pre-defined ephemeris model
  (see :ref:`environment_ephemeris_model`) or from the numerical propagation of the translational dynamics of the body
  exerting the acceleration.


.. _spherical_harmonic_acceleration:

Spherical Harmonic Gravity
##########################

The spherical harmonic gravity acceleration model can be created as indicated in the `API <https://tudatpy.readthedocs.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.spherical_harmonic_gravity>`_.
It requires the following environment models to be defined:

- Spherical harmonic gravity field for the body exerting acceleration. See :ref:`environment_gravity_field_model` for
  options on how to define one (if the default gravity field model of the exerting body is not spherical harmonic)
- Rotation model from the inertial frame to the body-fixed frame, either from a pre-defined rotation model
  (:ref:`environment_rotational_model`) or from the numerical propagation of the rotational dynamics of the body
  exerting the acceleration (Earth in the above example).
- Current state of body exerting acceleration, either from a pre-defined ephemeris model
  (see :ref:`environment_ephemeris_model`) or from the numerical propagation of the translational dynamics of the body
  exerting the acceleration (Earth in the above example).

.. note::
  The spherical harmonic acceleration up to degree N and order M includes the point-mass gravity acceleration
  (which is the degree and order 0 term).

.. _mutual_spherical_harmonic_acceleration:

Mutual Spherical Harmonic Gravity
##############################################

The spherical harmonic gravity acceleration model can be created as indicated in the `API <https://tudatpy.readthedocs.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.mutual_spherical_harmonic_gravity>`_.
This model is typically only used for detailed propagation of planetary systems. With additional parameters, it can
be used even if the bodies mutually exerting the spherical harmonic gravity acceleration are not the central body.
It requires the following environment models to be defined:

- Spherical harmonic gravity field for body exerting acceleration and body undergoing acceleration (see
  :ref:`environment_gravity_field_model` for non-default models)
- Rotation model from the inertial frame to the body-fixed frame and body undergoing acceleration (see
  :ref:`environment_rotational_model`)
- Current state of bodies undergoing and exerting acceleration, either from an Ephemeris model or from the numerical
  propagation (see :ref:`environment_ephemeris_model`).


.. _third_body_gravity:

Third Body Gravity & Central Gravity
####################################


In addition to the three models listed above, which define different models for gravitational interactions between two
bodies, you can of course define a **third-body acceleration**. In Tudat, however, you do *not* specify directly
whether an
acceleration is a 'third-body' acceleration. This is fully defined by what you've chosen as your center of propagation
(see :ref:`translational_dynamics`), and the bodies exerting and undergoing the acceleration. Similarly, when
calculating the dynamics of a massive body, a correction is required for expressing the gravitational acceleration
exerted by the propagation origin (*e.g.* acceleration exerted by Earth on Moon, with Earth as propagation origin).
We term this the 'central' acceleration (see :ref:`third_body_acceleration` for more details on both aspects).



########################
Aerodynamic
########################

The aerodynamic acceleration model can be created as indicated in the `API <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.aerodynamic>`_.
It requires the following environment models to be defined:

- Atmosphere model for body exerting acceleration (see :ref:`environment_atmosphere_model`).
- Aerodynamic coefficient interface for body undergoing acceleration (see
  :ref:`environment_aerodynamic_coefficient_interface`).
- Mass model for body undergoing acceleration.
- Current state of body undergoing acceleration and body with atmosphere.

.. warning::
   Defining settings for a vehicle’s orientation, which may influence your aerodynamic force, is done after creating
   the acceleration models, as discussed in --.

.. todo::
   Add link above.

#############################
Radiation Pressure
#############################

There are two different radiation pressure models available in tudat(py):

- :ref:`cannonball_radiation_pressure`
- :ref:`panelled_radiation_pressure`

.. _cannonball_radiation_pressure:

Cannonball Radiation Pressure
#############################

The cannonball radiation pressure acceleration model can be created as indicated in the `API <https://tudatpy
.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.cannonball_radiation_pressure>`_.
It requires the following environment models to be defined:

- Cannonball radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration), see :ref:`environment_radiation_pressure_interface`.
- Current state of body undergoing and body emitting radiation.


.. _panelled_radiation_pressure:

Panelled Radiation Pressure
###########################

.. todo::
   This entry is not yet exposed to tudatpy.

Settings for a panelled radiation pressure acceleration.
It requires the following environment models to be defined:

- Panelled radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration), see :ref:`environment_radiation_pressure_interface`.
- Current state of body undergoing and body emitting radiation.


####################################
Relativistic Acceleration Correction
####################################

The relativistic correction acceleration model can be created as indicated in the `API <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.relativistic_correction>`_.
This is a first-order (in 1/c^2) correction to the acceleration due to the influence of relativity, consisting of three
distinct effects:the Schwarzschild, Lense-Thirring and de Sitter accelerations.

.. todo::
   Add requirements, if needed.


#######################
Empirical Accelerations
#######################

The cannonball radiation pressure acceleration model can be created as indicated in the `API <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.empirical>`_.
This is constant/once-per-orbit acceleration, expressed in the RSW frame (see for instance `this function
<https://tudatpy.readthedocs.io/en/latest/frame_conversion.html#tudatpy.astro.frame_conversion
.inertial_to_rsw_rotation_matrix>`_), for which the magnitude is determined empirically (typically during an orbit
determination process).

.. todo::
   Add requirements, if needed.

###################
Thrust
###################

Used to define the accelerations resulting from a thrust force, requiring:

- Mass of body undergoing acceleration;
- Settings for both the direction and magnitude of the thrust force. These models may in turn have additional environmental dependencies.

Setting up a thrust acceleration is discussed in more detail on the page Thrust Guidance.

.. todo::
   Add reference to thrust guidance page.


##################################
Tidal effect on natural satellites
##################################

The cannonball radiation pressure acceleration model can be created as indicated in the `API <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.direct_tidal_dissipation_acceleration>`_.
It requires the following environment models to be defined:

.. todo::
   Add requirements, if needed.

#################################
Quasi Impulsive Shot Acceleration
#################################

.. todo::
   This entry is not yet exposed to tudatpy.

Settings used to define the resulting acceleration of a quasi-impulsive shot, requiring:

- Mass of the body undergoing acceleration.
- Settings for the characteristics of the quasi-impulsive shots (total duration, rise time, associated deltaVs), as well as the times at which they are applied.


.. _acceleration_types:

===================
Acceleration Types
===================

In certain pieces of code, such as when requesting the saving of a single acceleration, you will need to supply an
identified for the type of acceleration. The list of supported types can be found in the `API <https://tudatpy
.readthedocs.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.AvailableAcceleration>`_.
