initial_state_in_keplerian_elements = ...

epoch_of_initial_state = ...
central_body_gravitational_parameter = ...

frame_origin = "SSB"
frame_orientation = "J2000"

body_settings[ "Jupiter" ].environment_setup.kepler_ephemeris_settings( initial_state_in_keplerian_elements,
	epoch_of_initial_state, central_body_gravitational_parameter, frame_origin, frame_orientation)