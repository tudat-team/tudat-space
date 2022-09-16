# Add empty body settings for body Oumuamua, and add to existing list of settings 
body_settings.add_empty_settings( "Spacecraft" )

# Manually create and assign environment model settings to new body settings
body_settings.get( "Spacecraft" ).radiation_pressure_settings[ "Sun" ] = ...
body_settings.get( "Spacecraft" ).aerodynamic_coefficient_settings = ...
body_settings.get( "Spacecraft" ).constant_mass = 500.0;	
