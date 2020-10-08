density_scale_height = 7.2E3
constant_temperature = 290
density_at_zero_altitude = 1.225
specific_gas_constant = 287.06

body_settings["Earth"].atmosphere_settings = environment_setup.exponential_atmosphere_settings(
        density_scale_height, constant_temperature, density_at_zero_altitude, specific_gas_constant)