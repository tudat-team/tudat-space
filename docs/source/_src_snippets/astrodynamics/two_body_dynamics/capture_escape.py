# compute delta V required for Earth escape/departure from/to 100 km LEO
# requiring/exhibiting 1 km/s excess velocity
ΔV = two_body_dynamics.compute_escape_or_capture_delta_v(
    gravitational_param=EARTH_GM,
    semi_major_axis=EARTH_R + 100E3,  # 100 km LEO
    eccentricity=0.0,  # circular parking orbit
    excess_velocity=1E3  # 1 km/s needed in heliocentric
)
