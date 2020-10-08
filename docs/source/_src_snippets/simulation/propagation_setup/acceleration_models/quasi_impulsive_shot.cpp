SelectedAccelerationMap accelerationSettings;

std::vector< double > thrustMidTimes = { 1.0 * 3600.0, 2.0 * 3600.0, 3.0 * 3600.0 };

std::vector< Eigen::Vector3d > deltaVValues = { 1.0E-3 * ( Eigen::Vector3d( ) << 0.3, -2.5, 3.4 ).finished( ),
  1.0E-3 * ( Eigen::Vector3d( ) << 2.0, 5.9, -0.5 ).finished( ),
  1.0E-3 * ( Eigen::Vector3d( ) << -1.6, 4.4, -5.8 ).finished( ) };
  
double totalManeuverTime = 90.0;
double maneuverRiseTime = 15.0;

accelerationSettings[ "Apollo" ][ "Apollo" ] = std::make_shared< QuasiImpulsiveShotsAccelerationSettings >(
  thrustMidTimes, deltaVValues, totalManeuverTime, maneuverRiseTime );