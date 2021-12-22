# Define bodies that are propagated
bodies_to_propagate = ["Vehicle"]

# Define central bodies
central_bodies = ["Earth"]

# Set initial state
# Retrieve Earth's gravitational parameter
earth_gravitational_parameter = bodies.get("Earth").gravitational_parameter
# Retrieve Earth's radius
earth_radius = bodies.get("Earth").shape_model.average_radius
# Convert keplerian to cartesian elements
initial_state = element_conversion.keplerian_to_cartesian_elementwise(
    gravitational_parameter=earth_gravitational_parameter,
    semi_major_axis=earth_radius + 200.0E3,
    eccentricity=0.0,
    inclination=np.deg2rad(97.4),
    argument_of_periapsis=np.deg2rad(235.7),
    longitude_of_ascending_node=np.deg2rad(23.4),
    true_anomaly=np.deg2rad(139.87)
)

# Define termination settings
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
