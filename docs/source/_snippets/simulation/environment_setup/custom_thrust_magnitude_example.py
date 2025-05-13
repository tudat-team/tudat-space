
# Create bodies (same as in any other simulation)
bodies = ...

# Create guidance object
guidance_model = SimpleCustomGuidanceModel( bodies )

# Extract guidance function
thrust_magnitude_function = guidance_model.get_thrust_magnitude

# Create thrust settings from custom model
thrust_magnitude_settings = propagation_setup.thrust.custom_thrust_magnitude( thrust_magnitude_function, specific_impulse = 300.0 )

# Create engine model, and add to Vehicle
environment_setup.add_engine_model( "Vehicle", "MainEngine", thrust_magnitude_settings, system_of_bodies )

