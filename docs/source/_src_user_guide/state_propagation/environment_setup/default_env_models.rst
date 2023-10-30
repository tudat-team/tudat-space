.. _default_env_models:

==========================
Default environment models
==========================

.. attention::

  This page is only exact for Tudatpy version >= 0.7. Older versions use several slightly different Spice kernels and gravity fields.
  To use default Spice kernels from older versions, use the :func:`~tudatpy.interface.spice.load_standard_deprecated_kernels` instead of :func:`~tudatpy.interface.spice.load_standard_kernels`

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   default_env_models/default_bodies_limited_time_range 

   
To facilitate the creation of the celestial bodies in your simulation, Tudat provides the option of loading default
models for a broad range of solar system bodies.

.. contents:: Content of this page
   :local:

Many of these settings are derived from so-called Spice kernels. `Spice <https://naif.jpl.nasa.gov/naif/toolkit.html>`_
is a toolkit developed by NASA's Navigation and Ancillary Information Facility (NAIF) and is used throughout the space
industry for the design and analysis of (planetary) missions. In Tudat, we primarily use the modules of spice that deal
with pre-defined ephemerides and rotation models of solar system bodies (see section `Spice in Tudat` below for details on our usage of Spice).

Default settings
=================

Using the data from these Spice kernels into Tudat, the following default models
are used by Tudat when calling the :func:`~tudatpy.interface.spice.load_standard_kernels` function.

Ephemeris
---------

Directly from Spice (see :ref:`spice_in_tudat`). For our default settings, this includes all solar system
planets, the Sun, Earth's moon, the main Martian, Jovian and Saturnian satellites. as well as 300 major solar sysrem asteroids. Users can append this list with additional ephemeris files, for
instance for small bodies or other satellite systems, through the use of the
:func:`~tudatpy.interface.spice.load_kernel`.

