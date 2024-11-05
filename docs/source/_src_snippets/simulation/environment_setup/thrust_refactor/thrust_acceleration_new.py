# Create body rotation settings and create rotation model
rotation_model_settings = ...
environment_setup.add_rotation_model( system_of_bodies, 'Vehicle', rotation_model_settings )

...

# Define settings for thrust magnitude 
thrust_magnitude_settings = ...
# Create engine model with given thrust magnitude
environment_setup.add_engine_model(
    'Vehicle', 'MainEngine', thrust_magnitude_settings, system_of_bodies )

...

# Create acceleration model settings
acceleration_on_vehicle = dict(
    ...,
    Vehicle=[
        propagation_setup.acceleration.thrust_from_engine( 'MainEngine')
    ],
)
