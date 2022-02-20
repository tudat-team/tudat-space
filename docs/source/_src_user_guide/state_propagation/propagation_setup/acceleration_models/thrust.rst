.. _thrust_models:


========================
Use of thrust models
========================

This page deals with the inclusion of a thrust force into the dynamical model. Note that, when using thrust models, it
may often be desirable to propagate the mass of the vehicle at the same time (removing mass of the burnt propellant,
for instance).
Details on how to propagate the mass of a body are given in :ref:`mass_dynamics`. Details on combining translation and mass propagators is given in :ref:`multi_type_dynamics`.

Thrust acceleration methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Tudat, the acceleration that a body undergoes due to the addition of thrust can be setup in three different ways:

   - :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_custom_function`: this method lets you specify a custom variable thrust vector as a function, a constant specific impulse, and the frame in which the thrust is defined (default: inertial orientation).
   - :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_and_isp_from_custom_function`: this method adds the capability of specifying a custom variable specific impulse as a function.
   - :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_direction_and_magnitude`: this
     method takes :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustDirectionSettings` and
     :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` as inputs. These thrust
     objects are presented below separately for thrust `direction <#thrust-direction>`_ and
     `magnitude <#thrust-magnitude>`_. The settings are created using factory functions, in the same was as
     acceleration settings, environment settings, etc.
   

A typical representative example on how the thrust acceleration can be set up, using the available :func:`~tudatpy
.numerical_simulation.propagation_setup.acceleration.thrust_from_direction_and_magnitude` function, is provided below:

   .. tabs::

      .. tab:: Python

         The Tudat(Py) API docs give more details on the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustDirectionSettings` and :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` classes.

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_accelerations_basic_syntax.py
            :language: python

      .. tab:: C++

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_accelerations_basic_syntax.cpp
            :language: cp

In the above code snippet, note that we define the thrust acceleration as one that the vehicle exerts on itself.

Thrust direction
~~~~~~~~~~~~~~~~

Below, the different methods that have been implemented to define the direction of the thrust are outlined.
All of these methods return a :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustDirectionSettings` object.

Note that these settings are *only* relevant if you use the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_direction_and_magnitude` function.

.. note::
   In all of these methods, the thrust direction that is defined is always in the **inertial frame**, either directly
   or indirectly. It is important to realize that, when specifying a thrust direction, the vehicle orientation itself
   is automatically defined.
   The direction of the thrust in the body-fixed frame can be additionally defined when specifying the `thrust
   magnitude <#thrust-magnitude>`_ (note that this design is currently under review, and may well be refactored in the
   near future).

.. note::
   In Tudat(Py), a distinction is made between the thrust **orientation** and the thrust **direction**.
   The thrust direction refers to a unit vector that defines along which direction the thrust acceleration acts, defined in the inertial frame.
   The thrust orientation refers to a rotation matrix between the body-fixed frame to the inertial frame.


**Thrust direction from state guidance settings**

In various simplified cases, the thrust direction can be assumed to be in line with either the position or velocity vector of the body undergoing thrust w.r.t. some (central) body.

This thrust direction setting is shown on the Tudat(Py) API docs page of the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.thrust_direction_from_state_guidance` function.

..
   This thrust direction setting can be created in Tudat as follows:

      .. tabs::

         .. tab:: Python

            The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.thrust_direction_from_state_guidance` function.

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_direction_from_state_guidance.py
               :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_direction_from_state_guidance.cpp
               :language: cp

**Custom thrust direction settings**

For a generalized thrust direction guidance, the thrust direction can be defined as an arbitrary function of time. This allows a broad range of options to be defined, at the expense of increased complexity — somehow this thrust direction needs to be manually defined.

A custom thrust direction can be defined **in the inertial frame** as on the Tudat(Py) API docs page of the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_direction` function.

..
   A custom thrust direction can be defined **in the inertial frame** using the following:

      .. tabs::

         .. tab:: Python

            The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_direction` function.

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_direction.py
               :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_direction.cpp
               :language: cp

