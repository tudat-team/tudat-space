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
   translational/radiation_pressure_acceleration
   translational/thrust_models
   translational/aerodynamics

Settings to propagate the translational state of a body numerically can be created through the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` function. Using these settings to propagate dynamics us described on the page on :ref:`propagating_dynamics`.

The default (processed) representation for solving the translational equations of motion is by using the Cowell propagator
(using Cartesian elements as the propagated states), but other formulations can be used (see below and :ref:`processed_propagated_states`).

Inputs
======

In addition to the settings described :ref:`here <propagation_inputs>` for propagation settings of any kind, the definition of translational dynamics settings specifically requires:

- A set of acceleration models (see :ref:`acceleration_models_setup`)
- The central bodies of the propagation
- A type of propagator, since the translational state can have different representations
  (listed in :class:`~tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalPropagatorType`; default is Cowell).
- The initial conditions for the propagation (Cartesian state, and time)

.. warning::

    The initial state must be provided in Cartesian elements w.r.t. the central body(/bodies), **regardless of the propagator type**

The central bodies define the origin of the state vector that is to be propagated. For instance, when propagating a spacecraft :math:`s` w.r.t. the Earth :math:`E`, the propagated state vector :math:`\mathbf{x}` would be:

.. math::
    \mathbf{x} = \mathbf{x}_{s} - \mathbf{x}_{E}

where :math:`\mathbf{x}_{s}` and :math:`\mathbf{x}_{E}` are the states of the spacecraft and Earth, respectively, in a frame with inertial origin.

The governing equation that is solved numerically for the translational dynamics is a first-order differential equation. For the Cowell propagator, it takes the form, for :math:`\mathbf{x}=[\mathbf{r};\mathbf{v}]` (decomposed into position :math:`\mathbf{r}` and velocity :math:`\mathbf{v}`):

.. math::
    \frac{d\mathbf{x}}{dt} = \begin{pmatrix} \mathbf{v} \\ \sum_{i} \mathbf{a}_{i}(\mathbf{r},\mathbf{v},t)  \end{pmatrix}

where the summation runs over all accelerations specified by the user. When propagating multiple bodies, the state vectors of the various bodies and their derivatives are concatenated, see :ref:`multi_body_dynamics` for more details.

.. _translational_example:

Example
=======

In the example below, the body "Spacecraft" will be propagated w.r.t. body "Earth" (also termed the
'propagation origin'), using given acceleration models, a given initial state which defines the
initial Cartesian state of the center of mass of "Spacecraft" w.r.t. the center of mass of "Earth".
A Runge Kutta 4 integrator is defined with step-size of 2 seconds. The propagation will terminate
once the ``simulation_end_epoch`` termination condition is reached. The state will be propagated
through the Encke formulation. Finally the propagator is asked to save the total acceleration.
The time and state will be printed on the terminal once every 24 hours. 

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

     .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
        :language: python

