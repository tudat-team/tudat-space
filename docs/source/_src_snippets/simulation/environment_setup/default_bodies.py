# define bodies in simulation
bodies_to_create = ["Sun", "Earth", "Moon", "Mars", "Jupiter"]

# create body settings dictionary
body_settings = environment_setup.get_default_body_settings(
        bodies_to_create, "SSB", "J2000")
