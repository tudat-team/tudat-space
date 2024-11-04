.. _manual_state_definitions:

===========================================
Available State Definitions and Conversions
===========================================

A general, top-level, discussion on the definition of the terms frame origin, frame orientation, and element, are given
:ref:`here <translational_reference_frames>`, along with how the frame origins and orientation in Tudat are used and automatically converted
during the propagation. On the current page, we present the numerous options that are available to users for frame orientations and element sets,
both during and/or outside of a propagation. In addition, we start by briefly reviewing the way in which to transform between
different frame origins in Tudat.

Frame Origin Conversions
========================

The various frame types of frame origins used in the Tudat simulation framework are described on a :ref:`dedicated page <translational_frame_origins>`.
Here, we briefly outline how to manually convert states between frame origins. In Tudat, each body automatically defines a frame origin,
which is located at a predefined point in (or in exotic cases, outside), the body. Typically, the frame origin will coincide with the
center of mass of the body for natural bodies. However, in case (for instance) the body possesses a spherical harmonic gravity field
with non-zero degree 1 coefficients, the gravity field (which determines the internal mass distribution) can define an offset between
the origin of the body-centered frame, and its center-of-mass.

When retrieving the state from a ``Body`` :ref:`during the propagation <translational_state_during_propagation>`, this state is
*always* w.r.t. the :ref:`global frame origin <global_origin>`. Therefore, performing origin translations *during* the propagation
between states from the environment is simply done as:

.. code-block:: python

        bodies = ...
        mars_state_wrt_global_origin = bodies.get( "Mars" ).state
        earth_state_wrt_global_origin = bodies.get( "Mars" ).state

        mars_state_wrt_earth = mars_state_wrt_global_origin - earth_state_wrt_global_origin

You can also bypass body and ephemeris objects altogether, and use ``spice`` to obtain the relative state.
Note, however, that this will use whichever ``spice`` kernels you have loaded, and **may not be consistent with the states
you are using the bodies in your simulations.**

.. dropdown:: Required
	:color: muted

	.. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
		:language: python

.. code-block:: python

        current_time = ...

        mars_state_wrt_earth = spice.get_body_cartesian_state_at_epoch(
                target_body_name="Moon",
                observer_body_name="Earth",
                reference_frame_name="J2000",
                ephemeris_time=current_time )


.. _frame_orientations:

Frame Orientations Conversions
==============================

A conversion from a frame :math:`A` to a frame :math:`B` may be achieved by any one of a number of equivalent operators (rotation matrices, quaternions, etc.).
In what follows, we will use rotation matrices. We denote a rotation matrix from :math:`A` to frame :math:`B` as :math:`\mathbf{R}^{(B/A)}`.
Position, velocity and Cartesian state (column) vectors are denoted as :math:`\mathbf{r}`, :math:`\mathbf{v}` and :math:`\mathbf{x}(=[\mathbf{r};\mathbf{v}])`.
To explicitly denote the frame, we will write :math:`\mathbf{r}^{A}`.

Below, a list of numerous frame orientations, and the associated Tudat functionality to compute the associated rotation matrices, is discussed.
First, we note a fundamental difference between rotating a state between two frames that are inertial, and a rotation where one of the two frames
:math:`A` or :math:`B` is non-inertial.

For the general case, where at last one frame :math:`A` or :math:`B` is non-inertial, we have:

.. math::

 \mathbf{r}^{B}&=\mathbf{R}^{(B/A)}\mathbf{r}^{A}\\
 \mathbf{v}^{B}&=\dot{\mathbf{R}}^{(B/A)}\mathbf{r}^{A} + \mathbf{R}^{(B/A)}\mathbf{v}^{A}\\

where :math:`\dot{\mathbf{R}}^{(B/A)}` is the time-derivative of the associated rotation matrix. When both frames :math:`A` and :math:`B` are inertial,
this time-derivative vanishes, and we have:

.. math::

 \mathbf{r}^{B}&=\mathbf{R}^{(B/A)}\mathbf{r}^{A}\\
 \mathbf{v}^{B}&=\mathbf{R}^{(B/A)}\mathbf{v}^{A}\\

