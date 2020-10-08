SelectedAccelerationMap accelerationSettings;

bool calculateSchwarzschildCorrection = true;
bool calculateLenseThirringCorrection = true;
bool calculateDeSitterCorrection = true;

std::string primaryBody = "Sun";

const Eigen::Vector3d centralBodyAngularMomentum = ...

accelerationSettings[ "Orbiter" ][ "Mars" ] = std::make_shared< RelativisticAccelerationCorrectionSettings >(
   calculateSchwarzschildCorrection, calculateLenseThirringCorrection,  calculateDeSitterCorrection, primaryBody,
   centralBodyAngularMomentum )