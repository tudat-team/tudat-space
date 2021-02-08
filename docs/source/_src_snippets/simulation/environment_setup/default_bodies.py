# define bodies in simulation
bodies_to_create = ["Sun", "Earth", "Moon", "Mars", "Jupiter"]

# create body settings dictionary
global_frame_origin = "SSB"
global_frame_orientation = "J2000"
body_settings = environment_setup.get_default_body_settings(
        bodies_to_create, global_frame_origin, global_frame_orientation)
