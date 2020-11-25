===============================
Setting Up Estimated Parameters
===============================

.. _parameterArchitecture:

Parameter Architecture
######################

The parameter estimation framework of Tudat allows an ever increasing variety of parameters to be estimated, these parameters may be:

* Properties of a body, such as a gravitational parameter :math:`\mu`
* Properties of a ground station, such as its body-fixed position :math:`\mathbf{x}_{GS}^{(B)}`
* Global properties of the simulation, such a Parameterize Post_Newtonian (PPN) parameters :math:`\gamma` and :math:`\beta`
* Acceleration model properties, such as empirical acceleration magnitudes
* Observation model properties, such as absolute and relative observation biases

In Tudat, these parameters influence the simulation in a variety of manners, and during propagation and/or observation simulation, information of this parameter is transferred in manner different ways. To provide a unified framework for estimating any type of parameter, the :class:`EstimatableParameter` class has been set up. 

.. class:: EstimatableParameter

   This class has interfaces to retrieve and reset parameters, providing a single interface for modifying/obtaining any of the parameters that Tudat supports. For each estimated parameter, there is a dedicated derived class of :class:`EstimatableParameter`. 

.. class:: EstimatableParameterSet

   The full list of estimated parameters is stored in an object of type :class:`EstimatableParameterSet`. This class is templated by the state scalar type of the estimated initial state parameters. 

.. note::
   For the remainder of this page, we will implicitly assume that the template argument of an :class:`EstimatableParameterSet` object is double, unless explicitly mentioned otherwise.

As is the case for acceleration models, integration models, environment models, *etc.*, the parameter objects are created by defining settings for them, and subsequently calling the associated factory function. The settings and passed by creating objects of type :class:`EstimatableParameterSettings` (or one of its derived classes). Some parameters settings are provided through the :class:`EstimatableParameterSettings` base class, and some through its derived classes. A full list is provided in the section on :ref:`parameterSettingCreation`. An example of the creation of the parameter objects is given below:

   .. code-block:: cpp

       // Define parameter settings
       std::vector< std::shared_ptr< EstimatableParameterSettings > > parameterNames;
       parameterNames.push_back( std::make_shared< EstimatableParameterSettings >( 
          "Vehicle", radiation_pressure_coefficient ) );
       parameterNames.push_back( std::make_shared< EstimatableParameterSettings >( 
          "Vehicle", constant_drag_coefficient ) );
       parameterNames.push_back(  std::make_shared< EstimatableParameterSettings >(
          "Earth", rotation_pole_position ) );
          
       // Define parameter objects   
       std::shared_ptr< EstimatableParameterSet< double > > parametersToEstimate =
            createParametersToEstimate( parameterNames, bodyMap );
         
Which creates parameter objects for the radiation pressure coefficient and drag coefficient of body "Vehicle", and the orientation of the rotation axis of the body "Earth".

The :class:`EstimatableParameterSet` object contains three objects that have :class:`EstimatableParameter` as base class (one for each parameter). We distinguish two types of :class:`EstimatableParameter` objects:

* Those that represent initial conditions for dynamics (denoted as :math:`\mathbf{x}_{0}` below)
* Those that represent fixed parameters for environment, acceleration or observation models (denoted as :math:`\mathbf{q}` below)

Resetting the full parameter vector :math:`\mathbf{p}(=[\mathbf{x}_{0};\mathbf{q}])` is done as follows (for :literal:`double` state scalar type):
         
   .. code-block:: cpp

       // Create parameter set  
       std::shared_ptr< EstimatableParameterSet< double > > parametersToEstimate = ...
       
       Eigen::VectorXd parameterVector =
            parametersToEstimate->getFullParameterValues< double >( );

While resetting the full parameter vector is done as:

   .. code-block:: cpp

       // Create parameter set  
       std::shared_ptr< EstimatableParameterSet< double > > parametersToEstimate = ...
       
       // Define vector of new values of estimated parameters
       Eigen::VectorXd newParameterVector = ...
       
       // Reset parameter values
       parametersToEstimate->resetParameterValues< double >( );

