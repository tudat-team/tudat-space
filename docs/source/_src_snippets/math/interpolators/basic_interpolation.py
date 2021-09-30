# Generate data to interpolate
data_to_interpolate = dict( )
data_to_interpolate = ...

# Create settings for interpolation
linear_interpolation_settings = interpolators.linear_interpolation( )

# Create interpolator
interpolator = interpolators.create_one_dimensional_interpolator( data_to_interpolate, linear_interpolation_settings )

# Interpolate data set in data_to_interpolate at t=100
independent_variable = 100
interpolated_value = interpolator.interpolate( independent_variable )
