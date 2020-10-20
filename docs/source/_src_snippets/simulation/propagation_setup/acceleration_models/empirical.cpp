SelectedAccelerationMap accelerationSettings;

Eigen::Vector3d constantAcceleration = ( Eigen::Vector3d( ) << 0.4, -0.1, 0.05 ).finished( );
Eigen::Vector3d sineAcceleration = ( Eigen::Vector3d( ) << 0.0, 0.02, 0.0 ).finished( );
Eigen::Vector3d cosineAcceleration = ( Eigen::Vector3d( ) << -0.01, 0.0, 0.0 ).finished( );

accelerationSettings[ "Orbiter" ][ "Mars" ] = std::make_shared< EmpiricalAccelerationSettings >(
   constantAcceleration, sineAcceleration, cosineAcceleration );