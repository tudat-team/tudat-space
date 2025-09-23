cosine_variations_table = ...
sine_variations_table = ...
minimum_degree = 2
minimum_degree = 0
interpolator_settings = interpolators.linear_interpolation( )

gravity_field_variations.append( environment_setup.gravity_field_variation.tabulated( 
	cosine_variations_table, sine_variations_table, minimum_degree, minimum_order, interpolator_settings ) )
