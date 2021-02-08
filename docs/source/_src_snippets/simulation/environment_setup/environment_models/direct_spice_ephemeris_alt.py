frame_origin = 'SSB'
frame_orientation = 'J2000'
body_name_to_use =  'Jupiter'
body_settings.get( "CustomBody" ).ephemeris_settings = environment_setup.ephemeris.direct_spice( 
	frame_origin, frame_orientation, body_name_to_use )
