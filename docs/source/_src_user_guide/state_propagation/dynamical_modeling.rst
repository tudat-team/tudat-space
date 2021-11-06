
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