The time-derivative of the rotation matrix may be equivalently represented by the angular velocity vector :math:`\boldsymbol{\omega}_{BA}`,
which we take to represent the angular velocity of frame :math:`A`, w.r.t. frame :math:`B`, expressed with frame orientation :math:`A`.
For the typical case where :math:`B` is an inertial frame, :math:`\boldsymbol{\omega}_{BA}(=\boldsymbol{\omega}_{A})` is simply the angular
velocity of :math:`A` (w.r.t. inertial space), represented in the frame fixed to body :math:`A` (TODO: link to propagation).
More information is provided in the `Tudat mathematical model pdf <https://github.com/tudat-team/tudat-space/raw/master/Tudat_mathematical_model_definition.pdf>`_.

Manually, the above transformations would be done simply as:

.. code-block:: python

        rotation_to_frame = ... # 3D Matrix
        time_derivative_of_rotation_to_frame  = ... # 3D Matrix
        original_state = ... # 6D Vector

        rotated_state = np.zeros(6, dtype=float)
        rotated_state[ :3] = rotation_to_frame @ original_state[ :3 ]
        rotated_state[3: ] = rotation_to_frame @ original_state[ 3: ] + time_derivative_of_rotation_to_frame @ original_state[ :3 ]

Where the rotation matrix and its derivative (for body-fixed to inertial frames) can be obtained from the ``Body`` object during propagation, or a ``RotationalEphemeris``
object outside of the propagation, see :ref:`below <body_fixed_frames>` for more details.

Below, we give an overview of the available frames, and frame transformations in Tudat, and discuss how they can be accessed both during
(when setting up a :ref:`custom model <custom_models>`), and outside of a propagation. The available frames are:

  * :ref:`body_fixed_frames`: Each ``Body`` in Tudat can have a fixed frame assigned to it (see `API documentation <https://py.api.tudat.space/en/latest/rotation_model.html#functions>`_ for a list of options for model types).
  * :ref:`gcrs_itrs_frames`: The high-accuracy rotation from GCRS to ITRS is implemented in Tudat. The ITRS, TIRS, CIRS and ICRS frames are defined.
  * :ref:`aero_frames`: A number of frames typically used in entry and ascent trajectories: the Vertical, Trajectory and Aerodynamic frames.
  * :ref:`orbital_frames`: The TNW and RSW frames (defined by the current relative translational state).
  * :ref:`spice_frames`: Any frame defined by the currently loaded SPICE kernels can be accessed.
  * :ref:`predefined_orientations`: The J2000 and ECLIPJ2000 frame orientations (at present, the only two supported options for the global frame orientation).
  * :ref:`topocentric_frames`: Each ground station/lander on a body has a frame (East-North-Up) automatically associated with it.
  * :ref:`additional_frames`: The TEME frame, which is typically used for the definition of two-line elements (TLE).

.. _body_fixed_frames:

Body-fixed frames
-----------------

In Tudat, body-fixed frames are defined inside a :class:`~tudatpy.numerical_simulation.environment.Body` object (which is typically
stored in a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object). **Retrieving the current orientation (and its time-derivative)
during the propagation is described** :ref:`here <rotation_during_propagation>`.

Outside of the propagation, these quantities can be obtained
directly from the :class:`~tudatpy.numerical_simulation.environment.RotationalEphemeris` class, which is retrieved from a ``Body`` object using the
:attr:`~tudatpy.numerical_simulation.environment.Body.rotation_model`. Below, an example is shown on how to extract rotational properties
for the Earth outside of a propagation (assuming a ``SystemOfBodies`` object, named ``bodies`` has been created):

.. code-block:: python

        earth_rotation_model = bodies.get( "Earth" ).rotation_model

        # Define time at which to determine rotation quantities
        current_time = ...

        # Determine R^{(I/B)} rotation matrix
        rotation_matrix_to_inertial_frame = earth_rotation_model.body_fixed_to_inertial_rotation( current_time )

        # Determine first derivative of R^{(I/B)} rotation matrix
        rotation_matrix_to_inertial_frame = earth_rotation_model.time_derivative_body_fixed_to_inertial_rotation( current_time )

