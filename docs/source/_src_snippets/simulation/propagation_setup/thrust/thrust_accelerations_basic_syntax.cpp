std::shared_ptr< ThrustDirectionGuidanceSettings > thrustDirectionSettings;
std::shared_ptr< ThrustMagnitudeSettings > thrustMagnitudeSettings;

SelectedAccelerationMap accelerationSettingsMap;
accelerationSettingsMap[ "Vehicle" ][ "Vehicle" ].push_back( std::make_shared< ThrustAccelerationSettings >( thrustDirectionSettings, thrustMagnitudeSettings ) );