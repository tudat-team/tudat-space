original_frame = "J2000"
target_frame = "IAU_Earth"

body_settings[ "Earth" ].environment_setup.rotation_model_settings( spice_rotation_model,
	original_frame, target_frame)