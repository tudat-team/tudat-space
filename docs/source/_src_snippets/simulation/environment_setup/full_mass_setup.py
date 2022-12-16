# Create physical environment
bodies = environment_setup.create_system_of_bodies( ... )

# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Create mass rate models, note that the model below will only work as part of a
# multitype propagation, where mass and translational state are propagated, and
# a thrust acceleration is acting on the spacecraft
mass_rate_settings = dict(Vehicle=[propagation_setup.mass_rate.from_thrust()])
mass_rate_models = propagation_setup.create_mass_rate_models(
    bodies,
    mass_rate_settings,
    acceleration_models
)
# Define initial conditions
initial_mass = 3400.0  # kg

# Define numerical integrator (RK4; step size 2 seconds)
integrator_settings = propagation_setup.integrator.runge_kutta_4( 2.0 )

# Start of simulation
simulation_start_epoch = 9120.0 * constants.JULIAN_DAY

# Define termination settings
simulation_end_epoch = 9140 * constants.JULIAN_DAY
termination_settings = propagation_setup.propagator.time_termination(
    simulation_end_epoch )

# Define dependent variables
dependent_variables_to_save = [propagation_setup.dependent_variable.total_mass_rate("Spacecraft")]

# Define mass propagator settings
mass_propagator_settings = propagation_setup.propagator.mass(
    mass_rate_models,
    bodies_to_propagate,
    initial_mass,
    simulation_start_epoch,
    integrator_settings,
    termination_settings,
    output_variables=dependent_variables_to_save,
    print_interval=86400.0)
