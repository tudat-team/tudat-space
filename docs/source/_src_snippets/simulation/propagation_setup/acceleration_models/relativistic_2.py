angular_momentum_vector = ... # 3D vector
acceleration_settings_on_vehicle = dict(
            Mars = [ propagation_setup.acceleration.relativistic_correction(
		use_lense_thirring=True, lense_thirring_angular_momentum = angular_momentum_vector) ] )
