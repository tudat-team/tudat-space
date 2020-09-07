// set vehicle mass variable
double vehicleMass = 5.0E3;

// set vehicle name variable
std::string vehicleName = "Vehicle"

// assign trivial body as vehicle
bodyMap[vehicleName] = std::make_shared<simulation_setup::Body>();

// set constant vehicle mass
bodyMap[vehicleName]->setConstantBodyMass(vehicleMass);
