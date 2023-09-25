
// Earth albedo and thermal radiation with two rings as introduced by Knocke (1988)
// These line can be omitted in real code since this is the default source model for yEarth
bodySettings.at("Earth")->radiationSourceModelSettings =
        extendedRadiationSourceModelSettings({
                albedoPanelRadiosityModelSettings(SecondDegreeZonalPeriodicSurfacePropertyDistributionModel::albedo_knocke, "Sun"),
                delayedThermalPanelRadiosityModelSettings(SecondDegreeZonalPeriodicSurfacePropertyDistributionModel::emissivity_knocke, "Sun")
        }, {6, 12});


// Occulting bodies for source panels
// This can, for example, account for lunar eclipses (Earth occults Sun as seen from Moon)
std::vector<std::string> occultingBodies {"Earth"};

// Moon albedo and thermal with six rings
// The albedo distribution is given by the spherical harmonics distribution of DLAM-1
// More rings are necessary for lower altitudes
bodySettings.at("Moon")->radiationSourceModelSettings =
        extendedRadiationSourceModelSettings({
                albedoPanelRadiosityModelSettings(SphericalHarmonicsSurfacePropertyDistributionModel::albedo_dlam1, "Sun"),
                angleBasedThermalPanelRadiosityModelSettings(95, 385, 0.95, "Sun")
        }, {6, 12, 18, 24, 30, 36}, occultingBodies);