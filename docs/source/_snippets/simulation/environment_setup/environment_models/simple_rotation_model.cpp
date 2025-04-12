Eigen::Quaterniond initialOrientation = ...

double initialTime = ...
double rotationRate = ...

std::string originalFrame = "J2000";
std::string targetFrame = "IAU_Earth";

bodySettings[ "Earth" ]->rotationModelSettings = std::make_shared< SimpleRotationModelSettings >(
    originalFrame, targetFrame , initialOrientation, initialTime, rotationRate );