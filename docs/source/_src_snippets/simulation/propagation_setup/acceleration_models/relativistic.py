use_schwarzschild = True
use_lense_thirring = True
use_de_sitter = True

de_sitter_central_body = "Sun"
lense_thirring_angular_momentum = ... # 3D vector

acceleration_settings_on_vehicle = dict(
            Mars = [ propagation_setup.acceleration.relativistic_correction(
		use_schwarzschild, use_lense_thirring, use_de_sitter, 
		de_sitter_central_body, lense_thirring_angular_momentum) ] )
