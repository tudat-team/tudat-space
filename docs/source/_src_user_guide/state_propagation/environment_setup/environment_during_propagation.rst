.. _environment_during_propagation:

==============================
Environment during propagation
==============================

Each body object and its constituent members is updated to the current state and time automatically during the numerical propagation. We stress that only those models that are relevant for a given propagation are updated every time step (this is handled automatically, without user intervention). 

When wriing a custom model (see :ref:`custom_models`) you will in many cases need to access the properties of bodies in the environment to perform your calculations. Some examples are:

* Retrieving the translational state of a spacecraft w.r.t. a central body to calculate your thrust direction 
* Retrieving the current atmospheric density during entry to calculate the required vehicle orientation
* Retrieving properties that cannot be saved as a dependent variable to calculate a custom dependent variable
* ...

Below, we give a list of the ways in which to retrieve the relevant information of the current properties of a Body in Tudat. Note that these can *only* be used during a propagation. Retrieving properties of bodies outside of a propagation requires a different workflow (see :ref:`TODO`, as the various models are then not automatically updated.) 

..
  Some (time-dependent properties) of a body are set in the environment models themselves (e.g. . Others are updated and stored directly in the Body object. Below is a full list of (possibly) time varying environment models, and how to retrieve them from a body object during propagation.

In what follows below, we will assume that you have create a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` variable name ``bodies``, from which you want to access various properties during the propagation. 

- **Translational state**

    Retrieved directly from the ``Body`` object with the :func:`~tudatpy.numerical_simulation.environment.Body.state`  function as Cartesian elements. Note that this state is always in the global frame origin and orientation (see :ref:`translational state reference frames<translational_reference_frames>`). To retrieve the state of one body w.r.t. the other, if neither body is the global frame origin, you can use:   
    
	.. code-block:: python
	    
	    current_relate_state = bodies.get('Vehicle').state - bodies.get('Earth').state
	
    to retrieve the current state of a body name 'Vehicle' w.r.t. the Earth. Note that if the Earth is the global frame origin, the above will still work fine. However, the Earth state will be a zero-vector, and its subtraction from the vehicle state may be omitted for a 

    NOTE: If you are only interested in the position or velocity components, you can use the :func:`~tudatpy.numerical_simulation.environment.Body.position` or :func:`~tudatpy.numerical_simulation.environment.Body.velocity` functions. 


- **Rotational state**

    The current rotational state of a body is defined by its current orientation w.r.t. the global frame orientation (see :ref:`reference_frames_global_orientation`). This orientation is defined by a quaternion (see :ref:`quaternion_definition`), but during a simulation a user will typically interact with the rotation matrix. The rotation matrix from the inertial to body-fixed frame is retrieved from a ``Body`` object using the :func:`~tudatpy.numerical_simulation.environment.Body.inertial_to_body_fixed_frame` function. The inverse rotation matrix (body-fixed to inertial) is retrieved using the :func:`~tudatpy.numerical_simulation.environment.Body.body_fixed_to_inertial_frame` function.
    
    The time-derivative of the orientation is provided in two formulations (with equivalent information content): the angular velocity vector of the body-fixed frame, and the time derivative of the rotation matrix. The angular velocity vector, in inertial and body-fixed coordinates, is obtained from the :func:`~tudatpy.numerical_simulation.environment.Body.inertial_angular_velocity` and :func:`~tudatpy.numerical_simulation.environment.Body.body_fixed_angular_velocity` functions respectively. Note that the latter is the formulation that is used to represent the time-variation of the rotation when propagating rotational dynamics (see :ref:`TODO`). Alternatively, the time-derivative of the rotation matrix from inertial to body-fixed frame is given by :func:`~tudatpy.numerical_simulation.environment.Body.inertial_to_body_fixed_frame`, while the derivative of the inverse rotation is taken from :func:`~tudatpy.numerical_simulation.environment.Body.body_fixed_to_inertial_frame_derivative`.

- **Body inertial mass**

    Retrieved directly from a ``Body`` object with the :func:`~tudatpy.numerical_simulation.environment.Body.mass` function. Note that this mass is *not* necessarilly the mass used for calculation of gravitional interactions (gravitational mass), but the mass used to convert forced to accelerations and vice verse (inertial mass).
	
- **Spherical harmonic gravity field coefficients**

    These coefficients may be time variable (see :mod:`~tudatpy.numerical_simulation.environment_setup.gravity_field_variation`). The current cosine and sine coefficients can be retrieved from a body object through its gravity field model. A piece of example code on retrieving these coefficients is given below for the case of Earth:

	.. code-block:: python

		earth_gravity_field = bodies.at( "Earth" ).gravity_field_model
		cosine_coefficients = earth_gravity_field.cosine_coefficients
		sine_coefficients = earth_gravity_field.cosine_coefficients


    Note the above will only work if the ``earth_gravity_field`` is of the type :func:`~tudatpy.numerical_simulation.environment.SphericalHarmonicGravityFieldModel`, which typically means that the body has default spherical harmonic gravity field settings (see :ref:`default_environment_models`) or that spherical harmonic gravity field settings were defined using the :func:`tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic` function). For safety, the above could be put inside the ``try`` block of a ``try/except`` construction,  wherethe ``except`` block will be entered in case the gravity field model type of the Earth is not spherical harmonic

- **Flight conditions**

    The :class:`~tudatpy.numerical_simulation.environment.FlightConditions` class, and its derived class :class:`~tudatpy.numerical_simulation.environment.AtmosphericFlightConditions` stores data relating to altitude, flight angles, local atmospheric properties, etc. Follow the links for their detailed description. The ``FlightConditions`` class is 'atypical', in the sense that a user does not provide settigs for the flight conditions when creating a body object. The reason is that the ``FlightConditions`` does not contain any 'new' information. Instead, it is resposible for using the existing properties of the environment and the propagation to calculate various properties related to the current state. 
    
    The ``FlightConditions`` are related to a central body, and the object is created automatically whenever the code identifies that it is required for any of its calculations (state derivative; dependent variables, etc.). A user may also create the class themselves by using the :func:`~tudatpy.numerical_simulation.add_flight_conditions` function. The choice between the two classes (``FlightConditions`` and ``AtmosphericFlightConditions``, with the latter derived from teh former) is made based on the central body: if this has an atmospher model, ``AtmosphericFlightConditions`` are created, if it does not, the ``FlightConditions`` are created.
            
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
        
    The ``FlightConditions`` class also contains an object of type :class:`~tudatpy.numerical_simulation.environment.AerodynamicAngleCalculator`, which handles the calculation of angles (latitude, longitude, flight path angle, heading angle, angle of attack, sidelip angle, bank angle) and transformations between reference frames (inertial, central-body-fixed, vertical, trajectory, aerodynamic and body-fixed frames, see `this reference <https://repository.tudelft.nl/islandora/object/uuid%3Ae5fce5a0-7bce-4d8e-8249-e23293edbb55>`_ for details) typically used in flight dynamics. The angles and frames are listed in the tudatpy enums :class:`~tudatpy.numerical_simulation.environment.AerodynamicsReferenceFrameAngles` and :class:`~tudatpy.numerical_simulation.environment.AerodynamicsReferenceFrames`, respectively. Each of the angles, and the rotation between each of the frames, can be retrieved as follows (for two representative examples):

    .. code-block:: python

        angle_calculator = bodies.at( "Earth" ).flight_conditions.aerodynamic_angle_calculator
        bank_angle = angle_calculator.get_angle( environment.bank_angle )
        rotation_matrix_vertical_to_body_fixed = angle_calculator.get_rotation_matrix_between_frames( environment.vertical_frame, environment.body_frame )
        
    
    
    
    
    
    

