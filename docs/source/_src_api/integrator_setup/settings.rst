.. _simulation_integrator_settings:

Integrator Settings
###################

This page lists the available integrators within Tudat(Py) and provides code examples which illustrate their configuration. This section does however **not** include detailed descriptions of the integrators' mechanics and applications. More information and application examples are taught in the TU Delft Numerical Astrodynamics (AE4868) and Propagation & Optimization (AE4866) courses, or can be found in existing literature on the topic. Below, the various integrators in Tudat are discussed.


.. _simulation_integrator_type_euler:

.. class:: Euler

The Euler method is the simplest integrator that is available in Tudat. It is known to be inaccurate for complex dynamics and is therefore **discouraged for use in research**. It can however still be used for comparison studies or very simple propagations.

.. tabs::

   .. tab:: Python

    .. toggle-header:: 
       :header: Required **Show/Hide**

       .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup.py
          :language: python

    .. literalinclude:: /_src_snippets/simulation/integrator_setup/euler.py
       :language: python

    .. toggle-header:: 
     :header: Required after **Show/Hide**

     .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup_after.py
        :language: python

   .. tab:: C++


   - :literal:`initial_time`

      Floating point value that defines the simulation's start epoch. 

   - :literal:`fixed_step_size`

      Floating point valuethat defines the fixed step-size to be used either by the :literal:`euler` or the :literal:`rungeKutta4` numerical integrator. 
   
   - :literal:`save_frequency`

      Cadence at which to save the numerical integrated states. For instance, you may want to save one every 15 time steps, to give an output that is less demanding in terms of storage (in this case 15 would be the :literal:`save_frequency`). The default value is 1.

   - :literal:`assess_termination_on_minor_steps`

      Determines whether the propagation termination conditions should be evaluated during each function evaluation (or 'minor step') of the integrator (``true``) or only at the end of each integration step (``false``). The default value is ``false``, and the termination conditions are only checked on each full step of the intergator.


.. _simulation_integrator_type_rk4:       

.. class:: Runge-Kutta 4

The Runge-Kutta 4 integrator is a fixed step size integrator. It is a multistage method, meaning that it uses multiple stages (function evaluations) to perform a single time step. In the case of RK4, there are four stages.

.. tabs::

   .. tab:: Python

    .. toggle-header:: 
       :header: Required **Show/Hide**

       .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup.py
          :language: python

    .. literalinclude:: /_src_snippets/simulation/integrator_setup/runge_kutta_4.py
       :language: python

    .. toggle-header:: 
     :header: Required after **Show/Hide**

     .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup_after.py
        :language: python

   .. tab:: C++

   - :literal:`initial_time`

      Floating point value that defines the simulation's start epoch. 

   - :literal:`fixed_step_size`

      Floating point valuethat defines the fixed step-size to be used either by the :literal:`euler` or the :literal:`rungeKutta4` numerical integrator. 
   
   - :literal:`save_frequency`

      Cadence at which to save the numerical integrated states. For instance, you may want to save one every 15 time steps, to give an output that is less demanding in terms of storage (in this case 15 would be the :literal:`save_frequency`). The default value is 1.

   - :literal:`assess_termination_on_minor_steps`

      Determines whether the propagation termination conditions should be evaluated during each function evaluation (or 'minor step') of the integrator (``true``) or only at the end of each integration step (``false``). The default value is ``false``, and the termination conditions are only checked on each full step of the intergator.

.. _simulation_integrator_type_rkf_and_rkdp:
       
.. class:: Runge-Kutta-Fehlberg and Runge-Kutta Dormand-Prince

These variable-step multi-stage integrators allow for step size control using embedded Runge-Kitta methods, with the step size adaptation based on user-defined tolerances.  

One of a number of different sets of coefficient sets for the embedded Runge-Kutta methods may be selected

* RKF4(5), defined by ``propagation_setup.integrator.RKCoefficientSets.rkf_45`` (in Python)
* RKF5(6), defined by ``propagation_setup.integrator.RKCoefficientSets.rkf_56`` (in Python)
* RKF7(8), defined by ``propagation_setup.integrator.RKCoefficientSets.rkf_78`` (in Python)
* RKDP8(7), defined by ``propagation_setup.integrator.RKCoefficientSets.rkdp_87`` (in Python)

