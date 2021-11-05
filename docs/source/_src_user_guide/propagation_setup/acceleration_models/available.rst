.. _available_acceleration_models:

===============================
Available Acceleration Models
===============================

In this page, all the acceleration models available in tudat(py) are explained. Regardless of the type of acceleration
model, the procedure to link such acceleration model to the bodies exerting and undergoing the acceleration is
explained in this page: :ref:`Acceleration Model Setup`. Therefore, this information will not be repeated in this
page. Instead, for each model, a reference to the related API documentation entry and the requirements are provided.


.. note::
   In tudat(py), acceleration models are defined through factory functions, which define the properties required of
   the accelerations, but do not perform any calculations themselves. These properties are stored through instances
   of the
   ``AccelerationSettings`` class (see `API documentation <https://tudatpy.readthedocs.io/en/latest/acceleration.html#tudatpy
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

In Tudat, we currently provide three different formulations for the inertial gravitational acceleration of one body exerted on another:

* :ref:`point_mass_acceleration`
* :ref:`spherical_harmonic_acceleration`
* :ref:`mutual_spherical_harmonic_acceleration` (relevant for, for instance, natural satellite dynamics).


.. note::
    In addition to the three models listed above, which define different models for gravitational interactions between two
    bodies, you can of course define a **third-body acceleration**. In Tudat, however, you do *not* specify directly
    whether an
    acceleration is a 'third-body' acceleration. This is fully defined by what you've chosen as your center of propagation
    (see :ref:`translational_dynamics`), and the bodies exerting and undergoing the acceleration. Similarly, when
    calculating the dynamics of a massive body, a correction is required for expressing the gravitational acceleration
    exerted by the propagation origin (*e.g.* acceleration exerted by Earth on Moon, with Earth as propagation origin).
    We term this the 'central' acceleration (see :ref:`third_body_gravity` for details on both aspects).

.. _point_mass_acceleration:

Point Mass Gravity
##################

The point-mass gravity acceleration model can be created as indicated in the `API documentation <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.point_mass_gravity>`_.
It requires the following environment models to be defined:

- Gravity field for body exerting acceleration (see :ref:`environment_gravity_field_model` for non-default models).
- Current state of body exerting acceleration, either from a pre-defined ephemeris model
  (see :ref:`environment_ephemeris_model`) or from the numerical propagation of the translational dynamics of the body
  exerting the acceleration.


.. _spherical_harmonic_acceleration:

Spherical Harmonic Gravity
##########################

The spherical harmonic gravity acceleration model can be created as indicated in the `API documentation <https://tudatpy.readthedocs.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.spherical_harmonic_gravity>`_.
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

The spherical harmonic gravity acceleration model can be created as indicated in the `API documentation <https://tudatpy.readthedocs.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.mutual_spherical_harmonic_gravity>`_.
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

Settings for a third-body and central gravitational acceleration are defined identically to direct gravitational accelerations. During the creation and processing of the acceleration models, Tudat distinguishes three different cases, for the body :math:`A` exerting the acceleration, the body :math:`B` undergoing the acceleration, and the body :math:`C` as the center of propagation.

* **Third-body perturbation** The central body is non-inertial (e.g. is not the SSB), and the acceleration *is not* exerted by central body. The acceleration is then computed from:

.. math::

 \mathbf{a}=\nabla U_{B}(\mathbf{r}_{A})-\nabla U_{B}(\mathbf{r}_{C})

This is the typical *third body* perturbation, for instance for the case where :math:`A` is a spacecraft orbiting the Moon, :math:`B` is the Earth and :math:`C` is the Moon


* **Central gravitational acceleration** The central body is non-inertial (e.g. is not the SSB), and the acceleration *is* exerted by the central body. If the body undergoing the acceleration itself possesses a gravity field, the gravitational back-reaction is accounted for when setting up the gravitational acceleration.

.. math::

 \mathbf{a}=\nabla U_{B}(\mathbf{r}_{A})-\nabla U_{A}(\mathbf{r}_{B})

The backreaction (accounted for by the second term) becomes relevant when computing the mutual dynamics of two natural bodies. For instance, when propagating the Moon w.r.t. the Earth, and adding the point-mass gravitational acceleration of the Earth on the Moon, the following acceleration will be used:

.. math::

 \mathbf{a}=-\frac{\mu_{A}+\mu_{B}}{||\mathbf{r}||^{2}}\hat{\mathbf{r}}

with :math:`\mathbf{r}` the position of the Moon w.r.t. the Earth. The backreaction is taken into account by using the sum of the gravitational parameters (as opposed to only the gravitational parameter of the Earth).


* **Direct gravitational acceleration** The central body is inertial (e.g. is the SSB). In this case, the direct acceleration is used:

.. math::

 \mathbf{a}=\nabla U_{B}(\mathbf{r}_{A})

We stress that the above works equally well for **point-mass**, **spherical-harmonic** and **mutual-spherical-harmonic** accelerations. When propagating the dynamics of a spacecraft w.r.t. the Moon, the following will add the third-body point-mass acceleration of the Earth:

.. tabs::

     .. tab:: Python

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/point_mass_gravity.py
         :language: python

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/point_mass_gravity.cpp
         :language: cpp

while the following will add the third-body spherical-harmonic acceleration of the Earth (zonal coefficients up to degree 4)

.. tabs::

   .. tab:: Python

    .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/spherical_harmonic_gravity_zonal.py
       :language: python

   .. tab:: C++

    .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/spherical_harmonic_gravity_zonal.cpp
       :language: cpp

Note that above two code blocks are identical to those given as example in the API documentation
entries of :ref:`point_mass_acceleration` and :ref:`spherical_harmonic_acceleration`. It is through the definition
*of the central body* that a direct, central or third-body acceleration is created.

########################
Aerodynamic
########################

The aerodynamic acceleration model can be created as indicated in the `API documentation <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.aerodynamic>`_.
It requires the following environment models to be defined:

- Atmosphere model for body exerting acceleration (see :ref:`environment_atmosphere_model`).
- Aerodynamic coefficient interface for body undergoing acceleration (see
  :ref:`environment_aerodynamic_coefficient_interface`).
- Mass model for body undergoing acceleration.
- Current state of body undergoing acceleration and body with atmosphere.

.. note::
   By default, a body's angle of attack, sideslip angle, and bank angle are all set to 0. Defining a vehicle orientation is
   typically done in one of several ways: defining aerodynamic guidance directly (imposing these three angles), using the
   definition of vehicle orientation from an existing model for the vehicle (for instance thrust), or propagation of the body's
   rotational dynamics.

.. todo::
   Add reference to aerodynamic guidance page.

#############################
Radiation Pressure
#############################

There are two different radiation pressure models available in tudat(py):

- :ref:`cannonball_radiation_pressure`
- :ref:`panelled_radiation_pressure`

The distinction between them lies in the type of radiation pressure interface that is used for the body undergoing acceleration (see below)

.. _cannonball_radiation_pressure:

Cannonball Radiation Pressure
#############################

The cannonball radiation pressure acceleration model can be created as indicated in the `API documentation <https://tudatpy
.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.cannonball_radiation_pressure>`_.
It requires the following environment models to be defined:

- Cannonball radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration), see :ref:`environment_radiation_pressure_interface`.
- Current state of body undergoing and body emitting radiation.


