.. _thrust_models:


========================
Thrust Guide
========================
This page deals with the inclusion of a thrust force into the dynamical model. Note that when using thrust, it may often be desirable to propagate the mass of the vehicle at the same time (removing burnt propellant for instance).
Details on how to propagate the mass of a body are given in :ref:`mass_dynamics`. Details on combining translation and mass propagators is given in :ref:`multi_type_dynamics`.

In Tudat, a thrust model is defined by two separate types of settings (which may or may not be linked):

    - The direction of the thrust.
    - The magnitude of the thrust.

In fact, when creating acceleration settings from a thrust force, the user needs to provide settings for these two aspects of the force model:

    .. tabs::

         .. tab:: Python

          The two classes used are described in the Tudat(Py) API docs at the following pages: `ThrustDirectionSettings <https://tudatpy.readthedocs.io/en/latest/thrust.html#tudatpy.numerical_simulation.propagation_setup.thrust.ThrustDirectionSettings>`_ and `ThrustMagnitudeSettings <https://tudatpy.readthedocs.io/en/latest/thrust.html#tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings>`_.

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_accelerations_basic_syntax.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_accelerations_basic_syntax.cpp
             :language: cp

In the above code snippet, two things may stand out.
First of all, we define the thrust acceleration as one that the vehicle exerts on itself.
Secondly, to define the thrust acceleration, the user must provide two objects: one of type (derived from) :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustDirectionSettings` and one of type (derived from) :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings`.
The two settings (direction and magnitude) are used to create a :class:`~tudatpy.numerical_simulation.propagation_setup.acceleration.ThrustAccelerationSettings` object. 

Thrust direction
~~~~~~~~~~~~~~~~

Four distinct methods have been implemented to define the direction of the thrust.

In all of these methods, the thrust direction that is defined is always in the **inertial frame**.
The direction of the thrust in the body-fixed frame can be additionally defined in the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` class.

The base class for the thrust direction settings in TudatPy is the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustDirectionSettings` class.

Thrust direction from state guidance settings
=============================================

    In various simplified cases, the thrust direction can be assumed to be in line with either the position or velocity w.r.t. some body.

    This thrust direction setting can be created in Tudat as follows:

    .. tabs::

         .. tab:: Python

          The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.thrust_direction_from_state_guidance` function.

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_direction_from_state_guidance.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_direction_from_state_guidance.cpp
             :language: cp

Custom thrust direction settings
================================

   For a generalized thrust direction guidance, the thrust direction can be defined as an arbitrary function of time. This allows a broad range of options to be defined, at the expense of increased complexity — somehow this thrust direction needs to be manually defined.

   A custom thrust direction can be defined **in the inertial frame** using the following:

    .. tabs::

         .. tab:: Python

          The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_direction` function.

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_direction.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_direction.cpp
             :language: cp

   .. warning:: When using the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.CustomThrustDirectionSettings`, the inertial to body-fixed rotation cannot be unambiguously defined. If you require this rotation (for instance when you also incorporate aerodynamic forces), the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.CustomThrustOrientationSettings` class should be used instead.

   .. warning:: The direction vector that is being returned by the custom function should be a unit vector.

Custom thrust orientation settings
==================================

   Thrust orientation settings can also be created trough a custom function that returns this time not the direction but the orientation of the thrust.

   This thrust orientation needs to be provided through a rotation matrix representing the rotation from body-fixed thrust direction to the inertial thrust direction.

    .. tabs::

         .. tab:: Python

          The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_orientation` function.

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_orientation.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/custom_thrust_orientation.cpp
             :language: cp

Thrust direction from existing orientation
==========================================

    The orientation of the vehicle is in some cases already defined. This could be thanks to aerodynamic guidance or to the propagation of rotational dynamics.

    In this context, the thrust direction can be computed from the body-fixed direction. 

    In such a case, the thrust direction is computed from the existing vehicle orientation.
    Do note that an additional angle from the vehicle can be defined, for instance in case Thrust Vectoring Control is used.
    This angle, the body fixed thrust direction, can be defined in the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` class.
    
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

Two distinct ways are available in Tudat(Py) to implement the magnitude of the thrust. It can either be fixed to a constant force, or be specified as a function of time.

The base class for the thrust magnitude settings in TudatPy is the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings` class.

Constant thrust magnitude settings
==================================

    Thrust magnitude settings may be used to specified a constant thrust (in Newtons) and a constant specific impulse (in seconds).
    Optionally, the direction of the thrust with respect to the body can also be specified, for instance to define Thrust Vectoring Control.

    This constant thrust magnitude can be setup using the following:
   
    .. tabs::

         .. tab:: Python

          The Tudat(Py) API docs give more details on the :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.constant_thrust_magnitude` function.

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/constant_magnitude.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/constant_magnitude.cpp
             :language: cp

From function thrust magnitude settings
=======================================

    Thrust magnitude settings can also be created trough a custom function that returns it in Newton as a function of time.

    These settings can additionally be used to first specify whether the engine is on or off.
    This can save precious CPU time by avoiding to waste CPU time computing the thrust magnitude, by first checking wether the engine is indeed turned on.
    A so-called thrust reset function can also be specified, so that Tudat(Py) calls it first, before calling any of the other thrust magnitude-related functions.
    This thrust reset function can for instance be used to update all relevant aspects of the environment.

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
**To do**
 - Mass rate settings from thrust (add note in thrust magnitude that specific impulse is basically useless if a custom mass rate is used).
 - Later on (maybe?): explain how to use thrust direction from rotational dynamics.

Thrust Vectoring Control
~~~~~~~~~~~~~~~~~~~~~~~~
In some cases, the thrust may not be aligned with the orientation of the vehicle that has been defined.

For instance, if Thrust Vectoring Control is to be used, with a nozzle deflection that varies over time, the true thrust direction will vary from the x-axis of the vehicle.

In Tudat(Py), this deviation in thrust direction from the vehicle can be defined in the body-fixed frame, trough the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ThrustMagnitudeSettings`.
When using the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.ConstantThrustMagnitudeSettings`, a constant body-fixed thrust direction can be defined where,
when using the :class:`~tudatpy.numerical_simulation.propagation_setup.thrust.FromFunctionThrustMagnitudeSettings`, this body-fixed thrust direction can be defined as a function of time.

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
**To do**
 - Explain how to use custom direction for thrust, and then manually specify aerodynamic angles (using aerodynamic guidance).
 - Explain how to use thrust direction from existing orientation defined by aerodynamic guidance