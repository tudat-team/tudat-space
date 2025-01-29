
.. _propagating_dynamics:

Propagating Dynamics
====================

With all the necessary simulation settings in place (:ref:`environment_setup` and :ref:`propagation_setup`), it is time to run the simulation.
In Tudat(Py), this is done by means of a simulator object,
which handles the setup and execution of the simulation, by tieing all the settings and models defined on the above pages together,
defining and solving the state derivative equation:


.. math::

      \dot{\mathbf{x}}&=\mathbf{f}(\mathbf{x},t;\mathbf{p})\\
      \mathbf{x}(t_{0})&=\mathbf{x}_{0}

where :math:`\mathbf{x}` defines the state vector that is to be propagated, :math:`\mathbf{f}` the state derivative function (see :ref:`translational_dynamics` for one example)
:math:`t_{0}` and :math:`\mathbf{x}_{0}` define the initial time and state. The parameter vector :math:`\mathbf{p}` is
included explicitly in the state derivative function above to denote its dependence on various environmental and system
parameters.

The above differential equations are solved:

* Using the specific :ref:`choice of integrator <integrator_setup>`
* Are terminated by user-specified :ref:`termination settings <termination_settings>`.
* The output of
the propagation consists of the state that is propagated, as well as any number of :ref:`output (dependent) variables <printing_processing_results>`.

Simulations in which only the system state is propagated are handled by simulator objects derived from the ``Simulator`` base class. 
The creation of this object is done using the :func:`~tudatpy.numerical_simulation.create_dynamics_simulator` function :

.. code-block:: python

    dynamics_simulator = numerical_simulation.create_dynamics_simulator(
        body_system, propagator_settings)
    propagation_results = dynamics_simulator.propagation_results


where the two inputs specify (roughly) what the physical environment is (the bodies) and how the simulator is supposed to act on this
physical environment. By default, creating the dynamics simulator immediately starts the propagation.
The choice of single-, multi- or hybrid-arc (see :ref:`here <multi_arc_dynamics>`) is defined by the choice of ``propagator_settings``, resulting in the ``dynamics_simulator``
being of type :class:`~tudatpy.numerical_simulation.SingleArcSimulator`, :class:`~tudatpy.numerical_simulation.MultiArcSimulator` or
:class:`~tudatpy.numerical_simulation.HybridArcSimulator`, respectively.
The results of the numerical integration are stored in the ``propagation_results``, which is described in more detail below, along with a
more detailed description of the process that is executed during the propagation:

.. toctree::
   :titlesonly:
   :maxdepth: 1

   propagating_dynamics/propagation_results
   propagating_dynamics/propagation_architecture