.. _panelled_radiation_pressure:

Panelled Radiation Pressure
###########################

The panelled radiation pressure acceleration model can be created as indicated in the `API documentation <https://tudatpy
.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.panelled_radiation_pressure>`_.
It requires the following environment models to be defined:

- Panelled radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration), see :ref:`environment_radiation_pressure_interface`.
- Current state of body undergoing and body emitting radiation.


####################################
Relativistic Acceleration Correction
####################################

The relativistic correction acceleration model can be created as indicated in the `API documentation <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.relativistic_correction>`_.
This is a first-order (in 1/c^2) correction to the acceleration due to the influence of relativity for a
massless body (*e.g.* spacecraft) orbiting a massive body (*e.g.* Earth), which in turn orbits a third body (*e.g.* Sun),
consisting of three distinct effects: the Schwarzschild, Lense-Thirring and de Sitter accelerations.

It requires the following environment models to be defined:

- Mass of the orbited body and the third body (de Sitter only)
- Current state of body undergoing acceleration, the orbited body, and the third body (de Sitter only)

#######################
Empirical Accelerations
#######################

The empirical pressure acceleration model can be created as indicated in the `API documentation <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.empirical>`_.
This is constant and/or once-per-orbit sinusoidal acceleration, expressed in the RSW frame (see for instance `this function
<https://tudatpy.readthedocs.io/en/latest/frame_conversion.html#tudatpy.astro.frame_conversion
.inertial_to_rsw_rotation_matrix>`_), for which the magnitude is determined empirically (typically during an orbit
determination process).

It requires the following environment models to be defined:

- Mass of the central body (for calculation of true anomaly)

######
Thrust
######

Used to define the accelerations resulting from a thrust force, requiring:

- Mass of body undergoing acceleration;
- Settings for both the direction and magnitude of the thrust force. These models may in turn have additional environmental dependencies.

Setting up a thrust acceleration is discussed in more detail on the page Thrust Guidance.

.. todo::
   Add reference to thrust guidance page.


##################################
Tidal effect on natural satellites
##################################

The acceleration model for calculating the effect of tides on natural satellites can be created as indicated in the `API documentation <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.direct_tidal_dissipation_acceleration>`_.
It is a rather specialist model, which is only relevant for the dynamics of natural satellies *themselves*. When calculating
the dynamics of spacecraft orbiting natural satellites, use :ref:`gravity field variations <environment_gravity_field_variations>` instead.
Two types of accelerations can be computed: acceleration on the satellite due to tide on the planet, or acceleration on the satellite
due to tide on the satellite

It requires the following environment models to be defined:

- Masses of planet and satellite.
- Current state of planet and satellite.
- Spherical harmonic gravity field for body *on* which the tide is raised (planet or satellite)
- Planet rotaion model (only for effect of tide on planet)

#################################
Quasi Impulsive Shot Acceleration
#################################

The quasi-impulsive shots acceleration model can be created as indicated in the `API documentation <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.quasi_impulsive_shots_acceleration>`_.
This is a manner in which to incorporate short bursts of thrust into a numerical propagation. When using this model, ensure
that your integration step is sufficiently small to be able to capture the burst of thrust.

This acceleration model has no dependencies on the environment: all required information is provided through the associated
factory function.

######
Custom
######

Tudat allows you to write your own function in Python, as indicated in the `API documentation <https://tudatpy.readthedocs
.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.custom>`_ to define an acceleration model as
a function of time. The dependencies of this acceleration model are user-defined.

.. _acceleration_types:

===================
Acceleration Types
===================

In certain pieces of code, such as when requesting the saving of a single acceleration, you will need to supply an
identified for the type of acceleration. The list of supported types can be found in the `API documentation <https://tudatpy
.readthedocs.io/en/latest/acceleration.html#tudatpy.numerical_simulation.propagation_setup.acceleration.AvailableAcceleration>`_.
