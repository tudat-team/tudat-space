parameter_settings = estimation_setup.parameter.initial_states( 
	propagator_settings, bodies )
parameter_settings.append( estimation_setup.parameter.gravitational_parameter("Earth") )
parameter_settings.append( estimation_setup.parameter.constant_drag_coefficient("Delfi-C3") )
parameter_settings.append( estimation_setup.parameter.radiation_pressure_coefficient("Delfi-C3") )
