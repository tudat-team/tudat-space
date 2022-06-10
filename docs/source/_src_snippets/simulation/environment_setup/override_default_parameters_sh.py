# Get the current cosine coefficients of the Earth
cosine_coefficients = body_settings.get('Earth').gravity_field_settings.normalized_cosine_coefficients

# Modify the C_{2,0} coefficient of the Earth
cosine_coefficients[ 2, 0 ] = cosine_coefficients[ 2, 0 ] + 1.0E-12

# Reset the coefficients of the Earth
body_settings.get('Earth').gravity_field_settings.normalized_cosine_coefficients = cosine_coefficients
