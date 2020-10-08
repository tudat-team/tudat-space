std::map< double, Eigen::Vector6d > bodyStateHistory ...

std::string frameOrigin = "SSB"
std::string frameOrientation = "J2000"

bodySettings[ "Jupiter" ]->ephemerisSettings = std::make_shared< TabulatedEphemerisSettings >(
    bodyStateHistory, frameOrigin, frameOrientation );