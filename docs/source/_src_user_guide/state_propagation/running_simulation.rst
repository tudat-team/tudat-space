
.. _running_simulation:

Propagating Dynamics
====================

With all the necessary simulation settings in place, it is time to run the simulation. In Tudat(Py), this is done by means of a simulator object, which handles the setup and execution of the simulation, by tieing all the settings and models defined on the above pages together, defining and solving the state derivative equation:


.. math::

      \dot{\mathbf{x}}&=\mathbf{f}(\mathbf{x},t;\mathbf{p})\\
      \mathbf{x}(t_{0})&=\mathbf{x}_{0}

where :math:`\mathbf{x}` defines the state vector that is to be propagated (defined by the choice of your
:ref:`propagator <propagator_types>`),
:math:`t_{0}` and :math:`\mathbf{x}_{0}` define the initial time and state, defined in the
:ref:`propagation_setup` and :ref:`integrator_setup` pages, respectively. The parameter vector :math:`\mathbf{p}` is
included explicitly in the state derivative function to denote its dependence on various environmental and system
parameters, as defined through the :ref:`environment_setup`. Finally, the state derivative function :math:`\mathbf{f}`
is created through the definition of the type and formulation of the dynamics and the
state derivative model (see :ref:`acceleration_models_setup` and :ref:`torque_model_setup`).

The above differential equations is solved using the specific :ref:`choice of integrator <integrator_setup>`, and is
terminated by used-specified :ref:`termination_settings` (as defined in :ref:`propagation_setup`). The output of
the propagation consists of the state that is propagated, as well as any number of :ref:`output variables <simulation_output>`.


Simulations in which only the system state is propagated are handled by simulator objects from the ``Simulator`` base class.
For propagation of the system state along a single arc, see the page below:

.. toctree::
  :maxdepth: 1

  running_simulation/single_arc
