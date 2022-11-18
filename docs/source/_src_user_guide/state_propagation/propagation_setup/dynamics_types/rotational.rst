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

Settings to propagate the rotational state of a body numerically can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` factory function, described in detail in the `API documentation <https://py.api.tudat.space/en/latest/>`_. In the current page, only the Tudat-specific aspects of the input will be briefly described.
The default (conventional) representation for solving the rotational equations of motion is by using a vector of 7 elements:

  * The quaternion elements (vector :math:`\mathbf{q}` of size 4) of the rotation from body-fixed to inertial frame (see :ref:`quaternion_definition`)
  * The angular velocity (vector :math:`\boldsymbol{\omega}` of size 3) of the body w.r.t. the inertial frame, expressed in the body-fixed frame.

Several other formulations can be used if wanted (see below and :ref:`conventional_propagated_states`).



Inputs
=======

In addition to the settings described :ref:`here <propagation_inputs>`, the definition of rotational dynamics settings requires:

- A set of torque models (see :ref:`torque_model_setup`);
- The initial conditions for the propagation (rotational state as :math:`[\mathbf{q};\boldsymbol{\omega}]` and time)
- A propagator type, since the rotational state can have different representations (listed in :class:`~tudatpy.numerical_simulation.propagation_setup.propagator.RotationalPropagatorType`).

.. warning::

    The initial state must be provided as conventional state formulation :math:`[\mathbf{q};\boldsymbol{\omega}]`, **regardless of the propagator type**

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

