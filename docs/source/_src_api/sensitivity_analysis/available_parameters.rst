
.. _parameterSettingCreation:

==============================
Available Estimated Parameters
==============================

The framework discussed in the previous section explains how the :literal:`parameter_settings` list is populated. The goal of this section is to list the available parameters that can be estimated, what syntax they use, and explain to which environment models they are linked.

.. class:: Single Parameters

- :literal:`gravitational_parameter`
	
	Gravitational parameter of a body, linked to a :class:`GravityFieldModel` object, which may be a point-mass or (time-dependent) spherical harmonic field. Parameter size: 1. Secondary identifer: None.
	
	.. code-block:: python

		estimation_setup.parameter.gravitational_parameter( "Earth" )

- :literal:`constant_drag_coefficient`

	Drag coefficient of a body that is constant, linked to a :class:`CustomAerodynamicCoefficientInterface` object derived from :class:`AerodynamicCoefficientInterface`, which must have 0 independent variables for the coefficients. Parameter size: 1. Secondary identifer: None.
	
	.. code-block:: python

		estimation_setup.parameter.constant_drag_coefficient( "Spacecraft" )
	
- :literal:`constant_rotation_rate`

	Rotation rate of a body around a fixed axis, linked to a :class:`SimpleRotationalEphemeris` object derived from :class:`RotationalEphemeris`. Parameter size: 1. Secondary identifer: None.
	
	.. code-block:: python

		estimation_setup.parameter.constant_rotation_rate( "Earth" )
	
- :literal:`radiation_pressure_coefficient`

	Constant radiation pressure coefficient of a body, linked to a :class:`RadiationPressureInterface` object. Parameter size: 1. Secondary identifer: None.
	
	.. code-block:: python

		estimation_setup.parameter.radiation_pressure_coefficient( "Spacecraft" )

- :literal:`rotation_pole_position`

	Fixed rotation axis about which a body rotates with a fixed rotation rate, linked to a :class:`SimpleRotationalEphemeris` object. Parameter size: 2 (denoting pole right ascension and declination). Secondary identifer: None.
	
	.. code-block:: python

		estimation_setup.parameter.rotation_pole_position( "Earth" )

- :literal:`ground_station_position`
	
	Fixed body-fixed position of a ground station on a body, linked to a :class:`GroundStationState` object (requires a :class:`GroundStationState` class). Parameter size: 3 (denoting body-fixed *x*, *y* and *z* Cartesian position). Secondary identifer: Ground station name.
	
	.. code-block:: python

		estimation_setup.parameter.ground_station_position( "GroundStation" )

- :literal:`ppn_parameter_gamma`
	
	Parameter :math:`\gamma` used in Parametric Post-Newtonian (PPN) framework, linked to a :class:`PPNParameterSet` object (nominally the global :literal:`relativity::ppnParameterSet` variable). Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifer: None.

- :literal:`ppn_parameter_beta`
	
	Parameter :math:`\beta` used in Parametric Post-Newtonian (PPN) framework, linked to a :class:`PPNParameterSet` object (nominally the global :literal:`relativity::ppnParameterSet` variable). Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifer: None.

- :literal:`equivalence_principle_lpi_violation_parameter`

	Parameter used to compute influence of a gravitational potential on proper time rate, equals 0 in general relativity, not linked to any object, but instead the :literal:`equivalencePrincipleLpiViolationParameter` global variable (in namespace :literal:`relativity`. Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifer: None.


.. class:: Initial State Parameters

.. warning::
	These functions return **lists** of estimated parameters, which means that they can not be simply added in a list creation statement like ``[parameter_1, parameter_2, ...]``. Instead, this list needs to be concatenated to a list of 'simple' parameters, e.g. by using the ``+`` operator: ``parameter_settings + estimation_setup.parameter.initial_states(...)``.
	
The factory function for initial states uses the propagator settings to determine which type is needed, e.g. if a translational propagator is defined, the function will automatically create the parameters for initial translational state.
	
- :literal:`initial_translational_state`

- :literal:`initial_translational_state_from_ephemeris`

- :literal:`arc_wise_initial_translational_state`

- :literal:`arc_wise_initial_translational_state_from_ephemeris`

- :literal:`initial_rotational_state`
		
.. code-block:: python

	estimation_setup.parameter.initial_states( propagator_settings, bodies )

         
.. class:: Spherical Harmonic Parameters

- :literal:`spherical_harmonics_c_coefficients`

	Estimates the **cosine** coefficients in the spherical harmonics gravity model for a body. There are two ways to specify which coefficients are to be estimated: using min/max settings for degree and order, or using block indices. The latter constitutes a list of tuples, where the first value is the degree and the second the order of the coefficient to be estimated. The length of this list can be arbitrary, as long as the pairs are unique.

	.. code-block:: python

		estimation_setup.parameter.spherical_harmonics_c_coefficients( 
			"Earth", minimum_degree, minimum_order, maximum_degree,
			maximum_order )
		
	.. code-block:: python
	
		block_indices = [(1, 1), (2, 2), (3, 3)]
		estimation_setup.parameter.spherical_harmonics_c_coefficients(
			"Earth", block_indices )
		
- :literal:`spherical_harmonics_s_coefficients`

	
	Estimates the **sine** coefficients in the spherical harmonics gravity model for a body. There are two ways to specify which coefficients are to be estimated: using min/max settings for degree and order, or using block indices:

	.. code-block:: python

		estimation_setup.parameter.spherical_harmonics_s_coefficients( 
			"Earth", minimum_degree, minimum_order, maximum_degree,
			maximum_order )
			
	.. code-block:: python
	
		block_indices = [(1, 1), (2, 2), (3, 3)]
		estimation_setup.parameter.spherical_harmonics_s_coefficients(
			"Earth", block_indices )

   
         
.. class:: Tidal Love Number Parameters

- :literal:`full_degree_tidal_love_number`

- :literal:`single_degree_variable_tidal_love_number`

.. class:: Constant Observation Bias Parameters

- :literal:`constant_additive_observation_bias`

- :literal:`arc_wise_constant_additive_observation_bias`

- :literal:`constant_relative_observation_bias`

- :literal:`arc_wise_constant_relative_observation_bias`

.. class:: Empirical Acceleration Parameters

- :literal:`constant_empirical_acceleration_terms`

	.. code-block:: python
	
		estimation_setup.parameter.constant_empirical_acceleration_terms( body, central_body )
	

- :literal:`empirical_acceleration_coefficients`

- :literal:`arc_wise_empirical_acceleration_coefficients`
   
