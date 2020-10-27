.. _simulation_integrator_settings:

Integrator Settings
###################

Euler
-----

The Euler method is the simplest integrator that is available in Tudat. It is known to be inaccurate for complex dynamics and is therefore **discouraged** for use in research. It can however still be used for comparison studies or very simple propagations.

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

       
Runge-Kutta-Fehlberg
--------------------

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
       
Runge-Kutta Dormand-Prince
--------------------------

Bulirsch-Stoer
--------------

The following different sequences are available for the Bulirsch-Stoer method in Tudat:

* Bulirsch-Stoer sequence;
* Deufelhard sequence.

The example below shows how the user can specify the sequence to be used by the integrator.

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

