# Create ground station settings
ground_station_settings = environment_setup.ground_station.basic_station(
    "TrackingStation",
    [station_altitude, delft_latitude, delft_longitude],
    element_conversion.geodetic_position_type)

# Add the ground station to the environment
environment_setup.add_ground_station(
    bodies.get_body("Earth"),
    ground_station_settings )s
    

