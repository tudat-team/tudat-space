# Define torques per each exerting body
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
        propagation_setup.torque.spherical_harmonic_gravitational(4, 4),
        propagation_setup.torque.aerodynamic()
    ]
)

# Create global torque settings dictionary.
torque_settings = {
    "Vehicle1": torque_settings_vehicle,
	"Vehicle2": torque_settings_vehicle
}
