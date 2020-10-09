double densityScaleHeight = 7.2E3;
double constantTemperature = 290.0;
double densityAtZeroAltitude = 1.225;
double specificGasConstant = 287.06;

bodySettings[ "Earth" ]->atmosphereSettings = std::make_shared< ExponentialAtmosphereSettings >( 
	densityScaleHeight, constantTemperature, densityAtZeroAltitude, specificGasConstant );