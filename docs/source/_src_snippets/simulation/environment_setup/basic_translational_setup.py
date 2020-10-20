# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define central bodies.
central_bodies = ["Earth"]

# Define settings for propagator
propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    initial_state,
    simulation_end_epoch )
