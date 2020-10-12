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

* Specifying an additional formulation for teh translational state (see TODO)
* Specifying alternative termination conditions (see TODO)
* Speciyingg variables that are to be saved during the propagation (see TODO)
* Requesting terminal output during the propagation (see TODO) 


Rotational dynamics
###################

Mass dynamics
#############

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
