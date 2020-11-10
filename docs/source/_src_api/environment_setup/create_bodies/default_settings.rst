.. _default_environment_models:

==========================
Default Environment Models
==========================

To facilitate the creation of the celestial bodies in your simulation, Tudat provides the option of loading default models for a broad range of solar system bodies. Largely, these settings are derived from Spice kernels. When loading the default Spice kernels into Tudat, masses, ephemerides and rotation models of the planets in the solar system are automatically loaded. Loading additional Spice kernels will allow you to generate default settings for additional bodies. Details on loading additional Spice kernels, and on the kernels currently loaded into Tudat by default, are given here (see :ref:`spice`)

The following default models are used by Tudat when loaded:

* **Ephemeris** Directly from Spice (any body available through Spice kernels)
* **Rotation model** Directly from Spice (any body available through Spice kernels). For body Foo, Tudat uses the frame IAU_Foo defined in Spice as the body-fixed frame
* **Shape model** Directly loaded from Spice (any body available through Spice kernels). Tudat uses the average radius from Spice to define a spherical shape model for all bodies

* **Gravity field**

  * Point-mass gravity field with gravitational parameter loaded from Spice (any body available through Spice kernels, **unless defined in the list below** )
  * Spheric harmonic gravity field for (note that these are not, in all cases, the most accurate models available):

    * Earth: Full gravity field up to degree and order 360 (EGM96)
    * Moon: Full gravity field up to degree and order 200 (lpe200)
    * Mars: Full gravity field up to degree and order 120 (jgmro120d)
    * Jupiter: Zonal coefficients up to degree 8 from `Iess et al. (2018) <https://www.nature.com/articles/nature25776/>`_
    * Galilean Moons (Io, Europa, Ganymede, Callisto), :math:`\mu`, :math:`C_{20}` and :math:`C_{22}` from IMCCE ephemerides

* **Atmosphere**

  * All bodies: none (unless defined below)
    * Earth: US76 standard atmosphere, as loaded from a tabulated model

