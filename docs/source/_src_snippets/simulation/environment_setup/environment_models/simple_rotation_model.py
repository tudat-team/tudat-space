initial_orientation = ...

initial_time = ...
rotation_rate = ...

original_frame = "J2000"
target_frame = "IAU_Earth"

body_settings.get_body( "Earth" ).rotation_model_settings = environment_setup.rotation_model.simple( original_frame, target_frame, 
	initial_orientation, initial_time, rotation_rate)