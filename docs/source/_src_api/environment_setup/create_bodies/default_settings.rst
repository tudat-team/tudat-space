==========================
Default Environment Models
==========================

To facilitate the creation of the celestial bodies in your simulation, Tudat provides the option of loading default models for a broad range of bodies. Largely, these settings are derived from Spice kernels, and loading additional Spice kernels will allow you to generate default settings for additional bodies. Details on loading additional Spice kernels, and on the kernels currently loaded into Tudat by default, are given here (TODO)

The following default models are used by Tudat when loaded:

- **Ephemeris** Directly from Spice (all bodies)
- **Rotation model** Directly from Spice (all bodies). For body Foo, Tudat uses the frame IAU_Foo defined in Spice as the body-fixed frame
- **Shape model** Directly loaded from Spice (all bodies). Tudat uses the average radius from Spice to define a spherical shape model for all bodies
- **Gravity field** 
	- All bodies (unless defined below). Point-mass gravity field with gravitational parameter loaded from Spice (TODO list below)
	- Earth
	- Moon
	- Mars
	- Galilean moons (Io, Europa, Ganymede, Callisto)
**Atmosphere** 
	- All bodies: none (unless defined below)
	- Earth: US76 standard atmosphere, as loaded from a tabulated model


