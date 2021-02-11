scaling_constant = 1.5
unscaled_atmosphere_settings = body_settings.get( 'Earth' ).atmosphere_settings;

body_settings.get( 'Earth' ).atmosphere_settings =  environment_setup.atmosphere.scaled(
	unscaled_atmosphere_settings, scaling_constant )
