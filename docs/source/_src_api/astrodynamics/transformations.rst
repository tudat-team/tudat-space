===========================
Frame/State Transformations
===========================

State Type Conversions
######################

Depending on your application, you will be using any of a number of translational state (position and velocity) representations. In Tudat, conversions involving the following state representations are available:

- Cartesian elements.
- Keplerian elements.
- Spherical-orbital elements.
- Modified Equinoctial elements.
- Unified State Model elements.

For each of these element types, conversions to/from Cartesian elements are available. Converting between two element types, where neither is Cartesian, will typically involve first transforming to Cartesian elements, and then transforming to your output state type.

In case you are also working with rotational motion, in Tudat the following representations for attitude are available:

- Quaternions.
- Modified Rodrigues parameters.
- Exponential map.

Transformation between these elements is done by passing through quaternions first. In fact, this is the default attitude representation in Tudat. Conversion in ``tudatpy`` requires this import statement:

.. code-block:: python
	
        from tudatpy.kernel.astro import element_conversion

.. class:: Kepler Elements

	The Kepler elements are the standard orbital elements used in classical celestial mechanics, with the element indices shown above. Converting to/from Cartesian state requires an additional piece of information in addition to the state itself: the gravitational parameter of the body w.r.t. the Keplerian elements are defined. The physical meaning of each of the elements is

	.. list-table:: Kepler Elements Indices.
	     :widths: 50 50
	     :header-rows: 1

	     * - Column Indices
	       - Kepler Elements
	     * - 0
	       - Semi-major Axis
	     * - 1
	       - Eccentricity
	     * - 2
	       - Inclination
	     * - 3
	       - Argument of Periapsis
	     * - 4
	       - Right Ascension of the Ascending Node
	     * - 5
	       - True Anomaly
	     * - 0
	       - Semi-latus Rectum

    In this table of the Keplerian Element indices, you can see something peculiar: both the Semi-major Axis index and Semi-latus Rectum index are defined as index 0. The latter option is only applicable when the orbit is parabolic (when the eccentricity is 1.0). That is, if the orbit is parabolic, element 0 does not represent the semi-major axis (as it is not defined) but the semi-latus rectum.


	Conversion to/from Cartesian elements is done as

	.. code-block:: python

		cartesian_state = ...
		central_body = ...
		central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

		keplerian_state = conversion.cartesian_to_keplerian( cartesian_state, central_body_gravitational_parameter )

	Similarly, the inverse operation is done as:

	.. code-block:: python

		keplerian_state = ...
		central_body = ...
		central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

		cartesian_state = conversion.keplerian_to_cartesian( keplerian_state, central_body_gravitational_parameter )



	In the definition of the state elements, you will notice that element 5 is the *true* anomaly, not the *eccentric* or *mean* anomaly. Tudat also contains functions to convert to these alternative anomalies. Converting between true and eccentric anomaly is done as follows:

	.. code-block:: python

		true_anomaly = ...
		eccentricity = ...

		eccentric_anomaly = conversion.true_anomaly_to_eccentric_anomaly( true_anomaly, eccentricity )

	or directly from the orbital elements:

	.. code-block:: python

		keplerian_state = ...

		eccentric_anomaly = conversion.true_anomaly_to_eccentric_anomaly( keplerian_state( true_anomaly_index ), keplerian_state( eccentricity_index ) )


	Note that this function automatically identifies whether the orbit is elliptical or hyperbolic, and computes the associated eccentric anomaly. The function for the inverse operation is ``eccentric_anomaly_to_true_anomaly``. Similarly, Tudat contains functions to convert from eccentric to mean anomaly (automatically checking whether the orbit is elliptical or hyperbolic):

	.. code-block:: python

		true_anomaly = ...
		eccentricity = ...

		eccentric_anomaly = conversion.true_anomaly_to_eccentric_anomaly( true_anomaly, eccentricity )
		mean_anomaly = conversion.eccentric_anomaly_to_mean_anomaly( eccentric_anomaly, eccentricity )

	The inverse operation, mean to eccentric anomaly, is done separately for hyperbolic and elliptical orbits, through the functions ``mean_anomaly_to_eccentric_anomaly`` for elliptical and ``_mean_anomaly_to_hyperbolic_eccentric_anomaly`` for hyperbolic orbits. In general, you will use them as follows:

	.. code-block:: python

		mean_anomaly = ...
		eccentricity = ...

		eccentric_anomaly = conversion.mean_anomaly_to_eccentric_anomaly( eccentricity, mean_anomaly )

	However, this conversion involves the solution of an implicit algebraic equation, for which a root finder is used. Root finders are discussed in more detail here. When calling the function as in the above example, a root finder is created internally. However, in some cases you may want to specify your own root finder, as well as a first initial guess for the eccentric anomaly (which the root finder uses at its first iteration). When doing so, you create a root finder object and pass it to the conversion function as follows:

	.. code_block:: python

		mean_anomaly = ...
		eccentricity = ...
		initial_guess = ...
		root_finder = ...

		eccentric_anomaly = conversion.mean_anomaly_to_eccentric_anomaly( eccentricity, mean_anomaly, False, initial_guess, root_finder )

	where the argument ``False`` indicates that the user-specified initial guess is to be used. If you want to use a custom-defined root finder, but not an initial guess, use the following:

	.. code_block:: python

		mean_anomaly = ...
		eccentricity = ...
		root_finder = ...

		eccentric_anomaly = conversion.mean_anomaly_to_eccentric_anomaly( eccentricity, mean_anomaly, True, root_finder )


