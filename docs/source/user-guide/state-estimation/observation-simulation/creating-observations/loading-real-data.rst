.. _loading_real_data:

==========================
Loading Real Tracking Data
==========================

Minor Planet Center Astrometry
==============================

The `Minor Planet Center <https://www.minorplanetcenter.net/iau/mpc.html>`_ (MPC) collects and disseminates astrometric observations for minor solar system bodies. We have implemented an interface between Tudat and the MPC's observation database, by making use of the `astroquery <https://astroquery.readthedocs.io/en/latest/mpc/mpc.html#observations>`_ Python library.

Loading MPC astrometric observations into Tudat starts with creating a :class:`~tudatpy.data.mpc.BatchMPC` object. Then, data can be loaded into this object by calling the :meth:`~tudatpy.data.mpc.BatchMPC.get_observations` method, which takes a list of small body identifiers and queries all astrometric data of these bodies from the MPC. Subsequently, the data in the object can be filtered by:

- Keeping only data from a given set of observatories
- Removing data from a given set of observatories
- Retaining only data that falls in a given time span

Then, the :class:`~tudatpy.data.mpc.BatchMPC` object can be used to create an :class:`~tudatpy.estimation.observations.ObservationCollection` that contains all remaining data, using the :meth:`~tudatpy.data.mpc.BatchMPC.to_tudat` method. Note that, in the conversion to a Tudat-compatible data set, one has the option to filter any and all space observatories (e.g. WISE, Hubble).

For instance, the following example will retrieve all data from asteroids 433 (Eros), 238 (Hypatia) and 329 (Svea), over a period of 10 years (2010-2020).

.. code-block:: python

    import datetime
    from tudatpy.data.mpc import BatchMPC

    # Create MPC data container
    mpc_container = BatchMPC()

    # Load all data from selected asteroids
    asteroid_MPC_codes = ["433", "238", "329"]
    mpc_container.get_observations(asteroid_MPC_codes)

    # Filter data based on time
    start_epoch = datetime.datetime(2010, 1, 1)
    end_epoch = datetime.datetime(2020, 1, 1)
    mpc_container.filter(epoch_start=start_epoch, epoch_end=end_epoch)

    # Convert data to Tudat-compatible object
    observation_collection = mpc_container.to_tudat(bodies=bodies, included_satellites=None)

Several examples using MPC data can be found on our page with :ref:`estimation examples <estimation_using_real_observations>`.

Deep Space Tracking Radio Data
==============================

Radio tracking data from planetary spacecraft (Doppler, range, astrometry) collected by networks like NASA's Deep Space Network (DSN), ESA's ESTRACK, and the Joint Institute for VLBI ERIC (JIVE) is disseminated through a number of channels, most notably the `PDS geosciences Node <https://pds-geosciences.wustl.edu/dataserv/radio_science.htm>`_, in a variety of data formats.

Tudat supports reading multiple tracking data formats from DSN, ESTRACK and JIVE:

TRK-2-18 Orbit Data File (ODF)
---------------------

The Orbit Data File format is documented `here <https://pds-geosciences.wustl.edu/radioscience/urn-nasa-pds-radiosci_documentation/odf_071710/odf.pdf>`_. These are binary files that Tudat can 'unpack' and put the contents into Tudat-compatible data structures. Since the contents of the radio science data are significantly more complicated than (for instance) optical astrometric data, the loading of the files is done in several steps:

- Each ODF file is loaded into a single :class:`~tudatpy.io.OdfRawFileContents` object. In this step, the contents of the binary file are loaded and put into basic C++/Python data types.
- The list of :class:`~tudatpy.io.OdfRawFileContents` objects are processed, the relevant data combined and data structures set up, resulting in a :class:`~tudatpy.estimation.observations_setup.observations_wrapper.ProcessedOdfFileContents` object (holding all data for a given link ends and observable type):

  - Ramp tables per ground station are created from the combination of all ODF files
  - All observations of a given observable type and link ends from all ODF files are merged into a single object holding the observables and relevant metadata
  - All observation times are converted to TDB

