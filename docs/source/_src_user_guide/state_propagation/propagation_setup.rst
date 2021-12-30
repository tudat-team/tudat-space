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
   propagation_setup/state_coordinate_types
   propagation_setup/termination_settings
   propagation_setup/dependent_variables
   propagation_setup/acceleration_models/setup
   propagation_setup/torque_models/setup
   propagation_setup/acceleration_models/available
   propagation_setup/torque_models/available

Introduction
============

In Tudat, it is possible to perform the numerical propagation of different types of dynamics, namely:

- :ref:`translational_dynamics`: the translational state of a body is propagated;
- :ref:`rotational_dynamics`: the rotational state of a body is propagated;
- :ref:`mass_dynamics`: the mass of a body is propagated.

Furthermore, any combination of any number of types of dynamics for any number of bodies can be defined. Therefore,
in Tudat we also have:

- :ref:`multi_type_dynamics`: more than one dynamical quantity is propagated for a single body;
- :ref:`multi_body_dynamics`: only one dynamical quantity is propagated for multiple bodies;
- a combination of the two: more than one dynamical quantity is propagated for multiple bodies.

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
specific to the type of propagator. More information about inputs are explained in the dynamic-specific pages linked
above.

.. figure:: propagation_setup/_static/tudatpy_propagation_settings.png