These coefficient sets may be defined as follows:

The integrator settings for the variable step-size multi-stage integrator may be defined as follows:

.. tabs::

   .. tab:: Python

    .. toggle-header:: 
       :header: Required **Show/Hide**

       .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup.py
          :language: python

    .. literalinclude:: /_src_snippets/simulation/integrator_setup/runge_kutta_fehlberg.py
       :language: python

    .. toggle-header:: 
     :header: Required after **Show/Hide**

     .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup_after.py
        :language: python

   .. tab:: C++

   - :literal:`initial_time`

      Floating point value that defines the simulation's initial time. 
   
   - :literal:`initial_time_step`

      Floating point value that defines the initial step-size to be used by the numerical integrator. 

   - :literal:`coefficient_set`

      Setting that defines the coefficient set to be used by numerical integrator. The list of available coefficient sets is given above.

   - :literal:`minimum_step_size`

      Floating point value that defines the minimum step-size that the numerical integrator can take. 

   - :literal:`maximum_step_size`

      Floating point value that defines the maximum step-size that the numerical integrator can take.

   - :literal:`relative_error_tolerance`

      Floating point value that defines the relative error tolerance for step size control of the numerical integrator.

   - :literal:`absolute_error_tolerance`

      Floating point value that defines the absolute error tolerance for step size control of the numerical integrator.

   - :literal:`save_frequency`

      Cadence at which to save the numerical integrated states. For instance, you may want to save one every 15 time steps, to give an output that is less demanding in terms of storage (in this case 15 would be the :literal:`save_frequency`). The default value is 1.

   - :literal:`assess_termination_on_minor_steps`

      Determines whether the propagation termination conditions should be evaluated during each function evaluation (or 'minor step') of the integrator (``True``) or only at the end of each integration step (``False``). The default value is ``False``, and the termination conditions are only checked on each full step of the intergator.

   - :literal:`safety_factor`

      Safety factor for step size control. The default value is 0.8.

   - :literal:`maximum_factor_increase`

      Maximum increase factor in time step in subsequent iterations. The default value is 4.0.

   - :literal:`minimum_factor_increase`

      Minimum decrease factor in time step in subsequent iterations. The default value is 0.1.

       
.. _simulation_integrator_type_bs:

.. class:: Bulirsch-Stoer

The following different sequences are available for the Bulirsch-Stoer method in Tudat:

* Bulirsch-Stoer sequence;
* Deufelhard sequence.

These are available in the ``propagation_setup.ExtrapolationMethodStepSequences`` enum and must be supplied to the Python function that initializes the integrator, as shown below:

.. tabs::

   .. tab:: Python

    .. toggle-header:: 
       :header: Required **Show/Hide**

       .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup.py
          :language: python

    .. literalinclude:: /_src_snippets/simulation/integrator_setup/bulirsch_stoer.py
       :language: python

    .. toggle-header:: 
     :header: Required after **Show/Hide**

     .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup_after.py
        :language: python

   .. tab:: C++

.. _simulation_integrator_type_abm:

.. class:: Adams-Bashforth-Moulton

The last integrator in the list is a multi-step, predictor-corrector method. It uses multiple time steps in its approximation of the next step and is implicit, meaning that it needs a predictor-corrector setup to solve for the unknown time step. Its *order* is the number of steps used to predict the next value, so an order of two means that steps n-1 and n are used to predict n+1.

Bounds on the used order must be given to the Python function initializing the integrator, next to the customary arguments:

.. tabs::

   .. tab:: Python

    .. toggle-header:: 
       :header: Required **Show/Hide**

       .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup.py
          :language: python

    .. literalinclude:: /_src_snippets/simulation/integrator_setup/adams_bashforth_moulton.py
       :language: python

    .. toggle-header:: 
     :header: Required after **Show/Hide**

     .. literalinclude:: /_src_snippets/simulation/integrator_setup/req_integrator_setup_after.py
        :language: python

   .. tab:: C++

