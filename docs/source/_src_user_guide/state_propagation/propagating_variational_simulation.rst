
.. _propagating_variational_simulation:

Propagating Variational Equations
=================================

In addition to :ref:`propagating_dynamics`, Tudat is also capable of propagating the so-called variational equations associated with the dynamics to produce the state transition matrix :math:`\Phi(t,t_{0})` and sensitivity matrix :math:`S(t)`, which we define here as:

.. math::

      \Phi(t,t_{0}) &= \frac{\partial \mathbf{x}(t)}{\partial\mathbf{x}(t_{0})}\\
      S &= \frac{\partial \mathbf{x}(t)}{\partial \mathbf{p  }}\\

where :math:`\mathbf{x}` is the propagated state, :math:`\mathbf{p}` the vector of a parameter vector (e.g. gravity field parameters, rotation model parameters, etc.), and :math:`t_{0}` denotes the initial time.
These two matrices are based on linearization of the complex dynamics and can be used to quickly determine the influence of a change in initial state (:math:`\mathbf{x}(t_{0})`) and/or parameters (:math:`\mathbf{p}`) on the state :math:`\mathbf{x}(t)` at time :math:`t`.

.. _parameter_settings:

Parameter settings
------------------

If the user wishes to do propagate the variational equations alongside the system sate, settings for the parameters that are to be used in the variational equations have to be defined.
In terms of the equations above, it needs to be specified for which parameters :math:`\mathbf{x}_{0}` and :math:`\mathbf{p}` the solution for the state transition and sensitivity matrices is to be computed.
In Tudat(Py) these parameters are referred to as parameters or sometimes "estimated" parameters, because of their primary application in state estimation problems.

A description of how these parameters are to be defined and a comprehensive list of all available parameters are linked below:

.. toctree::
    :maxdepth: 3

    propagating_variational_equations/parameter_settings
    propagating_variational_equations/available_parameters


Performing the Propagation
--------------------------

Simulations in which only the system state and variational equations is propagated are handled by simulator objects from the ``VariationalSimulator`` base class.
For propagation of the system state and variational equations along a single arc, see the page below:

.. toctree::
  :maxdepth: 1

  propagating_variational_equations/single_arc_variational_propagation
