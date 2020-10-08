double loveNumber = 0.1;
double timeLag = 100.0;

SelectedAccelerationMap accelerationSettings;
accelerationSettings[ "Io" ][ "Jupiter" ] = std::make_shared< DirectTidalDissipationAccelerationSettings >(
   loveNumber, timeLag, false, false );