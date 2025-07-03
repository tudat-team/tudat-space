# Define the thrust magnitude function: thrust increases linearly with time
def thrust_magnitude_function(time):
    return 500 + time/2

# Define a lambda specific impulse function: constant at 350s
specific_impulse_function = lambda time: 350

# Define the "engine on" function: engine is off after 50s
def is_engine_on_function(time):
    return time < 50

# Define the custom thrust magnitude settings based on the pre-defined functions
thrust.custom_thrust_magnitude(thrust_magnitude_function, specific_impulse_function, is_engine_on_function)