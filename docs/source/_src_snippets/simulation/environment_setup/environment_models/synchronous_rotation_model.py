
original_frame = "ECLIPJ2000"
target_frame = "Phobos_Fixed"
central_body_name = "Mars"

body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.synchronous( 
	original_frame, target_frame, central_body_name)
