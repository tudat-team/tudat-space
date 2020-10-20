gravitational_parameter = ...

body_settings[ "Earth" ].gravity_field_settings( gravitational_parameter );

body_settings.get_body( "Earth" ).gravity_field_settings = environment_setup.gravity_field.central( gravitational_parameter )