std::string originalFrame = "J2000";
std::string targetFrame = "IAU_Earth";

bodySettings[ "Earth" ]->rotationModelSettings = std::make_shared< RotationModelSettings >( spice_rotation_model, 
	originalFrame, targetFrame );