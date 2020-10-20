SelectedAccelerationMap accelerationSettings;

accelerationSettings[ "Apollo" ][ "Earth" ].push_back( 
	std::make_shared< AccelerationSettings >( central_gravity ) );