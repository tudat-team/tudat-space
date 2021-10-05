# Create list of propagator settings
propagator_settings_list =[
	translational_propagator_settings, rotational_propagator_settings, mass_propagator_settings ]

# Define settings for multi-type propagator
termination_condition = propagation_setup.propagator.time_termination(
    simulation_end_epoch )
propagator_settings = propagation_setup.propagator.multi_type(
    propagator_settings_list,
    termination_condition,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0 )
