
original_frame = "ECLIPJ2000"
target_frame = "Earth_fixed"
constant_orientation = ...

body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.constant( 
	original_frame, target_frame, constant_orientation )
