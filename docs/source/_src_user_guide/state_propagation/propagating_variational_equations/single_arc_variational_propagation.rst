
.. _single_arc_propagation:

============================================
Single-arc Variational Equations Propagation
============================================

For propagation of the variational equations alongside the system state, a different sort of simulator object - a ``VariationalSimulator`` - has to be used.
``VariationalSimulator`` objects contain a ``Simulator`` object, which means that they can do anything that a ``Simulator`` can plus the added functionality of propagating variational equations.


To propagate the variational equations alongside the single-arc system state, the ``SingleArcVariationalSimulator`` derivative of the ``VariationalSimulator`` base class should be used.
With the basic simulation setup (system of bodies, integrator settings, propagator settings) and the parameter settings for the variational equations, a variational equations solver can be set up.
The setup works similarly to the normal dynamics simulator:

.. code-block:: python

        variational_equations_solver = estimation_setup.SingleArcVariationalSimulator(
                bodies, integrator_settings, propagator_settings,
                estimation_setup.create_parameters_to_estimate(parameter_settings, bodies)
                )

The state history, state transition matrices, and sensitivity matrices can then be extracted:

.. code-block:: python

        states = variational_equations_solver.state_history
        state_transition_matrices = variational_equations_solver.state_transition_matrix_history
        sensitivity_matrices = variational_equations_solver.sensitivity_matrix_history

For a complete example of propagation and usage of the variational equations, please see the tutorial :ref:`Linear sensitivity analysis of perturbed orbit </_src_getting_started/_src_examples/tudatpy-examples/propagation/linear_sensitivity_analysis.ipynb>`.


