double bodyRadius = 6378.0E3;
double bodyFlattening = 1.0 / 300.0;

bodySettings[ "Earth" ]->shapeModelSettings = std::make_shared< OblateSphericalBodyShapeSettings >( bodyRadius, bodyFlattening );