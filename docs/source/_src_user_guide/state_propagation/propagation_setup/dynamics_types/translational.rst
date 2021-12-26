.. _translational_dynamics:

======================
Translational Dynamics
======================

Settings to propagate numerically the translational state of a body can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` factory function, described in
detail in the API reference, which creates an object of type
:class:`~tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalStatePropagatorSettings` (see below
an :ref:`example`).

In this page, only the Tudat-native objects necessary as input will be described. For all the other inputs, please
refer to the related API entry (:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational`).

Inputs
=======

The Tudatpy-native inputs to create the settings for a translational propagator are the following:

- a set of acceleration models (see :ref:`acceleration_models_setup`);
- a type of propagator, since the translational state can have different representations (see
  :ref:`propagator_types`);
- settings to terminate the propagation (see :ref:`termination_settings`);
- dependent variables that should be saved (see :ref:`dependent_variables`).

.. _example:

Example
========

In the example below, the body "Spacecraft" will be propagated w.r.t. body "Earth", using given acceleration models (not
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

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup
                    from tudatpy.kernel.astro import element_conversion
                    import numpy as np

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp



