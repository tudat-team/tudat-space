
maximum_degree = 12
maximum_order = 12

accelerations_on_vehicle = dict(
            Earth = [ propagation_setup.Acceleration.spherical_harmonic_gravity(maximum_degree, maximum_order) ] 
        )


accelerations = {"Apollo": accelerations_on_vehicle}

acceleration_models = propagation_setup.create_acceleration_models_dict(
            bodies, accelerations, bodies_to_propagate, central_bodies)
