# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Define mass rate models

# Create acceleration models like in Translational ## SHOULD WE ADD THIS? ##
bodies_to_create = ["Earth"]
# Create bodies in simulation.
body_settings = environment_setup.get_default_body_settings(bodies_to_create)
system_of_bodies = environment_setup.create_system_of_bodies(body_settings)

accelerations_settings_spacecraft = dict( Sun=[propagation_setup.acceleration.point_mass_gravity()])
acceleration_settings = {"Spacecraft": accelerations_settings_spacecraft}
# Create acceleration models.
acceleration_models = propagation_setup.create_acceleration_models( bodies, acceleration_settings,
                                                                   bodies_to_propagate,
                                                                   central_bodies)

# Create acceleration models
mass_rate_settings = dict(Vehicle=[propagation_setup.mass_rate.from_thrust()])
mass_rate_models = propagation_setup.create_mass_rate_models(
    system_of_bodies,
    mass_rate_settings,
    acceleration_models
)
# Define initial conditions
initial_mass = 3400.0  # kg

# Define numerical integrator (RK4; step size 2 seconds)
integrator_settings = propagation_setup.integrator.runge_kutta_4( 2.0 )

# Define termination settings
simulation_end_epoch = 9140 * constants.JULIAN_DAY
termination_settings = propagation_setup.propagator.time_termination(
    simulation_end_epoch )

# Define dependent variables
dependent_variables_to_save = [propagation_setup.dependent_variable.keplerian_state("Spacecraft", "Earth")]

# Define mass propagator settings
mass_propagator_settings = propagation_setup.propagator.mass(
    mass_rate_models,
    bodies_to_propagate,
    initial_mass,
    integrator_settings,
    termination_settings,
    output_variables=dependent_variables_to_save,
    print_interval=86400.0)
