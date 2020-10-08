SelectedAccelerationMap accelerationSettings;

accelerationSettings[ "Apollo" ][ "Sun" ].push_back( 
	std::make_shared< AccelerationSettings >( panelled_radiation_pressure_acceleration ) );