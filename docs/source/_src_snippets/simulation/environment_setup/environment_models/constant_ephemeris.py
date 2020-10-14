constant_cartesian_state = ...

frame_origin = "SSB"
frame_orientation = "J2000"

body_settings.get_body( "Jupiter" ).ephemeris_settings = environment_setup.ephemeris.constant( constant_cartesian_state,
	frame_origin, frame_orientation)