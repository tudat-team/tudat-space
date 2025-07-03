.. _rotational_dynamics:

======================
Rotational Dynamics
======================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   rotational/torque-model-setup
   rotational/available-torque-models

Settings to propagate the rotational state of a body numerically can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` factory function, described in detail in the :doc:`API documentation <propagator>`. In the current page, only the Tudat-specific aspects of the input will be briefly described.
The default (processed) representation for solving the rotational equations of motion is by using a vector of 7 elements:

* The quaternion elements (vector :math:`\mathbf{q}` of size 4) of the rotation from body-fixed to inertial frame (see :ref:`quaternion_definition`)
* The angular velocity (vector :math:`\boldsymbol{\omega}` of size 3) of the body w.r.t. the inertial frame, expressed in the body-fixed frame.

Several other formulations can be used if wanted (see below and :ref:`processed_propagated_states`).

To propagate rotational dynamics, an inertia tensor for the propagated body must be defined. The inertia tensor is handled by the :doc:`Rigid body properties <rigid_body>` in Tudat. Note that, by endowing a body with a gravity field, such properties are automatically created (although in the case of a spherical harmonic gravity field, additional information must be provided, see :doc:`the API documentation <rigid_body>`).

The governing equation that is solved numerically for the rotational dynamics is a first-order differential equation. For the default propagator using :math:`\mathbf{x}=[\mathbf{q};\boldsymbol{\omega}]`, with quaternion vector :math:`\mathbf{q}` and body-fixed angular velocity vector :math:`\boldsymbol{\omega}`, it takes the form:

.. math::
    \frac{d\mathbf{x}}{dt} = \begin{pmatrix} \mathbf{Q}(\mathbf{q})\boldsymbol{\omega} \\ \mathbf{I}\left(-\dot{\mathbf{I}}+(\mathbf{I}\boldsymbol{\omega})\times\boldsymbol{\omega}+\sum_{i}\mathbf{M}_{i}(\mathbf{r},\mathbf{v},t) \right)  \end{pmatrix}

where the summation runs over all torques :math:`\mathbf{M}` specified by the user, :math:`\mathbf{I}` denotes the body's inertia tensor. The inertia tensor of a body is defined through its :ref:`rigid_body_properties`

.. note::

  At present, influence of the time-variability of the inertia tensor (and other effects related to time-variation of mass distribution such as jet damping) are not included in the evaluation of the rotational equations of motion, *even in the case where the inertia tensor is time variable*.

When propagating multiple bodies, the state vectors of the various bodies and their derivatives are concatenated, see :ref:`multi_body_dynamics` for more details.

Inputs
=======

In addition to the settings described :ref:`here <propagation_inputs>`, the definition of rotational dynamics settings requires:

- A set of torque models (see :ref:`torque_model_setup`);
- The initial conditions for the propagation (rotational state as :math:`[\mathbf{q};\boldsymbol{\omega}]` and time)
- A propagator type, since the rotational state can have different representations (listed in :class:`~tudatpy.numerical_simulation.propagation_setup.propagator.RotationalPropagatorType`; default is quaternions and angular velocity).

.. warning::

  The initial state must be provided as processed state formulation :math:`[\mathbf{q};\boldsymbol{\omega}]`, **regardless of the propagator type**.

.. _rotational_example:

Example
========

In the example below, the body "Spacecraft" will be propagated w.r.t. body "Earth", using given
torque models. A given initial state which defines the orientation of "Spacecraft" w.r.t. the
inertial reference frame is defined. A Runge Kutta 4 integrator is defined with step-size of 2
seconds. The propagation will terminate once the ``simulation_end_epoch`` termination condition is
reached. A rotational propagator that uses quaternions is defined. Next to that, the propagator is
asked to save the total torque norm as dependent variable. The time and rotational state will be
printed on the terminal once every 24 hours (simulation time).

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
        :color: muted

        .. code-block:: python

            from tudatpy.numerical_simulation import propagation_setup
            from tudatpy.astro import element_conversion
            import numpy as np

      .. literalinclude:: /_snippets/simulation/environment_setup/full_rotational_setup.py
          :language: python

