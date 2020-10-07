gravitational_parameter = ...
reference_radius = ...
normalized_cosine_coefficients = ... # NOTE: entry (i,j) denotes coefficient at degree i and order j
normalized_sine_coefficients = ... # NOTE: entry (i,j) denotes coefficient at degree i and order j
associated_reference_frame = ... # NOTE: provide as string

bodySettings[ "Earth" ].gravity_field_settings( gravitational_parameter, reference_radius, normalized_cosine_coefficients, 
	normalized_sine_coefficients, associated_reference_frame)