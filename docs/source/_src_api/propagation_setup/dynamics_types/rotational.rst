.. _rotational_dynamics:

===================
Rotational Dynamics
===================

Settings to define the propagation of rotational dynamics are largely similar to those of translational dynamics. Differences are:

* A set of torque models has to be supplied, as opposed to acceleration models. See :ref:`available_torque_models` for the list of options for torques in Tudat.
* No 'central body' is specified. The rotational state that is propagated is always that from the global inertial orientation, to the body-fixed orientation of the propagated body.
* The propagated state formulation is, by default, a vector of size 7 (for a single body), with:

   * Entries 1-4: The quaternion defining the rotation from inertial to body-fixed frame;
   * Entries 5-7: The body's angular velocity vector, expressed in its body-fixed frame.
Quaternions are used in lieu of e.g. Euler angles because they get rid of ambiguities and gimbal locks.
* Alternative formulations for the propagated state vector can be selected from the list at the end of this page.

Defining settings for the rotational dynamics is done by:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_rotational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp


where the final three inputs are all optional, and the ``simulation_end_epoch`` input may be replaced by the more general ``termination_settings`` (see :ref:`available_termination_settings`), as was the case for translational dynamics

.. class:: Rotational Motion Propagators

  - Quaternions (with ``quaternions`` propagator); state size: 7
  - Modified Rodrigues parameters, or MRPs (with ``modified_rodrigues_parameters`` propagator); state size: 7
  - Exponential map (with ``exponential_map`` propagator); state size: 7