Ephemerides from Spice kernels are only valid for a somewhat limited time interval (on the order of one or several centuries, depending on the specific body), which is limited by the valid range of the Spice kernels provided in Tudat by default. You can load additional Spice kernels with a longer coverage by using the :func:`~tudatpy.interface.spice.load_kernel` function for any additional kernels you like (see, for instance, the `generic kernels <https://naif.jpl.nasa.gov/naif/data_generic.html>`_ listed on the Spice website. Note that the contents will override data in the default kernels (if applicable).

.. note::
   In some cases, the extraction of the state of bodies from Spice kernels can be a computational bottleneck. Tudat has an :ref:`alternative set of default options <default_bodies_limited_time_range>`, which make this process signicantly faster, at the expense of higher RAM usage, and an environment that is only valid over a very limited time interval.

.. _default_rotation_models:

Rotation model
--------------

Directly from Spice (see :ref:`spice_in_tudat`). For body ``Foo``, Tudat uses the frame
``IAU_Foo`` defined in Spice as the body-fixed frame. These rotation models are implementations of results published by
the IAU Working Group on Cartographic Coordinates and Rotational Elements.

For the Earth, a high-accuracy rotation model is available, which is *not* loaded by default, but can be added to the default settings using the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.gcrs_to_itrs` function.

.. note::
   In some cases, the extraction of the rotational state of bodies from Spice kernels can be a computational bottleneck. Tudat has an :ref:`alternative set of default options <default_bodies_limited_time_range>`, which make this process signicantly faster, at the expense of higher RAM usage, and an environment that is only valid over a very limited time interval.

Shape model
-----------

Directly from Spice (any body available through Spice kernels). Tudat uses the average radius from Spice to define a
spherical shape model for all bodies.

.. _default_gravity_fields:

Gravity field
-------------

* Spherical harmonic gravity field for the following bodies:

   - **Earth**: Full gravity field up to degree and order 200, described `here <https://link.springer.com/article/10.1007/s10712-016-9406-y>`__ (GOCO05c, data obtained from `GFZ <https://dataservices.gfz-potsdam.de/icgem/showshort.php?id=escidoc:1504398>`__; coefficient are available up to degree/order 720, but are not all loaded by default for efficiency purposes)
   - **Moon**: Full gravity field up to degree and order 200, described `here <https://pgda.gsfc.nasa.gov/products/50>`__ (gggrx1200, data obtained from `PDS <https://pds-geosciences.wustl.edu/grail/grail-l-lgrs-5-rdr-v1/grail_1001/shadr/>`__; coefficient are available up to degree/order 1199, but are not all loaded by default for efficiency purposes)
   - **Mars**: Full gravity field up to degree and order 120, described `here <https://www.sciencedirect.com/science/article/pii/S0019103516001305>`__ (jgmro120d, data obtained from `PDS <https://pds-geosciences.wustl.edu/mro/mro-m-rss-5-sdp-v1/mrors_1xxx/data/shadr/>`__)
   - **Venus**: Full gravity field up to degree and order 180, described `here <https://www.sciencedirect.com/science/article/pii/S0019103599960864>`__ (shgj180u, data obtained from `PDS <https://pds-geosciences.wustl.edu/mgn/mgn-v-rss-5-gravity-l2-v1/mg_5201/gravity/>`__)
   - **Mercury**: Full gravity field up to degree and order 160, described `here <https://www.sciencedirect.com/science/article/pii/S0019103519302192>`__ (jgmess160a, data obtained from `PDS <https://pds-geosciences.wustl.edu/messenger/mess-h-rss_mla-5-sdp-v1/messrs_1001/data/shadr/>`__)
   - **Jupiter**: Zonal coefficients up to degree 8 from, described `here <https://www.nature.com/articles/nature25776/>`__
   - **Galilean Moons** (Io, Europa, Ganymede, Callisto), :math:`\mu`, :math:`C_{20}` and :math:`C_{22}` from IMCCE ephemerides

* For all the other bodies not mentioned above, point-mass gravity field with gravitational parameter loaded from Spice are used
  (for any body available through Spice kernels).

.. warning::
   Temporal variations of the gravity field are zero by default, but can be included for high-accuracy
   applications. See `API reference <https://py.api.tudat.space/en/latest/gravity_field_variation.html#functions>`_

Atmosphere
-----------

- Earth: US76 density model (using interpolation of tabulated data :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.us76`)
- All other bodies: none

Radiation source
----------------
- Sun: Isotropic point source with a luminosity of 3.828 × 10\ :sup:`26` W
- Earth: seasonally varying albedo and thermal model with two rings, described `here <https://doi.org/10.2514/6.1988-4292>`__
- All other bodies: none

.. _c:

.. _spice_in_tudat:

SPICE in Tudat
===============

The ``cspice`` toolkit (version of spice written in the C language) is included in the conda environment when installing
Tudat, and Tudat contains a number of functions to directly interact with spice, listed `here <https://py.api.tudat.space/en/latest/spice.html>`_.

The Spice toolkit has extensive `lessons <https://naif.jpl.nasa.gov/naif/lessons.html>`_, `tutorials <https://naif.jpl.nasa.gov/naif/tutorials.html>`_ and  `detailed documentation <https://naif.jpl.nasa.gov/naif/documentation.html>`_.

Spice relies on a set of user-supplier input files (kernels) to perform its calculations. A number of these kernels are installed automatically with Tudat, and loaded when calling the :func:`~tudatpy.interface.spice.load_standard_kernels` function (see this API docs entry for list of kernels).

When using the default kernels/body settings, we have introduced one small difference for the sake of expediency. For the cases of Uranus, Neptune and Pluto, where we only have the ephemeris of the barycenter of the planetary system loaded, the planet is placed at the barycenter of the planetary system. This introduces a minor offset in the position of this planet (Mercury and Venus have no moons, and therefore their state coincides with their planetary system barycenter; dedicated planetary system ephemerides are loaded for teh Earth, Mars, Jupiter and Saturn system). For Uranus, for example, the default settings will place Uranus at the center of mass (barycenter) of the combined system of Uranus and its moons. To correct this behaviour, a user can load a kernel for this body's planetary system (see `here <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/>`__, for example), and modify the default settings.
