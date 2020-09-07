# define bodies in simulation
bodies_to_create = ["Sun", "Earth", "Moon"]

# create body settings dictionary
body_settings = environment_setup.get_default_body_settings(bodies_to_create)

# create body system
body_system = environment_setup.create_bodies(body_settings)