To automatically rotate a vector from the body-fixed frame to the inertial frame using the ``RotationalEphemeris``, we provide the
:class:`~tudatpy.numerical_simulation.environment.transform_to_inertial_orientation` function, which automatically
performs the rotation with the rotation matrix and its derivative:

.. dropdown:: Required
	:color: muted

	.. code-block:: python
		
		from tudatpy.numerical_simulation import environment

.. code-block:: python

        earth_rotation_model = bodies.get( "Earth" ).rotation_model

        # Define time at which to determine rotation quantities
        current_time = ...

        # Set the body-fixed state
        body_fixed_state = ...

        # Transform state to inertial frame, using Earth rotation model
        inertial_state = environment.transform_to_inertial_orientation(
            body_fixed_state, current_time, earth_rotation_model )


The full list of functions to extract rotational quantities from a rotational model can be found under
:class:`~tudatpy.numerical_simulation.environment.RotationalEphemeris`. Depending on the selected rotation model,
additional intermediate frames (in addition to the inertial to/from body-fixed rotation) may be available. One example is the
high-accuracy rotation model, which is discussed in some more detail :ref:`below <gcrs_itrs_frames>`.

For certain applications, a used must specify the *identifier* of a body-fixed frame in Tudat. This name can be retrieved using
:attr:`~tudatpy.numerical_simulation.environment.RotationalEphemeris.body_fixed_frame_name`.

For manual calculations of a body-fixed to inertial frame (or vice versa) from the typical pole right ascension/declination and prime meridian
longitude, the low-level functions :func:`~tudatpy.astro.frame_conversion.inertial_to_body_fixed_rotation_matrix` and
:func:`~tudatpy.astro.frame_conversion.body_fixed_to_inertial_rotation_matrix` can be used.

.. _gcrs_itrs_frames:

GCRS/ITRS frames
----------------

Using the `Standards of Fundamental Astronomy (SOFA) <https://www.iausofa.org/>`_ software, disseminated by the IAU, as well as
internal implementation of correction terms from the `IERS Conventions <https://iers-conventions.obspm.fr/content/tn36.pdf>`_, Tudat
provides functionality for high-accuracy Earth-orientation calculations.

This functionality is implemented as a rotation model, defined using the
:func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.gcrs_to_itrs` function
which will in most cases be created during the :ref:`setup of the environment <creation_celestial_body_settings>`
(and, typically, assigned to the body object representing Earth).

When this rotation model is assigned to Earth, it can be extracted as an object of type :func:`~tudatpy.numerical_simulation.environment.GcrsToItrsRotationModel`:

.. code-block:: python

        # Create body settings (typically from defaults), and modify the Earth's rotation settings
        body_settings = ...
        body_settings.get("Earth").rotation_model_settings = environment_setup.rotation_model.gcrs_to_itrs( )

        # Create bodies
        bodies = environment_setup.create_system_of_bodies(body_settings)

        # Extract GcrsToItrsRotationModel object
        high_fidelity_earth_rotation_model = bodies.get( "Earth" ).rotation_model

The rotation matrices produced by the ``high_fidelity_earth_rotation_model`` will not have the GCRS as their base frame,
but rather the global frame orientation of the environment (typically J2000 or ECLIPJ2000), as defined in the ``body_settings``.

The ``GcrsToItrsRotationModel`` class possesses all properties of a :ref:`regular body rotation model <body_fixed_frames>`.
In addition, it provides a number of functions to extract intermediate angles/rotations. These angles are defined in detail in the IERS
conventions (chapter 5 of 2010 conventions), and can be extracted from the :class:`~tudatpy.numerical_simulation.environment.GcrsToItrsRotationModel`,
and the :class:`~tudatpy.numerical_simulation.environment.EarthOrientationAnglesCalculator` (where the latter can be obtained from the
former).

.. _aero_frames:

Aerodynamic/vehicle frames
--------------------------

Typically in, but not exclusively to, the calculation of aerodynamic quantities and ascent trajectories, a number of intermediate frames
are used, which link the inertial frame to the body-fixed frame of the vehicle. Identifiers for these frames are defined in the
:class:`~tudatpy.numerical_simulation.environment.AerodynamicsReferenceFrames` enumeration. They are listed here for completeness:

- Inertial frame (corresponding exactly to the global frame orientation of the environment)
- Central-body-fixed frame (corresponding exactly to the :ref:`body-fixed frame <body_fixed_frames>` of the central body)
- Vertical frame
- Trajectory frame
- Aerodynamic frame
- Vehicle body-fixed frame (corresponding exactly to the :ref:`body-fixed frame <body_fixed_frames>` of the central body)

For the mathematical model definition (and graphical representation), we refer the reader to `Mooij (1994) <https://repository.tudelft.nl/islandora/object/uuid:e5fce5a0-7bce-4d8e-8249-e23293edbb55/datastream/OBJ/download>`_.

