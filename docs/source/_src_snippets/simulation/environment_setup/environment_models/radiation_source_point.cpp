// Luminosity given directly
// These lines can be omitted in real code since this is the default source model for the Sun
double luminosity = 3.828e26;  // W
bodySettings.at("Sun")->radiationSourceModelSettings =
        isotropicPointRadiationSourceModelSettings(
                constantLuminosityModelSettings(3.828e26));

// Luminosity given as irradiance at a certain distance
double irradianceAtDistance = 1361;  // W/m²
double distance = 1.496e11;  // m
bodySettings.at("Sun")->radiationSourceModelSettings =
        isotropicPointRadiationSourceModelSettings(
                irradianceBasedLuminosityModelSettings(irradianceAtDistance, distance));