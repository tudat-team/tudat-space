import pygmo

# Instantiation of the UDP problem
udp = HimmelblauOptimization(-5.0, 5.0, -5.0, 5.0)

# Creation of the pygmo problem object
prob = pygmo.problem(udp)