- The properties of the ground stations (ramp tables) are taken from the :class:`~tudatpy.estimation.observations_setup.observations_wrapper.ProcessedOdfFileContents` object and set in the environment using the :func:`~tudatpy.estimation.observations_setup.observations_wrapper.set_odf_information_in_bodies` function.
- Convert the :class:`~tudatpy.estimation.observations_setup.observations_wrapper.ProcessedOdfFileContents` to an object of type :class:`~tudatpy.estimation.observations.ObservationCollection`, which can be used in the estimation.

TRK-2-34 Tracking and Navigation File (TNF)
-------------------------------------------

The TRK-2-34 Tracking and Navigation File format is documented `here <https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/dsn_trk-2-34/dsn_trk-2-34.2021-06-03.pdf>`_. This is another format used by the DSN to store tracking data. Like ODF files, TRK-2-34 files are binary files but have a different internal structure. The :mod:`~tudatpy.data.processTrk234` module provides specialized converters to handle the unique structure of these files and extract tracking observables.

Processing Architecture
^^^^^^^^^^^^^^^^^^^^^^^

The :mod:`~tudatpy.data.processTrk234` module uses a modular converter-based architecture:

1. **Binary File Parsing**: TRK-2-34 files are read and parsed according to their specific binary format structure, extracting raw data records.

2. **Observable-Specific Converters**:

   - **converter.py**: Main converter interface that coordinates the processing of different data types
   - **derivedDoppler.py**: Processes Doppler observables, handling frequency measurements and their conversion to Doppler observables
   - **derivedSraRange.py**: Processes Sequential Ranging Assembly (SRA) range data with appropriate calibrations and corrections
   - **radioBase.py**: Provides base functionality for radio observable processing

3. **Ramp Table Processing** (ramp.py): Extracts frequency ramp information describing how ground station transmission frequencies vary over time.

Usage Example
^^^^^^^^^^^^^

.. code-block:: python

    from tudatpy.data.processTrk234 import processor

    # Process TRK-2-34 files
    tnf_file_paths = ["path/to/file1.tnf", "path/to/file2.tnf"]
    processed_data = processor.process_trk234_files(
        tnf_file_paths,
        spacecraft_name="MarsExpress"
    )

Intermediate Frequency & Modem System (IFMS) Files
--------------------------------------------------

The Intermediate Frequency & Modem System (IFMS) files contain tracking data from ESA's ESTRACK network with a hybrid structure: open-loop data-sets are binary files (except the first one, containing only the standard header), while all other data-sets are stored as ASCII text files.

IFMS files can contain multiple types of tracking observables that are automatically extracted during processing.

File Structure
^^^^^^^^^^^^^^

IFMS files are ASCII text files with 12 columns separated by commas, spaces, or tabs:

1. **sample_number**: Sequential observation identifier
2. **utc_datetime_string**: Observation time in ISO string format (YYYY-MM-DDTHH:MM:SS)
3. **utc_day_of_year**: Day of year representation
4. **tdb_seconds_since_j2000**: Reception time in TDB (seconds since J2000)
5. **reference_body_distance**: Distance to reference body (km, converted to m)
6. **ramp_reference_time**: UTC reference time for frequency ramp (ISO string format)
7. **transmission_frequency_constant_term**: Base transmission frequency (Hz)
8. **transmission_frequency_linear_term**: Frequency ramp rate (Hz/s)
9. **doppler_averaged_frequency_hz**: Time-averaged Doppler frequency shift (Hz)
10. **doppler_predicted_frequency_hz**: Predicted Doppler frequency shift (Hz)
11. **doppler_troposphere_correction**: Tropospheric delay correction (Hz)
12. **doppler_noise_hz**: Noise estimate (Hz)

Lines starting with ``#`` are treated as comments and ignored during processing.

Supported Observable Types
^^^^^^^^^^^^^^^^^^^^^^^^^^

IFMS files can contain data for the following observable types, which are automatically detected and extracted:

1. **dsn_n_way_averaged_doppler**: Time-averaged Doppler frequency measurements (from ``doppler_averaged_frequency_hz`` column)
2. **doppler_measured_frequency**: Instantaneous Doppler frequency measurements (if ``doppler_measured_frequency_hz`` column is present)
3. **n_way_range**: Range measurements derived from light-time data (if ``n_way_light_time`` column is present)

