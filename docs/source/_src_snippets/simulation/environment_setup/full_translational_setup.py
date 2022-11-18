# Define central bodies
central_bodies = ["Earth"]

# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Define the acceleration models
# Define acceleration settings acting on spacecraft
accelerations_settings_spacecraft = dict( Sun=[propagation_setup.acceleration.point_mass_gravity()])
acceleration_settings = {"Spacecraft": accelerations_settings_spacecraft}
# Create acceleration models.
acceleration_models = propagation_setup.create_acceleration_models( bodies, acceleration_settings,
                                                                   bodies_to_propagate,
                                                                   central_bodies) ## BODIES MAYBE NEED TO BE ADDED? ##

# Define initial conditions
initial_state = [5.89960424e+06, 2.30545977e+06, 1.74910449e+06, -1.53482795e+03, -1.71707683e+03, 7.44010957e+03]
# Start of simulation
simulation_start_epoch = 9120 * constants.JULIAN_DAY

# Define numerical integrator (RK4; step size 2 seconds)
integrator_settings = propagation_setup.integrator.runge_kutta_4( 2.0 )

# Define termination settings
simulation_end_epoch = 9140 * constants.JULIAN_DAY
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
    output_variables= dependent_variables_to_save,
    print_interval=86400.0)
