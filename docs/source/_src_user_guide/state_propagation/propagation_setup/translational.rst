.. _translational_dynamics:

======================
Translational Dynamics
======================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   translational/acceleration_model_setup
   translational/available_acceleration_models
   translational/third_body_acceleration
   translational/thrust_models
   translational/aerodynamics

Settings to propagate the translational state of a body numerically can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` factory function, described in detail in the `API documentation <https://py.api.tudat.space/en/latest/>`_. In the current page, only the Tudat-specific aspects of the input will be briefly described.

The default (processed) representation for solving the translational equations of motion is by using the Cowell propagator
(using Cartesian elements as the propagated states), but other formulations can be used (see below and :ref:`processed_propagated_states`).

Inputs
======

In addition to the settings described :ref:`here <propagation_inputs>`, the definition of translational dynamics settings requires:

- A set of acceleration models (see :ref:`acceleration_models_setup`)
- The initial conditions for the propagation (Cartesian state, and time)
- The central bodies of the propagation
- A type of propagator, since the translational state can have different representations
  (listed in :class:`~tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalPropagatorType`; default is Cowell).

.. warning::

    The initial state must be provided in Cartesian elements w.r.t. the central body(/bodies), **regardless of the propagator type**

.. _translational_example:

Example
=======

In the example below, the body "Spacecraft" will be propagated w.r.t. body "Earth" (also termed the
'propagation origin'), using given acceleration models, a given initial state which defines the
initial Cartesian state of the center of mass of "Spacecraft" w.r.t. the center of mass of "Earth".
A Runge Kutta 4 integrator is defined with step-size of 2 seconds. The propagation will terminate
once the ``simulation_end_epoch`` termination condition is reached. The state will be propagated
through the Encke formulation. Next to that, the propagator is asked to save the total acceleration.
The time and state will be printed on the terminal once every 24 hours. 

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup
                    from tudatpy.kernel.astro import element_conversion
                    import numpy as np

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp



