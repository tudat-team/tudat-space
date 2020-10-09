double bodyRadius = 6378.0E3;

bodySettings[ "Earth" ]->shapeModelSettings = std::make_shared< SphericalBodyShapeSettings >( bodyRadius );