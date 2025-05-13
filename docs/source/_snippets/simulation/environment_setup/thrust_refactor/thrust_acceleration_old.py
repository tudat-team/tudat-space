# Define settings for inertial thrust direction
thrust_direction_settings = ...

# Define settings for thrust magnitude 
thrust_magnitude_settings = ...

# Create acceleration model settings
acceleration_on_vehicle = dict(
    ...,
    Vehicle=[
        # Define the thrust acceleration from its direction and magnitude
        propagation_setup.acceleration.thrust_from_direction_and_magnitude(
            thrust_direction_settings=thrust_direction_settings,
            thrust_magnitude_settings=thrust_magnitude_settings,
        )
    ],
    )