initial_time = 0.0
final_time = 1.0E8
time_step = 3600.0

frame_origin = "SSB"
frame_orientation = "J2000"

body_settings.get_body( "Jupiter" ).ephemeris_settings = environment_setup.ephemeris.interpolated_spice(
	initial_time, final_time, time_step, frame_origin, frame_orientation )