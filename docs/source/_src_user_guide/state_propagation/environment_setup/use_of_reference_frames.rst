.. _reference_frames:

===================================================
Reference Frames in the Environment and Propagation
===================================================

In any state propagation tool, the careful use of reference frames is essential: small mistakes in definitions and conventions are a notorious source of errors in simulations. The environment and state propagation framework in Tudat handles all the relevant state translations/rotations/transformations. On this page, we describe various manners in which reference frames are used in Tudat, and what the differences are when extracting a state from different places in Tudat.

Translational states
====================

The translational state of a body is a critical piece of information for numerous calculations in the Tudat propagation framework. For instance, (almost) any acceleration acting on a body :math:`A` will require the Cartesian state of this body as input. 

When running a state propagation, one of the first steps that is performed when evaluating the state derivative function :math:`\mathbf{f}(\mathbf{x},t)` is to update the full environment to the current time :math:`t` and state :math:`\mathbf{x}` (in a basic simulation, :math:`\mathbf{x}` is the translational state of a single body). This update step ensures that each Body object (see :class:`~tudatpy.numerical_simulation.environment.Body`) has all time/state dependent properties updated before any calculations of the state derivative are performed.  Once this update step is performed, each body relevant for the simulation will have their current translational state computed and set. Even when propagating the dynamics using a non-Cartesian propagator, for instance Keplerian elements, (see :class:`tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalPropagatorType` for full list of options), the translational state of a body is *always* set as its Cartesian state, with any relevant element conversions performed automatically. The Cartesian state may extracted from one of two places when the body is updated:

* The state vector: if the translational state of body :math:`A` is among the states that is numerically propagated, these elements will be extracted from the full state, and any relevant frame and elements conversions performed to define the current state of the body :math:`A`
* The ephemeris of a body: if the translational state of a body is required for a simulation, and this body is *not* numerically propagated, its state is retrieved from this body's ephemeris (see :class:`~tudatpy.numerical_simulation.environment.Ephemeris`).

Presently, Tudat does not support the automatic rotation of states between the state vector, ephemeris, or body objects. Consequenly, the frame *orientation* of each must be equal, as well as inertial. Currently, the frame origins J2000 and ECLIPJ2000 are supported (see :ref:`below<predefined_orientations>`).

Due to the above setup, three different definitions of states are used, where each may have its own distinct origin.

* State vector - the variables for which the differential equations are solved numerically during the propagation
* Ephemeris - a function of time that us fully defined before the state propagationm
* Body - defined from propagared state vector and/or ephemeris at the start of each state derivative evaluation

Tudat allows the flexibility to define a different origin for each one, with relevant translations automatically performed. Below, we summarize each one:

The propagation origin - the propagated state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When define translational propagator settings (see :ref:`translational_dynamics`), the propagation origin defines the origin w.r.t. which the state vector is defined. For instance if the propagated body is 'spacecraft' and the propagation origin (or synonymously, the central body) is 'Earth', the state vector will be relative position/velocity of spacecraft w.r.t. Earth.

| **How a user defines the propagation origin:** through the definition of the central body in the translational propagation settings
|
| **When the propagation origin is relevant to a user**
* When defining the initial state of a body: this must be w.r.t. the propagation origin
* When retrieving the numerical propagation results, these are always w.r.t. the propagation origin

The ephemeris origin - the states computed by an ephemeris
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each body that is not numerically propagated is typically (but not necesarilly) endowed with an ephemeris, which contains a pre-defined function of the body's translational state as a function of time. Unlike the global origin, the ephemeris origin of each body may be different. In the context of a numerical simulation, users do not often interrogate the ephemeris directly. However, it can be useful to do so outside of a numerical propagation, for instance to analyze the predefined trajectory of a body outside of the propagation framework

| **How a user defines the ephemeris origin**: through the definition of ephemeris settings when creating the settings for the body objects (see :ref:`environment_ephemeris_model`). Often, the default settings will be used in the case of celestial bodies (see :ref:`default_environment_models`).
|
| **When the propagation origin is relevant to a user**:
* When directly retrieving the state from an ephemeris object.