.. warning:: When using this option, the inertial to body-fixed rotation cannot be unambiguously defined. If you require this rotation (for instance when you also incorporate aerodynamic forces), the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_orientation` option should be used instead.

.. warning:: The direction vector that is being returned by the custom function should be a unit vector.

**Custom thrust orientation settings**

Thrust orientation settings can also be created trough a custom function that returns this time not the direction but the orientation of the thrust.

This thrust orientation needs to be provided through a rotation matrix representing the rotation from body-fixed thrust direction to the inertial thrust direction.

The use of this orientation setting is shown on the Tudat(Py) API docs page of the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_orientation` function.

..
   .. tabs::

      .. tab:: Python

         The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_orientation` function.

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_orientation.py
            :language: python

      .. tab:: C++

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_orientation.cpp
            :language: cp

**Thrust direction from existing orientation**

The orientation of the vehicle is in some cases already defined. This could be because of the aerodynamic guidance or
the propagation of rotational dynamics. In this context, the thrust direction can be computed from the body-fixed orientation.

In such a case, the thrust direction is computed from the existing vehicle orientation.
Do note that an additional angle from the vehicle can be defined, for instance in case Thrust Vectoring Control is used.
This angle, the body fixed thrust direction, can be defined in the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` class.

How to use this thrust orientation setting is shown on the Tudat(Py) API docs page of the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.thrust_from_existing_body_orientation` function.

..
   This thrust direction does not require a specific derived class, but instead only requires the use of the following function:

      .. tabs::

         .. tab:: Python

            The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.thrust_from_existing_body_orientation` function.

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/from_existing_orientation.py
               :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/from_existing_orientation.cpp
               :language: cp

Thrust magnitude
~~~~~~~~~~~~~~~~

Below, the different methods that have been implemented to define the magnitude of the thrust are outlined.
All of these methods return a :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` object.

Note that these settings are *only* relevant if you use the :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_direction_and_magnitude` function.

**Constant thrust magnitude**

Thrust magnitude settings may be used to specified a constant thrust (in Newtons) and a constant specific impulse (in seconds).
Optionally, a constant direction of the thrust with respect to the body can also be specified. When a time-varying body-fixed thrust is required, for instance to define Thrust Vectoring Control, the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude` option should be used.

An example of how to use this constant thrust magnitude setting is shown on the Tudat(Py) API docs page of the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.constant_thrust_magnitude` function.

..
   This constant thrust magnitude can be setup using the following:
      .. tabs::

         .. tab:: Python

            The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.constant_thrust_magnitude` function.

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/constant_magnitude.py
               :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/constant_magnitude.cpp
               :language: cp

**Custom thrust magnitude**

Thrust magnitude settings can also be created trough a custom function that returns the magnitude in Newton as a function of time.

These settings can additionally be used to first specify whether the engine is on or off.
This can save precious CPU time by avoiding to waste CPU time computing the thrust magnitude, by first checking
whether the engine is indeed turned on.
A so-called thrust reset function can also be specified, so that Tudat(Py) calls it first, before calling any of the other thrust magnitude-related functions.
This thrust reset function can for instance be used to update all relevant aspects of the environment.

How to use this custom thrust magnitude setting is shown on the Tudat(Py) API docs page of the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude` function.

..
   Custom thrust magnitude settings can be defined in Tudat(Py) as follows:

      .. tabs::

         .. tab:: Python

            The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude` function.

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_magnitude.py
               :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_magnitude.cpp
               :language: cp

.. note:: When :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.FromFunctionThrustMagnitudeSettings` are used, it is recommended to setup a custom :literal:`thrust` class, encompassing all of the following functions:
         :literal:`thrust_magnitude_function()`, :literal:`specific_impulse_function()`, and :literal:`is_engine_on_function()`. Potentially, one may also wish to include the following functions in this class:
         :literal:`body_fixed_thrust_direction()`, :literal:`custom_thrust_reset_function()`, and/or :literal:`thrust_direction_function()`.
         The idea being that using one global user-defined :literal:`thrust` class gives more control on all of the aspects that have to be updated to define whether thrust is turned on, what is its magnitude, and orientation.

