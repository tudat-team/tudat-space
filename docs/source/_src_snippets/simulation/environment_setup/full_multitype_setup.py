# Create list of propagator settings
propagator_settings_list =[
	translational_propagator_settings, rotational_propagator_settings, mass_propagator_settings ]

# Define settings for multi-type propagator
termination_condition = propagation_setup.propagator.time_termination(
    simulation_end_epoch )
propagator_settings = propagation_setup.propagator.multitype(
    propagator_settings_list,
    integrator_settings,
    initial_time,
    termination_condition,
    output_variables =  dependent_variables_to_save )
