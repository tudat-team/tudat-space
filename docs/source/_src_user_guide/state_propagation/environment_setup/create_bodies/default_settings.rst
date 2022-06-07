.. _default_environment_models:

==========================
Default environment models
==========================

To facilitate the creation of the celestial bodies in your simulation, Tudat provides the option of loading default
models for a broad range of solar system bodies.

.. contents:: Content of this page
   :local:

About SPICE
===========

Largely, these settings are derived from so-called Spice kernels. `Spice <https://naif.jpl.nasa.gov/naif/toolkit.html>`_
is a toolkit developed by NASA's Navigation and Ancillary Information Facility (NAIF) and is used throughout the space
industry for the design and analysis of (planetary) missions. In Tudat, we primarily use the modules of spice that deal
with pre-defined ephemerides and rotation models of solar system bodies (see section `SPICE in Tudat` below).

Default settings
=================

Using the data from these Spice kernels into Tudat, the following default models
are used by Tudat when calling the :func:`~tudatpy.interface.spice.load_standard_kernels` function.

Ephemeris
---------

Directly from Spice (any body available through Spice kernels). For our default settings, this includes solar system
planets and Martian, Jovian and Saturnian satellites. Users can append this list with additional ephemeris files, for
instance for small bodies or other satellite systems, through the use of the
:func:`~tudatpy.interface.spice.load_kernel`.

.. note:: 
  Note that the ephemerides that are used by default are only valid for a somewhat limited time interval (on the order of a century, depending on the specific body).


Rotation model
--------------

Directly from Spice (any body available through Spice kernels). For body ``Foo``, Tudat uses the frame
``IAU_Foo`` defined in Spice as the body-fixed frame. These rotation models are implementations of results published by
the IAU Working Group on Cartographic Coordinates and Rotational Elements.

Shape model
--------------

Directly from Spice (any body available through Spice kernels). Tudat uses the average radius from Spice to define a
spherical shape model for all bodies.

Gravity field
-------------------


* Spherical harmonic gravity field for the following bodies:

    - Earth: Full gravity field up to degree and order 720 (GOCO05c)
    - Moon: Full gravity field up to degree and order 1199 (gggrx1200)
    - Mars: Full gravity field up to degree and order 120 (jgmro120d)
    - Jupiter: Zonal coefficients up to degree 8 from `Iess et al. (2018) <https://www.nature.com/articles/nature25776/>`_
    - Galilean Moons (Io, Europa, Ganymede, Callisto), :math:`\mu`, :math:`C_{20}` and :math:`C_{22}` from IMCCE ephemerides

* For all the other bodies not mentioned above, point-mass gravity field with gravitational parameter loaded from Spice
  (any body available through Spice kernels).

.. warning::
   Temporal variations of the gravity field are zero by default, but they should be included for high-accuracy
   applications.

Atmosphere
-----------

- Earth: NRLMSISE-00 density model
- All other bodies: none

.. todo::
   Add something about NRLMSISE-00 model and how it is compiled in Tudat?


SPICE in Tudat
===============

The ``cspice`` toolkit (version of spice written in the C language) is included in the conda environment when installing
tudat, and Tudat contains a number of functions to directly interact with spice.
Spice relies on a set of user-supplier input files, or 'kernels' to perform its calculations.
A number of these kernels are installed automatically with Tudat; specifically, Tudat comes with the following Spice
kernels:

* Ephemerides and masses:

  - Solar system planets, Sun, Moon, Pluto: DE440(ephemerides)/DE431(masses) ( (time interval, 1750-2499)
  - Martian satellites Phobos and Deimos: NOE-4-2020 (time interval, 1975-2049)
  - Jovian satellites Io, Europa, Ganymede, Callisto: NOE-5-2021 (time interval, 1880-2049)
  - Saturnian satellites Mima, Enceladus, Tethys, Dione, Rhea, Titan : NOE-6-2018 (time interval, 1975-2049)

* Other solar system body properties (rotation models, shapes, *etc.*): PCK0010
* Leap second kernel: NAIF0012

.. note::
   Some kernels have been reduced in size, so that we can host them through Github, and ship them with Tudat.

.. seealso::
   See `here <https://tudatpy.readthedocs.io/en/latest/spice.html>`_ for all available functions in our spice
   interface).