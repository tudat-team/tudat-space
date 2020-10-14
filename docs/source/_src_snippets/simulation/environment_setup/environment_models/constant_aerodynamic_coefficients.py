reference_area = 20.0
drag_coefficient = 1.5
lift_coefficient = 0.3

aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area, [ drag_coefficient, 0, lift_coefficient ]
)
environment_setup.add_aerodynamic_coefficient_interface(
            bodies, "Spacecraft", aero_coefficient_settings );