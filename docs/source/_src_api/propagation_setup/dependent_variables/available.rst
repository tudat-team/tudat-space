.. _available_dependent_variables:

Available Dependent Variables
#############################

All variables are saved in SI units. Dependent variables can be added to the propagation settings by first defining a list of desired dependent variables.


.. code-block:: python
      
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
        propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" )
    ]

Then, add this list to the propagating settings.

.. code-block:: python

    propagator_settings = propagation_setup.propagator.translational(
	    central_bodies,
	    acceleration_models,
	    bodies_to_propagate,
	    initial_state,
	    simulation_end_epoch,
	    output_variables = dependent_variables_to_save
    )

After the dynamics simulator has been called, the dependent variable history can be retrieved as:

.. code-block:: python

	dependent_variables = dynamics_simulator.dependent_variable_history

.. note::

	Dependent variables can be saved for each (celestial) body, as long as it has been defined in the environment.

- **Mach Number**

	Mach number in atmosphere. Requires an aerodynamic acceleration to be acting on the vehicle.

	.. code-block:: python

		 propagation_setup.dependent_variable.mach_number( "Spacecraft", "Earth" )

- **Altitude** 

	Altitude above body exerting aerodynamic acceleration. Requires an aerodynamic acceleration to be acting on the vehicle.

	.. code-block:: python

		propagation_setup.dependent_variable.altitude( "Spacecraft", "Earth" )

- **Airspeed**
	
	Airspeed in atmosphere of body exerting aerodynamic acceleration. Requires an aerodynamic acceleration to be acting on the vehicle.

	.. code-block:: python

		propagation_setup.dependent_variable.airspeed( "Spacecraft", "Earth" )

- **Density**

	Local density in atmosphere of body exerting aerodynamic acceleration (at position of body undergoing acceleration). Requires an aerodynamic acceleration to be acting on the vehicle. 

	.. code-block:: python

		propagation_setup.dependent_variable.density( "Spacecraft", "Earth" )

- **Relative Position**

	Vector position of a body with respect to a second body (between centers of mass).

	.. code-block:: python

		propagation_setup.dependent_variable.relative_position( "Spacecraft", "Earth" )

- **Relative Distance**

	Scalar distance of a body with respect to a second body (between centers of mass). 

	.. code-block:: python

		propagation_setup.dependent_variable.relative_distance( "Spacecraft", "Earth" )

- **Relative Velocity**

	Vector velocity of a body with respect to a second body (between centers of mass).

	.. code-block:: python

		propagation_setup.dependent_variable.relative_velocity( "Spacecraft", "Earth" )

- **Relative Speed**

	Scalar velocity of a body with respect to a second body (between centers of mass).

	.. code-block:: python

		propagation_setup.dependent_variable.relative_speed( "Spacecraft", "Earth" )

- **Keplerian State**

	.. code-block:: python

		propagation_setup.dependent_variable.keplerian_state( "Spacecraft", "Earth" )


	Returns six columns:
	1: Semi-major Axis. 2: Eccentricity. 3: Inclination. 4: Argument of Periapsis. 5. Right Ascension of the Ascending Node. 6: True Anomaly.

- **Single Acceleration**

	.. code-block:: python

		propagation_setup.dependent_variable.single_acceleration( 
			propagation_setup.acceleration.point_mass_gravity_type, "Spacecraft", "Earth" )

- **Single Acceleration Norm**

	.. code-block:: python

		propagation_setup.dependent_variable.single_acceleration_norm( 
			propagation_setup.acceleration.point_mass_gravity_type, "Spacecraft", "Earth" )

- **Spherical Harmonic Terms Acceleration**

	.. code-block:: python

		spherical_harmonic_terms = [ (2,0), (2,1), (2,2) ]
		propagation_setup.dependent_variable.spherical_harmonic_terms_acceleration( "Spacecraft", "Earth", spherical_harmonic_terms )

	The entries in the ``spherical_harmonic_terms`` define the (degree, order) pairs of which the contribution to the spherical harmonic acceleration is to be retrieved.

- **Spherical Harmonic Terms Acceleration Norm**

	.. code-block:: python

		spherical_harmonic_terms = [ (2,0), (2,1), (2,2) ]
		propagation_setup.dependent_variable.spherical_harmonic_terms_acceleration_norm( "Spacecraft", "Earth", spherical_harmonic_terms )

	The entries in the ``spherical_harmonic_terms`` define the (degree, order) pairs of which the norm of the contribution to the spherical harmonic acceleration is to be retrieved.

- **Total Acceleration**

	.. code-block:: python

		propagation_setup.dependent_variable.total_acceleration( "Spacecraft" )

- **Total Acceleration Norm**

	.. code-block:: python

		propagation_setup.dependent_variable.total_acceleration_norm( "Spacecraft" )

- **Aerodynamic Force Coefficients**

	.. code-block:: python

		propagation_setup.dependent_variable.aerodynamic_force_coefficients( "Spacecraft" )

- **Aerodynamic Moment Coefficients**

	.. code-block:: python

		propagation_setup.dependent_variable.aerodynamic_moment_coefficients( "Spacecraft" )

- **Latitude**

	.. code-block:: python

		propagation_setup.dependent_variable.latitude( "Spacecraft", "Earth" )

- **Longitude**

	.. code-block:: python

		propagation_setup.dependent_variable.longitude( "Spacecraft", "Earth" )

- **Heading Angle**

	.. code-block:: python

		propagation_setup.dependent_variable.heading_angle( "Spacecraft", "Earth" )

- **Flight Path Angle**

	.. code-block:: python

		propagation_setup.dependent_variable.flight_path_angle( "Spacecraft", "Earth" )

- **Radiation Pressure**

	.. code-block:: python

		propagation_setup.dependent_variable.radiation_pressure( "Spacecraft", "Earth" )


      


