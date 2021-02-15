constant_acceleration = ... #3D vector
sine_acceleration = ... #3D vector
cosine_acceleration = ... #3D vector

acceleration_settings_on_vehicle = dict(
            Vehicle = [ propagation_setup.acceleration.empirical(
		constant_acceleration, sine_acceleration, cosine_acceleration ) ] )
