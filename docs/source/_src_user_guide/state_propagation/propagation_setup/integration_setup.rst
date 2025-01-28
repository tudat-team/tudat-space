.. _integrator_setup:

Integration Setup
=================

The environment and formulation of dynamical equations are now in place. In order to solve these equations
you need to define the settings for a numerical integrator. These settings specify *how* the equations are solved.
In Tudat, we offer three general types of integrators:

* :ref:`Multi-stage integrators <integrator_rk>` (Runge-Kutta)
* :ref:`Extrapolation integrators <integrator_bs>` (Bulirsch-Stoer)
* :ref:`Multistep integrators <integrator_abm>`  (Adams-Bashforth-Moulton)

These integrators are available in fixed- and variable-step varieties, as described in more detail below. The integrators
are implemented in Tudat, and do not use an external integrator library. For the background of these methods, we recommend people to refer to

* Satellite Orbits: Models, Methods and Applications, by Montenbruck and Gill
* Numerical Recipes in C++: The Art of Scientific Computing, by Press et al.  


Integrator types
----------------

In Tudat you can choose between different types of integrators.
For code examples and additional information on the interfaces, please follow the links to the API documentation given below.

.. _integrator_rk:

Multi-stage integrators
^^^^^^^^^^^^^^^^^^^^^^^

The fixed- and variable-step multi-stage integrator settings in Tudat are defined using the
:func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_fixed_step` and 
:func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_variable_step` functions, respectively. In both cases,
the user supplies the specific integrator through the definition of a :class:`~tudatpy.numerical_simulation.propagation_setup.integrator.CoefficientSets`,
which provides a long list of options for integrators, from the 1st order Euler, and classical Runge-Kutta 4 method, to very high order methods,
such as Feagin's 14(12) integrator. The step-size control for the multi-stage methods is described :ref:`below <integrator_step_size_control>`.

