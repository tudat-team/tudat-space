std::string sourceBody = "Sun";

double area = 20.0;
const double radiationPressureCoefficient = 1.2;

std::vector< std::string > occultingBodies;
occultingBodies.push_back( "Earth" );

bodySettings[ "TestVehicle" ]->radiationPressureSettings[ sourceBody ] = std::make_shared< CannonBallRadiationPressureInterfaceSettings >(
    sourceBody, area, radiationPressureCoefficient, occultingBodies );