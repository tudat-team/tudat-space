
==================
Parameter Settings
==================

The parameter estimation framework of Tudat allows an ever increasing variety of parameters to be estimated, examples of which include:

* Initial translational and rotational states of any number of bodies, 
* Properties of a body, such as a gravitational parameter :math:`\mu`
* Properties of a ground station, such as its body-fixed position :math:`\mathbf{x}_{GS}^{(B)}`
* Global properties of the simulation, such a Parameterize Post_Newtonian (PPN) parameters :math:`\gamma` and :math:`\beta`
* Acceleration model properties, such as empirical acceleration magnitudes
* Observation model properties, such as absolute and relative observation biases

In Tudat, these parameters influence the simulation in a variety of manners, and during propagation and/or observation simulation. Nevertheless, a *unified* framework is provided for defining any type of parameter. Very similar to the manner in which, for instance, acceleration or dependent variable settings are defined, a user must supply a list of parameter settings.

When only wishing to propagate the state transition matrix :math:`\Phi(t,t_{0})` (or depending on your use case, only estimate initial state parameters), the following line the relevant settings:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/sensitivity_analysis/state_only_parameters.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/sensitivity_analysis/state_only_parameters.cpp
             :language: cpp
             
which defines the initial state parameters to be fully consistent with the settings in the `propagator_settings`. 

.. note:: Options exist to manually define initial state parameters. However, at present, the initial state parameters **must** be consistent with the propagator settings, and these additional options are not described here. 

When wishing to propagate the sensitivity matrix :math:`S(t)` (or depending on your use case, estimate parameters in addtion to initial state parameters), the set of parameters can be extended using the following:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/sensitivity_analysis/full_parameter_settings.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/sensitivity_analysis/full_parameter_settings.cpp
	
         
In the snippet above, parameters are created to estimate the initial states in the `propagator_settings` (presumably Delfi C-3 initial translational states), the gravitational parameter of the Earth, the constant drag and the radiation pressure coefficient of Delfi-C3.

For the full list of available parameters, see :ref:`parameterSettingCreation`.