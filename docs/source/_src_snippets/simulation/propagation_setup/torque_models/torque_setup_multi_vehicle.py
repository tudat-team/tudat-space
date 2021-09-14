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
        propagation_setup.torque.spherical_harmonic_gravity(4, 4),
        propagation_setup.torque.aerodynamic()
    ]
)

# Create global accelerations settings dictionary.
acceleration_settings = {
    "Vehicle1": torque_settings_vehicle,
	"Vehicle2": torque_settings_vehicle
}
