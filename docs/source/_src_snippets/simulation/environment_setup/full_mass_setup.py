# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define settings for propagator
termination_condition = propagation_setup.propagator.time_termination(
    simulation_end_epoch )
mass_propagator_settings = propagation_setup.propagator.mass(
    mass_rate_models,
    bodies_to_propagate,
    initial_state,
    termination_condition,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0 )
