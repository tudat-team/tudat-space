.. _thrust_models:


====================
Use of thrust models
====================

This page deals with the inclusion of a thrust force into the dynamical model. Note that, when using thrust models, it
may often be desirable to propagate the mass of the vehicle at the same time (removing mass of the burnt propellant,
for instance). Details on how to propagate the mass of a body are given in :ref:`mass_dynamics`. Details on combining translation and mass propagators is given in :ref:`multi_type_dynamics`.

.. _thrust_acceleration_setup:

Thrust dynamics
===============

In Tudat, the acceleration that a body undergoes due to the addition of thrust can be setup is set up by combining two different pieces of information from the environment:

*  One or several ``EngineModel`` objects assigned to the vehicle that is using thrust. For the thrust acceleration, this is used to compute/define:

   *  The body-fixed thrust direction :math:`\hat{\mathbf{T}}_{B}` (which direction is the nozzle pointed, in a frame fixed to the spacecraft
   *  What is the thrust magnitude exerted by the engine (typically as a force in N, but can be defined as acceleration in m/s\ :sup:`2`\, see below)
   *  (When using the mass rate due to thrust: the specific impulse of the engine)

*  A rotation model for the vehicle, which is used to provide the inertial thrust direction  :math:`\hat{\mathbf{T}}`. Here, we can distinguish three different approaches in the context of thrust:
  
   *  The vehicle has a rotation model defined using the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_inertial_direction_based` settings. By using this model, the inertial direction of the thrust can be provided by the user *directly*. The orientation of the vehicle is then derived from this direction
   *  The vehicle has any other rotation model defined, in this case the inertial thrust direction is computed from :math:`\hat{\mathbf{T}}=\mathbf{R}^{(I/B)}\hat{\mathbf{T}}_{B}`
   *  The rotational dynamics of the vehicle is propagated, and the orientation of the vehicle is taken from the current rotational state. The inertial thrust direction then follows from :math:`\hat{\mathbf{T}}=\mathbf{R}^{(I/B)}\hat{\mathbf{T}}_{B}`.

Three functions are provided to define a thrust acceleration:

*  :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_engine`.
*  :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_engines`
*  :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_all_engines`

which differ only in the manner that the engine models are selected. For a thrust acceleration comprised of :math:`N` engines, the total thrust acceleration is calculated from:

.. math::

 \mathbf{a}_{T}=\mathbf{R}^{(I/B)}\sum_{i=1}^{N}\hat{\mathbf{T}}_{B,i}a_{T,i}

where :math:`\mathbf{T}_{B,i}` is the body-fixed thrust direction of body :math:`i`, and :math:`a_{T,i}` is the thrust acceleration norm exerted by engine :math:`i`. In the (typical) case that the engine thrust force :math:`F_{T,i}` is defined directly (instead of the acceleration, see :ref:`below <thrust_acceleration_magnitude>`), we have :math:`a_{T,i}=F_{T,i}/m`, with :math:`m` the mass of the body.
Once one (or more) engine models, and a rotation model, for the vehicle are defined, the thrust acceleration can simply be added to the acceleration settings as any other acceleration model.


.. code-block:: python

   acceleration_on_vehicle = dict( 
      ...,
      Vehicle=[  propagation_setup.acceleration.thrust_from_engine( 'MainEngine') ],
   )

Where the thrust acceleration due to the single engine model named 'MainEngine' will be used

Thrust torque
~~~~~~~~~~~~~

When using thrust in conjunction with the propagation of rotational dynamics of a body, the current body's orientation used to compute the thrust force is extracted from the current state (as described above). The torque exerted about the vehicle's center of mass due to the thrust force may also be taken into account. This requires the definition of the location of the engine model on the vehicle (w.r.t. its center of mass)

TODO: implement this in Tudat. 


Thrust guidance
===============

A typical thrust acceleration application will include some sort of guidance for the thrust. The inertial *direction* of the thrust acceleration is defined by the rotation model of the body under consideration (see :ref:`thrust_acceleration_setup`). Below, we provide more details on how to define the thrust magnitude and body-fixed thrust direction, as well as some considerations on typical manners in which to define the body's rotation (e.g. inertial thrust direction).

.. _thrust_acceleration_magnitude:

Thrust magnitude
~~~~~~~~~~~~~~~~

The engine model(s) used for the vehicle is each assigned an object that computes the magnitude of thrust as a function of time. These objects are created using settings from the factory functions discussed below, each of which returns a :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` object.

Typically, thrust magnitude setting types define a thrust *force* :math:`\mathbf{T}`, and the thrust acceleration :math:`\mathbf{a}_{T}` is computed from this by :math:`\mathbf{a}_{T}=\mathbf{T}/m`. It is also possible to define a thrust magnitude law by directly imposing the thrust acceleration :math:`\mathbf{a}_{T}`. This allows more direct control of the resulting trajectory, as it does not depend on the vehicle's current mass. However, it is slightly less realistic, as it assumes a perfectly knowledge of the current vehicle's mass when commanding the engine.

**Constant thrust magnitude**

Thrust magnitude settings may be used to specified a constant thrust (in Newtons) and a constant specific impulse (in seconds).

An example of how to use this constant thrust magnitude setting is shown on the Tudat(Py) API docs page of the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.constant_thrust_magnitude` function.


**Custom thrust magnitude**

Thrust magnitude settings can also be created trough a custom function that returns the magnitude in Newton as a function of time. More details, and an example on how to use these thrust magnitude settings, are given on the API docs page :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude`. Even though the interface for the thrust magnitude permits only a function as input, the user may let the thrust magnitude depend on any and all other properties of the environment. See :ref:`custom_models` for more information of how to define custom models in Tudat, and how to achieve such dependencies. If a custom thrust *magnitude*, but a constant *specific impulse* are to be used, the function :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude_fixed_isp` can be used (using this last interface allows derivatives of thrust properties w.r.t. the constant specific impulse :math:`I_{sp}` to be calculated when propagating the associated variational equations).


**Custom thrust acceleration magnitude**

Similarly to the previous method, a custom model may be provided that returns the thrust *acceleration* in m/s:sup:`2` directly, as a function of time. This can be defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_acceleration_magnitude` or :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_acceleration_magnitude_fixed_isp` functions.

Thrust Vectoring Control
~~~~~~~~~~~~~~~~~~~~~~~~
In some cases, it may be desirable to have the body-fixed thrust direction :math:`\hat{\mathbf{T}}_{B}` be time-varying. A typical application of this is for implementing thrust vector control (TVC). Alternatively, such a model may be incorporated in, for instance, a sensitivity analysis to gauge the impact of variations in :math:`\hat{\mathbf{T}}_{B}`.

In Tudat, the body-fixed thrust direction for the vehicle is defined in the ``EngineModel`` class. We showed an example :ref:`above <thrust_acceleration_setup>` on how to create an engine model using the :func:`~tudatpy.numerical_simulation.environment_setup.add_engine_model`, which takes a *fixed* body-fixed thrust direction. To define a time-variable body-fixed thrust direction, you can use the similar :func:`~tudatpy.numerical_simulation.environment_setup.add_variable_direction_engine_model` function. This model takes a custom function as input to define the thrust direction. See :ref:`custom_models` for more details on how to define such inputs. In particular, when applying TVC, it is likely that the guidance algorithm used to define the current body-fixed thrust direction is linked to the algorithm for thrust magnitude, body orientation, etc. For such a case, see the section on :ref:`couple_custom_models` in particular.

.. _thrust_and_aerodynamics:

Thrust and aerodynamics
~~~~~~~~~~~~~~~~~~~~~~~

This section elaborates on the use of thrust orientation in case aerodynamics are also taken into account in the simulation model. Even though, in principle, the thrust model is not affected by the presence of an aerodynamic acceleration, there are a number of considerations that may be useful to take into account when setting up such a simulation. In particular, this relates to the manner in which the body's orientation is typically defined in such cases, and how the body's orientation influences the accelerations.  For aerodynamics, the body's orientation is typically defined w.r.t. the trajectory frame (which is itself defined by the body's relative translational state w.r.t. a central body) by the angle of attack :math:`\alpha`, the sideslip angle :math:`\beta` and the bank angle :math:`\sigma` (see TODO). The thrust and aerodynamic accelerations are influenced by the body's orientation as follows:

