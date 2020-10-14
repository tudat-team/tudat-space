precession_nutation_theory = iau_2006

original_frame = "J2000"

body_settings.get_body( "Earth" ).rotation_model_settings = environment_setup.rotation_model.gcrs_to_itrs_rotation_model(
	precession_nutation_theory, original_frame)