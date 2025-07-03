initial_time = 86400 # seconds since J2000
initial_time_step = 10 # seconds
extrapolation_sequence = propagation_setup.integrator.ExtrapolationMethodStepSequences.bulirsch_stoer_sequence
maximum_number_of_steps = 10 # -
minimum_step_size = 0.1 # seconds
maximum_step_size = 100 # seconds
relative_error_tolerance = 1.0e-9 # -
absolute_error_tolerance = 1.0e-9 # -

integrator_settings = propagation_setup.integrator.bulirsch_stoer(
	initial_time,
	initial_time_step,
	extrapolation_sequence,
	maximum_number_of_steps,
	minimum_step_size,
	maximum_step_size,
	relative_error_tolerance,
	absolute_error_tolerance
)