Thrust with the environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section deals with selected cases in which the thrust model is integrated with the simulated environment.

Mass rate settings
==================

If thrust is added to the model, the vehicle is most likely going to loose mass (its propellant) over time.

A mass rate setting is available in Tudat(Py) to make the loss of mass of the vehicle consistent with the magnitude of the thrust and its specific impulse over time.
This is available trough the :func:`~tudatpy.numerical_simulation.propagation_setup.mass_rate.from_thrust` function, which has to be setup after the acceleration models are defined, as follows:

   .. tabs::

      .. tab:: Python

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_mass_rate.py
            :language: python

      .. tab:: C++

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_mass_rate.cpp
            :language: cp

More details and options on mass propagation are provided on the :ref:`mass_dynamics` page.

.. note::
   The specific impulse is in principle only used for mass rate settings.
   If the mass is not to be propagated, or if custom mass rate settings are used, the specific impulse input of the `thrust magnitude <#thrust-magnitude>`_ settings
   can in most cases be set to any value without impacting the results.

Thrust and rotational dynamics
==============================
.. todo::
   A more detailed explanation on how to integrate and use thrust direction from rotational dynamics is to be added here later. As discussed above, the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.thrust_from_existing_body_orientation` can be used to automatically use the current body orientation to calculate the thrust. Details on how to incorporate the thrust torque are to be added later.
   

Thrust Vectoring Control
~~~~~~~~~~~~~~~~~~~~~~~~
In some cases, the thrust may not be aligned with the orientation of the vehicle that has been defined.

For instance, if Thrust Vectoring Control (TVC) is to be used, with a nozzle deflection that varies over time, the true
thrust direction will vary from the x-axis of the vehicle.

In Tudat(Py), this deviation in thrust direction from the vehicle can be defined in the body-fixed frame through the
thrust magnitude definition.
When using the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.constant_thrust_magnitude`, a constant body-fixed thrust direction can be defined where,
when using the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude`, this
body-fixed thrust direction can be defined as a function of time, allowing TVC to be incorporated.

This can be done as follows:

   .. tabs::

      .. tab:: Python

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_orientation_body_fixed.py
            :language: python

      .. tab:: C++

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_orientation_body_fixed.cpp
            :language: cp

Thrust and aerodynamic guidance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section elaborates on the definition of the thrust orientation in case aerodynamics are also taken into account in the simulation model.

For instance, let's assume that an aerodynamic coefficient interface is set up, in which the aerodynamic coefficients
depend on the vehicle's orientation (angle of attack/sideslip), and that an aerodynamic acceleration is used in the
propagation. The orientation of the vehicle must then somehow be specified.
In this section, we will discuss the option of defining the orientation of the vehicle for thrust and aerodynamic either separately, or linked to one another. 

Separate orientations
=====================

.. todo::
   An explanation on how to define thrust orientation separately from aerodynamic guidance is to be added here later.

..
   The orientation of the thrust of the vehicle, and its aerodynamics, can be separately defined.

   For instance, let's say that we define our thrust orientation as being colinear with velocity, using the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.thrust_direction_from_state_guidance` function.
   Then, the orientation of the vehicle itself is still undefined for our aerodynamic acceleration computation.
   This can be fixed by adding, for instance, aerodynamic guidance, using the :class:`~tudatpy.numerical_simulation.propagation.AerodynamicGuidance` class.

   This leads to the overall simulation setup of the following code snippet, using an aerodynamic guidance class that varies the angle of attack between -1.5deg and 1.5deg:

      .. tabs::

         .. tab:: Python

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_vs_aero_orientation.py
               :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_vs_aero_orientation.cpp
               :language: cp

   The above example then shows how to have full but separate control over the vehicle orientation used to compute the thrust and the  aerodynamic acceleration.

Thrust direction from aerodynamics
==================================
.. todo::
   An explanation on how to use thrust direction from existing orientation defined by aerodynamic guidance is to be added here later.
