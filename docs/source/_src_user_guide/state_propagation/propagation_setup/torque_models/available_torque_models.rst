.. _available_torque_models:

====================================
Available Torque Models
====================================

In this page, all the torque models available in TudatPy are explained. Regardless of the type of torque
model, the procedure to link such torque model to the bodies exerting and undergoing the torque is
explained in this page: :ref:`torque_model_setup`. Therefore, this information will not be repeated in this
page. Instead, for each model, a reference to the related API documentation entry and the requirements are provided.


.. note::
   In TudatPy, torque models are defined through factory functions, which define the properties required of
   the torques, but do not perform any calculations themselves. These properties are stored through instances
   of the :class:`~tudatpy.numerical_simulation.propagation_setup.torque.TorqueSettings` class or of its
   derived classes.


.. contents:: List of available torque models
   :depth: 1
   :local:

In certain pieces of code, such as when requesting the saving of a single torque (see :ref:`dependent_variables`
for saving of dependent variables), you will need to supply an identifier for the type of torque you are requesting.
See the list of supported identifier types in the API documentation:
:class:`~tudatpy.numerical_simulation.propagation_setup.torque.AvailableTorque`.


Aerodynamic Torque
######################

| **Description**
| The aerodynamic torque model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.torque.aerodynamic` factory function.

| **Dependencies**
| 1. Atmosphere model for body exerting acceleration (see `Atmosphere models <https://py.api.tudat.space/en/latest/atmosphere.html>`_).
| 2. Aerodynamic coefficient interface for body undergoing acceleration (see
  `Aerodynamic coefficients <https://py.api.tudat.space/en/latest/aerodynamic_coefficients.html>`_).
| 3. Inertia tensor model for body undergoing acceleration.
| 4. Current states of body undergoing acceleration and body with atmosphere.
| 5. Shape model for the body exerting an acceleration (to allow for the calculation of vehicle altitude)
| 6. Roation model for the body undergoing an acceleration (or numerical propagation of this body's rotational dynamics)

.. note::
   The aerodynamic acceleration is calculated in the vehicles body-fixed or aerodynamic frame. Expressing the
   acceleration in an inertial frame (as required by the propagation) requires the vehicle's orientation to be defined.
   For a simple definition, in which the body’s angle of attack, sideslip angle, and bank angle are all set to 0, see
   :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`.

   More details on aerodynamic guidance can be found on :ref:`this page <aerodynamic_models>`.

Second Degree Gravitational Torque
###################################

| **Description**
| The second degree gravitational torque model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.torque.second_degree_gravitational` factory function.

| **Dependencies**
| 1. Gravity field model for body exerting acceleration (see `Atmosphere models <https://py.api.tudat.space/en/latest/atmosphere.html>`_).
| 2. Inertia tensor model for body undergoing acceleration.
| 3. Current states of body undergoing acceleration and body with atmosphere.

.. tip::

    This implementation of the gravitational torque model uses the inertia tensor if the body undergoing the torque to infer its degree two spherical harmonics gravity field.
    It is therefore convenient for modelling the gravitational torque acting on a custom body, such as a vehicle, because its custom spherical harmonics model does not have to be created manually.


Spherical Harmonics Gravitational Torque
##########################################

| **Description**
| The second degree gravitational torque model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.torque.spherical_harmonic_gravitational` factory function.

| **Dependencies**
| 1. Gravity field model for body exerting acceleration (see `Atmosphere models <https://py.api.tudat.space/en/latest/atmosphere.html>`_).
| 2. Spherical harmonic gravity field for body undergoing torque (see `Gravity field models <https://py.api.tudat.space/en/latest/gravity_field.html>`_).
| 3. Current states of body undergoing acceleration and body with atmosphere.

.. tip::

    In contrast to the second degree gravitational torque, the spherical harmonics gravity torque implementation requires the spherical harmonics gravity field model of the torque-undergoing body.
    It is therefore more suited for modelling the gravity torques acting on "standard" celestial bodies, for which spherical harmonics mass distributions are readily available.



Custom Torque
#################

| **Description**
| The custom torque model can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.torque.custom` factory function.

| **Dependencies**
| None.
