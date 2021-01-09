    integrator_settings = propagation_setup.integrator.runge_kutta_4(
        initial_time,
        fixed_step_size,
        save_frequency = 1,
        assess_termination_on_minor_steps = false
    )
