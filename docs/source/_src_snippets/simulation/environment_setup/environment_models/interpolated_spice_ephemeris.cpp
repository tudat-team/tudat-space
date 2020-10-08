double initialTime = 0.0;
double finalTime = 1.0E8;
double timeStep = 3600.0;

std::string frameOrigin = "SSB";
std::string frameOrientation = "J2000";

bodySettings[ "Jupiter" ]->ephemerisSettings = std::make_shared< InterpolatedSpiceEphemerisSettings >(
    initialTime, finalTime, timeStep, frameOrigin, frameOrientation );