Eigen::Vector6d constantCartesianState = ...

std::string frameOrigin = "SSB";
std::string frameOrientation = "J2000";

bodySettings[ "Jupiter" ]->ephemerisSettings = std::make_shared< ConstantEphemerisSettings >(
    constantCartesianState, frameOrigin, frameOrientation );