body_identifier = environment_setup.ephemeris.BodiesWithEphemerisData.jupiter
use_circular_coplanar_approximation = False

body_settings.get_body( "Jupiter" ).ephemeris_settings = environment_setup.ephemeris.approximate_planet_positions( body_identifier, use_circular_coplanar_approximation )
