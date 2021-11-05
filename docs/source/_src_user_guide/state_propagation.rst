******************
State Propagation
******************

In this section, the different stages of a typical simulation setup are described. The user is guided along the creation of the environment, the dynamical model, output variables, termination settings, the integrator, and the actual simulation itself. Code examples will illustrate the usage of the application programming interface (API), both in Python and C++. (C++ is WIP)

 .. figure:: flowchart.png
    :width: 800

.. _environment_setup:

Environment Setup
==================

In Tudat, the physical environment is defined by a system of bodies, each encapsulated in a :class:`~tudatpy.numerical_simulation.environment.Body` object. Such an object may represent a celestial body, or a manmade vehicle, and Tudat makes *no* a priori distinction between the two. The distinction is made by the user when creating the bodies The combination of all Body objects is stored in a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object (typically named simple ``bodies`` in the code). Each body contains a list of properties (gravity field, ephemeris, *etc.*, see below for a comprehensive list), which may be interdependent. During the propagation, all the required properties of bodies are extracted and combined to evaluated accelerations/torques/guidance/... and compute the state derivative of thee system.

The typical procedure to create the environment is the following:

* Load default settings for celestial bodies in the simulation
* Modify default settings as required for the simulation (if needed)
* Create body objects from these settings (automatically resolving any interdependencies)
* Create any additional bodies which have no defaults (typically spacecraft)
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

When defining the environment, it is important to understand a number of aspects related to computations that are happening 'under the hood'. Below, several key aspects are discussed:

.. toctree::
    :maxdepth: 1

    environment_setup/use_of_reference_frames

In various applications, the environment models that are already implemented in Tudat will not suffice for a given application, and you will want to define your own custom models. The manner in which to do this is similar for each environment model, and is discussed in more detail below:

.. toctree::
    :maxdepth: 1

    environment_setup/custom_settings

When using these custom models, and in various other cases, you may need to interact with the simulation environment *during* the propagation, below you find details on how to extract information (states, orientations, altitude, *etc.*) from the simulation during the propagation
 
.. toctree::
    :maxdepth: 1
  
    environment_setup/environment_during_propagation


.. _simulation_propagator_setup:

Propagation Setup
=================

In Tudat, the term 'propagator' is used to denote the formulation of the differential equations that are to be numerically solved. This includes the type of dynamics (translational, rotational, mass), but also the formulation for a given type of dynamics (e.g. Encke, Cowell, Kepler elements for translational dynamics).

.. _propagator_setup:

================
Propagator Setup
================

Tudat currently supports the propagation of three types of dynamics: translational, rotational and mass. Any combination of any number of types of dynamics, for any number of bodies, may be defined.

.. toctree::
    :maxdepth: 1

    propagation_setup/dynamics_types/translational
    propagation_setup/dynamics_types/rotational
    propagation_setup/dynamics_types/mass

You may also propagate any combination of dynamics types, for any number of bodies, as discussed on the pages below.

.. toctree::
    :maxdepth: 1

    propagation_setup/dynamics_types/multi_type
    propagation_setup/dynamics_types/multi_body


The state that is propagated may be one of a number of state representations. For the case of translational dynamics, for instance, there are various options besides a simple Cartesian state representation. However, even when using a non-Cartesian state vector, the Cartesian representation still plays a role in calculating *e.g.* acceleration models. More on the role of different state representations is discussed on the page below:

.. toctree::
    :maxdepth: 1

    propagation_setup/settings/conventional_vs_propagated_coordinates

.. _state_derivative_model_setup:

==============================
State Derivative Model Setup
==============================

For each of the dynamics types, you must provide models to calculate the state derivative, specifics are discussed below

Acceleration Model Setup
-------------------------

To propagate translational dynamics, you must provide a set of acceleration models. The acceleration model setup is provided here:

.. toctree::
    :maxdepth: 1

    propagation_setup/acceleration_models/setup

Below, a comprehensive list of all available acceleration models in Tudat, and the manner in which to define them, is given

.. toctree::
    :maxdepth: 1
    
    propagation_setup/acceleration_models/available

.. _torque_models:


Torque Model Setup
-------------------

To propagate rotational dynamics, you must provide a set of torque models.
Torque models are handled in a similar manner to the translational acceleration models:


.. toctree::
    :maxdepth: 1

    propagation_setup/torque_models/setup
    propagation_setup/torque_models/available



Mass rate Model Setup
---------------------

Due to the simplicity of setting up mass rate models, this functionality has already by included in the :ref:`mass propagator setings <mass_dynamics>`

.. _simulation_output_variables:

=========================
Output Variables
=========================

By default, propagating the dynamics of a body provides only the numerically integrated state history of your model as output. Tudat has the option to provide any number of additional outputs from your simulation, by defining the ``output_variables`` input to the propagator settings. For more details, see the page below:

