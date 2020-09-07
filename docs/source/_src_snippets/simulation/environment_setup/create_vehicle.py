# set vehicle mass variable
vehicle_mass = 5.0E3

# set vehicle name variable
vehicle_name = "Vehicle"

# assign trivial body as vehicle
body_system[vehicle_name] = environment_setup.Body()

# set constant vehicle mass
body_system[vehicle_name].set_constant_body_mass(vehicle_mass)
