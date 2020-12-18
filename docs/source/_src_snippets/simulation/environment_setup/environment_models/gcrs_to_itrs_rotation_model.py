precession_nutation_theory = environment_setup.rotation_model.IAUConventions.iau_2006

original_frame = "J2000"

body_settings.get( "Earth" ).rotation_model_settings = environment_setup.rotation_model.gcrs_to_itrs(
	precession_nutation_theory, original_frame)
