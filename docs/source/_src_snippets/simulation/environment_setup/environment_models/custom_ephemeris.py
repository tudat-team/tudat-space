custom_state_function = ...

body_settings.get( "Earth" ).ephemeris_settings = environment_setup.ephemeris.custom( 
	custom_state_function, frame_origin, frame_orientation)
