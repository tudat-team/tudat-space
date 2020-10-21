# Create list of propagator settings
propagator_settings_list =[
	translational_propagator_settings, rotational_propagator_settings, mass_propagator_settings

# Define settings for multi-type propagator
propagator_settings = propagation_setup.propagator.multi_type(
    propagator_settings_list,
    simulation_end_epoch,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0 )
