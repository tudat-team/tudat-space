# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define central bodies.
central_bodies = ["Earth"]

# Define settings for propagator
translational_propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    initial_state,
    termination_settings,
    propagator = encke,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0 )
