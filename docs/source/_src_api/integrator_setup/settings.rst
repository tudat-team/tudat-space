.. _simulation_integrator_settings:

Integrator Settings
###################

This page lists the available integrators within Tudat(Py) and provides code examples which illustrate their configuration. This section does however **not** include detailed descriptions of the integrators' mechanics and applications. More information and application examples are taught in the TU Delft Numerical Astrodynamics (AE4868) and Propagation & Optimization (AE4866) courses, or can be found in existing literature on the topic.

Euler
-----

The Euler method is the simplest integrator that is available in Tudat. It is known to be inaccurate for complex dynamics and is therefore **discouraged for use in research**. It can however still be used for comparison studies or very simple propagations.

Its configuration is straightforward: it only needs an initial time and a fixed time step to operate.

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
       

Runge-Kutta 4
-------------

The Runge-Kutta 4 integrator is the only other integrator in Tudat that uses a fixed step size. It is a multistage method, meaning that it uses multiple stages in between time steps to better predict the state at the next time step; in this case, there are four stages.

Since it is a fixed time step method, configuration is straightforward and follows the same template as the Euler integrator: it only needs an initial time and step size.

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

       
Runge-Kutta-Fehlberg and Runge-Kutta Dormand-Prince
---------------------------------------------------

Being an extension to the RK4 method described above, Runge-Kutta-Fehlberg performs two integrations: a 'normal' one and a more high-fidelity one using one more stage. This means that the method now has a means of estimating the integration error and thus correcting the time step.

The user can choose from the following coefficient sets for RKF, where the numbers indicate the number of stages in each time step:

* RKF4(5);
* RKF5(6);
* RKF7(8);
* RKDP8(7).

These are available in the enum ``propagation_setup.CoefficientSets`` and must be supplied to the Python function that initializes the integrator, as follows:

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
       

Bulirsch-Stoer
--------------

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

Adams-Bashforth-Moulton
-----------------------

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

