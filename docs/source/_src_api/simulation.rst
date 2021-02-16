**********
Simulation
**********

In this section, the different stages of a typical simulation setup are described. The user is guided along the creation of the environment, the dynamical model, output variables, termination settings, the integrator, and the actual simulation itself. Code examples will illustrate the usage of the application programming interface (API), both in Python and C++. (C++ is WIP)

 .. figure:: flowchart.png
    :width: 800

Environment Setup
==================

In Tudat, the physical environment is defined by a system of bodies, each encapsulated in a Body object. Such an object may represent a celestial body, or a manmade vehicle, and Tudat makes *no* a priori distinction between the two. The distinction is made by the user when creating the bodies The combination of all Body objects is stored in a ``bodies`` object. 

The typical procedure to create the environment is the following:

* Load default settings for celestial bodies in the simulation
* Modify default settings as required for the simulation (if needed)
* Create celestial bodies based on these settings
* Create any additional bodies which have no defaults
* Assign properties to these additional bodies

All the options available to you for creating bodies are given in the following pages:

.. toctree::
    :maxdepth: 3

    environment_setup/create_bodies/settings
    environment_setup/create_bodies/add_bodies
    

Details on all available environment models, and how to define them in your simulation, is given below:

.. toctree::
    :maxdepth: 1

    environment_setup/create_bodies/default_settings
    environment_setup/create_models/available
    environment_setup/create_models/custom
    environment_setup/create_models/system

Specifics on the environment during propagations can be found here:

.. toctree::
    :maxdepth:3

    environment_setup/environment_during_propagation
    environment_setup/valid_time_range

.. _simulation_propagator_setup:

Propagation Setup
=================

In Tudat, the term 'propagator' is used to denote the formulation of the differential equations that are to be numerically solved. This includes the type of dynamics (translational, rotational, mass), but also the formulation for a given type of dynamics (e.g. Encke, Cowell, Kepler elements for translational dynamics).

================
Propagator Setup
================

Tudat currently supports the propagation of three types of dynamics: translational, rotational and mass. Any combination of any number of types of dynamics, for any number of bodies, may be defined.

.. toctree::
    :maxdepth: 3

    propagation_setup/dynamics_types/translational
    propagation_setup/dynamics_types/rotational
    propagation_setup/dynamics_types/mass
    propagation_setup/dynamics_types/multi_type

On the following page, we give a brief description of how propagate the dynamics of multiple bodies concurrently:

.. toctree::
    :maxdepth: 3

    propagation_setup/dynamics_types/multi_body


The following page provides you with the difference between *conventional* and *propagated* coordinates in the propagator settings. It is important to keep in mind that this page covers some details which happen 'under the hood'.

.. toctree::
    :maxdepth: 1

    propagation_setup/settings/conventional_vs_propagated_coordinates

=========================
Acceleration Model Setup
=========================

To propagate translational dynamics, you must provide a set of acceleration models. The acceleration model setup is provided here:

.. toctree::
    :maxdepth: 1

    propagation_setup/acceleration_models/setup

Below, a comprehensive list of all available acceleration models in Tudat, and the manner in which to define them, is given

.. toctree::
    :maxdepth: 1
    
    propagation_setup/acceleration_models/available

.. _torque_models:

==================
Torque Model Setup
==================

.. toctree::
    :maxdepth: 2

    propagation_setup/torque_models/setup
    propagation_setup/torque_models/available



.. _simulation_output_variables:

=========================
Output Variables
=========================

By default, propagating the dynamics of a body provides only the numerically integrated state history of your model as output. Tudat has the option to provide any number of additional outputs from your simulation, by defining the ``output_variables`` input to the propagator settings. A comprehensive list of available outputs is given below 

.. toctree::
    :maxdepth: 2
    
    propagation_setup/dependent_variables/available

=========================
Termination Settings
=========================

The typical propagation is terminated when a specific final time is reached. Tudat provides additional possibilities for defining when the simulator terminates the propagation. A full list is given below:

.. toctree::
    :maxdepth: 2
    
    propagation_setup/termination/available


Integrator Setup
=================

The environment and formulation of dynamical equations are now in place. In order to solve these equations you still need to define the numerical integrator settings. These settings specify *how* the equations are solved. In Tudat(Py) you can choose between different types of integrators.


Since the choice of integrator strongly depends on the nature of the dynamical problem and the requirements of the user, there is no 'best' integrator that works in all cases. Details about the different types will **not** be given here; you are referred to existing literature on the topic of numerical integrators. We only show you how to create the integrator settings, given on the following page:

.. toctree::
  :maxdepth: 1

  integrator_setup/settings

    
Running the Simulation
======================

With all the necessary simulation settings in place, it is time to run the simulation. In Tudat(Py), this is done by means of a DynamicsSimulator object, which handles the setup and execution of the simulation. It also contains functions to retrieve the propagated state history and dependent variables for further analysis and plotting.

In its simplest form, the ``DynamicsSimulator`` is used as shown in this example:

.. tabs::

     .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. code-block:: python
          
      		# Create simulation object and propagate dynamics.
      		dynamics_simulator = propagation_setup.SingleArcDynamicsSimulator(
        		bodies, integrator_settings, propagator_settings, True)
        		
    		states = dynamics_simulator.state_history
    		unprocessed_states = dynamics_simulator.unprocessed_state_history

     .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp
             
First, a ``SingleArcDynamicsSimulator`` is created using the system of bodies, integrator settings, and propagator settings objects. Tudat will then automatically read and setup the simulation accordingly. The ``True`` at the end of the line indicates that the equations of motion should be integrated immediately after creating the object, such that the state history can be retrieved afterwards. The latter is done in the next line when extracting the ``states``. The simulator will return a dictionary (Python) or map (C++) containing the state of the vehicle at each epoch, which can be exported or used for subsequent analysis. 

