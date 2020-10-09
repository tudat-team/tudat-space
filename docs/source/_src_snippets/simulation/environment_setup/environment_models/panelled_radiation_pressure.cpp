 std::string sourceBody = "Sun";

 std::vector< double > emissivities = { 0.1, 0.0, 0.1, 0.1 };
 std::vector< double > areas = { 4.0, 6.0, 2.3, 2.3 };
 std::vector< double > diffusionCoefficients = { 0.46, 0.06, 0.46, 0.46 };
 
 std::vector< std::string > occultingBodies;
 occultingBodies.push_back( "Earth" );

 std::vector< std::function< Eigen::Vector3d( const double ) > > panelSurfaceNormals;
panelSurfaceNormals.push_back( [ = ]( const double ){ return Eigen::Vector3d::UnitZ( ); } );
panelSurfaceNormals.push_back( [ = ]( const double ){ return - Eigen::Vector3d::UnitZ( ); } );
panelSurfaceNormals.push_back( [ = ]( const double ){ return Eigen::Vector3d::UnitX( ); } );
panelSurfaceNormals.push_back( [ = ]( const double ){ return - Eigen::Vector3d::UnitX( ); } );

 bodySettings[ "Vehicle" ]->radiationPressureSettings[ sourceBody ] = std::make_shared< PanelledRadiationPressureInterfaceSettings >(
     sourceBody, emissivities, areas, diffusionCoefficients, surfaceNormalsInBodyFixedFrameFunctions, occultingBodies );