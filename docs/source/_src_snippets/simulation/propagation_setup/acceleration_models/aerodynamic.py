accelerations_on_vehicle = dict(
            Earth = [ propagation_setup.Acceleration.aerodynamic() ] 
        )


accelerations = {"Apollo": accelerations_on_vehicle}

acceleration_models = propagation_setup.create_acceleration_models_dict(
            bodies, accelerations, bodies_to_propagate, central_bodies)
