
.. _loading_real_data:

==========================
Loading Real Tracking Data
==========================

Minor Planet Center Astrometry
==============================

The `Minor Planet Center <https://www.minorplanetcenter.net/iau/mpc.html>`_ (MPC) collects and disseminates astrometric observations
for minor solar system bodies. We have implemented an interface between Tudat and the MPC's observation database, by making use
of the `astroquery <https://astroquery.readthedocs.io/en/latest/mpc/mpc.html#observations>`_ Python library.

Loading MPC astrometric observations into Tudat starts with creating a :class:`~tudatpy.data.mpc.BatchMPC` object. Then, data can be loaded into this object by
calling the :meth:`~tudatpy.data.mpc.BatchMPC.get_observations` method, which takes a list of small body identifiers and queries all astrometric data of these bodies from the MPC.
Subsequently, the data in the object can be filtered by:

* Keeping *only* data from a given set of observatories
* Removing data from a given set of observatories
* Retaining *only* data that falls in a given time span

Then, the :class:`~tudatpy.data.mpc.BatchMPC` object can be used to create an :class:`~tudatpy.numerical_simulation.estimation.ObservationCollection` that
contains all remaining data, using the :meth:`~tudatpy.data.mpc.BatchMPC.to_tudat` method. Note that, in the conversion to a Tudat-compatible data set,
one has the option to filter any and all space observatories (e.g. WISE, Hubble).

For instance, the following example will retrieve all data from asteroids 433 (Eros), 238 (Hypatia) and 329 (Svea), over a period of
10 years (2010-2020)

.. code-block:: python

  import datetime
  from tudatpy.data.mpc import BatchMPC

  # Create MPC data container
  mpc_container = BatchMPC()

  # Load all data from given asteroids
  asteroid_MPC_codes = [433, 238, 329]
  mpc_container.get_observations(asteroid_MPC_codes)

  # Filter data based on time
  mpc_container.filter(epoch_start=datetime.datetime(2010, 1, 1), epoch_end=datetime.datetime(2020, 1, 1))

  # Convert data to Tudat-compatible object
  observation_collection = mpc_container.to_tudat(bodies, included_satellites=None)



Several examples using MPC data can be found on our page with :ref:`estimation examples <estimation_using_real_observations>`.

Natural Satellite Data Center Astrometry
========================================

The `Natural Satellite Data Center <http://nsdb.imcce.fr/obspos/obsindhe.htm>`_ is the largest database of astrometric observations
of natural satellites of solar system planets (except Earth's moon). Unlike astrometry from the MPC, there is no
existing library to extract data from this website, and there is more diversity in the layout of the files in the NSDC. For this reason,
some manual steps are required. 

First, the raw NSDC data should be downloaded or copied into a txt file. At the top of this file, one should place the metadata (TODO: link metadata file).
One can then call the process_file function, which will convert this raw data into a CSV file with tudat-compatible observations, with standard settings. 
These standard settings are intended to meet the use cases of the majority of the users. However, it is possible to redefine the output, add intermediate steps,
or only use a fraction of the process by using the underlying functionality.

The following example shows the simplest form of processing the NSDC observations. A more extensive example, including 
how to convert these observations into an observation collection, is available in (TO DO: link example).

.. code-block:: python

     # Load necessary spice kernels
     spice.load_standard_kernels()
     spice.load_kernel('jup344.bsp')

     # Specify data location and 
     folder_path = 'Observations\InnerJovianMoons'
     raw_observation_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]

     # Process files
     for raw_file in raw_observation_files:
        process_file(raw_file,True,'ECLIPJ2000')


Deep Space Tracking Radio Data
==============================

.. note::

    This functionality is still under construction

Radio tracking data from planetary spacecraft (Doppler, range, astrometry) collected by NASA's Deep Space Network (DSN) or
ESA's ESTRACK network is disseminated through a number of channels, most notably the `PDS geosciences Node <https://pds-geosciences.wustl.edu/dataserv/radio_science.htm>`_, in a
variety of data formats.

At the moment, Tudat is set up to read the Orbit Data File (ODF) files, documented `here <https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/dsn_trk-2-18/dsn_trk-2-18.2008-02-29.pdf>`_.
These are binary files that Tudat can 'unpack' and put the contents into Tudat-compatible data structures. Since the contents of the
radio science data are significantly more complicated than (for instance) optical astrometric data, the loading of the files is done in several
steps:

* Each ODF file is loaded into a single :class:`~data.odf.OdfRawFileContents` object. In this step, the contents of the binary file are loaded and put into basic C++/Python data types
* The list of :class:`~data.odf.OdfRawFileContents` objects are processed, the relevant data combined and data structures set up, resulting in a set of :class:`~data.odf.ProcessedOdfFileContents` objects (each holding all data for a given link ends and observable type):

  * Ramp tables per ground station are created from the combination of all ODF files
  * All observations of a given observable type and link ends from all ODF files are merged into a single object holding the observables and relevant metadata
  * All observation times are converted to TDB

* The properties of the ground stations (ramp tables) are taken from the :class:`~data.odf.ProcessedOdfFileContents` object and set in the environment using the :func:`~data.odf.set_odf_information_in_bodies` function
* Convert the :class:`~data.odf.ProcessedOdfFileContents` to an object of type :class:`~tudatpy.numerical_simulation.estimation.ObservationCollection`, which can be used in the estimation

To further use the :class:`~tudatpy.numerical_simulation.estimation.ObservationCollection`

Pseudo-observations from External Ephemerides
=============================================

Using some external source (for instance: SPICE kernels) to compute/extract position observables (e.g. using the 3-dimensional
Cartesian position of a body at an epoch as an 'observable'), and then fitting these observations to a dynamical model in Tudat can be very useful.
In particular, such a procedure allows you to quantify exactly how closely the dynamical model settings used in Tudat can recreate the published orbit.
Using such Cartesian positions from an external data source is sometimes termed using 'pseudo-observations'.

The source of the Cartesian positions is up to the user, but typical sources are:

* Body positions from SPICE kernels. NOTE: SPICE kernels with spacecraft orbits for a large number of planetary missions can be found
* Body positions from JPL Horizons
* TLEs propagated in time using an SGP4 propagator, and rotated to an inertial frame
* SP3c files containing tabulated state histories, typically for Earth-orbiting spacecraft

The Galilean moon state estimation example on :ref:`this page <estimation_using_pseudo_observations>` gives a good examples of the full procedure that can be used
for this, where the states are (in this case) extracted from SPICE kernels.

In Tudat Cartesian position (pseudo-)observations are processed using the :func:`~tudatpy.numerical_simulation.estimation_setup.observation.relative_cartesian_position`
observation model. In addition to creating the :class:`~tudatpy.numerical_simulation.estimation.ObservationCollection`
manually from external data, we provide a function of convenience to generate such pseudo-observations, using the following procedure:

* Create the body for which the pseudo-observations are to be generated in your environment, using the :doc:`ephemeris` tudatpy module. Note that the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.tabulated_from_existing` option can be used to turn any ephemeris settings into tabulated ephemeris settings (which is required if using the same bodies in the estimation).
* Generate relative position observations (and associated observation model settings) using the :func:`~tudatpy.numerical_simulation.estimation.create_pseudo_observations_and_models`

The latter function provides both the observations (as an :class:`~tudatpy.numerical_simulation.estimation.ObservationCollection`),
and a list of :class:`~tudatpy.numerical_simulation.estimation_setup.observation.ObservationSettings` to be used
for simulating the observables. The combination of these two can be used directly for the subsequent steps
of defining estimation settings and performing the estimation.



