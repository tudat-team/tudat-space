initial_orientation = ...

initial_time = ...
rotation_rate = ...

original_frame = "J2000"
target_frame = "IAU_Earth"

body_settings[ "Earth" ].environment_setup.simple_rotation_model_settings( original_frame, target_frame, initial_orientation
	initial_time, rotation_rate)