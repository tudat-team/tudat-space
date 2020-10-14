.. _available_dependent_variables:

Available Dependent Variables
#############################

.. role:: python(code)
   :language: python


- Mach Number :python:`propagation_setup.dependent_variable.mach_number( "Spacecraft", "Earth" )`
- Altitude :python:`propagation_setup.dependent_variable.altitude( "Spacecraft", "Earth" )`
- Airspeed :python:`propagation_setup.dependent_variable.airspeed( "Spacecraft", "Earth" )`
- Density :python:`propagation_setup.dependent_variable.density( "Spacecraft", "Earth" )`

- Relative Speed :python:`propagation_setup.dependent_variable.relative_speed( "Spacecraft", "Earth" )`
- Relative Position :python:`propagation_setup.dependent_variable.relative_position( "Spacecraft", "Earth" )`
- Relative Distance :python:`propagation_setup.dependent_variable.relative_distance( "Spacecraft", "Earth" )`
- Relative Velocity :python:`propagation_setup.dependent_variable.relative_velocity( "Spacecraft", "Earth" )`
- Keplerian State :python:`propagation_setup.dependent_variable.keplerian_state( "Spacecraft", "Earth" )`

- Single Acceleration :python:`propagation_setup.dependent_variable.single_acceleration( point_mass_gravity, "Spacecraft", "Earth" )`
- Single Acceleration Norm :python:`propagation_setup.dependent_variable.single_acceleration_norm( point_mass_gravity, "Spacecraft", "Earth" )`
- Spherical Harmonic Terms Acceleration :python:`propagation_setup.dependent_variable.spherical_harmonics_terms_acceleration( "Spacecraft", "Earth", (2,2) )` TODO: component indices
- Spherical Harmonic Terms Acceleration Norm :python:`propagation_setup.dependent_variable.spherical_harmonics_terms_acceleration_norm( "Spacecraft", "Earth", (2,2) )` TODO: component indices
- Total Acceleration :python:`propagation_setup.dependent_variable.total_acceleration( "Earth" )`
- Total Acceleration Norm :python:`propagation_setup.dependent_variable.total_acceleration_norm( "Earth" )`

- Aerodynamic Force Coefficients :python:`propagation_setup.dependent_variable.aerodynamic_force_coefficients( "Spacecraft" )`
- Aerodynamic Moment Coefficients :python:`propagation_setup.dependent_variable.aerodynamic_moment_coefficients( "Spacecraft" )`

- Latitude :python:`propagation_setup.dependent_variable.latitude( "Spacecraft", "Earth" )`
- Longitude :python:`propagation_setup.dependent_variable.longitude( "Spacecraft", "Earth" )`
- Heading Angle :python:`propagation_setup.dependent_variable.heading_angle( "Spacecraft", "Earth" )`
- Flight Path Angle :python:`propagation_setup.dependent_variable.flight_path_angle( "Spacecraft", "Earth" )`

- Radiation Pressure :python:`propagation_setup.dependent_variable.radiation_pressure( "Spacecraft", "Earth" )`


      


