def neptune_state_function( current_time ):
    # Define constants for Neptune ephemeris
    orbital_radius = 4.5E12    
    sun_gravitational_parameter = 1.32712440042E20
    anomaly_at_j2000 = np.deg2rad( 304.88003 )

    # Compute orbitall velocity and orbital period
    orbital_velocity = math.sqrt( sun_gravitational_parameter / orbital_radius )
    orbital_period = 2.0 * math.pi * math.sqrt( orbital_radius ** 3 / sun_gravitational_parameter )

    # Compute current angular position along orbit
    anomaly_at_epoch = anomaly_at_j2000 + 2.0 * math.pi * ( current_time / orbital_period )

    # Compute and return Neptune state
    return np.array([orbital_radius * math.cos(anomaly_at_epoch)],[orbital_radius * math.cos(anomaly_at_epoch)],[0.0] )

...

# Retrieve custom state function, and set as ephemeris function w.r.t. Sun, with axes along J2000
custom_state_function = neptune_state_function
body_settings.get( "Neptune" ).ephemeris_settings = environment_setup.ephemeris.custom( 
	custom_state_function, 'Sun', 'ECLIPJ2000' )
