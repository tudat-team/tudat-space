
# define bodies in simulation
bodies_to_create = ["Sun", "Earth", "Moon"]

# create body settings dictionary
body_settings = environment_setup.get_default_body_settings(
        bodies_to_create, "SSB", "J2000")

# create body system
bodies = environment_setup.create_system_of_bodies(body_settings)
