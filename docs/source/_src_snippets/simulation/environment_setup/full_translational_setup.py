# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define central bodies.
central_bodies = ["Earth"]

# Define termination settings.
termination_variable = propagation_setup.dependent_variable.altitude( "Spacecraft", "Earth" )
termination_settings = propagation_setup.propagator.dependent_variable_termination(
        dependent_variable_settings = termination_variable,
        limit_value = 25.0E3,
        use_as_lower_limit = True,
        terminate_exactly_on_final_condition = False
        )

# Define output variables
dependent_variables_to_save = [
    propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
    propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
    propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
    propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" )
    ]

# Define settings for propagator
translational_propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    initial_state,
    termination_settings,
    propagator = propagation_setup.propagator.encke,
    output_variables =  dependent_variables_to_save,
    print_interval = 86400.0 )
