# Define bodies that are propagated.
bodies_to_propagate = ["Vehicle"]

# Define accelerations acting on Vehicle
torque_settings_vehicle = dict(
    Sun=
    [
        propagation_setup.torque.second_degree_gravitational()
    ],
    Moon=
    [
        propagation_setup.torque.second_degree_gravitational()
    ],
    Earth=
    [
        propagation_setup.torque.spherical_harmonic_gravity(4, 4),
        propagation_setup.torque.aerodynamic()
    ])

# Create global accelerations settings dictionary.
torque_settings = {"Delfi-C3": torque_settings_delfi_c3}

# Create acceleration models.
torque_models = propagation_setup.create_torque_models(
    bodies, torque_settings,  bodies_to_propagate )
