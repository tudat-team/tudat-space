.. _translational_dynamics:

======================
Translational Dynamics
======================

Settings to propagate numerically the translational state of a body can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` factory function, described in
detail in the API reference, which creates an object of type
:class:`~tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalStatePropagatorSettings` (see below
an :ref:`example`).

Acceleration Model Setup
========================

To propagate translational dynamics, a set of acceleration models must be provided. This can be created via the
:func:`~tudatpy.numerical_simulation.propagation_setup.create_acceleration_models` factory function, described in the
API reference and in the page :ref:`acceleration_models_setup`.


Propagators
============

As explained in :ref:`convention_propagated_coordinates`, the translational state can have different representations.
The available propagators are listed in `the API reference <https://tudatpy.readthedocs.io/en/latest/propagator.html#tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalPropagatorType>`_.

.. _example:

Example
========

In the example below, the body "Vehicle" will be propagated w.r.t. body "Earth", using given acceleration models (not
provided), a given initial state which defines the initial Cartesian state of the center
of mass of "Vehicle" w.r.t. the center of mass of "Earth". The propagation will terminate once the
``simulation_end_epoch`` epoch is reached. Furthermore, this example defines a termination condition using a dependent
variable: the simulation will stop when the propagated vehicle reaches an altitude of 25.0 km. Next to that, the
propagator is asked to save the total acceleration, Keplerian state, latitude, and longitude of the spacecraft as
dependent variables. The time and state will be printed on the terminal once every 24 hours (simulation time), while
the state will be propagated through the Encke formulation.

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp



