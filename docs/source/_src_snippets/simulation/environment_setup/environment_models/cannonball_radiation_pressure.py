# Create radiation pressure settings
 reference_area_radiation = 4.0
 radiation_pressure_coefficient = 1.2
 occulting_bodies = [ "Earth" ]

 radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
     "Sun", reference_area_radiation, radiation_pressure_coefficient, occulting_bodies )

 environment_setup.add_radiation_pressure_interface(
             bodies, "Delfi-C3", radiation_pressure_settings );