# Create physical environment
bodies = environment_setup.create_system_of_bodies( ... )

# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Define torque models
# Define torque settings acting on spacecraft
torque_settings_spacecraft = dict( Sun=[propagation_setup.torque.second_degree_gravitational()])
torque_settings = {"Spacecraft": torque_settings_spacecraft}

# Create torque models.
torque_models = propagation_setup.create_torque_models( 
    bodies, torque_settings, bodies_to_propagate) 

# Below, we define the initial state in a somewhat trivial manner (body axes along global frame
# axes; no initial rotation). A real application should use a more realistic initial rotational state
# Set initial rotation matrix (identity matrix)
initial_rotation_matrix = np.eye(3)
# Set initial orientation by converting a rotation matrix to a Tudat-compatible quaternion
initial_state = element_conversion.rotation_matrix_to_quaternion_entries(initial_rotation_matrix)
# Complete initial state by adding angular velocity vector (zero in this case)
initial_state.append([0,0,0])

# Define numerical integrator (RK4; step size 2 seconds)
integrator_settings = propagation_setup.integrator.runge_kutta_4( 2.0 )

# Start of simulation
simulation_start_epoch = 9120.0 * constants.JULIAN_DAY 

# Define termination settings
simulation_end_epoch = 9140.0 * constants.JULIAN_DAY
termination_settings = propagation_setup.propagator.time_termination(
    simulation_end_epoch )

# Define propagator type
propagator_type = propagation_setup.propagator.modified_rodrigues_parameters

# Define dependent variables
dependent_variables_to_save = [propagation_setup.dependent_variable.total_torque_norm("Spacecraft")]

# Define rotational propagator settings
rotational_propagator_settings = propagation_setup.propagator.rotational(
    torque_models,
    bodies_to_propagate,
    initial_state,
    simulation_start_epoch,
    integrator_settings,
    termination_settings,
    propagator=propagator_type,
    output_variables=dependent_variables_to_save)