* For thrust, the body's orientation influences the inertial acceleration, as it influences the direction in which the engine is pointed (see :ref:`thrust_acceleration_setup`)
* For aerodynamics, the body's orientation influences the inertial acceleration, as the aerodynamic force is typically computed in either aerodynamic frame, or body-fixed frame. In these cases the either :math:`\sigma`, or :math:`\alpha`, :math:`\beta` and :math:`\sigma`, respectively. In addition, in many cases the aerodynamic coefficients *themselves* are a function of the :math:`\alpha` (and :math:`\beta`).

A typical body rotation model for problems such as aerodynamics is the model defined using the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based` (or, related, the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.zero_pitch_moment_aerodynamic_angle_based`) model. If these models are used in conjunction with thrust, the rotation matrix :math:`\mathbf{R}^{(I/B)}` defined by this model defines the inertial thrust direction.

A typical body rotation model for problems involving thrust is the model defined by :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_inertial_direction_based`. When using such a model, the body-fixed axis along which the thrust force acts is automatically aligned with a user-specified (time-dependent) inertial direction. However, this does *not* fully specify the rotation matrix :math:`\mathbf{R}^{(I/B)}`, as it leaves the rotation about the thrust vector :math:`\hat{\mathbf{T}}` (to which the thrust force itself is insensitive) undefined. The :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_inertial_direction_based` function has an optional input to define a ``free_rotation_angle_function`` to define this free angle (by definition this angle is 0; see API entry documentation for details on how this angle is defined). This free rotation angle can be used to exert partial control over the aerodynamic force. When this rotation model (or any rotation model not based on aerodynamic angles) is used, the :math:`\mathbf{R}^{(I/B)}` matrix (and latitude, longitude, flight path and heading angles) are used to computed the angles :math:`\alpha`, :math:`\beta` and :math:`\sigma`. By specifying the rotation angle about :math:`\hat{\mathbf{T}}`, the matrix :math:`\mathbf{R}^{(I/B)}` is modified, leading to a change in :math:`\alpha`, :math:`\beta` and :math:`\sigma`.

Mass rate from thrust
=====================

If thrust is added to the model, the vehicle will physically lose mass (its propellant) over time.

A mass rate setting is available in Tudat(Py) to make the loss of mass of the vehicle consistent with the magnitude of the thrust and its specific impulse over time, by propagating the mass of the body as a state entry. This is available trough the :func:`~tudatpy.numerical_simulation.propagation_setup.mass_rate.from_thrust` function, which has to be setup after the acceleration models are defined, as follows:

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. literalinclude:: /_snippets/simulation/propagation_setup/thrust/thrust_mass_rate.py
         :language: python

   .. tab-item:: C++

      .. literalinclude:: /_snippets/simulation/propagation_setup/thrust/thrust_mass_rate.cpp
         :language: cpp

More details and options on mass propagation are provided on the :ref:`mass_dynamics` page.

.. note::
   The specific impulse is in principle only used for mass rate settings.
   If the mass is not to be propagated, or if custom mass rate settings are used, the specific impulse input of the `thrust magnitude <#thrust-magnitude>`_ settings
   can in most cases be set to any value without impacting the results.



