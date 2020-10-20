SelectedAccelerationMap accelerationSettings;

int maximumDegree = 12;
int maximumOrder = 12;

accelerationSettings[ "Apollo" ][ "Earth" ].push_back( 
	std::make_shared< SphericalHarmonicAccelerationSettings >( maximumDegree, maximumOrder ) );