# Define constant thrust magnitude settings of 1.5kN, an Isp of 315s, and a deviation from the body-fixed x-axis of 0.1 rad.
thrust.constant_thrust_magnitude(
    thrust_magnitude=1.5e3,
    specific_impulse=315,
    body_fixed_thrust_direction=[np.cos(0.1), np.sin(0.1), 0]
)