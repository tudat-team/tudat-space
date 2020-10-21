# Define bodies that are propagated.
bodies_to_propagate = ["Earth","Mars","Sun","Moon"]

# Define central bodies.
central_bodies = ["Sun","Sun","SSB","Earth"]

# Define settings for propagator
propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    initial_state,
    simulation_end_epoch )
