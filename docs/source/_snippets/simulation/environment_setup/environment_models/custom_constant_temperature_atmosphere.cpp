// Outside main
double customDensityFunction( const double altitude, const double longitude, const double latitude, const double time )
{
   // Return a linear combination of the input values
   return 0.5 * altitude + 0.25 * longitude + 0.15 * latitude + 0.1 * time;
}

int main( )
{
  // ...

  // Define atmosphere settings
  double constantTemperature = 250.0;
  double specificGasConstant = 300.0;
  double ratioOfSpecificHeats = 1.4;
  bodySettings[ "Earth" ]->atmosphereSettings = std::make_shared< CustomConstantTemperatureAtmosphereSettings >( 
                                      &customDensityFunction, constantTemperature, specificGasConstant, ratioOfSpecificHeats );

  // ...
}