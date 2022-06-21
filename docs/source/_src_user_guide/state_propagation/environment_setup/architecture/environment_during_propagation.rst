.. _environment_during_propagation:

===================================================
Interacting with the environment during propagation
===================================================

Each body object and its constituent members is updated to the current state and time automatically during the numerical propagation. We stress that only those objects that are relevant for a given propagation are updated every time step. See :ref:`single_propagation_evaluation` for a more detailed discussion on what happens during a function evaluation of the state derivative model.

Even though the environment is updated automatically, in various cases a user has control over *how* it gets updated. This is the case when using any of the :ref:`custom models <custom_models>` in Tudat. Typical examples of such models are aerodynamic guidance, or thrust guidance. When defining such custom models, you will in many cases need to access the properties of bodies in the environment to perform your calculations. This page lists how to access such properties, and how to use/interpret them (if relevant). Some examples are:

* Retrieving the translational state of a spacecraft w.r.t. a central body to calculate its thrust direction  
* Retrieving the current atmospheric density during entry to calculate the required vehicle orientation
* Retrieving properties that cannot be saved as a dependent variable to calculate a custom dependent variable (note - this option does not influence the propagation results, but can be used to obtain more flexible output, see :function:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.custom_dependent_variable`)
* ...

Below, we list how to retrieve the relevant information of the current properties of a Body in Tudat. Note that these can *only* be used during a propagation, and therefore are only relevant when setting up custom models. Retrieving properties of bodies outside of a propagation requires a different workflow (see :ref:`TODO`, as the various models are then not automatically updated.) 

..
  Some (time-dependent properties) of a body are set in the environment models themselves (e.g. . Others are updated and stored directly in the Body object. Below is a full list of (possibly) time varying environment models, and how to retrieve them from a body object during propagation.

In what follows below, we will assume that you have created a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` variable named ``bodies``, from which you want to access various properties during the propagation. 

.. _translational_state_during_propagation:

Translational state
-------------------

    Retrieved directly from the :class:`~tudatpy.numerical_simulation.environment.Body` object with the :attr:`~tudatpy.numerical_simulation.environment.Body.state` function in Cartesian elements. Note that this state is always w.r.t. the global frame origin and orientation (see :ref:`translational state reference frames<translational_reference_frames>`). To retrieve the state of one body w.r.t. the other, if neither body is designated as the global frame origin, you can use:
    
	.. code-block:: python
	    
	    current_relate_state = bodies.get('Vehicle').state - bodies.get('Earth').state
	
    to retrieve the current state of a body named 'Vehicle' w.r.t. the Earth. Note that if the Earth is the global frame origin, the above will still work fine. However, the Earth state will be a zero-vector, and its subtraction from the vehicle state may be omitted for efficiency purposes 

    NOTE: If you are only interested in the position or velocity components, you can use the :attr:`~tudatpy.numerical_simulation.environment.Body.position` or :attr:`~tudatpy.numerical_simulation.environment.Body.velocity` functions.


Rotational state
----------------

    The current rotational state of a body is defined by its current orientation w.r.t. the global frame orientation (see :ref:`reference_frames_global_orientation`). This orientation is defined by a quaternion (see :ref:`quaternion_definition`), but during a simulation a user will typically interact with the rotation matrix. The rotation matrix from the inertial to body-fixed frame is retrieved from a :class:`~tudatpy.numerical_simulation.environment.Body` object using the :attr:`~tudatpy.numerical_simulation.environment.Body.inertial_to_body_fixed_frame` function. The inverse rotation matrix (body-fixed to inertial) is retrieved using the :attr:`~tudatpy.numerical_simulation.environment.Body.body_fixed_to_inertial_frame` function.
    
    The time-derivative of the orientation is provided in two formulations (with equivalent information content): the angular velocity vector of the body-fixed frame, and the time derivative of the rotation matrix. The angular velocity vector, in inertial and body-fixed coordinates, is obtained from the :attr:`~tudatpy.numerical_simulation.environment.Body.inertial_angular_velocity` and :attr:`~tudatpy.numerical_simulation.environment.Body.body_fixed_angular_velocity` functions respectively. Note that the latter is the formulation that is used to represent the time-variation of the rotation when propagating rotational dynamics (see :ref:`TODO`). Alternatively, the time-derivative of the rotation matrix from inertial to body-fixed frame is given by :attr:`~tudatpy.numerical_simulation.environment.Body.inertial_to_body_fixed_frame_derivative`, while the derivative of the inverse rotation is taken from :attr:`~tudatpy.numerical_simulation.environment.Body.body_fixed_to_inertial_frame_derivative`.

Body inertial mass
------------------

    Retrieved directly from a :class:`~tudatpy.numerical_simulation.environment.Body` object with the :attr:`~tudatpy.numerical_simulation.environment.Body.mass` function. Note that this mass is *not* (at least, not by definition) the mass used for calculation of gravitional interactions (the gravitational mass :math:`m_{g}`, as you would find it in Newton's law of gravity :math:`a=\frac{Gm_{g}}{r^{2}}`), but the mass used to convert forces to accelerations and vice versa (the inertial mass :math:`m_{i}`, as you would find it in Newton's law of motion :math:`F=m_{i}a`). Although, to our best knowledge, the two masses are equal for all bodies, various alternatives to general relativity predict a difference between the two. Moreover, we have found it useful to *not* define a gravity field for any body which happens to have a mass assigned to it. For instance, a spacecraft will have an (inertial) mass which is needed for computing most non-gravitational accelerations. But, it does *not* require its own gravity field to compute gravitational accelerations.
	
Spherical harmonic gravity field coefficients
---------------------------------------------

    These coefficients may be time variable (see :mod:`~tudatpy.numerical_simulation.environment_setup.gravity_field_variation`). The current cosine and sine coefficients can be retrieved from a body object through its gravity field model. A piece of example code on retrieving these coefficients is given below for the case of Earth:

	.. code-block:: python

		earth_gravity_field = bodies.at( "Earth" ).gravity_field_model
		cosine_coefficients = earth_gravity_field.cosine_coefficients
		sine_coefficients = earth_gravity_field.cosine_coefficients


    Note the above will only work if the ``earth_gravity_field`` is of the type :func:`~tudatpy.numerical_simulation.environment.SphericalHarmonicGravityFieldModel`, which typically means that the body has default spherical harmonic gravity field settings (see :ref:`default_environment_models`) or that spherical harmonic gravity field settings were defined using the :func:`tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic` function). For safety, the above could be put inside the ``try`` block of a ``try/except`` construction,  wherethe ``except`` block will be entered in case the gravity field model type of the Earth is not spherical harmonic.