A subset of the :class:`~tudatpy.numerical_simulation.propagation_setup.integrator.CoefficientSets` allows for variable-step integrator definition,
through the use of a so-called embedded method. Although designed to allow variable-step integration, these methods essentially define two
fixed-step integration schemes: the RK7(8) scheme can be used for a fixed 7th-order, or a fixed 8th order integrator, if so desired. This
can be done by specifying the ``order_to_use`` input to the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.runge_kutta_fixed_step`,
which allows you to choose the lower- or higher-order method of the two.

In many typical cases, where a good accuracy and reasonable runtime is required, we have found that, out of the options provided in Tudat,
the ``rkf_78`` or ``rkdp_87`` coefficients (either in fixed or variable-step mode, depending on the type of problem) often provide a good trade-off
between accuracy, runtime, robustness and output density.


.. _integrator_bs:

Extrapolation integrators
^^^^^^^^^^^^^^^^^^^^^^^^^


The fixed- and variable-step extrapolation integrations in Tudat are defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.bulirsch_stoer_fixed_step` and :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.bulirsch_stoer_variable_step` functions, respectively. In both cases, the user provides the number substep-iterations to use, and the extrapolation sequence that is to be user (see function descriptions in API). The step-size control for the multi-stage methods is described :ref:`below <integrator_step_size_control>`.

For orbital mechanics problems, the Bulirsch-Stoer integrator is popular for long integration
periods, owing to its generally good trade-off between computational efficiency and solution quality. However, since it
takes exceptionally long time steps (may be on the order of an orbital period for high-order variants), the results are generally not useful
for creating interpolator to obtain continuous results, since Tudat has no options for dense output at the moment.

.. _integrator_abm:

Multi-step integrator
^^^^^^^^^^^^^^^^^^^^^

Variable step-size, variable-order Adams-Bashforth-Moulton integrator, defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.adams_bashforth_moulton` function.
Fixed-step and/or fixed-order options can be used through the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.adams_bashforth_moulton_fixed_step`, :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.adams_bashforth_moulton_fixed_order` and :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.adams_bashforth_moulton_fixed_step_fixed_order` functions.
The step-size control for this method is similar to that used by the previous two integrators, but uses a different interface (see note below).

The ABM method generally takes relatively short time steps, and therefore produces very dense
output, making the creation of an interpolator from the numerical results less prone to interpolation error. Step size
control for this integrator is more limited than for other integrators, with the step size being adaptable by a factor
:math:`N` or :math:`1/N` only (with :math:`N` an integer). Since the integrator requires a past state history, it has to
be initialized. Current initialization is hard-coded to the use of an RKF8(7) integrator using the same tolerances/step
as the ABM integrator. Due to the simplicity of the step-size control implementation, this integrator has the tendency to get 'stuck' at very small
time steps, and it is *strongly* advised to provide a realistically small minimum time step.

**NOTE** The ABM integrator in Tudat is due for a thorough refactoring, and revision of some of the implementation (in particular
step-size control). Therefore, it does not yet use the same interfaces for step-size control as the other methods, and it is
not recommended to use variable-step variant of this method without proper testing and tuning of settings.


.. _integrator_step_size_control:

Step-size control
-----------------

The step-size control algorithms used in Tudat consist of two aspects, a module that recommends a new step size based on an estimate of the error
at the current time step (the core of which is described in the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_control_elementwise_scalar_tolerance`),
and a module that may revise this recommended step, based on (mainly) settings for minimum/maximum time step settings. Settings for the latter are defined using the 
:func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_validation` function.

The methodology for the time-step control is equivalent in each type of integrator, with the difference stemming from the manner in which
a given integrator provides an estimate of the local error :math:`\boldsymbol{\epsilon}`. For the multi-stage integrator, this estimate is
obtained by comparing two embedded methods For the extrapolation integrator, this is obtained by comparing the computed state from the final,
and second to final, iteration.

The main parameters driving the step-size control are the relative and absolute tolerances, :math:`\epsilon_{r}` and :math:`\epsilon_{a}`. These can be provided and used in several different ways:

For **element-wise**, or **block-wise**, step size control. In the element-wise case, the step-size control algorithm is run separately for each of the state elements, with the state element resulting in the smallest required time step producing the recommended time step. Depending on the types of tolerances provided, the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_control_elementwise_scalar_tolerance` or :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_control_elementwise_matrix_tolerance` is used. 
  
In the block-wise case, the algorithm is performed on the norm of user-defined blocks of the state. For instance, when considering Cartesian positions, the element-wise control computes the required step-size based on the estimate for :math:`\epsilon_{x}`, :math:`\epsilon_{y}` and :math:`\epsilon_{z}` (estimated errors for each separate component) separately. For the block-wise control, the required step-size can be computed based on :math:`||\boldsymbol{\epsilon}_{r}||`, the norm of the error of the position vector (note that, when propagating Cartesian states, the state vector consists of both position and velocity). We provide two ways in which to define the state blocks on which the step-size control is to be defined:
  
* **User-specified matrix blocks** on which the step-size control is to be performed. In this case, the user manually specifies a list of rows/columns. Depending on the types of tolerances provided, the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_control_blockwise_scalar_tolerance` or :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_control_blockwise_matrix_tolerance` is used.
* **User-specified function that generates a matrix block** from the propagated state. In this case, the user provides a function that takes the state size (as number of rows and columns) as input
  and the integrator creates the matrix blocks when it is initialized (at which point the size of the state is defined). For instance, the 
  :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.standard_cartesian_state_element_blocks` function can be provided, which will apply step-size control on position and velocity 
  blocks of the state. This same function will provide the required step-size control blocks, regardless of whether a user propagates one or many bodies, or whether variational equations are 
  propagated or not. Depending on the types of tolerances provided, the :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_control_custom_blockwise_scalar_tolerance` or :func:`~tudatpy.numerical_simulation.propagation_setup.integrator.step_size_control_custom_blockwise_matrix_tolerance` is used.
* Either a **scalar tolerance** or a **vector/matrix tolerance**. When providing a scalar, the same tolerances are used for each element/block. When providing the tolerances as a vector/matrix,
  different tolerances can be set for every element/block. This can be advantageous to put stronger emphasis on controlling the error in some of the entries of the state vector,
  or in properly scaling teh absolute tolerance to the magnitudes of the state entries/blocks at hand.

For step-size control, the relative tolerance typically has the driving impact on the solution quality.
Typical ranges for its value are :math:`10^{-14}-10^{-6}`. The absolute tolerance only becomes active when one or more of the state
elements/blocks get close to 0. It is standard (but not at all ideal!) practice to set the absolute tolerance equal to
the relative
tolerance.



