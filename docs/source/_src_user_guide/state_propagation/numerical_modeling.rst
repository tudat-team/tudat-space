.. _integrator_setup:

Integration Setup
=================

The environment and formulation of dynamical equations are now in place. In order to solve these equations
you still need to define the numerical integrator settings. These settings specify *how* the equations are solved.
In Tudat(Py) you can choose between different types of integrators.


For code examples and additional information on the interfacees, please follow the links to the API documentation given below.

Euler integrator
---------

Simple forward Euler integrator, defined by the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.euler` function.


Runge-Kutta 4 integrator
------------------------

The well-known and often used RK4 integrator, defined by the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_4` function.

Variable step-size Runge-Kutta integrators
------------------------------------------

Variable step-size multistage integrators, which can be defined by specifying scalar tolerances
(using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_variable_step_size` function) or vector
tolerances (using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_variable_step_size_vector_tolerances` function).
In the case of the former, the same absolute and relative tolerance is used for each state entry. In the latter case, the tolerances
can be made to vary for the different state entries. Several different Butcher Tableaus, corresponding to different
specific integrators, and integrator error, can be specified by using the :class:`~tudatpy.numerical_simulation.propagation_setup.integrator.RKCoefficientSets` enum.

Bulirsch-Stoer integrator
-------------------------

Variable step-size extrapolation integrator, defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.bulirsch_stoer` function.
Tolerances are defined using scalars, and each state element has equal absolute and relative tolerances.

Adams-Bashforth-Moulton integrator
----------------------------------

Variable step-size, variable-order multi-step integrator, defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.adams_bashforth_moulton` function.
Tolerances are defined using scalars, and each state element has equal absolute and relative tolerances.

Forcing fixed step-size
-----------------------

Many of the above integrators allow you to supply absolute and relative tolerances, which the integrators use to adapt the
step size that is taken, based on the behaviour of the dynamics. You can force these integrators to a fixed step size by:
* Setting the initial time step, minimum time step and maximum time step to the same value (the fixed time step you wish to impose)
* Setting the relative and absolute tolerances to infinity (or a similarly high value)