The global origin - the current states in the bodies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When :ref:`creating a set of body objects<creating_celestial_bodies>`, you define a global frame origin, and a global frame orientation. When a body's state gets updated, regardless of whether it is retrieved from the propagated state vector, or an ephemeris, it is *always* converted to this global frame origin/orientation before being assigned to a body object. Consequently, any time that a state is retrieved directly from a body object, it will be defined in this global frame. The global frame is the same for each body in a simulation. It are also these states in the global frame which are used for *any* calculations of the state derivative. Consequently, an (in)judicious choice of global frame origin may have an impact on the numerical noise in a simulation. For instance, when calculating the dynamics of a spacecraft w.r.t. the Earth, the relative position of the spacecraft w.r.t. the Earth is computed by extracting the position :math:`\mathbf{r}` from the body object representing Earth, and from the body representing the spacecraft. If the global frame origin is Earth, we will have :math:`\mathbf{r}=\mathbf{0}`, by definition. However, if the global frame origin set to ``SSB``, the relative position of spacecraft w.r.t. Earth will be calculated by subtracting the barycentric positions of the spacecraft and Earth (of order :math:`10^{11}` m) to compute the relative position (or order :math:`10^{7}` m for low-to-medium altitude orbits). As a result, 4 orders of magnitude of numerical precision may be lost in the calulcation of the spacecraft position that is used in the calculation of the accelerations.

| **How a user defines the global origin**: when creating the settings for the body objects (or the bodies themselves in case of manual body creation).
|
| **When the global frame origin is relevant to a user**
* Any time the state (or position or velocity) are retrieved directly from a body. This will, for instance, be done in custom guidance models.
* When high numerical precision is relevant, the global frame origin should be set such that numerical error in evaluating the strongest acceleration(s) is minimized

Rotational states
=================

The handling of rotational states in the environment and propagation framework follows that of the translational states to a large degree. However, there is one fewer complication for rotational states: no frame 'origin' has to be defined, which simplifies the overall book-keeping of the states. Still, a rotation may be extracted from one of three places during the numerical propagation:

* State vector (if a rotational state is propagated)
* Rotational ephemeris
* Body

However, Tudat presently requires all **translational** state vectors to be defined w.r.t. the same inertial orientation (J2000 or ECLIPJ2000, selected by the user). As such, rotations in Tudat that are defined in one of the above three places will always be from this inertial frame to the body-fixed frame (of the body associated with it). 

.. _quaternion_definition:

Definition of rotational state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic definition of a rotational states in Tudat uses quaternions, which is a typical non-singular choice of elements.
However, the exact definition of the quaternion entries :math:`q_{0},q_{1},q_{2},q_{3}` is non-unique, with several conventions
in use. Our quaternion definition is that used in the `Eigen library <https://eigen.tuxfamily.org/dox/classEigen_1_1Quaternion.html>`_.
Instead of having to manually determine each of the quaternion entries for a given rotation, we provide a function which converts
a rotation matrix to the corresponding quaternion :func:`~tudatpy.astro.element_conversion.rotation_matrix_to_quaternion_entries`,
and the inverse :func:`~tudatpy.astro.element_conversion.quaterion_entries_to_rotation_matrix`. Here, we stress that, in
the context of these functions, we are not dealing with actual quaternions (in the sense of mathematical operators that can
rotate a vector), but merely with 4x1 arrays which store the four quaternion elements, using the correct conventions.

.. _predefined_orientations:

Predefined orientations
=======================

For the definition of pre-defined states and rotations, Tudat relies heavily on the spice toolkit. In fact, most of the default ephemerides and rotational models are taken directly from spice (see :ref:`default_environment_models`). Through spice, the following two inertial reference frame orientations are defined:

* J2000: Right-handed inertial frame which has :math:`x`-axis towards vernal equinox, and the :math:`z`-axis aligned with Earth’s rotation axis as it was at the J2000 epoch. We stress that this frame is inertial, and its :math:`z`-axis direction does *not* move with the Earth's rotation axis. (Note that this frame is *almost* identical to teh GCRS frame, with a small frame bias between the two, see for instance section 2.5 of `this document <https://www.iausofa.org/2013_1202_F/sofa/sofa_pn.pdf>`_)
* ECLIPJ2000: Right-handed inertial frame which has :math:`x`-axis towards vernal equinox, and the :math:`z`-axis perpendicular to the ecliptic, at the J2000 epoch.

In our default rotation models, we use spice kernels that implement the models developed by the IAU Working Group on Cartographic Coordinates and Rotational Elements. The resulting body-fixed frames for solar system bodies are denoted in spice (and therefore in Tudat), as IAU_XXXX for body XXXX. For instance, the default body-fixed frame of Mars is denoted IAU_Mars. We stress that it is not required that the body-fixed frames follow this nomenclature, but this is merely the default. To change the identifier associated with a rotation model, you can modify the ``base_frame`` input for a body's rotational ephemeris settings when calling the associated `factory functions <https://tudatpy.readthedocs.io/en/latest/rotation_model.html#functions>`_.



