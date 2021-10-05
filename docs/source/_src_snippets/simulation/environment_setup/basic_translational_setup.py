# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define central bodies.
central_bodies = ["Earth"]

# Define settings for propagator
termination_condition = propagation_setup.propagator.time_termination(
    simulation_end_epoch )
propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    initial_state,
    termination_condition )
