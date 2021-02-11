density_function = ...
constant_temperature = 250.0
specific_gas_constant = 300.0
ratio_of_specific_heats = 1.4

body_settings.get( "Earth" ).atmosphere_settings = environment_setup.atmosphere.custom_constant_temperature( 
    density_function, constant_temperature, specific_gas_constant, ratio_of_specific_heats)


