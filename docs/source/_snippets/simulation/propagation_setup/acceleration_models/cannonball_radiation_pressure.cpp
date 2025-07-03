SelectedAccelerationMap accelerationSettings;

accelerationSettings[ "Apollo" ][ "Sun" ].push_back( 
	std::make_shared< AccelerationSettings >( cannon_ball_radiation_pressure ) );