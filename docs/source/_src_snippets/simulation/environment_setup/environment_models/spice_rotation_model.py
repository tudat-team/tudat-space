original_frame = "J2000"
target_frame = "IAU_Earth"

body_settings.get_body( "Earth" ).rotation_model_settings = environment_setup.rotation_model.spice_rotation_model(
    original_frame, target_frame)