The rotation matrix between any two of these frames, as well the angles that define these rotations, can be determined **during the propagation**
using the :class:`~tudatpy.numerical_simulation.environment.AerodynamicAngleCalculator` class, as described :ref:`here <flight_conditions_during_propagation>`.

To save these rotation matrices **during** the propagation, and then inspect them **after** the propagation, the
:ref:`dependent variable <dependent_variables>` :func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.intermediate_aerodynamic_rotation_matrix_variable`
can be used. The constituent angles that define this rotation can be saved using the :func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.latitude`,
:func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.longitude`, :func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.heading_angle`,
:func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.flight_path_angle`, :func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.angle_of_attack`,
:func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.sideslip_angle` and :func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.bank_angle` functions.

At present, the functionality to compute these matrices/angles *outside* of the propagation is not exposed to Python. Please contact the development team if you require this functionality.

.. _orbital_frames:

Orbital frames
--------------

To represent the state of a body orbiting a central body, it can often be convenient to align one of the axes with the position or velocity
vector w.r.t. this central body, and another axis perpendicular to its instantaneous orbital plane.
For this purpose, the following frames and rotation functions are defined:

* TNW frame: See :func:`~tudatpy.astro.frame_conversion.inertial_to_tnw_rotation_matrix` and :func:`~tudatpy.astro.frame_conversion.tnw_to_inertial_rotation_matrix` for usage and definition.
* RSW frame: See :func:`~tudatpy.astro.frame_conversion.inertial_to_rsw_rotation_matrix` and :func:`~tudatpy.astro.frame_conversion.rsw_to_inertial_rotation_matrix` for usage and definition.

