
body_name = 'Jupiter'
initial_state_epoch = ...
central_body_gravitational_parameter = ...

frame_origin = 'SSB'
frame_orientation = 'J2000'

body_settings.get( 'Jupiter' ).ephemeris_settings = environment_setup.ephemeris.keplerian_from_spice( 
	body_name, initial_state_epoch, central_body_gravitational_parameter, frame_origin, frame_orientation )
