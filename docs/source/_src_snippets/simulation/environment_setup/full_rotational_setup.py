# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Define torque models
torque_models =  ## ADD TORQUE MODELS HERE ##

# Define initial conditions
# Set initial rotation matrix (identity matrix)
initial_rotation_matrix = np.eye(3)
# Set initial orientation by converting a rotation matrix to quaternions
initial_state = element_conversion.rotation_matrix_to_quaternion_entries(initial_rotation_matrix)
# Complete initial state by adding angular velocity vector (zero in this case)
initial_state.append([0,0,0])
# Start of simulation
simulation_start_epoch = 9120 * constants.JULIAN_DAY ## IS THIS NECESSARY HERE? ##

# Define numerical integrator (RK4; step size 2 seconds)
integrator_settings = propagation_setup.integrator.runge_kutta_4( 2.0 )

# Define termination settings
simulation_end_epoch = 9140 * constants.JULIAN_DAY
termination_settings = propagation_setup.propagator.time_termination(
    simulation_end_epoch )

# Define propagator type
propagator_type = RotationalPropagatorType.quaternions ## DOES THIS NEED WORK? ##

# Define dependent variables
dependent_variables_to_save = [propagation_setup.dependent_variable.total_torque_norm("Spacecraft")]

# Define rotational propagator settings
rotational_propagator_settings = propagation_setup.propagator.rotational(
    torque_models,
    bodies_to_propagate,
    initial_state,
    integrator_settings,
    termination_settings,
    propagator=propagator_type,
    output_variables=dependent_variables_to_save,
    print_interval=86400.0)
