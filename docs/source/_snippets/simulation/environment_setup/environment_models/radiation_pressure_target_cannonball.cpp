double area = 20.0;
const double radiationPressureCoefficient = 1.2;

// Same occulting bodies for all sources
std::vector<std::string> occultingBodies {"Earth"};

bodySettings.at("TestVehicle")->radiationPressureTargetModelSettings =
        cannonballRadiationPressureTargetModelSettings(
            area, radiationPressureCoefficient, occultingBodies);

// OR

// Different occulting bodies depending on source
// Sun is occulted by Earth and Moon, Earth is occulted by Moon
std::map<std::string, std::vector<std::string>> occultingBodies {
        {"Sun", {"Earth", "Moon"}},
        {"Earth", {"Moon"}}
    };

bodySettings.at("TestVehicle")->radiationPressureTargetModelSettings =
        cannonballRadiationPressureTargetModelSettingsWithOccultationMap(
            area, radiationPressureCoefficient, occultingBodies);