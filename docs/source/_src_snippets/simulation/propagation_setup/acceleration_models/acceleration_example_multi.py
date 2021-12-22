# Define bodies that are propagated
bodies_to_propagate = ["Moon", "Earth"]

# Define central bodies
central_bodies = ["Sun", "Sun"]

# Define accelerations acting on Vehicle
accelerations_settings_moon = dict(
    Sun=
    [
        propagation_setup.acceleration.point_mass_gravity()
    ],
    Earth=
    [
        propagation_setup.acceleration.point_mass_gravity()
    ]
    )

accelerations_settings_earth = dict(
    Sun=
    [
        propagation_setup.acceleration.point_mass_gravity()
    ],
    Moon=
    [
        propagation_setup.acceleration.point_mass_gravity()
    ]
    )


# Create global accelerations settings dictionary.
acceleration_settings = {"Moon": accelerations_settings_moon,
			            "Earth": accelerations_settings_earth}

# Create acceleration models
acceleration_models = propagation_setup.create_acceleration_models(
    bodies, acceleration_settings,  bodies_to_propagate, central_bodies)