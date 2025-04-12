std::string sourceBody = "Sun";

double area = 2.0;

std::function< double( const double ) > coneAngle = [ = ]( const double ){ return 0.25; };
std::function< double( const double ) > clockAngle = [ =  ]( const double ){ return 0.2; };

double frontEmissivityCoefficient = 0.4;
double backEmissivityCoefficient = 0.4;
double frontLambertianCoefficient = 0.4;
double backLambertianCoefficient = 0.4;
double reflectivityCoefficient = 0.3;
double specularReflectionCoefficient = 1.0;

std::vector< std::string > occultingBodies; occultingBodies.push_back( "Earth" );
std::string& centralBody = "Earth";

bodySettings[ "Vehicle" ]->radiationPressureSettings[ sourceBody ] = std::make_shared< SolarSailRadiationInterfaceSettings >(
    sourceBody, area, coneAngle, clockAngle, frontEmissivityCoefficient, backEmissivityCoefficient,
    frontLambertianCoefficient, backLambertianCoefficient, reflectivityCoefficient, specularReflectionCoefficient, 
    occultingBodies, centralBody );