calculate_schwarzschild_correction = True
calculate_lense_thirring_correction = True
calculate_de_sitter_correction = True

primary_body = "Sun"

central_body_angular_momentum = ... # 3D vector

acceleration_settings_on_vehicle = dict(
            Mars = [ propagation_setup.acceleration.relativistic_acceleration_correction(calculate_schwarzschild_correction,
            								calculate_lense_thirring_correction, calculate_de_sitter_correction, primary_body
            								central_body_angular_momentum) ] 
        )