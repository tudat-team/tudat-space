
.. _parameterSettingCreation:

====================
Available Parameters
====================

The framework discussed in the previous section explains how the :literal:`parameter_settings` list is populated. The goal of this section is to list the available parameters that can be used in the variational equations (and which are therefore available for estimation in a state estimation problem), what syntax they use, and explain to which environment models they are linked.

-----------------
Single Parameters
-----------------

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.gravitational_parameter`: Gravitational parameter of a body, linked to a :class:`GravityFieldModel` object, which may be a point-mass or (time-dependent) spherical harmonic field. Parameter size: 1. Secondary identifier: None.

  .. code-block:: python

  	estimation_setup.parameter.gravitational_parameter( "Earth" )

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.constant_drag_coefficient`: Drag coefficient of a body that is constant, linked to a :class:`CustomAerodynamicCoefficientInterface` object derived from :class:`AerodynamicCoefficientInterface`, which must have 0 independent variables for the coefficients. Parameter size: 1. Secondary identifier: None.

  .. code-block:: python

    estimation_setup.parameter.constant_drag_coefficient( "Spacecraft" )
	
- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.constant_rotation_rate`: Rotation rate of a body around a fixed axis, linked to a :class:`SimpleRotationalEphemeris` object derived from :class:`RotationalEphemeris`. Parameter size: 1. Secondary identifier: None.

  .. code-block:: python

    estimation_setup.parameter.constant_rotation_rate( "Earth" )
	
- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.radiation_pressure_coefficient`: Constant radiation pressure coefficient of a body, linked to a :class:`RadiationPressureInterface` object. Parameter size: 1. Secondary identifier: None.
	
  .. code-block:: python

    estimation_setup.parameter.radiation_pressure_coefficient( "Spacecraft" )

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.rotation_pole_position`: Fixed rotation axis about which a body rotates with a fixed rotation rate, linked to a :class:`SimpleRotationalEphemeris` object. Parameter size: 2 (denoting pole right ascension and declination). Secondary identifier: None.
	
  .. code-block:: python

    estimation_setup.parameter.rotation_pole_position( "Earth" )

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.ground_station_position`: Fixed body-fixed position of a ground station on a body, linked to a :class:`GroundStationState` object (requires a :class:`GroundStationState` class). Parameter size: 3 (denoting body-fixed *x*, *y* and *z* Cartesian position). Secondary identifier: Ground station name.
	
  .. code-block:: python

    estimation_setup.parameter.ground_station_position( "GroundStation" )

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.ppn_parameter_gamma`: Parameter :math:`\gamma` used in Parametric Post-Newtonian (PPN) framework, linked to a :class:`PPNParameterSet` object (nominally the global :literal:`relativity::ppnParameterSet` variable). Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifier: None.

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.ppn_parameter_beta`: Parameter :math:`\beta` used in Parametric Post-Newtonian (PPN) framework, linked to a :class:`PPNParameterSet` object (nominally the global :literal:`relativity::ppnParameterSet` variable). Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifier: None.

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.equivalence_principle_lpi_violation_parameter`: Parameter used to compute influence of a gravitational potential on proper time rate, equals 0 in general relativity, not linked to any object, but instead the :literal:`equivalencePrincipleLpiViolationParameter` global variable (in namespace :literal:`relativity`). Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifier: None.


------------------------
Initial State Parameters
------------------------

.. warning::
	These functions return **lists** of parameters, which means that they can not be simply added in a list creation statement like ``[parameter_1, parameter_2, ...]``. Instead, this list needs to be concatenated to a list of 'simple' parameters, e.g. by using the ``+`` operator: ``parameter_settings + estimation_setup.parameter.initial_states(...)``.
	
The factory function for initial states uses the propagator settings to determine which type is needed, e.g. if a translational propagator is defined, the function will automatically create the parameters for initial translational state.
	
- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.initial_translational_state`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.initial_translational_state_from_ephemeris`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.arc_wise_initial_translational_state`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.arc_wise_initial_translational_state_from_ephemeris`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.initial_rotational_state`
		
.. code-block:: python

	estimation_setup.parameter.initial_states( propagator_settings, bodies )

         
-----------------------------
Spherical Harmonic Parameters
-----------------------------

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.spherical_harmonics_c_coefficients`: Considers the **cosine** coefficients in the spherical harmonics gravity model for a body. There are two ways to specify which coefficients are to be used: giving min/max settings for degree and order, or giving block indices. The latter constitutes a list of tuples, where the first value is the degree and the second the order of the coefficient to be used. The length of this list can be arbitrary, as long as the pairs are unique.

  .. code-block:: python

    estimation_setup.parameter.spherical_harmonics_c_coefficients( 
    	"Earth", minimum_degree, minimum_order, maximum_degree,
    	maximum_order )
  	
  .. code-block:: python

    block_indices = [(1, 1), (2, 2), (3, 3)]
    estimation_setup.parameter.spherical_harmonics_c_coefficients(
    	"Earth", block_indices )
		
- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.spherical_harmonics_s_coefficients`: Considers the **sine** coefficients in the spherical harmonics gravity model for a body. There are two ways to specify which coefficients are to be used: giving min/max settings for degree and order, or giving block indices:

  .. code-block:: python

    estimation_setup.parameter.spherical_harmonics_s_coefficients( 
    	"Earth", minimum_degree, minimum_order, maximum_degree,
    	maximum_order )
		
  .. code-block:: python

    block_indices = [(1, 1), (2, 2), (3, 3)]
    estimation_setup.parameter.spherical_harmonics_s_coefficients(
    	"Earth", block_indices )

   
----------------------------
Tidal Love Number Parameters
----------------------------

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.full_degree_tidal_love_number`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.single_degree_variable_tidal_love_number`

------------------------------------
Constant Observation Bias Parameters
------------------------------------

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.constant_additive_observation_bias`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.arc_wise_constant_additive_observation_bias`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.constant_relative_observation_bias`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.arc_wise_constant_relative_observation_bias`

------------------------------------
Empirical Acceleration Parameters
------------------------------------

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.constant_empirical_acceleration_terms`

  .. code-block:: python

    estimation_setup.parameter.constant_empirical_acceleration_terms( body, central_body )
	

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.empirical_acceleration_coefficients`

- :func:`~tudatpy.numerical_simulation.estimation_setup.parameter.arc_wise_empirical_acceleration_coefficients`
   
