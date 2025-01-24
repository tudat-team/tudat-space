# Set mass of vehicle
bodies.get( "Vehicle").mass = 5000.0

# Alternative, more extensive, approach to do the same (add constant mass)
#rigid_body_properties = environment_setup.rigid_body.constant_rigid_body_properties( 5000.0 )
#environment_setup.add_rigid_body_properties( bodies, "Vehicle", rigid_body_properties )

# Create aerodynamic coefficient interface settings, and add to vehicle
aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area = 50.0,
    constant_force_coefficient = [drag_coefficient,0,0]
)
environment_setup.add_aerodynamic_coefficient_interface(
            bodies, "Vehicle", aero_coefficient_settings )

# Create radiation pressure settings, and add to vehicle
radiation_pressure_settings = environment_setup.radiation_pressure.cannonball_radiation_target(
    reference_area = 50.0, 
    radiation_pressure_coefficient = 1.5, 
    per_source_occulting_bodies = {"Sun": ["Earth"]},
)
environment_setup.add_radiation_pressure_target_model(
            bodies, "Vehicle", radiation_pressure_settings )
