# Add atmosphere settings to body (if body does not yet have amosphere settings)
body_settings.get( "Mars" ).atmosphere_settings = ...

# Define settings for wind
wind_frame = environment.vertical_frame
wind_velocity = np.ndarray([0.0, 0.0, 10.0])
body_settings.get( "Mars" ).atmosphere_settings.wind_settings = environment_setup.atmosphere.constant_wind_model( wind_velocity, wind_frame ) 		

