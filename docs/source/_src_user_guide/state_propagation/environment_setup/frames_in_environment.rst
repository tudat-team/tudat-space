.. _reference_frames:

=========================
Frames in the Environment
=========================


In any state propagation tool, the careful use of reference frames is essential: small mistakes in definitions and conventions
are a notorious source of errors in simulations. The environment and state propagation framework in Tudat handles all the
relevant state translations/rotations/transformations. On this page, we describe various manners in which reference frames
are used in the environment Tudat, in particular in the :class:`~tudatpy.numerical_simulation.environment.Body` objects (which
constitute the environment). In addition, we highlight what the differences are when extracting a state from different places in Tudat.
This page is limited mainly in the manner that Tudat *automatically* deals with various different frames. A comprehensive list of
all available frames that are available to the user can be found :ref:`here <manual_state_definitions>`.

.. contents:: Content of this page
   :local:

.. _translational_reference_frames:

Translational states
====================

The translational state of a body is a critical piece of information for numerous calculations in the Tudat propagation framework.
For instance, (almost) any acceleration acting on a body :math:`A` will require the Cartesian state of this body as input.

In Tudat, we use the terms *frame* and *element* to describe the following distinct concepts:

- **Frame orientation**: Defines the orientation in inertial space of the set of unit vectors the :math:`x`, :math:`y` and :math:`z` axes.
  These orientations may be constant in time, in which case the frame is said to have an inertial orientation (for instance the J2000 frame orientation),
  or a time-dependent orientation (for instance an Earth-fixed frame orientation).
- **Frame origin**: Defines the point in inertial space that defines the :math:`\mathbf{0}` position (:math:`x=y=z=0`).
  This point may be constant in time, in which case the frame is said to have an inertial origin (for instance: the solar
  system barycentric origin), or a time-dependent orientation (for instance an Earth-centered origin).
- **Elements**: The physical meaning of the values of a state vector that represent a (translational) state.
  Examples are Cartesian, Keplerian and Modified Equinoctial. With the exception of possible singularities,
  these different element types can use six (or more) values to defines the same physical state, but using a very different set of numbers.

The frame itself does not define anything concerning the (state) vector, instead it defines how a specific set of elements represents
a specific physical state. In Tudat, a state vector is represented as a vector (numpy in Python; Eigen in C++).
The state vector itself cannot store the element set or frame orientation in which it is defined.
This information is tracked by Tudat (for internal computations) or should be tracked by a user (for any user-defined state vector).

In the rest of this section, we will present how Tudat deals with the calculation and transformation of frame origins and orientations.
Through out, we will assume that all translational state vectors are represented in Cartesian coordinates.

When running a state propagation, one of the first steps that is performed when evaluating the state derivative
function :math:`\mathbf{f}(\mathbf{x},t)` (see :ref:`single_propagation_evaluation`) is to update the full environment to the current time :math:`t` and state 
:math:`\mathbf{x}`. Note that in a basic simulation, :math:`\mathbf{x}` is the translational state of a single body. See :ref:`environment_during_propagation` for details on how to access the current properties of the environment during a propagation.

..
  This update
  step ensures that each Body object (see :class:`~tudatpy.numerical_simulation.environment.Body`) has all time/state
  dependent properties updated before any calculations of the state derivative are performed. Once this update step is
  performed, each body relevant for the simulation will have their current translational state computed and set. 

Even when propagating the dynamics using a non-Cartesian propagator, for instance Keplerian elements,
(see :class:`~tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalPropagatorType`
for full list of options), the translational state of a body is *always* set as its Cartesian state,
with any relevant element conversions performed automatically. The Cartesian state may extracted from one
of two places when the body is updated:

  *  **State vector**: if the translational state of body :math:`A` is among the states that is numerically propagated, these elements will be extracted from the full state, and any relevant frame and elements conversions performed to define the current state of the body :math:`A`
  *  **Ephemeris of a body**: if the translational state of a body is required for a simulation, and this body is *not* numerically propagated, its state is retrieved from this body's ephemeris (see :class:`~tudatpy.numerical_simulation.environment.Ephemeris`).

.. _translational_frame_origins:

Frame origin
------------
Due to the above setup, three different definitions of states are used, where each may have its own distinct origin.

* State vector - the variables for which the differential equations are solved numerically during the propagation
* Ephemeris - a function of time that is fully defined before the state propagation
* Body - defined from propagated state vector and/or ephemeris at the start of each state derivative evaluation

Tudat allows the flexibility to define a different origin for each one, with relevant translations automatically
performed. Below, we summarize each one:

- :ref:`propagation_origin`
- :ref:`ephemeris_origin`
- :ref:`global_origin`

.. _propagation_origin:

The propagation origin - the propagated state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When defining translational propagator settings (see :ref:`translational_dynamics`), the propagation origin defines the origin w.r.t. which the state vector is defined. For instance if the propagated body is 'spacecraft' and the propagation origin (or synonymously, the central body) is 'Earth', the state vector will be relative position/velocity of spacecraft w.r.t. Earth.

| **How a user defines the propagation origin:** through the definition of the central body in the translational propagation settings
|
| **When the propagation origin is relevant to a user:**

