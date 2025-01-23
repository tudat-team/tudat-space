.. _propagation_setup:

=================
Propagation Setup
=================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   propagation_setup/translational
   propagation_setup/rotational
   propagation_setup/mass
   propagation_setup/multi_type
   propagation_setup/multi_body
   propagation_setup/multi_hybrid_arc
   propagation_setup/processed_propagated_elements
   propagation_setup/integration_setup
   propagation_setup/termination_settings
   propagation_setup/dependent_variables
   propagation_setup/printing_processing_results
   

In this part of the user guide, we will explain the relevant inputs as well as present the different
categories of numerical propagation.

.. explain how to define settings for a numerical propagation of
.. different types of dynamics, with a wide variety of available settings. The propagator settings allow you to define:
..
.. - The exact state derivative model (e.g. the equations of motion that are to be solved), including initial and final conditions
.. - The numerical integrator that is to be used to solve these equations of motion
.. - The list of output variables that are to be provided after thee propagation is finished
.. - The output that is to be printed to the console during the propagation
.. - ...

.. _propagation_inputs:

Inputs and setup
================

Using Tudat, you can propagate different kinds of equations of motion, including those for translation and/or rotational dynamics.
These equations can be propagated for one or more bodies, and over a single arc or multiple arcs.
The figure below gives an overview of the inputs that are required to define so-called propagator settings in Tudat

.. figure:: propagation_setup/_static/tudatpy_propagation_settings.png

On the left is a list of arguments (some optional) that can be provided
to the propagator settings, regardless of their type:

- **List of propagated bodies**: the names of the bodies for which the dynamics is to be propagated.
- **Dependent variables**: which quantities to save as output, in addition to the states, described :ref:`here <dependent_variables>`. These settings are optional (none by default).
- **Numerical integrator**: the solver used to create an approximate solution, described :ref:`here <integrator_setup>`. This setting is mandatory
- **Termination conditions**: when to terminate the propagation, described :ref:`here <termination_settings>`. This setting is mandatory
- **Processing/output settings**: what to print to the terminal before, during and after propagation, and what to do with the numerical results after propagation, both described :ref:`here <auto_processing>`. This setting is optional (no terminal output or resetting of environment by default)

.. _dynamics_types_intro:

Dynamics types
==============

There are a number different types of dynamics that Tudat can numerically propagate, settings for which are created by calling the associated functions in the `propagator module <https://py.api.tudat.space/en/latest/propagator.html#functions>`_. Below, we provide links for pages discussing each type in more detail

- :ref:`translational_dynamics`: the translational state of a body is propagated;
- :ref:`rotational_dynamics`: the rotational state of a body is propagated;
- :ref:`mass_dynamics`: the mass of a body is propagated.
- Custom Dynamics: an arbitrary user-defined state derivative model, see :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.custom_state` (typically in the context of a multi-type propagation).

Furthermore, any combination of any number of types of dynamics for any number of bodies can be defined. Therefore,
in Tudat we also have:

- :ref:`multi_type_dynamics`: more than one dynamical quantity is propagated for a single body;
- :ref:`multi_body_dynamics`: only one dynamical quantity is propagated for multiple bodies;
- A combination of the two: more than one dynamical quantity is propagated for multiple bodies.

The above list defines different types of dynamics that are propagated over a single continuous arc.
Propagation using a :ref:`multi-arc setup <multi_arc_dynamics>` is also supported in Tudat.

.. note::

   For a given type of dynamics, the propagated state can be formulated through a number of different
   state representations. For the case of translational
   dynamics, for instance, there are various options besides a simple Cartesian state representation. However, even
   when using a non-Cartesian state vector, the Cartesian representation still plays a role in calculating, *e.g.*,
   acceleration models, as well as in defining the initial state. For more information on the role of different state
   representations, please visit the page :ref:`processed_propagated_states`.






