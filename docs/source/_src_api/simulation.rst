**********
Simulation
**********



Environment Set-Up
==================

In Tudat, the physical environment is defined by a system of bodies, each encapsulated in a Body object. Such an object may represent a celestial body, or a manmade vehicle, and Tudat makes *no* a priori distinction between the two. The distinction is made by the user when creating the bodies The combination of all Body objects is stored a SystemOfBodies object. 

The typical procedure to create the environment is the following:

* Load default settings for celestial bodies in the simulation
* Modify default settings as required for the simulation (if needed)
* Create celestial bodies based on these settings
* Create any additional bodies which have no defaults
* Assign properties to these additional bodies

A typical procedure for carrying out this process is given on page TODO(getting started), to create a default Sun, Earth and Moon, and a body named "Vehicle" with a mass of 5000 kg, and constant aerodynamic coefficients (reference area of 50 m^2, drag coefficient of 1.2)

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/create_bodies_1.py
          .. literalinclude:: /_src_snippets/simulation/environment_setup/create_vehicle.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp


Details on the above procedure, and various additional/alternative options available to you for creating bodies, are given in the following pages:

.. toctree::
    :maxdepth: 3

    environment_setup/create_bodies/settings
    environment_setup/create_bodies/add_bodies
    environment_setup/create_bodies/default_settings

Details on all available environment models, and how to define them in your simulation, is given below:

.. toctree::
    :maxdepth: 3

    environment_setup/create_models/available
    environment_setup/create_models/custom
    environment_setup/create_models/system
    .. environment_setup/create_models/tabulated_atmosphere
    .. environment_setup/create_models/aerodynamic_coefficients



Propagator Set-Up
=================

In Tudat, the term 'propagator' is used to denote the formulation of the differential equations that are to be numerically solved. This includes the type of dynamics (translational, rotational, mass), but also the formulation for a given type of dynamics (e.g. Encke, Cowell, Kepler elements for translational dynamics)

=============
Dynamics type
=============

Tudat currently supports the propagation of three types of dynamics: translational, rotational and mass. Any combination of any number of types of dynamics, for any number of bodies, may be defined.

Translational dynamics
######################

Basic settings for propagating translational dynamics require:

* The names of the bodies that are to be propagated
* The centers of propagation w.r.t. which they are to be propagated
* Acceleration models that are to be used for the dynamics
* Initial state, in Cartesian elements with the same frame orientation as the environment (see TODO)
* Termination time of propagation

Such a propagation is defined as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

With these settings, the body "Vehicle" will be propagated w.r.t. body "Earth", using given acceleration models (see TODO), a given initial state which defines the initial Cartesian state of the center of mass of "Vehicle" w.r.t. the center of mass of "Earth". The propagation will terminate once the ``simulation_end_epoch`` epoch is reached.

Additional options that can be used for the propagation:

* Specifying alternative termination conditions (see TODO), this input replaces the ``simulation_end_epoch`` above
* Specifying an alternative formulation for the translational state (see TODO). Default: Cowell formulation (Cartesian position and velocity) is used
* Specifying variables that are to be saved during the propagation (see TODO). Default: None
* Requesting terminal output during the propagation (see TODO) . Default: None

These additional options can be provided as follows (TODO code):

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

Where the three final, and optional, input arguments can be used with both when ``termination_settings`` and ``simulation_end_epoch`` input. 

Rotational dynamics
###################

Settings and optionsto define the propagation of rotational dynamics are largely similar to those of translational dynamics. Differences are:

* A set of torque models has to be supplied, as opposed to acceleration models. See (TODO) for the list of options for torques in Tudat
* No 'central body' is specified. The rotational state that is propagated is always that from the global inertial orientation, to the body-fixed orientation of the propagated body
* The propagated state formulation is, by default, a vector of size 7 (for a single body), with:
	- Entries 1-4: The quaternion defining the rotation from inertial to body-fixed frame
	- Entries 5-7: The body's angular velocity vector, expressed in its body-fixed frame
* Alternative formulations for propagated state vector can be selected from (TODO)

Defining settings for the rotational dynamics is done by:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_rotational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp


