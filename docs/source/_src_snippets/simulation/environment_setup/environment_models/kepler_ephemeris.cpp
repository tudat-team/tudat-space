Eigen::Vector6d initialStateInKeplerianElements = ...

double epochOfInitialState = ...
double centralBodyGravitationalParameter = ...

std::string frameOrigin = "SSB";
std::string frameOrientation = "J2000";

bodySettings[ "Jupiter" ]->ephemerisSettings = std::make_shared< KeplerEphemerisSettings >(
    initialStateInKeplerianElements, epochOfInitialState, centralBodyGravitationalParameter, frameOrigin, frameOrientation );