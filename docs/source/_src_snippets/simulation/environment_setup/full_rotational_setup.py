# Define bodies that are propagated
bodies_to_propagate = ["Spacecraft"]

# Set initial rotation matrix (identity matrix)
initial_rotation_matrix = np.eye(3)

# Set initial orientation by converting a rotation matrix to quaternions
initial_state = element_conversion.rotation_matrix_to_quaternion_entries(initial_rotation_matrix)

# Complete initial state by adding angular velocity vector (zero in this case)
initial_state.append([0,0,0])

# Define termination settings
termination_condition = propagation_setup.propagator.time_termination(
    simulation_end_epoch )

# Define output variables
dependent_variables_to_save = [propagation_setup.dependent_variable.total_torque_norm("Spacecraft")]

# Create rotational propagator settings
rotational_propagator_settings = propagation_setup.propagator.rotational(
    torque_models,
    bodies_to_propagate,
    initial_state,
    termination_condition,
    propagator = RotationalPropagatorType.quaternions,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0)
