acceleration_settings = {"Apollo": acceleration_settings_on_vehicle}

acceleration_models = propagation_setup.create_acceleration_models_dict(
            bodies, acceleration_settings, bodies_to_propagate, central_bodies)