
.. _propagation_setup:

=================
Propagation Setup
=================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

    propagation_setup/dynamics_types/translational
    propagation_setup/dynamics_types/rotational
    propagation_setup/dynamics_types/mass
    propagation_setup/dynamics_types/multi_type
    propagation_setup/dynamics_types/multi_body
    propagation_setup/conventional_vs_propagated_coordinates
    propagation_setup/termination_settings
    propagation_setup/dependent_variables
    propagation_setup/acceleration_models/available

Introduction
============


In Tudat, it is possible to perform the numerical propagation of different types of dynamics, namely:

- :ref:`translational_dynamics`: the translational state of a body is propagated;
- :ref:`rotational_dynamics`: the rotational state of a body is propagated;
- :ref:`mass_dynamics`: the mass of a body is propagated.

Furthermore, any combination of any number of types of dynamics, for any number of bodies, can be defined. When more
than one dynamical quantity is propagated, we refer to a :ref:`multi_type_dynamics` simulation. Conversely, when more
than one body is numerically propagated, we refer to a :ref:`multi_body_dynamics` simulation.

.. note::

   Regardless of the type of dynamics, the propagated state can be formulated through a number of different
   state representations. For the case of translational
   dynamics, for instance, there are various options besides a simple Cartesian state representation. However, even
   when using a non-Cartesian state vector, the Cartesian representation still plays a role in calculating, *e.g.*,
   acceleration models. For more information on the role of different state representations, please visit
   the page :ref:`convention_propagated_coordinates`.


Inputs
======

As the figure shows, there are some input arguments common to all types of dynamics, while some others are
dynamics-specific.

Common inputs
*************************

These are input arguments that are common to all types of dynamics and should always be defined. These are:

- the names of the bodies to be propagated numerically;
- when the propagation should stop (see :ref:`termination_settings`);
- what dependent variables should be saved (see :ref:`dependent_variables`);
- how often the current state and time should be printed to the console.


Dynamics-specific inputs
*************************

These are input arguments that are specific to a type of dynamics. These are described in more detail in the page
related to a specific type of dynamics, but they are summarized below:

- *Dynamical model*, defining the equations of motion of the propagated bodies;
- *Initial conditions*, defining the initial states of the propagated bodies;

In addition, only for rotational and translational dynamics:

- *Propagator type*, defining the representation of the states

Finally, only for the translational dynamics:

- *Central bodies*, defining a central body for each propagated body (only for translational dynamics)