.. _flight_conditions_during_propagation:

Flight conditions
-----------------

    The :class:`~tudatpy.numerical_simulation.environment.FlightConditions` class, and its derived class :class:`~tudatpy.numerical_simulation.environment.AtmosphericFlightConditions` stores data relating to altitude, flight angles, local atmospheric properties, etc. The ``FlightConditions`` class is atypical, in the sense that a user does not provide settings for the flight conditions when creating a body object. The reason is that the ``FlightConditions`` does not contain any 'new' information. Instead, it is responsible for using the existing properties of the environment and the propagation to calculate various properties related to the current state. 
    
    The reason is that ``FlightConditions`` are related to a central body, and the object is created automatically whenever the code identifies that it is required for any of its calculations (state derivative; dependent variables, etc.). A user may also create the class themselves by using the :func:`~tudatpy.numerical_simulation.add_flight_conditions` function. The choice between the two classes (``FlightConditions`` and ``AtmosphericFlightConditions``, with the latter derived from the former) is made based on the central body: if this has an atmosphere model, ``AtmosphericFlightConditions`` are created, if it does not, then ``FlightConditions`` are created.
            
    Below are some examples of information that can be retrieved from the flight conditions (base class): 

	.. code-block:: python

		current_altitude = bodies.at( "Earth" ).flight_conditions.altitude
		current_longitude = bodies.at( "Earth" ).flight_conditions.longiude
		current_latitude = bodies.at( "Earth" ).flight_conditions.latitude
    
    as well as its derived class that also incorporates atmospheric properties
    
	.. code-block:: python
	
	    current_airspeed = bodies.at( "Earth" ).flight_conditions.airspeed
	    current_freestream_density = bodies.at( "Earth" ).flight_conditions.density
	    current_mach_number = bodies.at( "Earth" ).flight_conditions.mach_number
        
    The ``FlightConditions`` class also contains an object of type :class:`~tudatpy.numerical_simulation.environment.AerodynamicAngleCalculator`, which handles the calculation of angles (latitude, longitude, flight path angle, heading angle, angle of attack, sidelip angle, bank angle) and transformations between reference frames (inertial, central-body-fixed, vertical, trajectory, aerodynamic and body-fixed frames; see `this reference <https://repository.tudelft.nl/islandora/object/uuid%3Ae5fce5a0-7bce-4d8e-8249-e23293edbb55>`_ for details) typically used in flight dynamics. The angles and frames are listed in the tudatpy enums :class:`~tudatpy.numerical_simulation.environment.AerodynamicsReferenceFrameAngles` and :class:`~tudatpy.numerical_simulation.environment.AerodynamicsReferenceFrames`, respectively. Each of the angles, and the rotation between each of the frames, can be retrieved as follows (for two representative examples):

    .. code-block:: python

        angle_calculator = bodies.at( "Earth" ).flight_conditions.aerodynamic_angle_calculator
        bank_angle = angle_calculator.get_angle( environment.bank_angle )
        rotation_matrix_vertical_to_body_fixed = angle_calculator.get_rotation_matrix_between_frames( environment.vertical_frame, environment.body_frame )
        

