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
    ]
)

# Create global accelerations settings dictionary.
acceleration_settings = {
    "Vehicle1": accelerations_settings_vehicle,
	"Vehicle2": accelerations_settings_vehicle
}
