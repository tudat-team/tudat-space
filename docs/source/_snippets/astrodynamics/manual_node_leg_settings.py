# Define the order of bodies (nodes) for gravity assists
transfer_body_order = ['Earth', 'Venus', 'Venus', 'Earth',  'Jupiter',  'Saturn']

# define ToF values per leg
time_of_flight = np.array([1.97844702e+07, 6.68197546e+07, 1.00154317e+07, 3.2306349e+8, 4.21392438e+8]) #s

# define number of revolutions per leg
number_of_revolutions = np.array([2, 0, 1, 1, 0]) 

# Define the departure and insertion orbits
departure_semi_major_axis = np.inf
departure_eccentricity = 0.
arrival_semi_major_axis = 1.0895e8 / 0.02
arrival_eccentricity = 0.98

# Determine number of legs and GA's
no_of_legs = len(transfer_body_order) - 1
no_of_gas = len(transfer_body_order) - 2

#Create transfer leg settings
transfer_leg_settings = []
for i in range(no_of_legs):
    radial_velocity_functions = shape_based_thrust.recommended_radial_hodograph_functions(time_of_flight)
    normal_velocity_functions = shape_based_thrust.recommended_normal_hodograph_functions(time_of_flight)
    axial_velocity_functions = shape_based_thrust.recommended_axial_hodograph_functions(time_of_flight,
                                                              number_of_revolutions)
    transfer_leg_settings.append(transfer_trajectory.hodographic_shaping_leg( 
        radial_velocity_functions, normal_velocity_functions, axial_velocity_functions))

#Create transfer node settings
transfer_node_settings = []
transfer_node_settings.append( transfer_trajectory.departure_node(departure_semi_major_axis, departure_eccentricity) )
for i in range(no_of_gas):
    transfer_node_settings.append( transfer_trajectory.swingby_node() )
transfer_node_settings.append( transfer_trajectory.capture_node(arrival_semi_major_axis, arrival_eccentricity) )