.. class:: Spherical-orbital Elements

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

.. class:: Modified Equinoctial Elements
	
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

	The modified equinoctial elements consists of 6 elements. The conversion to/from Cartesian elements requires the gravitation parameter of the body w.r.t. which the Modified Equinoctial elements are defined. Furthermore, a ``bool`` is used to indicate whether the singularity of this element set occurs for inclinations of 0 or :math:`\pi`. The conversion from Cartesian elements is done as:

	.. code-block:: python

		cartesian_state = ...
		central_body = ...
		central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

		modified_equinoctial_state = conversion.cartesian_to_modified_equinoctial( cartesian_state, central_body_gravitational_parameter, flip_singularity_to_zero_inclination )

	.. note:: 
		The input ``flip_singularity_to_zero_inlination`` is optional for this conversion. If left empty, an overloaded function will determine whether this value is true or false based on the inclination of the orbit.

	Similarly, the inverse operation is done as:

	.. code-block:: python

		modified_equinoctial_state = ...
		central_body = ...
		central_body_gravitational_parameter = bodies.get( central_body ).gravitational_parameter

		cartesian_state = conversion.modified_equinoctial_to_cartesian( modified_equinoctial_state, central_body_gravitational_parameter, flip_singularity_to_zero_inclination )
		


.. class:: Unified State Model Elements

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
		   - :math:`\sigma` 1
		   - e1
		 * - 4
		   - :math:`\epsilon` 1
		   - :math:`\sigma` 2
		   - e2
		 * - 5
		   - :math:`\epsilon` 2
		   - :math:`\sigma` 3
		   - e3
		 * - 6
		   - :math:`\epsilon` 3
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

.. class:: Quaternions

	As mentioned at the beginning of this chapter, quaternions are the default attitude representation in Tudat. Depending on the location in the Tudat framework, you will find a quaternion element expressed as either of the two types below:

	**TODO-Dominic**

.. class:: Modified Rodrigues Parameters

	One of the other two supported attitude representations is the modified Rodrigues parameters (MRPs). The indeces for MRPs are defined as follows:

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


	Transformation to and from quaternions is achieved with the functions ``conversion.modified_rodrigues_parameters_to_quaternions`` and ``conversion.quaterns_to_modified_rodrigues_parameter_elements``, respectively, where the only input is the attitude element (in vector format).

	.. note::

		The last index is the flag that triggers the shadow modifed Rodrigues parameters (SMRPs). Its use is introduced to avoid the singularity at :math:`\pm 2 \pi` radians. If its value is 0, then the elements are MRPs, whereas if it is 1, then they are SMRPs. The use of SMRPs results in slightly different equations of motion and transformations. The switch between MRPs and SMRPs occurs whenever the magnitude of the rotation represented by the MRP vector is larger than :math:`\pi`.


.. class:: Exponential Map

	The final attitude representations is the exponential map (EM). The indeces for EM are defined as follows:

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

	and transformation to and from quaternions is achieved with the aid of the functions ``conversion.exponential_map_to_quaternions`` and ``conversions.quaternions_to_exponential_map``, respectively. Also for these equations the only input is the attitude element (in vector format).


	.. note:: 

		Similarly to MRPs, the exponential map elements also make use of the shadow flag. In this case, this flag signals whether the shadow exponential map (SEM) is in use. This flag is also introduces to avoid the singularity at :math:`\pm 2 \pi` radians, but interestingly, there is no difference between the equations of motion and transformations in terms of EM or SEM. In fact, they are only introduced to make sure that when converting from EM to quaternions, the resulting quaternion sign history is continuous. The switch between EM and SEM occurs whenever the magnitude of the rotation represented by the EM vector is larger than :math:`\pi`.


