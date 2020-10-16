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
	
	from tudatpy.kernel.astro import conversion

.. class:: Kepler Elements

	The Kepler elements are the standard orbital elements used in classical celestial mechanics, with the element indices shown above. Converting to/from Cartesian state requires an additional piece of information in addition to the state itself: the gravitational parameter of the body w.r.t. the Keplerian elements are defined. The physical meaning of each of the elements is

	.. list-table:: Kepler Elements Indices
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
		central_body_gravitational_parameter = bodies.get_body( central_body ).gravitational_parameter

		keplerian_state = conversion.cartesian_to_keplerian( cartesian_state, central_body_gravitational_parameter )

	Similarly, the inverse operation is done as:

	.. code-bock:: python

		keplerian_state = ...
		central_body = ...
		central_body_gravitational_parameter = bodies.get_body( central_body ).gravitational_parameter

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

	.. list-table:: Spherical-orbital Elements Indices
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

	.. list-table:: Modified Equinoctial Elements Indices
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
		central_body_gravitational_parameter = bodies.get_body( central_body ).gravitational_parameter

		modified_equinoctial_state = conversion.cartesian_to_modified_equinoctial( cartesian_state, central_body_gravitational_parameter, flip_singularity_to_zero_inclination )

	.. note:: 
		The input ``flip_singularity_to_zero_inlination`` is optional for this conversion. If left empty, an overloaded function will determine whether this value is true or false based on the inclination of the orbit.

	Similarly, the inverse operation is done as:

	.. code-block:: python

		modified_equinoctial_state = ...
		central_body = ...
		central_body_gravitational_parameter = bodies.get_body( central_body ).gravitational_parameter

		cartesian_state = conversion.modified_equinoctial_to_cartesian( modified_equinoctial_state, central_body_gravitational_parameter, flip_singularity_to_zero_inclination )
		