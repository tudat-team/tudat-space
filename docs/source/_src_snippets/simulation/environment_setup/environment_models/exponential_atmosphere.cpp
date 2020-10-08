densityScaleHeight = 7.2E3
constantTemperature = 290.0
densityAtZeroAltitude = 1.225
specificGasConstant = 287.06

bodySettings[ "Earth" ]->atmosphereSettings = std::make_shared< ExponentialAtmosphereSettings >( densityScaleHeight, constantTemperature, 
													densityAtZeroAltitude, specificGasConstant );