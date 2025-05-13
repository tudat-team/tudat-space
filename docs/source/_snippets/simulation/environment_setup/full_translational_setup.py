# Create physical environment
bodies = environment_setup.create_system_of_bodies( ... )

# Define central bodies
central_bodies = ["Earth"]

# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Define acceleration settings acting on spacecraft
acceleration_settings_spacecraft = dict( Sun=[propagation_setup.acceleration.point_mass_gravity()])
acceleration_settings = {"Spacecraft": acceleration_settings_spacecraft}

# Create acceleration models.
acceleration_models = propagation_setup.create_acceleration_models( 
    bodies, acceleration_settings, bodies_to_propagate, central_bodies) 

# Define initial conditions as Cartesian elements w.r.t. central body (Earth) with axes along global orientation
initial_state = [5.89960424e+06, 2.30545977e+06, 1.74910449e+06, -1.53482795e+03, -1.71707683e+03, 7.44010957e+03]

# Define numerical integrator (RK4; step size 2 seconds)
integrator_settings = propagation_setup.integrator.runge_kutta_fixed_step(
    2.0, integrator.CoefficientSets.rk_4 )

# Start of simulation
simulation_start_epoch = 9120.0 * constants.JULIAN_DAY

# Define termination settings
simulation_end_epoch = 9140.0 * constants.JULIAN_DAY
termination_settings = propagation_setup.propagator.time_termination(
    simulation_end_epoch )

# Define propagator type
propagator_type = propagation_setup.propagator.encke

# Define dependent variables
dependent_variables_to_save = [propagation_setup.dependent_variable.total_acceleration( "Spacecraft" )]

# Define translational propagator settings
translational_propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    initial_state,
    simulation_start_epoch,
    integrator_settings,
    termination_settings,
    propagator=propagator_type,
    output_variables= dependent_variables_to_save)

# Set print frequency (to terminal) at once per day
translational_propagator_settings.print_settings.results_print_frequency_in_seconds = 86400.0
