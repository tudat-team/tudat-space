# Create the acceleration model, which contains the thrust of the vehicle on itself
acceleration_model = propagation_setup.create_acceleration_models(
    system_of_bodies, accelerations_on_vehicle_dict, bodies_to_propagate, central_bodies
)

# Define the mass rate settings of the Vehicle from its thrust
mass_rate_settings = {
    "Vehicle": [propagation_setup.mass_rate.from_thrust()]
}

# Create the mass rate model
mass_rate_models = propagation_setup.create_mass_rate_models(
    system_of_bodies,
    mass_rate_settings,
    acceleration_model
)