
initial_time = ...
original_frame = "J2000"
target_frame = "IAU_Earth_Simplified"
target_frame_spice = "IAU_Earth"

body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.simple_from_spice( 
	original_frame, target_frame, target_frame_spice, initial_time)
