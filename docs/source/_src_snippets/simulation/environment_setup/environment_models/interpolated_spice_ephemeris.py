initial_time = 0.0
final_time = 1.0E8
time_step = 3600.0

frame_origin = "SSB"
frame_orientation = "J2000"

body_settings[ "Jupiter" ].environment_setup.interpolated_spice_ephemeris_settings( 
	initial_time, final_time, time_step, frame_origin, frame_orientation)