.. toctree::
    :maxdepth: 2
    
    propagation_setup/dependent_variables/available

.. _termination_settings:

=========================
Termination Settings
=========================

The typical propagation is terminated when a specific final time is reached. Tudat provides additional possibilities for defining when the simulator terminates the propagation. A full list is given below:

.. toctree::
    :maxdepth: 2
    
    propagation_setup/termination/available

.. _integrator_setup:


Integrator Setup
=================

The environment and formulation of dynamical equations are now in place. In order to solve these equations you still need to define the numerical integrator settings. These settings specify *how* the equations are solved. In Tudat(Py) you can choose between different types of integrators.


Since the choice of integrator strongly depends on the nature of the dynamical problem and the requirements of the user, there is no 'best' integrator that works in all cases. Details about the different types will **not** be given here; you are referred to existing literature on the topic of numerical integrators. We only show you how to create the integrator settings, given on the following page:

.. toctree::
  :maxdepth: 1

  integrator_setup/settings


Running the Simulation
======================

With all the necessary simulation settings in place, it is time to run the simulation. In Tudat(Py), this is done by means of a simulator object, which handles the setup and execution of the simulation, by tieing all the settings and models defined on the above pages together, defining and solving the state derivative equation:


.. math::

      \dot{\mathbf{x}}&=\mathbf{f}(\mathbf{x},t;\mathbf{p})\\
      \mathbf{x}(t_{0})&=\mathbf{x}_{0}

where :math:`\mathbf{x}` defines the state vector that is to be propagated (defined by the choice of your :ref:`propagator_setup`), :math:`t_{0}` and :math:`\mathbf{x}_{0}` define the initial time and state, defined in the :ref:`propagator_setup` and :ref:`integrator_setup`, respectively. The parameter vector :math:`\mathbf{p}` is included explicitly in the state derivative function to denote its dependence on various environmental and system parameters, as defined throug the :ref:`environment_setup`. Finally, the state derivative function :math:`\mathbf{f}` is created through the definition of the type and formulation of the dynamics, and the :ref:`state_derivative_model_setup`.

The above differential equations is solved using the specific :ref:`choice of integrator <integrator_setup>`, and is terminated by used-specified :ref:`termination_settings` (as defined in the :ref:`propagator_setup`). The output of the propagation consists of the state that is propagated, as well as any number of :ref:`simulation_output_variables`.

====================
Propagating Dynamics
====================

Simulations in which only the system state is propagated are handled by simulator objects from the ``Simulator`` base class.
For propagation of the system state along a single arc, see the page below:

.. toctree::
  :maxdepth: 1

  running_simulation/single_arc

=================================
Propagating Variational Equations
=================================

In addition to propagating dynamics, Tudat is also capable of propagating the so-called variational equations associated with the dynamics to produce the state transition matrix :math:`\Phi(t,t_{0})` and sensitivity matrix :math:`S(t)`, which we define here as:

.. math::

      \Phi(t,t_{0}) &= \frac{\partial \mathbf{x}(t)}{\partial\mathbf{x}(t_{0})}\\
      S &= \frac{\partial \mathbf{x}(t)}{\partial \mathbf{p  }}\\

where :math:`\mathbf{x}` is the propagated state, :math:`\mathbf{p}` the vector of a parameter vector (e.g. gravity field parameters, rotation model parameters, etc.), and :math:`t_{0}` denotes the initial time.
These two matrices are based on linearization of the complex dynamics and can be used to quickly determine the influence of a change in initial state (:math:`\mathbf{x}(t_{0})`) and/or parameters (:math:`\mathbf{p}`) on the state :math:`\mathbf{x}(t)` at time :math:`t`.

Parameter settings
------------------

If the user wishes to do propagate the variational equations alongside the system sate, settings for the parameters that are to be used in the variational equations have to be defined.
In terms of the equations above, it needs to be specified for which parameters :math:`\mathbf{x}_{0}` and :math:`\mathbf{p}` the solution for the state transition and sensitivity matrices is to be computed.
In Tudat(Py) these parameters are referred to as parameters or sometimes "estimated" parameters, because of their primary application in state estimation problems.

A description of how these parameters are to be defined and a comprehensive list of all available parameters are linked below:

.. toctree::
    :maxdepth: 3

    sensitivity_analysis/parameter_settings
    sensitivity_analysis/available_parameters


Performing the Propagation
--------------------------

Simulations in which only the system state and variational equations is propagated are handled by simulator objects from the ``VariationalSimulator`` base class.
For propagation of the system state and variational equations along a single arc, see the page below:

.. toctree::
  :maxdepth: 1

  running_simulation/single_variational_arc



