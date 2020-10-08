# Outside main
def custom_density_function( altitude, longitude, latitude, time ):

   # Return a linear combination of the input values
   return 0.5 * altitude + 0.25 * longitude + 0.15 * latitude + 0.1 * time;


def main( ):

  # ...

  # Define atmosphere settings
  constant_temperature = 250.0
  specific_gas_constant = 300.0
  ratio_of_specific_heats = 1.4

  body_settings[ "Earth" ].environment_setup.custom_constant_temperature_atmosphere_settings( custom_density_function,
                              constant_temperature, specific_gas_constant, ratio_of_specific_heats )

  # ...