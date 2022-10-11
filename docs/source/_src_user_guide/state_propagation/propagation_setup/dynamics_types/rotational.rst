.. _rotational_dynamics:

======================
Rotational Dynamics
======================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   ../torque_models/setup
   ../torque_models/available

Settings to propagate numerically the translational state of a body can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` factory function, described in
detail in the API reference, which creates an object of type
:class:`~tudatpy.numerical_simulation.propagation_setup.propagator.RotationalStatePropagatorSettings` (see below
an :ref:`example`).

In this page, only the Tudat-native objects necessary as input will be described. For all the other inputs, please
refer to the related API entry (:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational`).

.. note::
  Settings to define the propagation of rotational dynamics reflect those specified in :ref:`translational_dynamics`.
  Besides the obvious differences, an important one is that no 'central body' is specified. The rotational state that
  is propagated is always the one from the global inertial orientation to the body-fixed orientation of the propagated
  body.


Inputs
=======

The Tudatpy-native inputs to create the settings for a translational propagator are the following:

- A set of acceleration models (see :ref:`torque_model_setup`)
- An initial state vector (Quaternions defining rotation to body-fixed frame, angular velocity vector in body-fixed frame; see :ref:`conventional_states`)
- A propagator type, since the rotational state can have different representations (see
  :ref:`propagator_types`) NOTE: the initial state must be provided as quaternions/angular velocity, regardless of the propagator type
- Settings to terminate the propagation (see :ref:`termination_settings`)
- Dependent variables that should be saved (see :ref:`dependent_variables`)

.. _example:

Example
========

In the example below, the body "Spacecraft" will be propagated w.r.t. body "Earth", using given torque models (not
provided), a given initial state which defines the orientation of "Spacecraft" w.r.t. the inertial reference frame.
The propagation will terminate once the
``simulation_end_epoch`` epoch is reached. Furthermore, the
propagator is asked to save the total torque norm as
dependent variable. The time and rotational state will be printed on the terminal once every 24 hours (simulation
time), while the state will be propagated through the quaternion formulation.


    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup
                    from tudatpy.kernel.astro import element_conversion
                    import numpy as np

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_rotational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

