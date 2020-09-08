# instantiate lambert targeter class using Dario Izzo's algorithm.
lambert_targeter = two_body_dynamics.LambertTargeterIzzo(
    departure_position=EARTH_POS_INITIAL_EPOCH,
    arrival_position=MARS_POS_FINAL_EPOCH,
    time_of_flight=FINAL_EPOCH - INTIIAL_EPOCH,
    gravitational_parameter=SUN_GM
    # is_retrograde(default=false)
    # tolerance(default=1e-9)
    # max_iter(default=50) -> (max iterations attempting to achieve tolerance)
)

# calculate the initial and final velocity vectors
v1, v2 = lambert_targeter.get_velocity_vectors()