When resetting the parameter vector, the change in the values in :math:`\mathbf{q}` immediately take effect. For the initial state parameters to take effect, however, the dynamics must be re-propagated. This occurs automatically when estimating parameters. It can also be performed manually by calling the :literal:`resetParameterEstimate` member function of the :class:`VariationalEquationsSolver` class. 

.. _parameterSettingCreation:

Available Estimated Parameters
#############################

The framework discussed in the previous section explains how the :literal:`parameterNames` is populated. The goal of this section is to list the available parameters that can be estimated, and which environment models they are linked to.

.. class:: Single Parameters (NAME!)

- :literal:`gravitational_parameter`
	
	Gravitational parameter of a body, linked to a :class:`GravityFieldModel` object, which may be a point-mass or (time-dependent) spherical harmonic field. Parameter size: 1. Secondary identifer: None.

- :literal:`constant_drag_coefficient`

	Drag coefficient of a body that is constant, linked to a :class:`CustomAerodynamicCoefficientInterface` object derived from :class:`AerodynamicCoefficientInterface`, which must have 0 independent variables for the coefficients. Parameter size: 1. Secondary identifer: None.
	
- :literal:`constant_rotation_rate`

	Rotation rate of a body around a fixed axis, linked to a :class:`SimpleRotationalEphemeris` object derived from :class:`RotationalEphemeris`. Parameter size: 1. Secondary identifer: None.
	
- :literal:`radiation_pressure_coefficient`

	Constant radiation pressure coefficient of a body, linked to a :class:`RadiationPressureInterface` object. Parameter size: 1. Secondary identifer: None.

- :literal:`rotation_pole_position`

	Fixed rotation axis about which a body rotates with a fixed rotation rate, linked to a :class:`SimpleRotationalEphemeris` object. Parameter size: 2 (denoting pole right ascension and declination). Secondary identifer: None.

- :literal:`ground_station_position`
	
	Fixed body-fixed position of a ground station on a body, linked to a :class:`GroundStationState` object (requires a :class:`GroundStationState` class). Parameter size: 3 (denoting body-fixed *x*, *y* and *z* Cartesian position). Secondary identifer: Ground station name.

- :literal:`ppn_parameter_gamma`
	
	Parameter :math:`\gamma` used in Parametric Post-Newtonian (PPN) framework, linked to a :class:`PPNParameterSet` object (nominally the global :literal:`relativity::ppnParameterSet` variable). Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifer: None.

- :literal:`ppn_parameter_beta`
	
	Parameter :math:`\beta` used in Parametric Post-Newtonian (PPN) framework, linked to a :class:`PPNParameterSet` object (nominally the global :literal:`relativity::ppnParameterSet` variable). Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifer: None.

- :literal:`equivalence_principle_lpi_violation_parameter`

	Parameter used to compute influence of a gravitational potential on proper time rate, equals 0 in general relativity, not linked to any object, but instead the :literal:`equivalencePrincipleLpiViolationParameter` global variable (in namespace :literal:`relativity`. Parameter size: 1. Note that the name of the associated body should be :literal:`"global_metric"`. Secondary identifer: None.


.. class:: Initial State Parameters

- :literal:`initial_translational_state`

- :literal:`initial_translational_state_from_ephemeris`

- :literal:`arc_wise_initial_translational_state`

- :literal:`arc_wise_initial_translational_state_from_ephemeris`

- :literal:`initial_rotational_state`

         
.. class:: Spherical Harmonic Parameters

- :literal:`spherical_harmonic_block`

- :literal:`spherical_harmonic_full_set`
   
         
.. class:: Tidal Love Number Parameters

- :literal:`full_degree_tidal_love_number`

- :literal:`single_degree_variable_tidal_love_number`

.. class:: Constant Observation Bias Parameters

- :literal:`constant_additive_observation_bias`

- :literal:`arc_wise_constant_additive_observation_bias`

- :literal:`constant_relative_observation_bias`

- :literal:`arc_wise_constant_relative_observation_bias`

.. class:: Empirical Acceleration Parameters

- :literal:`empirical_acceleration_coefficients`

- :literal:`arc_wise_empirical_acceleration_coefficients`
   
