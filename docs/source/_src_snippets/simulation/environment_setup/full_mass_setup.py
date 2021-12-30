# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Define central bodies
central_bodies = ["Earth"]

# Set initial mass
initial_mass = 3400.0  # kg

# Define termination settings
termination_settings = propagation_setup.propagator.time_termination(simulation_end_epoch)

# Define output variables
dependent_variables_to_save = [
    propagation_setup.dependent_variable.total_acceleration("Spacecraft"),
    propagation_setup.dependent_variable.keplerian_state("Spacecraft", "Earth"),
    propagation_setup.dependent_variable.latitude("Spacecraft", "Earth"),
    propagation_setup.dependent_variable.longitude("Spacecraft", "Earth")
]

# Create mass propagator settings
mass_propagator_settings = propagation_setup.propagator.mass(
    mass_rate_models,
    bodies_to_propagate,
    initial_mass,
    termination_settings,
    output_variables=dependent_variables_to_save,
    print_interval=86400.0)
