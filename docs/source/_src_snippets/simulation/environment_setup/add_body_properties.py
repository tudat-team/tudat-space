# Set mass of vehicle
bodies.get( "Vehicle").mass = 5000.0

# Create aerodynamic coefficient interface settings, and add to vehicle
aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area = 50.0,
    constant_force_coefficient = [drag_coefficient,0,0]
)
environment_setup.add_aerodynamic_coefficient_interface(
            bodies, "Vehicle", aero_coefficient_settings );

# Create radiation pressure settings, and add to vehicle
radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
    source_body = "Sun", 
    reference_area = 50.0, 
    radiation_pressure_coefficient = 1.5, 
    occulting_bodies = ["Earth"]
)
environment_setup.add_radiation_pressure_interface(
            bodies, "Vehicle", radiation_pressure_settings );
