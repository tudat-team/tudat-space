# define bodies in simulation
bodies_to_create = ["Sun", "Earth", "Moon", "Mars", "Jupiter"]

# create body settings dictionary
global_frame_origin = "SSB"
global_frame_orientation = "J2000"
initial_time = 2.0 * constants.JULIAN_YEAR 
final_time = 4.0 * constants.JULIAN_YEAR
time_step = 300.0
body_settings = environment_setup.get_default_body_settings_time_limited(
        bodies_to_create, initial_time, final_time, global_frame_origin, global_frame_orientation time_step)
