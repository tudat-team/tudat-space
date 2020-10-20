density_scale_height = 7.2E3
constant_temperature = 290
density_at_zero_altitude = 1.225
specific_gas_constant = 287.06

body_settings.get_body( "Earth" ).atmosphere_settings = environment_setup.atmosphere.exponential(
	density_scale_height, constant_temperature, density_at_zero_altitude, specific_gas_constant)