It's important to realize that, *regardless* of the formulation of the equations of motion (Cowell, Gauss-Kepler, etc.), the ``state_history`` attribute will always provide the results of the propagation, converted to Cartesian elements (for the case of translational dynamics). In the case where a different formulation than the Cowell formulation is used, the states that were actually used during the numerical integration can be accessed through the ``unprocessed_state_history``. For instance, whe using the ``gauss_keplerian`` propagator, it is the equations of motion in Keplerian elements which are solved numerically. The ``unprocessed_state_history`` will provide you with the history of the Keplerian elements (as directly solved for by the integrator), while the  ``state_history`` provides the Cartesian elements, obtained from the conversion of the propagated Keplerian elements(see :ref:`convention_propagated_coordinates` for more details).

If the user chose to also export dependent variables, they can be extracted from the dynamics simulator as follows:

.. tabs::

     .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. code-block:: python
          
          	# Retrieve dependent variables
      		dependent_variable_history = dynamics_simulator.get_dependent_variable_history()

     .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp
             
             
This concludes the section on simulation of this API guide. For more detailed information, refer to the pages listed in this section or refer to the next few sections for information and examples on e.g. interpolators, coordinate and time conversions, and interfaces to Spice, JSON, and Sofa.


Linear Sensitivity Analysis
============================

 .. figure:: flowchart_var_eq.png
    :width: 800

Up to this point, we have been concerned with propagating states of bodies only. Tudat is also capable of propagating the so-called variational equations associated with the dynamics to produce the state transition matrix :math:`\Phi(t,t_{0})` and sensitivity matrix :math:`S(t)`, which we define here as:

.. math::
      
      \Phi(t,t_{0}) &= \frac{\partial \mathbf{x}(t)}{\partial\mathbf{x}(t_{0})}\\
      S &= \frac{\partial \mathbf{x}(t)}{\partial \mathbf{p  }}\\

where :math:`\mathbf{x}` is the propagated state, :math:`\mathbf{p}` the vector of a parameter vector (e.g. gravity field parameters, rotation model parameters, etc.), and :math:`t_{0}` denotes the initial time.
These two matrices are based on linearization of the complex dynamics and can be used to quickly determine the influence of a change in initial state (:math:`\mathbf{x}(t_{0})`) and/or parameters (:math:`\mathbf{p}`) on the state :math:`\mathbf{x}(t)` at time :math:`t`.


.. note:: In some literature, the sensitivity matrix is not defined separately, but the state transition matrix :math:`\Phi(t,t_{0})` is defined as :math:`\frac{\partial[\mathbf{x}(t);\text{ }\mathbf{p}]}{\partial[\mathbf{x}(t_{0};\text{ }\mathbf{p}])}`

===============
Parameter Setup
===============

The propagation of the variational equations is done similarly to that of the dynamics. In addition to the settings described above, settings for the parameters that are considered are to be defined. In terms of the equations above, it needs to be specified for which parameters :math:`\mathbf{x}_{0}` and :math:`\mathbf{p}` the solution for the state transition and sensitivity matrices is to be computed.

The manner in which these parameters are to be defined, and a comprehensive list of all available paramaters, is described

.. toctree::
    :maxdepth: 3

    sensitivity_analysis/parameter_settings
    sensitivity_analysis/available_parameters
    
=====================================
Propagating the Variational Equations
=====================================
    
    
Now that the parameter settings have been created, the variational equations solver can be set up as well. This solver acts as a replacement of the normal dynamics simulator:

.. code-block:: python
	
	variational_equations_solver = estimation_setup.SingleArcVariationalEquationsSolver(
		bodies, integrator_settings, propagator_settings,
		estimation_setup.create_parameters_to_estimate(parameter_settings, bodies),
		integrate_on_creation=1 )
		
The state history, state transition matrices, and sensitivity matrices can then be extracted:

.. code-block:: python

	states = variational_equations_solver.state_history
	state_transition_matrices = variational_equations_solver.state_transition_matrix_history
	sensitivity_matrices = variational_equations_solver.sensitivity_matrix_history
	
For a complete example of propagating the variational equations, please see the tutorial :ref:`propagating_variational_equations`.

The :class:`EstimatableParameterSet` object contains three objects that have :class:`EstimatableParameter` as base class (one for each parameter). We distinguish two types of :class:`EstimatableParameter` objects:

* Those that represent initial conditions for dynamics (denoted as :math:`\mathbf{x}_{0}` below)
* Those that represent fixed parameters for environment, acceleration or observation models (denoted as :math:`\mathbf{q}` below)

Resetting the full parameter vector :math:`\mathbf{p}(=[\mathbf{x}_{0};\mathbf{q}])` is done as follows (for :literal:`double` state scalar type):
         
   .. code-block:: cpp

       // Create parameter set  
       std::shared_ptr< EstimatableParameterSet< double > > parametersToEstimate = ...
       
       Eigen::VectorXd parameterVector =
            parametersToEstimate->getFullParameterValues< double >( );

While resetting the full parameter vector is done as:

   .. code-block:: cpp

       // Create parameter set  
       std::shared_ptr< EstimatableParameterSet< double > > parametersToEstimate = ...
       
       // Define vector of new values of estimated parameters
       Eigen::VectorXd newParameterVector = ...
       
       // Reset parameter values
       parametersToEstimate->resetParameterValues< double >( );

When resetting the parameter vector, the change in the values in :math:`\mathbf{q}` immediately take effect. For the initial state parameters to take effect, however, the dynamics must be re-propagated. This occurs automatically when estimating parameters. It can also be performed manually by calling the :literal:`resetParameterEstimate` member function of the :class:`VariationalEquationsSolver` class. 


