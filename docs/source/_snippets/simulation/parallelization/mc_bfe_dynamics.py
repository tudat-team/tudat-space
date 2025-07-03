def run_dynamics(arg_1, arg_2, spice=spice.load_standard_kernels()):
    """
    Function that creates the initial conditions, termination settings, and propagation settings, and runs
    create_dynamics_simulator() function and returns the state as an array.
    """
    # Set simulation start and end epochs
    simulation_start_epoch = 0.0
    simulation_end_epoch = constants.JULIAN_DAY

    # Create default body settings for "Earth"
    bodies_to_create = ["Earth"]

    # Create default body settings for bodies_to_create, with "Earth"/"J2000" as the global frame origin and orientation
    global_frame_origin = "Earth"
    global_frame_orientation = "J2000"
    body_settings = environment_setup.get_default_body_settings(
        bodies_to_create, global_frame_origin, global_frame_orientation)

    # Create system of bodies (in this case only Earth)
    bodies = environment_setup.create_system_of_bodies(body_settings)
    bodies.create_empty_body("Delfi-C3")
    bodies_to_propagate = ["Delfi-C3"]
    central_bodies = ["Earth"]

    # Define accelerations acting on Delfi-C3
    acceleration_settings_delfi_c3 = dict(
        Earth=[propagation_setup.acceleration.point_mass_gravity()]
    )

    acceleration_settings = {"Delfi-C3": acceleration_settings_delfi_c3}

    # Create acceleration models
    acceleration_models = propagation_setup.create_acceleration_models(
        bodies, acceleration_settings, bodies_to_propagate, central_bodies
    )

    earth_gravitational_parameter = bodies.get("Earth").gravitational_parameter
    initial_state = element_conversion.keplerian_to_cartesian_elementwise(
        gravitational_parameter=earth_gravitational_parameter,
        semi_major_axis=arg_1,
        eccentricity=arg_2,
        inclination=np.deg2rad(85.3),
        argument_of_periapsis=np.deg2rad(235.7),
        longitude_of_ascending_node=np.deg2rad(23.4),
        true_anomaly=np.deg2rad(139.87),
    )

    # Create termination settings
    termination_settings = propagation_setup.propagator.time_termination(simulation_end_epoch)

    # Create numerical integrator settings
    fixed_step_size = 10.0
    integrator_settings = propagation_setup.integrator.runge_kutta_fixed_step(
        2.0, integrator.CoefficientSets.rk_4 )

    # Create propagation settings
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_state,
        simulation_start_epoch,
        integrator_settings,
        termination_settings
    )

    # Create simulation object and propagate the dynamics
    dynamics_simulator = numerical_simulation.create_dynamics_simulator(
        bodies, propagator_settings
    )

    # Extract the resulting state history and convert it to an ndarray
    states = dynamics_simulator.state_history
    return result2array(states)

