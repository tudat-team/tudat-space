# Define a function for the thrust orientation as a function of time
def thrust_direction_function(time):
    thrust_direction = np.array([0, np.sin(time*np.pi/1000), -np.cos(time*np.pi/1000)])
    return thrust_direction/np.linalg.norm(thrust_direction)

# Define thrust direction settings based on a function of time
thrust.custom_thrust_direction(thrust_direction_function)