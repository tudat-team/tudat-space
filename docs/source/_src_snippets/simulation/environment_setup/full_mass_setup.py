# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define settings for propagator
mass_propagator_settings = propagation_setup.propagator.mass(
    mass_rate_models,
    bodies_to_propagate,
    initial_state,
    simulation_end_epoch,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0 )
