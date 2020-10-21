# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define settings for propagator
rotational_propagator_settings = propagation_setup.propagator.rotational(
    torque_models,
    bodies_to_propagate,
    initial_state,
    simulation_end_epoch,
    propagator = quaternions,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0 )
