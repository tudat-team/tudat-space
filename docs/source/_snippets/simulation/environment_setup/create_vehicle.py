# assign trivial body as vehicle
body_system.create_empty_body( "Vehicle" )

# set constant vehicle mass
bodies.get( "Vehicle").mass = 5.0E3

# Create aerodynamic coefficient interface settings, and add to vehicle
aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area = 50.0,
    constant_force_coefficient = [1.2,0,0] )
environment_setup.add_aerodynamic_coefficient_interface(
    bodies, "Vehicle", aero_coefficient_settings )

