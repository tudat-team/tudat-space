scaling_constant = 1.001
unscaled_ephemeris_settings = body_settings.get( 'Jupiter' ).ephemeris_settings

body_settings.get( 'Jupiter' ).ephemeris_settings =  environment_setup.ephemeris.scaled(
       unscaled_ephemeris_settings, scaling_constant )

