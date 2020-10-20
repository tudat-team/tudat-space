double gravitationalParameter = ...
double referenceRadius = ...

Eigen::MatrixXd normalizedCosineCoefficients =  // NOTE: entry (i,j) denotes coefficient at degree i and order j
Eigen::MatrixXd normalizedSineCoefficients =  // NOTE: entry (i,j) denotes coefficient at degree i and order j

std::string associatedReferenceFrame = ...

bodySettings[ "Earth" ]->gravityFieldSettings = std::make_shared< SphericalHarmonicsGravityFieldSettings >(
   gravitationalParameter, referenceRadius, normalizedCosineCoefficients, normalizedSineCoefficients, associatedReferenceFrame );