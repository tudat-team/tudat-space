initial_time = 86400 # seconds since J2000
initial_time_step = 10 # seconds
coefficient_set = propagation_setup.CoefficientSets.runge_kutta_fehlberg_78
minimum_step_size = 0.1 # seconds
maximum_step_size = 100 # seconds
relative_error_tolerance = 1.0e-9 # -
absolute_error_tolerance = 1.0e-9 # -

integrator_settings = propagation_setup.integrator.runge_kutta_variable_step_size_scalar_tolerances(
	initial_time,
	initial_time_step,
	coefficient_set,
	minimum_step_size,
	maximum_step_size,
	relative_error_tolerance,
	absolute_error_tolerance
)
