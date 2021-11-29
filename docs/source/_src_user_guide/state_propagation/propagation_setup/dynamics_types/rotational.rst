.. _rotational_dynamics:

===================
Rotational Dynamics
===================

Settings to define the propagation of rotational dynamics are largely similar to those of :ref:`translational_dynamics`. Differences are:

* A set of torque models has to be supplied, as opposed to acceleration models. See :ref:`available_torque_models` for the list of options for torques in Tudat.
* No 'central body' is specified. The rotational state that is propagated is always that from the global inertial orientation, to the body-fixed orientation of the propagated body.
* The propagated state formulation is depends on the choice of propagator for rotational dynamics, with the full list of options and their definition enumerated by :class:`~tudatpy.numerical_simulation.propagation_setup.propagator.RotationalPropagatorType`. The default rotational propagator is the  ``quaternions`` option in this enumeration.

Defining settings for the rotational dynamics is done as follows, using the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` function:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_rotational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

