body_state_history = ...

frame_origin = "SSB"
frame_orientation = "J2000"

body_settings.get_body( "Jupiter" ).ephemeris_settings = environment_setup.ephemeris.tabulated( body_state_history, 
	frame_origin, frame_orientation )