source_body = "Sun"

area = 2.0

def cone_angle(): return 0.25

def clock_angle(): return 0.2

front_emissivity_coefficient = 0.4
back_emissivity_coefficient = 0.4
front_lambertian_coefficient = 0.4
back_lambertian_coefficient = 0.4
reflectivity_coefficient = 0.3
specular_reflection_coefficient = 1.0

occulting_bodies = [ "Earth" ]
central_body = "Earth"

body_settings[ "Vehicle"].environment_setup.solar_sail_radiation_interface_settings( source_body, area, cone_angle, clock_angle,
	front_emissivity_coefficient, back_emissivity_coefficient, front_lambertian_coefficient, back_lambertian_coefficient,
	reflectivity_coefficient, specular_reflection_coefficient, occulting_bodies, central_body)