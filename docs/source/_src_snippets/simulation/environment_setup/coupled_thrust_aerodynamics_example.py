
# Create bodies (same as in any other simulation)
bodies = ...

# Create guidance object
guidance_model = SimpleCustomGuidanceModel( bodies )

# Extract guidance function
thrust_magnitude_function = guidance_model.get_thrust_magnitude
aerodynamic_angle_function = guidance_model.get_aerodynamic_angles

# Create thrust settings from custom model, create engine model and add it to vehicle
thrust_magnitude_settings = environment_setup.thrust.custom_thrust_magnitude( thrust_magnitude_function, specific_impulse = 300.0 )
environment_setup.add_engine_model( "Vehicle", "MainEngine", thrust_magnitude_settings, system_of_bodies )

# Create angle-based rotation model settings for vehicle, create rotation model, and add it to vehicle
rotation_model_settings = environment_setup.rotation_model.aerodynamic_angle_based(
    "Earth", "J2000", "Vehicle_fixed", aerodynamic_angle_function)
environment_setup.add_rotation_model( bodies, "Vehicle", rotation_model_settings )
