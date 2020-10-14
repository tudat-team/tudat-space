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

radiation_pressure_settings = environment_setup.radiation_pressure.solar_sail( source_body, area, cone_angle, clock_angle,
	front_emissivity_coefficient, back_emissivity_coefficient, front_lambertian_coefficient, back_lambertian_coefficient,
	reflectivity_coefficient, specular_reflection_coefficient, occulting_bodies, central_body)

environment_setup.add_radiation_pressure_interface( bodies, "Vehicle", radiation_pressure_settings )