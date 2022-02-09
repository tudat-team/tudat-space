# Create the dictionary containing the thrust acceleration
accelerations_on_vehicle_dict = {
    "vehicle": [
        propagation_setup.acceleration.thrust_from_direction_and_magnitude(
            thrust_direction_settings,
            thrust_magnitude_settings
        )
    ]
}
# Apply the accelerations to the bodies
acceleration_models = propagation_setup.create_acceleration_models(
    bodies, accelerations_on_vehicle_dict, bodies_to_propagate, central_bodies
)