initial_time = 86400 # seconds since J2000
initial_time_step = 10 # seconds
minimum_step_size = 0.1 # seconds
maximum_step_size = 100 # seconds
relative_error_tolerance = 1.0e-9 # -
absolute_error_tolerance = 1.0e-9 # -
minimum_order = 6
maximum_order = 11

integrator_settings = propagation_setup.integrator.runge_kutta_variable_step_size(
	initial_time,
	initial_time_step,
	minimum_step_size,
	maximum_step_size,
	relative_error_tolerance,
	absolute_error_tolerance,
	minimum_order,
	maximum_order
)
