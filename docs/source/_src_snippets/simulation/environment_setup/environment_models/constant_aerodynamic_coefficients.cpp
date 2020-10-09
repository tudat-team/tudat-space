double referenceArea = 20.0;

Eigen::Vector3d constantCoefficients;
constantCoefficients( 0 ) = 1.5;
constantCoefficients( 2 ) = 0.3;

bodySettings[ "TestVehicle" ]->aerodynamicCoefficientSettings = std::make_shared< ConstantAerodynamicCoefficientSettings >(
    referenceArea, constantCoefficients, true, true );