The input to both functions is the current state of a body w.r.t. a central body, expressed in an inertial frame. For these
specific functions, it is *not relevant* which specific inertial frame this is. Note that, even though the RSW and TNW frames that are associated
with a body both change in time (as the vehicle's relative state w.r.t. the central body changes), each relative state defines a *separate*
TNW and RSW frame. As such a given TNW and RSW frame are considered to be inertial.

.. _spice_frames:

SPICE-defined frames
--------------------

The :ref:`default rotation models <default_rotation_models>` in Tudat make extensive use of the SPICE toolbox [Acton1996]_.
A user may directly access the functionality of extracting rotations in SPICE. For any frame identifiers for which SPICE kernels are loaded, the function
:func:`~tudatpy.interface.spice.compute_rotation_matrix_derivative_between_frames` may be used to determine the rotation matrix between them.
The derivative of the rotation matrix may be determined from :func:`~tudatpy.interface.spice.compute_rotation_matrix_derivative_between_frames`.

Similarly, a rotation model may be created and assigned to a body that automatically extracts the rotation from SPICE, using the
:func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.spice` rotation mode setting (as is done by default for most bodies).

The typical body-fixed frames for solar system bodies are denoted in SPICE as ``IAU_XXXX`` for body ``XXXX``.
For instance, the default body-fixed frame of Mars is denoted ``IAU_Mars``.

.. _predefined_orientations:

Predefined inertial frames
--------------------------

Through SPICE, the following two inertial reference frame orientations are defined by definition:

* ``J2000``: Right-handed inertial frame which has :math:`x`-axis towards vernal equinox, and the :math:`z`-axis aligned
  with Earth’s rotation axis as it was at the J2000 epoch. We stress that this frame is inertial, and its
  :math:`z`-axis direction does *not* move with the Earth's rotation axis. (Note that this frame is *almost* identical
  to the :ref:`GCRS frame <gcrs_itrs_frames>`, with a small frame bias between the two,
  see for instance section 2.5 of `this document <https://www.iausofa.org/2013_1202_F/sofa/sofa_pn.pdf>`_)
* ``ECLIPJ2000``: Right-handed inertial frame which has :math:`x`-axis towards vernal equinox, and the :math:`z`-axis
  perpendicular to the ecliptic, at the J2000 epoch.

The J2000 and ECLIPJ2000 frame names can be used for the base or target frames in any of the :ref:`SPICE rotation functions<spice_frames>`.

.. _topocentric_frames:

Station topocentric frames
--------------------------

Each :class:`~tudatpy.numerical_simulation.environment.GroundStation` which is placed on a body automatically has a topocentric
frame assigned to it. The rotation matrix from body-fixed to topocentric frame can be extracted as follows:

.. code-block:: python

        # Extract station, and object storing its state
        delft_station = bodies.get( "Earth" ).get_ground_station( "DopTrack" )
        delft_station_state = station.station_state

        # Extract rotation from Earth-fixed to station topocentric frame.
        rotation_earth_fixed_to_delft_topocentric = delft_station_state.rotation_matrix_body_fixed_to_topocentric

The rotation matrix is stored in a :class:`~tudatpy.numerical_simulation.environment.GroundStationState` object (which is obtained
in the second code line above for the specific station), and the :attr:`~tudatpy.numerical_simulation.environment.GroundStationState.rotation_matrix_body_fixed_to_topocentric`
returns the required rotation matrix. The axes of the topocentric frame are defined such that the x-axis is in East direction, the z-direction is upwards, perpendicular to
the body's surface sphere (typically: sphere or flattened sphere). The y-axis completes the frame, and is in northern direction.
For more details see the API docs entries for this function.

.. _additional_frames:

Additional frames
-----------------

A number of other frames are defined in Tudat, which can be used either during or outside of a propagation

**TEME frame**



Element Types
======================

Translational
-------------

Depending on your application, you will be using any of a number of translational state (position and velocity) representations.
In Tudat, conversions involving the following state representations are available:

- Cartesian elements.
- Keplerian elements.
- Spherical-orbital elements.
- Modified Equinoctial elements.
- Unified State Model elements.

For each of these element types, conversions to/from Cartesian elements are available. Converting between two element types,
where neither is Cartesian, will typically involve first transforming to Cartesian elements, and then transforming to your output
state type. For a number of combinations of state types, a direct conversion is available.

TODO: introduce element index enums

Note that most, but not all, of these types of elements can also be used for the definition of a
:ref:`translational state propagator <processed_propagated_states>`,
where these elements are numerically propagated (instead of the typical Cartesian elements of the Cowell propagator). By definition,
each element set that can be propagated has conversion functions available in Tudat, but not necessarily vice versa.

Kepler elements
^^^^^^^^^^^^^^^

The Kepler elements are the standard orbital elements used in classical celestial mechanics, and are represented as a size 6 vector in Tudat.
The meaning of each of the six entries is given in the `API docs <https://py.api.tudat.space/en/latest/element_conversion.html#notes>`_.
In this list you can see something peculiar: both the semi-major axis index and semi-latus rectum index are defined as index 0.
The latter option is only applicable when the orbit is parabolic (when the eccentricity is 1.0). That is, if the orbit is parabolic,
element 0 does not represent the semi-major axis (as it is not defined) but the semi-latus rectum.
Converting to/from Cartesian state is done using the :func:`~tudatpy.astro.element_conversion.cartesian_to_keplerian` and
:func:`~tudatpy.astro.element_conversion.keplerian_to_cartesian` functions, and requires the gravitational parameter of the body
w.r.t. which the Keplerian elements are defined, in addition to the state itself.

Often, these functions will be used in conjunction with numerical propagation, where the properties of bodies are stored in an
object of type :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies`

.. dropdown:: Required
	:color: muted

	.. code-block:: python

		import tudatpy.astro.element_conversion as conversion

.. code-block:: python

   cartesian_state = ...

   central_body = 'Earth'
   central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter
   keplerian_state = conversion.cartesian_to_keplerian( cartesian_state, central_body_gravitational_parameter )

In the above examples, it is crucial to be aware that the Cartesian and Keplerian elements are the representation
of a state in the same **frame**. That is, if the ``cartesian_state`` in the first example is in the `ECLIPJ2000` frame orientation,
with the Earth as frame origin, the ``keplerian_state`` will also be defined w.r.t. the axes of this frame.
As a result, the inclination (for example) will be measured w.r.t. the x-y plane of the `ECLIPJ2000`  frame, **not** w.r.t. the Earth's equator.

.. note::
   A Keplerian state cannot be computed w.r.t. the Solar System Barycenter (SSB), as it does not possess a gravitational parameter.

In the definition of the state elements, you will notice that element 5 is the *true* anomaly, not the *eccentric* or
*mean* anomaly. Tudat also contains functions to convert to these alternative anomalies. The various available functions
are found in our :doc:`API docs <element_conversion>`.

As an example, converting from true to eccentric anomaly is done as follows:

.. code-block:: python

	true_anomaly = ...
	eccentricity = ...
	eccentric_anomaly = conversion.true_to_eccentric_anomaly( true_anomaly, eccentricity )

or directly from the orbital elements:

.. code-block:: python

	keplerian_state = ...
	eccentric_anomaly = conversion.true_to_eccentric_anomaly( keplerian_state( true_anomaly_index ), keplerian_state( eccentricity_index ) )


Note that this function automatically identifies whether the orbit is elliptical or hyperbolic, and computes the associated eccentric anomaly.
Similarly, Tudat contains functions to convert from eccentric to mean anomaly (automatically checking whether the orbit is elliptical or hyperbolic):

.. code-block:: python

	true_anomaly = ...
	eccentricity = ...

	eccentric_anomaly = conversion.true_to_eccentric_anomaly( true_anomaly, eccentricity )
	mean_anomaly = conversion.eccentric_to_mean_anomaly( eccentric_anomaly, eccentricity )

The conversion from mean to eccentric anomaly involves the solution of an implicit algebraic equation (Kepler's equation), for which a root finder is used.
Root finders are discussed in more detail here (TODO: insert link). Tudat has a default root finder, and default selection for
initial guess of the root-finding implemented see :func:`~tudatpy.astro.element_conversion.mean_to_eccentric_anomaly`.
However, in some cases you may want to specify your own initial guess for the eccentric anomaly, and/or your own root finder.
You can do this as follows:

.. code-block:: python

	mean_anomaly = ...
	eccentricity = ...
	initial_guess = ...
	root_finder = ...

	eccentric_anomaly = conversion.mean_to_eccentric_anomaly(
		eccentricity = eccentricity,
		mean_anomaly = mean_anomaly,
		use_default_initial_guess = False, #Optional; set to False to use optional user-defined initial guess
		non_default_initial_guess = initial_guess, #optional
		root_finder = root_finder #optional
		)

The above function can be used with only the eccentricity and mean anomaly inputs, in which case the defaults are used for the
initial guess and root finders.

Spherical-orbital Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^

The spherical elements are typically used to denote the conditions in atmospheric flight. In most applications, they will be used to denote the state in a body-fixed frame. The details of the physical meaning of the elements is discussed here. The element indices in Tudat are the following:

.. list-table:: Spherical-orbital Elements Indices.
	:widths: 50 50
	:header-rows: 1

	* - Column Indices
	  - Spherical-orbital Elements
	* - 0
	  - Radius
	* - 1
	  - Latitude
	* - 2
	  - Longitude
	* - 3
	  - Speed
	* - 4
	  - Flight Path Angle
	* - 5
	  - Heading Angle

The spherical elements consist of 6 entries, with no additional information required for the conversion to/from Cartesian elements. The conversion from Cartesian to spherical elements is performed as:

.. code-block:: python

	cartesian_state = ...

	spherical_state = conversion.cartesian_to_spherical( cartesian_state )

Similarly, the inverse operation is done as:

.. code-block:: python

	spherical_state = ...

	cartesian_state = conversion.spherical_to_cartesian( spherical_state )


Modified Equinoctial Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The modified equinoctial elements are typically used for orbits with eccentricities near 0 or 1 and/or inclinations near 0 or :math:`\pi`. The element indices in Tudat are the following:

.. list-table:: Modified Equinoctial Elements Indices.
	:widths: 50 50
	:header-rows: 1

	* - Column Indices
	  - Modified Equinoctial Elements
	* - 0
	  - Semi-parameter
	* - 1
	  - f-element
	* - 2
	  - g-element
	* - 3
	  - h-element
	* - 4
	  - k-element
	* - 5
	  - True Longitude

The modified equinoctial elements consists of 6 elements. The conversion to/from Cartesian elements requires the gravitational parameter of the body w.r.t. which the Modified Equinoctial elements are defined. The conversion from Cartesian elements is done using the :func:`~tudatpy.astro.element_conversion.cartesian_to_mee` function:

.. code-block:: python

	cartesian_state = ...
	central_body = ...
	central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

	modified_equinoctial_state = conversion.cartesian_to_mee( cartesian_state, central_body_gravitational_parameter )

The :func:`~tudatpy.astro.element_conversion.cartesian_to_mee` function computes the singularity-flipping element :math:`I` automatically using the :func:`~tudatpy.astro.element_conversion.flip_mee_singularity` function. Alternatively, the singularity-flipping element can be provided manually with the :func:`~tudatpy.astro.element_conversion.cartesian_to_mee_manual_singularity` function. 

Similarly, the inverse operation is done as:

.. code-block:: python

	modified_equinoctial_state = ...
	central_body = ...
	central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

	cartesian_state = conversion.mee_to_cartesian( modified_equinoctial_state, central_body_gravitational_parameter )


Unified State Model Elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Three different versions of the Unified State Model are present in Tudat. They differ based on the coordinates chosen to represent the rotation from local orbital to inertial frame, which can be expressed in quaternions (USM7), modified Rodrigues parameters (USM6) or exponential map (USMEM). The element indices are the following:

.. list-table:: Unified State Model indices with quaternions (USM7), modified Rodrigues parameters (USM6) or exponential map (USMEM).
	:widths: 25 25 25 25
	:header-rows: 1

	* - Column Indices
	  - USM7
	  - USM6
	  - USMEM
	* - 0
	  - C Hodograph
	  - C Hodograph
	  - C Hodograph
	* - 1
	  - Rf1 Hodograph
	  - Rf1 Hodograph
	  - Rf1 Hodograph
	* - 2
	  - Rf2 Hodograph
	  - Rf2 Hodograph
	  - Rf2 Hodograph
	* - 3
	  - :math:`\eta`
	  - :math:`\sigma_1`
	  - e1
	* - 4
	  - :math:`\epsilon_1`
	  - :math:`\sigma_2`
	  - e2
	* - 5
	  - :math:`\epsilon_2`
	  - :math:`\sigma_3`
	  - e3
	* - 6
	  - :math:`\epsilon_3`
	  - Shadow flag
	  - Shadow flag

Regardless of the rotational coordinates chosen, the Unified State Model elements consists of 7 elements. For each Unified State Model representation, conversion to and from Keplerian and Cartesian coordinates is implemented. As an example, the conversion from Keplerian elements for the USM7 elements is shown here:

.. code-block:: python

	keplerian_elements = ...
	central_body = ...
	central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

	unified_state_model_elements = conversion.keplerian_to_unified_state_model( keplerian_elements, central_body_gravitational_parameter )

Similarly, the inverse operation is done as:

.. code-block:: python

	unified_state_model_elements = ...
	central_body = ...
	central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

	keplerian_elements = conversion.unified_state_model_to_keplerian( keplerian_elements, central_body_gravitational_parameter )



Rotational
----------

In case you are also working with rotational motion, in Tudat the following representations for attitude/orientation are available:

- Quaternions.
- Modified Rodrigues parameters.
- Exponential map.

Transformation between these elements is done by passing through quaternions first (TODO: include link to rotational state propagation).
For rotational dynamics, the derivative can be expressed as either angular velocity, or time-derivative of the rotation matrix (see :ref:`above <frame_orientations>`).

Quaternions
^^^^^^^^^^^

As mentioned at the beginning of this chapter, quaternions are the default attitude representation in Tudat. Depending on the location in the Tudat framework, you will find a quaternion element expressed as either of the two types below:

**TODO-Dominic**

Modified Rodrigues Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the other two supported attitude representations is the modified Rodrigues parameters (MRPs). The indices for MRPs are defined as follows:

.. list-table:: Modified Rodrigues Parameters Indices.
   :widths: 50 50
   :header-rows: 1

   * - Column Indices
     - Modified Rodrigues Parameter
   * - 0
     - :math:`\sigma` 1
   * - 1
     - :math:`\sigma` 2
   * - 2
     - :math:`\sigma` 3
   * - 3
     - Shadow flag


Transformation to and from quaternions is achieved with the functions :func:`~tudatpy.astro.element_conversion.modified_rodrigues_parameters_to_quaternions` and :func:`~tudatpy.astro.element_conversion.quaternions_to_modified_rodrigues_parameters`, respectively, where the only input is the attitude element (in vector format).

.. note::

	The last index is the flag that triggers the shadow modified Rodrigues parameters (SMRPs). Its use is introduced to avoid the singularity at :math:`\pm 2 \pi` radians. If its value is 0, then the elements are MRPs, whereas if it is 1, then they are SMRPs. The use of SMRPs results in slightly different equations of motion and transformations. The switch between MRPs and SMRPs occurs whenever the magnitude of the rotation represented by the MRP vector is larger than :math:`\pi`.


Exponential Map
^^^^^^^^^^^^^^^

The final attitude representations is the exponential map (EM). The indices for EM are defined as follows:

.. list-table:: Exponential Map Indices.
	:widths: 50 50
	:header-rows: 1

	* - Column Indices
	  - Exponential Map
	* - 0
	  - e1
	* - 1
	  - e2
	* - 2
	  - e3
	* - 3
	  - Shadow flag

and transformation to and from quaternions is achieved with the aid of the functions :func:`~tudatpy.astro.element_conversion.exponential_map_to_quaternions` and :func:`~tudatpy.astro.element_conversion..quaternions_to_exponential_map`, respectively. Also for these equations the only input is the attitude element (in vector format).


.. note:: 

	Similarly to MRPs, the exponential map elements also make use of the shadow flag. In this case, this flag signals whether the shadow exponential map (SEM) is in use. This flag is also introduces to avoid the singularity at :math:`\pm 2 \pi` radians, but interestingly, there is no difference between the equations of motion and transformations in terms of EM or SEM. In fact, they are only introduced to make sure that when converting from EM to quaternions, the resulting quaternion sign history is continuous. The switch between EM and SEM occurs whenever the magnitude of the rotation represented by the EM vector is larger than :math:`\pi`.



=================

.. [Acton1996] Acton, (1996). Ancillary data services of NASA's Navigation and Ancillary Information Facility.
   Planetary and Space Science, Volume 44, Issue 1, https://doi.org/10.1016/0032-0633(95)00107-7.
