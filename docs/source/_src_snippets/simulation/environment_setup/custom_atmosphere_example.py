# Custom function to compute density (https://www.grc.nasa.gov/www/k-12/airplane/atmosmrm.html)
def compute_mars_density( altitude ):

# Compute pressure
pressure = 0.699 * math.exp( -0.00009 * altitude )

# Compute altitude-dependent temperature
if( altitude > 7.0E3 ):
    temperature -23.4 - 0.00222 * altitude

else:
    temperature -31.0 - 0.000998 * altitude

# Compute and return density from equation of state
density = pressure / (.1921 * (temperature + 273.1))
return density


