
# Extract Mach number from fliht conditions
mach_number = vehicle_flight_conditions.mach_number

# Compute angle attach attack according to user-defined guidance law
angle_of_attack = np.deg2rad(30 / (1 + np.exp(-2*(mach_number-9))) + 10)
        
# Update the variables on which the aerodynamic coefficients are based (AoA and Mach)
current_aerodynamics_independent_variables = [self.angle_of_attack, mach_number]
        
# Update the aerodynamic coefficients
aerodynamic_coefficient_interface.update_coefficients(
            current_aerodynamics_independent_variables, current_time)

# Extract the current force coefficients (in order: C_D, C_S, C_L)
current_force_coefficients = aerodynamic_coefficient_interface.current_force_coefficients

# Compute bank angle using guidance law requiring current_force_coefficients as input
bank_angle = ... #=f(current_force_coefficients)
