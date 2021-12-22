# Define bodies that are propagated
bodies_to_propagate = ["Vehicle"]

# Define central bodies
central_bodies = ["Earth"]

# Define accelerations acting on Vehicle
accelerations_settings_vehicle = dict(
    Sun=
    [
        propagation_setup.acceleration.point_mass_gravity()
    ],
    Moon=
    [
        propagation_setup.acceleration.point_mass_gravity()
    ],
    Earth=
    [
        propagation_setup.acceleration.spherical_harmonic_gravity(5, 5),
        propagation_setup.acceleration.aerodynamic()
    ])

# Create global accelerations settings dictionary
acceleration_settings = {"Delfi-C3": accelerations_settings_delfi_c3}

# Create acceleration models
acceleration_models = propagation_setup.create_acceleration_models(
    bodies, acceleration_settings,  bodies_to_propagate, central_bodies)
