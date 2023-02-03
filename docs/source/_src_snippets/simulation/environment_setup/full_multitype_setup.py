# Create list of propagator settings
propagator_settings_list =[
	translational_propagator_settings, rotational_propagator_settings, mass_propagator_settings ]

# Define settings for multi-type propagator
propagator_settings = propagation_setup.propagator.multitype(
    propagator_settings_list,
    integrator_settings,
    simulation_start_epoch,
    termination_condition,
    output_variables =  dependent_variables_to_save )
