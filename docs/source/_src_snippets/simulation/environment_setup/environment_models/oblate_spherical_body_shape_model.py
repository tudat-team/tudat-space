body_radius = 6378.0E3
body_flattening = 1.0 / 300.0

body_settings.get_body( "Earth" ).shape_settings = environment_setup.shape.oblate_spherical( body_radius, body_flattening )