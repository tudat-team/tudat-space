# Define selected torques per each exerting body
torque_settings_moon = dict(
    Sun=
    [
        propagation_setup.torque.second_degree_gravitational()
    ],
    Earth=
    [
        propagation_setup.torque.spherical_harmonic_gravity(4, 4)
    ]
)

# Define selected torques per each exerting body
torque_settings_earth = dict(
    Sun=
    [
        propagation_setup.torque.second_degree_gravitational()
    ],
    Moon=
    [
        propagation_setup.torque.second_degree_gravitational()
    ]
)

# Create global accelerations settings dictionary and
# assign the torque selections to respective bodies that act upon
acceleration_settings = {
    "Moon": torque_settings_moon,
	"Earth": torque_settings_earth
}
