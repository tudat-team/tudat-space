parameter_settings = dynamics.parameters_setup.initial_states(
	propagator_settings, bodies )
parameter_settings.append( dynamics.parameters_setup.gravitational_parameter("Earth") )
parameter_settings.append( dynamics.parameters_setup.constant_drag_coefficient("Delfi-C3") )
parameter_settings.append( dynamics.parameters_setup.radiation_pressure_coefficient("Delfi-C3") )
