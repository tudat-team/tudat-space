// Occulting bodies can also be specified as map (see cannonball target)
std::vector<std::string> occultingBodies {"Earth"};

bodySettings.at("TestVehicle")->radiationPressureTargetModelSettings =
       paneledRadiationPressureTargetModelSettings({
                // Panel properties: area, specular reflectivity, diffuse reflectivity, with/without instantaneous reradiation, normal vector
                // The normal vector is given in the spacecraft local frame
                // Absorptivity is calculated as 1 - (specular reflectivity + diffuse reflectivity)

                // Body panels, similarly for Y and Z
                TargetPanelSettings(2.82, 0.29, 0.22, true, Eigen::Vector3d::UnitX()),
                TargetPanelSettings(2.82, 0.39, 0.19, true, -Eigen::Vector3d::UnitX()),
                // Solar array tracks the Sun
                TargetPanelSettings(11.0, 0.05, 0.05, true, "Sun"),
                TargetPanelSettings(11.0, 0.30, 0.20, true, "Sun", false)
        }, occultingBodies);