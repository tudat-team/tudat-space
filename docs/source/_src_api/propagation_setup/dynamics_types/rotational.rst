===================
Rotational Dynamics
===================

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