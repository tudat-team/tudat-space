.. _integrator_setup:

Integration Setup
=================

The environment and formulation of dynamical equations are now in place. In order to solve these equations
you still need to define the numerical integrator settings. These settings specify *how* the equations are solved.
In Tudat(Py) you can choose between different types of integrators.

Integrator types
----------------

For code examples and additional information on the interfacees, please follow the links to the API documentation given below.

Euler integrator
^^^^^^^^^^^^^^^^

Simple forward Euler integrator, defined by the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.euler` function.

**General considerations** It is known to be a highly inaccurate integrator (global truncation error of :math:`O(\Delta t)` and is
therefore discouraged for use in research. It can however still be used for comparison studies or very simple analyses.


Runge-Kutta 4 integrator
^^^^^^^^^^^^^^^^^^^^^^^^

The well-known and often used RK4 integrator, defined by the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_4` function.

**General considerations** The RK4 integrator is a popular method for problems in which computational efficiency is not
at an absolute premium, and which do not have large variations in the dynamics (for which a variable time-step would be more favorable).

Variable step-size Runge-Kutta integrators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variable step-size multistage integrators, which can be defined by specifying scalar tolerances
(using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_variable_step_size` function) or vector
tolerances (using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_variable_step_size_vector_tolerances` function).
In the case of the former, the same absolute and relative tolerance is used for each state entry. In the latter case, the tolerances
can be made to vary for the different state entries. Several different Butcher Tableaus, corresponding to different
specific integrators, and integrator error, can be specified by using the :class:`~tudatpy.numerical_simulation.propagation_setup.integrator.RKCoefficientSets` enum.
Normallly, this integrator uses a :ref:`step size control <integrator_step_size_control>` to adapt its step, but it can also
be :ref:`forced to take a fixed step <integrator_force_fixed_step>`.

**General considerations** This type of integrator is generally robust, and can be applied to a broad variety of dynamical systems
without many special considerations. It generally has a decent balance between computational efficiency and solution quality for
orbital dynamics problems.

Bulirsch-Stoer integrator
^^^^^^^^^^^^^^^^^^^^^^^^^

Variable step-size extrapolation integrator, defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.bulirsch_stoer` function.
Normallly, this integrator uses a :ref:`step size control <integrator_step_size_control>` to adapt its step, but it can also
be :ref:`forced to take a fixed step <integrator_force_fixed_step>`.

**General considerations** For orbital mechanics problems, the Bulirsch-Stoer integrator is popular for long integration
periods, owing to its generally good trade-off between computational efficiency and solution quality. However, since it
takes exceptionally long time steps (may be on the order of an orbital period), the results are generally not useful
for creating interpolator to obtain continuous results (Tudat has no options for dense output).

Adams-Bashforth-Moulton integrator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variable step-size, variable-order multi-step integrator, defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.adams_bashforth_moulton` function.
Normallly, this integrator uses a :ref:`step size control <integrator_step_size_control>` to adapt its step, but it can also
be :ref:`forced to take a fixed step <integrator_force_fixed_step>`.

**General considerations** The ABM method generally takes relatively short time steps, and therefore produces very dense
output, making the creation of an interpolator from the numerical results less prone to interpolation error. Step size
control for this integrator is more limited than for other integrators, with the step size being adaptable by a factor
:math:`N` or :math:`1/N` only (with :math:`N` an integer). Since the integrator requires a past state history, it has to
be initialized. Current initialization is hard-coded to the use of an RKF8(7) integrator using the same tolerances
as the ABM integrator. Due to an issue in the implementation, this integrator has the tendency to get 'stuck' at very small
time steps, and it is *strongly* advised to provide a realistically small minimum time step.


.. _integrator_step_size_control:

Step-size control
-----------------

For step-size control, the relative tolerance has the largest impact on the solution quality.
Typical ranges for its value are :math:`10^{-14}-10^{-10}`. The absolute tolerance only becomes active when one or more of the state
elements get close to 0. It is standard (but not necesarilly ideal) practice to set the absolute tolerance equal to the relative
tolerance.

.. _integrator_force_fixed_step:

Forcing fixed step-size
-----------------------

Many of the above integrators allow you to supply absolute and relative tolerances, which the integrators use to adapt the
step size that is taken, based on the behaviour of the dynamics. You can force these integrators to a fixed step size by:
* Setting the initial time step, minimum time step and maximum time step to the same value (the fixed time step you wish to impose)
* Setting the relative and absolute tolerances to infinity (or a similarly high value)



