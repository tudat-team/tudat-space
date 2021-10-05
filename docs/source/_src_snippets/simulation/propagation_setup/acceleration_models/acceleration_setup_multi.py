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
acceleration_settings = {
    "Moon": accelerations_settings_moon,
    "Earth": accelerations_settings_earth
}
