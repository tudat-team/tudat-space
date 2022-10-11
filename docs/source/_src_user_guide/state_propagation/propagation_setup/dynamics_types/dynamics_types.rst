==============
Dynamics Types
==============

.. _translational_dynamics:

Translational Dynamics
======================

Settings to propagate numerically the translational state of a body can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` factory function, described in
detail in the API documentation. A number of the inputs to this function are described in more detail on a dedicated page here:

- A set of acceleration models (see :ref:`acceleration_models_setup`)
- Settings for the numerical integration (see :ref:`integrator_setup`)
- The initial conditions for the propagation (state and time, see AAAs)
- A type of propagator, since the translational state can have different representations (see
  :ref:`propagator_types`);
- Settings to terminate the propagation (see :ref:`termination_settings`);
- Dependent variables that should be saved (see :ref:`dependent_variables`).

.. _rotational_dynamics:

Rotational Dynamics
======================


Settings to propagate numerically the translational state of a body can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` factory function, described in
detail in the API documentation. A number of the inputs to this function are described in more detail on a dedicated page here:

The Tudatpy-native inputs to create the settings for a translational propagator are the following:

- A set of torque models (see :ref:`torque_model_setup`);
- A type of propagator, since the rotational state can have different representations (see
  :ref:`propagator_types`);
- The initial conditions for the propagation (rotational state and time, see AAAs)
- Settings to terminate the propagation (see :ref:`termination_settings`);
- Dependent variables that should be saved (see :ref:`dependent_variables`).

.. note::
  Settings to define the propagation of rotational dynamics reflect those specified in :ref:`translational_dynamics`.
  Besides the obvious differences, an important one is that no 'central body' is specified. The rotational state that
  is propagated is always the one from the global inertial orientation to the body-fixed orientation of the propagated
  body.



