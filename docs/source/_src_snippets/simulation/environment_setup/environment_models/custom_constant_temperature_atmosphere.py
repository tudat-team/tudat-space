# Outside main
def density_function( altitude, longitude, latitude, time ):

   # Return a linear combination of the input values
   return 0.5 * altitude + 0.25 * longitude + 0.15 * latitude + 0.1 * time


def main( ):

  # ...

  # Define atmosphere settings
  constant_temperature = 250.0
  specific_gas_constant = 300.0
  ratio_of_specific_heats = 1.4

  body_settings.get_body( "Earth" ).atmosphere_settings = environment_setup.atmosphere.custom_constant_temperature( 
    density_function, constant_temperature, specific_gas_constant, ratio_of_specific_heats)

  # ...