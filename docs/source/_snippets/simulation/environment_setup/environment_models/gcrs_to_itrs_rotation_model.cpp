IAUConventions precessionNutationTheory = iau_2006;

std::string originalFrame = "J2000";

bodySettings[ "Earth" ]->rotationModelSettings = boost::make_shared< GcrsToItrsRotationModelSettings >(
   precessionNutationTheory, originalFrame );