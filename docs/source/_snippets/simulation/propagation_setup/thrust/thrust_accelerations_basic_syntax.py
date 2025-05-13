# Create the dictionary containing the thrust acceleration
accelerations_on_vehicle_dict = {
    "Vehicle": [
        propagation_setup.acceleration.thrust_from_direction_and_magnitude(
            thrust_direction_settings,
            thrust_magnitude_settings
        )
    ]
}
# Setup the accelerations as acting on the Vehicle
acceleration_dict = {"Vehicle": accelerations_on_vehicle_dict}
# Create the acceleration model in the system of bodies
acceleration_model = propagation_setup.create_acceleration_models(
    system_of_bodies, accelerations_on_vehicle_dict, bodies_to_propagate, central_bodies
)