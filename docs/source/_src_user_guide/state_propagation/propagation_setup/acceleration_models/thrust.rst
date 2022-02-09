.. _thrust_models:


========================
Thrust Guidance
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
Secondly, to define the thrust acceleration, the user must provide two objects: one of type (derived from) :class:`ThrustDirectionSettings` and one of type (derived from) :class:`ThrustMagnitudeSettings`.
The two settings are used to create a :class:`ThrustAccelerationSettings` object. 

.. class:: ThrustAccelerationSettings

   Class containing the properties of the thrust acceleration (direction and magnitude). Set by the settings classes described below.


Thrust direction
~~~~~~~~~~~~~~~~

For the direction of the thrust, there are presently four available types of guidance.

.. class:: ThrustDirectionFromStateGuidanceSettings

    In various simplified cases, the thrust direction can be assumed to be in line with either the position or velocity w.r.t. some body.

    This thrust direction setting can be created in Tudat as follows:

    .. tabs::

         .. tab:: Python

          The Tudat(Py) API docs give more details the :literal:`thrust_direction_from_state_guidance()` function `on this page <https://tudatpy.readthedocs.io/en/latest/thrust.html#tudatpy.numerical_simulation.propagation_setup.thrust.thrust_direction_from_state_guidance>`_.

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_direction_from_state_guidance.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/thrust/thrust_direction_from_state_guidance.cpp
             :language: cp

.. class:: CustomThrustDirectionSettings

   For a generalized thrust direction guidance, the thrust can be defined as an arbitrary function of time. This allows a broad range of options to be defined, at the expense of increased complexity (somehow this thrust direction needs to be manually defined):

   .. code-block:: cpp

 	CustomThrustDirectionSettings( 
		thrustDirectionFunction );


- :literal:`thrustDirectionFunction`

        A :literal:`std::function< Eigen::Vector3d( const double ) >` returning a the thrust direction in the inertial frame as an ``Eigen::Vector3d`` (which should be of unit norm!) as a function of a ``double`` (representing time). Details on how to create such an :literal:`std::function` are given on :ref:`externalUtilityExamples`. 

.. warning:: When using the :class:`CustomThrustDirectionSettings`, the inertial to body-fixed rotation cannot be unambiguously defined. If you require this rotation (for instance when you also incorporate aerodynamic forces), the :class:`CustomThrustOrientationSettings` class should be used instead.

.. warning:: The direction vector that is being returned by the custom function should be a unit vector.

As a possible example of how to use this function:

    .. tabs::

         .. tab:: Python

          PPP

         .. tab:: C++

          CCC