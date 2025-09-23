original_frame = "J2000"
target_frame = "IAU_Earth"

body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.spice(
    original_frame, target_frame)