where the final three inputs are all optional, and the ``simulation_end_epoch`` input may be replaced by the more general ``termination_settings`` (see TODO), as was the case for translational dynamics

Mass dynamics
#############

Propagating the mass of a body is typically (but not exclusively) coupled with the use of a thrust model. For a full description of mass-rate models and thrust models, see (TODO and TODO). Defining mass propagation settings is done similarly to the translational and rotational dynamics:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_mass_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

where the final two inputs are optional, and the ``simulation_end_epoch`` input may be replaced by the more general ``termination_settings`` (see TODO).

Multi-type dynamics
###################

Tudat permits the propagation of any combination of types of dynamics, for any number of bodies
One example is the simulation of coupled translational-rotational dynamics of one or more bodies, or the combined translational and mass dynamics of a body (e.g. spacecraft under thrust). N

To define multi-type propagaor settings, you must first define the propagaor settings for each type of dynamics separately, after which you combine these using the TODO function, as follows: 

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/full_rotational_setup.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/full_mass_setup.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_multitype_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

This example shows the use of the translational, rotational and mass dynamics of a single body ``Vehicle``. However, the framework is not limited to propagating the differnet types of dynamics for only one body. You may for instance propagate the translational state and mass of a spacecraft concurrently with the rotational state of the Earth. Also, you may propagate any number of any type of dynamics of any body, e.g. translational dynamics of 6 bodies, rotational dynamics of 4 bodies and mass of 2 bodies, where these three sets of bodies may but need not fully or partially overlap)
   
   .. Warning:: When using multi-type propagator settings, the output variables, termination settings, and print interval defined through the ``propagation_setup.propagator.multi_type`` function are used. Settings of the same kind are also stored in the constituent single-type propagator settings, but these are fully ignored when using multi-type settings 


Multi-body dynamics
###################

The propagation framework in Tudat is implemented such that any number of bodies may be propagated numerically. Taking the translational dynamics as an example, propagating multiple bodies is achieved simply by extending the list of propagated bodies and central bodies:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_multi_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cp

Where the ``acceleration_models`` should contain a set of acceleration models acting upon each propagated body (if one or more of the bodies is omitted from the ``acceleration_models``, no accelerations are assumed to act on this body, without warning or error).

The use of a 'hierarchical' system is also supported by Tudat. For instance, one can propagate the Earth and Mars w.r.t. the Sun, the Sun w.r.t. the barycenter, the Moon w.r.t the Earth:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_multi_hierarchy_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cp

In either case, any and all physical interactions are automatically formulated as required for the specific dynamical system under consideration. Specifically, the use of direct and third-body gravitational accelerations, and the definition of the correct effective gravitational parameter, are automatically handled. See TODO for details on this process


=========================
Acceleration Model Set-Up
=========================

In Tudat, an acceleration acting on a body is defined by

*  The body undergoing acceleration
*  The body exerting the acceleration
*  The type and settings of the acceleration

A user defines these settings for each acceleration in their simulation. These settings are then used to create the acceleration models:


    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/acceleration_example.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

where a spherical harmonic (degree and order 5) gravitational acceleration, and aerodynamic acceleration, of the Earth are defined, as well as a point-mass gravity of Sun and Moon. The variable ``accelerations_settings_vehicle`` denotes the list of bodies exerting accelerations, and the types of accelerations, and the variable ``acceleration_settings`` associates this list with the body undergoing the acceleration. The function ``create_acceleration_models`` creates the list of models that compute the accelerations during the propagation.

Below, a comprehensive list of all available acceleration models in Tudat, and the manner in which to define them, is given

.. toctree::
    :maxdepth: 2
    
    propagation_setup/acceleration_models/available


    
=========================
Output Variables
=========================

By default, propagating the dynamics of a body provides only the numerically integrated state history of your model as output. Tudat has the option to provide any number of additional outputs from your simulation, by defining the ``output_variables`` input to the propagator settings. For instance:


To save the altitude of ' Vehicle' w.r.t. Earth and the aerodynamic acceleration exerted by the Earth on this vehicle. A comprehensive list of available outputs is given below 

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


Integrator Set-Up
=================


.. toctree::
    :maxdepth: 2
    
    integrator_setup/settings
