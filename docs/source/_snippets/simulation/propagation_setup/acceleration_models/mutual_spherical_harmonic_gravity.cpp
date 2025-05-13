SelectedAccelerationMap accelerationSettings;

int maximumDegreeOfIo = 12;
int maximumOrderOfIo = 12;
int maximumDegreeOfJupiter = 4;
int maximumOrderOfJupiter = 4;

accelerationSettings[ "Io" ][ "Jupiter" ].push_back( std::make_shared< MutualSphericalHarmonicAccelerationSettings >(
    maximumDegreeOfJupiter, maximumOrderOfJupiter, maximumDegreeOfIo, maximumOrderOfIo ) );