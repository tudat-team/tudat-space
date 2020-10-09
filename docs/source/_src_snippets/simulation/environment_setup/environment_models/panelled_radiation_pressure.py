source_body = "Sun"

emissivities = [0.1, 0.0, 0.1, 0.1]
areas = [4.0, 6.0, 2.3, 2,3]
diffusion_coefficients = [0.46, 0.06, 0.46, 0.46]

occulting_bodies = [ "Earth" ]

panel_surface_normals = [ [0.0, 0.0, 1.0], [0.0, 0.0, -1.0],
						[1.0, 0.0, 0.0], [-1.0, 0.0, 0.0] ] 

body_settings[ "Vehicle" ].environment_setup.panelled_radiation_pressure_settings( source_body, emissivities,
	areas, diffusion_coefficients, surfaceNormalsInBodyFixedFrameFunctions, occulting_bodies )