.. _aerodynamics_during_propagation:

Aerodynamic coefficients
------------------------

    Aerodynamic coefficients in Tudat can be a function of a number of independent variables, such as angle of attack, Mach number, etc (see :class:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientsIndependentVariables` for comprehensive list of options). During the propagation, the :class:`~tudatpy.numerical_simulation.environment.AtmosphericFlightConditions` object (see above) automatically calculates the values of the independent variables, and passes the list of independent variables to an :class:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface` of the body (if it possesses any) to update the aerodynamic coefficients to the current state/time. The current values can be extracted from the :class:`~tudatpy.numerical_simulation.environment.AtmosphericFlightConditions using the :attr:`~tudatpy.numerical_simulation.environment.AtmosphericFlightConditions.aero_coefficient_independent_variables` attribute. The current force and moment coefficients can be extracted from the coefficient interface using the :attr:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface.current_force_coefficients` and :attr:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface.current_moment_coefficients` attributes, respectively.
    
    It may happen that a custom model influences the values of the independent variables, for instance when specifying a custom function for the angle of attack using the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based` rotation model. If the algorithm *itself* depends on these angles, it may be necessary to update the aerodynamic coefficients in the guidance algorithm. One example is shown in the :ref:`TODO` example. 
    
    .. code-block:: python


        # Extract Mach number from fliht conditions
        mach_number = vehicle_flight_conditions.mach_number        
        # Compute angle attach attack according to user-defined guidance law
        angle_of_attack = np.deg2rad(30 / (1 + np.exp(-2*(mach_number-9))) + 10)        
        # Update the variables on which the aerodynamic coefficients are based (AoA and Mach)
        current_aerodynamics_independent_variables = [self.angle_of_attack, mach_number]        
        # Update the aerodynamic coefficients
        aerodynamic_coefficient_interface.update_coefficients(
                    current_aerodynamics_independent_variables, current_time)
        # Extract the current force coefficients (in order: C_D, C_S, C_L)
        current_force_coefficients = aerodynamic_coefficient_interface.current_force_coefficients
        # Compute bank angle using guidance law requiring current_force_coefficients as input
        bank_angle = ... #=f(current_force_coefficients)
   
   In the above example, the aerodynamic coefficients are a function of angle of attack and Mach number (in that order). For an arbitrary coefficient interface, the independent variable types may be       extracted using the :attr:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface.independent_variable_names` attribute.
   
   Note that the :attr:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface.current_force_coefficients` may represent the set :math:`\pm[C_{D}, C_{S}, C_{L}]` (in the aerodynamic frame) or :math:`\pm[C_{X}, C_{Y}, C_{Z}]` (in the body-fixed frame). This information can be determined using the :attr:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface.are_coefficients_in_aerodynamic_frame` (for aerodynamic or body frame) and :attr:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface.are_coefficients_in_negative_direction` (for plus or minus sign).
           
    
     
    
    