Frame Transformations
######################

Every state, regardless of its representation is expressed with a particular origin and orientation. This is most easy to understand for Cartesian elements, where the origin represents the (0,0,0) position, and the orientation defines the direction of the x-, y- and z-axes. Below, we discuss how to perform these operations in Tudat.

Transformations in ``tudatpy`` requires this import statement:

.. code-block:: python
	
        from tudatpy.kernel.astro import frame_conversion


.. warning::
	
	Do not use the ``get_current_state`` or ``get_current_rotation`` function in the body objects! These functions are used during numerical propagation, and calling them outside of the numerical propagation will generally not lead to meaningful results.

.. class:: Frame Translations

	To change the origin of a Cartesian, one can simply add a Cartesian state that represents the difference between the original and the new origin. For instance, when transforming a vector (state of a vehicle) from Earth-centered to Moon-centered (keeping the orientation constant):

	.. code-block:: python

		vehicle_cartesian_state_in_earth_centered_frame = ...
		moon_cartesian_state_in_earth_centered_frame = ...

		vehicle_cartesian_state_in_moon_centered_frame = vehicle_cartesian_state_in_earth_centered_frame + moon_cartesian_state_in_earth_centered_frame

	The challenge here, of course, is determining the ``moon_cartesian_state_in_earth_centered_frame`` vector. We provide a few ways in which to achieve this. When performing a numerical simulation using a set of body objects, you can use the following (assuming that ``bodiesz`` contains both an ``"Earth"`` and ``"Moon"`` entry):

	.. code-block:: python

		bodies = ...
		current_time = ...

                moon_cartesian_state_in_earth_centered_frame = bodies.at( "Moon" ).state_in_base_frame_from_ephemeris( current_time ) - bodies.at( "Earth" ).state_in_base_frame_from_ephemeris( current_time )

	You can also bypass the body map altogether, and use ``spice`` to obtain the relative state. Note, however, that this will use whichever ``spice`` kernels you have loaded, and may not be consistent with the states you are using the bodies in your simulation.

	.. code-block:: python

		current_time = ...
		frame_orientation = "J2000"

		moon_cartesian_state_in_earth_centered_frame = spice_interface.get_body_cartesian_state_at_epoch(
				target_body_name="Moon"
			observer_body_name="Earth",
			reference_frame_name=frame_orientation,
			aberration_corrections="NONE",
			ephemeris_time=current_time
		)

	where the ``"NONE"`` arguments indicates that no light-time corrections are used, and the frame orientation denotes the orientation of the frame in which the relative state is returned.

.. class:: Frame Rotations

	Rotating the frame in which a Cartesian state is expressed requires two pieces of information:

	1. The rotation matrix from one frame to the other
	2. The first time derivative of the rotation matrix from one frame to the other

	Manually, the state may then be transformed as:

	.. code-block:: python

		rotation_to_frame = ... # 3D Matrix
		time_derivative_of_rotation_to_frame  = ... # 3D Matrix
		original_state = ... # 6D Vector

		rotated_state = np.zeros(6, dtype=float);
		rotated_state[ :3 ] = rotation_to_frame * original_state[ :3 ];
		rotated_state[ 3: ] = rotation_to_frame * original_state[ 3: ] + time_derivative_of_rotation_to_frame * original_state[ :3 ];

	In many cases, however, your frame rotation will be from the inertial frame to a body-fixed frame. All information required for this is stored in the rotational ephemeris objects. This object contains a base (inertial) and target (body-fixed) frame and defines the rotation between the two. Assuming that you are using a body map to store your environment, you can transform the state from an inertial to a body-fixed frame as follows, for the example of transforming a vehicle’s Cartesian state from an inertial to the body-fixed frame of the Earth:

	.. code-block:: python

		bodies = ...
		current_time = ...
		inertial_state = ...

                body_fixed_state = environment.transform_to_inertial_orientation( inertial_state, current_time, bodies.at( "Earth" ).rotational_ephemeris( ) )

	The inverse is done as follows:

	.. code-block:: python

		bodies = ...
		current_time = ...
		body_fixed_state = ...

                inertial_state = environment.transform_to_inertial_orientation( body_fixed_state, current_time, bodies.at( "Earth" ).rotational_ephemeris( ) )