* When defining the initial state of a body: this must be w.r.t. the propagation origin
* When retrieving the numerical propagation results, these are always w.r.t. the propagation origin

.. _ephemeris_origin:

The ephemeris origin - the states computed by an ephemeris
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each body that is not numerically propagated is typically (but not necessarily) endowed with an ephemeris, which contains a pre-defined function of the body's translational state as a function of time. Unlike the global origin, the ephemeris origin of each body may be different. In the context of a numerical simulation, users do not often interrogate the ephemeris directly. However, it can be useful to do so outside of a numerical propagation, for instance to analyze the predefined trajectory of a body outside of the propagation framework

| **How a user defines the ephemeris origin**: through the definition of ephemeris settings when creating the settings for the body objects (see :doc:`Ephemeris models <ephemeris>`). Often, the default settings will be used in the case of celestial bodies (see :ref:`default_env_models`).
|
| **When the ephemeris origin is relevant to a user:**

* When directly retrieving the state from an ephemeris object.

.. _global_origin:

The global origin - the current states in the bodies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When :ref:`creating a set of body objects<creation_celestial_body_settings>`, you define a global frame origin, and a global frame orientation.
When a body's state gets updated (see :ref:`propagation architecture page <single_propagator_time_step>`, regardless of whether it is retrieved
from the propagated state vector, or an ephemeris, it is *always*
converted to this global frame origin/orientation before being assigned to a body object.
Consequently, any time that a state is retrieved directly from a body object during the propagation using the :attr:`~tudatpy.numerical_simulation.environment.Body.state`
function (as described :ref:`here <translational_state_during_propagation>`), it will *always* be defined in this global frame.

The global frame is the same for each body in a simulation. All used for calculations of the state derivative are in this global frame.
Consequently, an (in)judicious choice of global frame origin may have an impact on the numerical noise in a simulation.
For instance, when calculating the dynamics of a spacecraft w.r.t. the Earth, the relative position of the spacecraft w.r.t. the
Earth is computed by extracting the position :math:`\mathbf{r}` from the body object representing Earth, and from the body representing the spacecraft.
If the global frame origin is Earth, we will have :math:`\mathbf{r}=\mathbf{0}`, by definition. However, if the global frame origin set to ``SSB``, the relative position of spacecraft w.r.t. Earth will be calculated by subtracting the barycentric positions of the spacecraft and Earth (of order :math:`10^{11}` m) to compute the relative position (or order :math:`10^{7}` m for low-to-medium altitude orbits). As a result, 4 orders of magnitude of numerical precision may be lost in the calculation of the spacecraft position that is used in the calculation of the accelerations.

| **How a user defines the global origin**: when creating the settings for the body objects (or the bodies themselves in case of manual body creation).
|
| **When the global frame origin is relevant to a user:**

* Any time the state (or position or velocity) are retrieved directly from a body. This will, for instance, be done in custom guidance models.
* When high numerical precision is relevant, the global frame origin should be set such that numerical error in evaluating the strongest acceleration(s) is minimized


Frame orientation
-----------------

Presently, Tudat does not support the automatic rotation of states between the state vector, ephemeris, or body objects (as it does
for the frame origin). Consequently, the frame *orientation* of each must be equal, as well as inertial. Currently, the frame orientations
``J2000`` and ``ECLIPJ2000`` are supported (see :ref:`here<predefined_orientations>`). A large number of additional frame orientations can be
used (either by the user or built-in functionality), a comprehensive list of which is provided :ref:`here <frame_orientations>`

.. _rotational_reference_frames:

Rotational states
=================

The handling of rotational states in the environment and propagation framework follows that of the translational states to a large degree.
However, there is one fewer complication for rotational states: no frame 'origin' has to be defined, which simplifies the overall book-keeping
of the states. A rotation may be extracted from/defined in one of three places:

* During the propagation: directly from a Body object (see :ref:`rotation_during_propagation`)
* Rotational ephemeris
* State vector (if a rotational state is propagated, see :ref:`rotational_dynamics`)

Since Tudat presently requires all **translational** state vectors to be defined w.r.t. the same inertial orientation
(J2000 or ECLIPJ2000, selected by the user), all **rotational states** in Tudat that are will always be from this inertial
frame to the body-fixed frame (of the body associated with it).

.. _quaternion_definition:

Definition of rotational state
------------------------------

The basic definition of a rotational states in Tudat uses quaternions, which is a typical non-singular choice of elements.
However, the exact definition of the quaternion entries :math:`q_{0},q_{1},q_{2},q_{3}` is non-unique, with several conventions
in use. Our quaternion definition is that used in the `Eigen library <https://eigen.tuxfamily.org/dox/classEigen_1_1Quaternion.html>`_.
Instead of having to manually determine each of the quaternion entries for a given rotation, we provide a function which converts
a rotation matrix to the corresponding quaternion :func:`~tudatpy.astro.element_conversion.rotation_matrix_to_quaternion_entries`,
and the inverse :func:`~tudatpy.astro.element_conversion.quaternion_entries_to_rotation_matrix`. Here, we stress that, in
the context of these functions, we are not dealing with actual quaternions (in the sense of mathematical operators that can
rotate a vector), but merely with 4x1 arrays which store the four quaternion elements, using the correct conventions.



