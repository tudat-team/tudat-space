# Generate data to interpolate
data_to_interpolate = dict( )
data_derivatives = dict( )
data_to_interpolate = ...
data_derivatives = ...

# Create settings for Hermite spline interpolation
linear_interpolation_settings = interpolators.hermite_interpolation( )

# Create interpolator
interpolator = interpolators.create_one_dimensional_scalar_interpolator( data_to_interpolate, linear_interpolation_settings, data_derivatives )

# Interpolate data set in data_to_interpolate at t=100
independent_variable = 100
interpolated_value = interpolator.interpolate( independent_variable )
