# Define constant thrust magnitude settings with a deviation from the body-fixed x-axis of 0.5 rad
thrust.constant_thrust_magnitude(
    thrust_magnitude=1.5e3,
    specific_impulse=315,
    body_fixed_thrust_direction=[np.cos(0.5), np.sin(0.5), 0]
)

# Define a variable deflection of TVC from the centreline that varies with time from -0.5rad to +0.5rad
def body_fixed_thrust_direction_function(time):
    TVC_deflection_angle = 0.5*np.sin(time*np.pi/1000)
    return [np.cos(TVC_deflection_angle), np.sin(TVC_deflection_angle), 0]

# Define custom thrust magnitude settings with the variable TVC deflection
thrust.custom_thrust_magnitude( 
	thrust_magnitude_function = lambda t: 1.5e3, 
	specific_impulse_function = lambda t: 315, 
	body_fixed_thrust_direction = body_fixed_thrust_direction_function)