The most common observable type in IFMS files is **dsn_n_way_averaged_doppler**, which represents Doppler measurements averaged over an integration time period.

Loading IFMS Files
^^^^^^^^^^^^^^^^^^

**Single Ground Station**

For observations from a single ground station:

.. code-block:: python

    from tudatpy.estimation.observations_setup.observations_wrapper import observations_from_ifms_files
    from tudatpy.estimation.observations_setup.ancillary_settings import FrequencyBands

    # Load IFMS files for single station
    observation_collection = observations_from_ifms_files(
        ifms_file_names=["path/to/ifms_file1.txt", "path/to/ifms_file2.txt"],
        bodies=bodies,
        target_name="MarsExpress",
        ground_station_name="CEBREROS",
        reception_band=FrequencyBands.x_band,
        transmission_band=FrequencyBands.x_band,
        apply_troposphere_correction=True
    )

**Multiple Ground Stations**

For observations from multiple ESTRACK ground stations (one file per station):

.. code-block:: python

    from tudatpy.estimation.observations_setup.observations_wrapper import observations_from_multi_station_ifms_files
    from tudatpy.estimation.observations_setup.ancillary_settings import FrequencyBands

    # Load IFMS files for multiple stations
    observation_collection = observations_from_multi_station_ifms_files(
        ifms_file_names=["path/to/cebreros_file.txt", "path/to/newNorcia_file.txt"],
        bodies=bodies,
        target_name="MarsExpress",
        ground_station_names=["CEBREROS", "NEW_NORCIA"],
        reception_band=FrequencyBands.x_band,
        transmission_band=FrequencyBands.x_band,
        apply_troposphere_correction=True
    )

.. important::
   The ``ifms_file_names`` and ``ground_station_names`` lists must have the same length, with each file corresponding to the ground station at the same index.

IFMS Processing Steps
^^^^^^^^^^^^^^^^^^^^^

The IFMS file processing automatically performs the following operations:

1. **File Parsing**:

   - Reads ASCII text format with comma, space, or tab separators
   - Ignores comment lines (starting with ``#``)
   - Handles missing columns gracefully with the ``ignoreOmittedColumns`` option
   - Extracts observation data and metadata

2. **Observable Type Detection**:

   - Scans the file columns to identify available tracking data types
   - Determines which observable types can be created based on ``observableRequiredDataTypesMap``:

     - ``doppler_averaged_frequency`` → ``dsn_n_way_averaged_doppler``
     - ``doppler_measured_frequency`` → ``doppler_measured_frequency``
     - ``n_way_light_time`` → ``n_way_range``

3. **Time Conversion**:

   - Converts observation times from UTC (ISO string format) to TDB (Barycentric Dynamical Time)
   - Uses SPICE for accurate time scale conversion
   - TDB times are stored as seconds since J2000

4. **Troposphere Corrections** (optional):

   - If ``apply_troposphere_correction=True``, subtracts the tropospheric delay correction from the averaged Doppler frequency:

     .. code-block:: python

         doppler_averaged_frequency -= doppler_troposphere_correction

   - Correction is performed at the file reading stage before observable creation
   - This accounts for signal propagation delays through Earth's troposphere

5. **Ramp Table Extraction**:

   - Extracts transmission frequency information from the file:

     - **Constant term** (``transmission_frequency_constant_term``): Base transmission frequency in Hz
     - **Linear term** (``transmission_frequency_linear_term``): Frequency ramp rate in Hz/s

   - Creates time-dependent frequency models for each ground station
   - Frequency at time :math:`t` is calculated as: :math:`f(t) = f_{\text{constant}} + f_{\text{linear}} \times (t - t_{\text{ramp reference}})`
   - Sets ramp tables in the ground station models within the ``bodies`` system

6. **Observation Collection Creation**:

   - Converts processed data into Tudat's :class:`~tudatpy.estimation.observations.ObservationCollection` format
   - Organizes observations by observable type and link ends
   - Stores ancillary settings (frequency bands, integration times, etc.)

Ground Station Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When processing IFMS files, the ground station properties are automatically configured in the ``bodies`` system:

.. code-block:: python

    # After loading IFMS data, ground stations are automatically set up with:
    # - Transmitting frequency models (including time-dependent ramp tables)
    # - Proper link geometry (transmitter → reflector → receiver)
    # - Frequency band information for signal modeling

The link geometry for IFMS observations follows this structure:

- **Transmitter**: ESTRACK ground station on Earth
- **Reflector**: Spacecraft (e.g., Mars Express, ExoMars TGO)
- **Receiver**: Same ESTRACK ground station on Earth (two-way configuration)

Example: Complete IFMS Processing Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from tudatpy.dynamics import environment_setup
    from tudatpy.estimation.observations_setup.observations_wrapper import observations_from_multi_station_ifms_files
    from tudatpy.estimation.observations_setup.ancillary_settings import FrequencyBands

    # Create system of bodies
    bodies_to_create = ["Earth", "Mars", "Sun", "Moon"]
    global_frame_origin = "SSB"
    global_frame_orientation = "J2000"
    body_settings = environment_setup.get_default_body_settings(
        bodies_to_create, global_frame_origin, global_frame_orientation
    )
    bodies = environment_setup.create_system_of_bodies(body_settings)

    # Add spacecraft
    bodies.create_empty_body("MarsExpress")
    # ... configure spacecraft properties ...

    # Add ESTRACK ground stations to Earth
    environment_setup.add_ground_station(
        bodies.get_body("Earth"),
        "CEBREROS",
        station_position_itrf  # ITRF Cartesian position
    )
    environment_setup.add_ground_station(
        bodies.get_body("Earth"),
        "NEW_NORCIA",
        station_position_itrf  # ITRF Cartesian position
    )

    # Load IFMS tracking data from multiple stations
    observation_collection = observations_from_multi_station_ifms_files(
        ifms_file_names=[
            "data/cebreros_2024_100.txt",
            "data/cebreros_2024_101.txt",
            "data/newNorcia_2024_100.txt"
        ],
        bodies=bodies,
        target_name="MarsExpress",
        ground_station_names=["CEBREROS", "CEBREROS", "NEW_NORCIA"],
        reception_band=FrequencyBands.x_band,
        transmission_band=FrequencyBands.x_band,
        apply_troposphere_correction=True
    )

    # The observation_collection now contains:
    # - All dsn_n_way_averaged_doppler observations (and any other available types)
    # - Observations sorted by observable type and link ends
    # - Proper time tags in TDB
    # - Ground station frequency models (ramp tables) set in bodies
    # - Tropospheric corrections applied
    # - Ready for use in orbit determination
    print(f"Number of observation sets: {observation_collection.get_number_of_observation_sets()}")
    print(f"Observable types: {observation_collection.get_observable_types()}")

FDETS Files
-----------

Tudat also supports the loading of Very Long Baseline Interferometry (VLBI) data in the FDETS format. This format is provided by the Joint Institute for VLBI ERIC (JIVE), a European research infrastructure for radio astronomy. The process for loading these files is similar to handling ODF files, involving parsing the raw file and converting its contents into the standard :class:`~tudatpy.estimation.observations.ObservationCollection` structure. FDETS files are ASCII text format files containing open-loop Doppler measurements, typically produced from the `European VLBI Network (EVN) <https://www.evlbi.org/>`_.

.. code-block:: python

    from tudatpy.estimation.observations_setup.observations_wrapper import observations_from_fdets_files
    from tudatpy.estimation.observations_setup.ancillary_settings import FrequencyBands

    observation_collection = observations_from_fdets_files(
        ifms_file_name="path/to/fdets_file.txt",
        base_frequency=8.4e9,  # X-band uplink frequency in Hz
        column_types=["utc_datetime_string", "signal_to_noise_ratio", 
                      "normalised_spectral_max", "doppler_measured_frequency_hz", 
                      "doppler_noise_hz"],
        target_name="Cassini",
        transmitting_station_name="DSS-43",
        receiving_station_name="DSS-43",
        reception_band=FrequencyBands.x_band,
        transmission_band=FrequencyBands.x_band
    )
