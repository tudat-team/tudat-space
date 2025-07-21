.. _times_and_dates:

===============
Times and dates
===============

A proper definition of epochs, time intervals, time scales, dates, *etc.* is essential for setting up a proper numerical simulation, and for data analysis. In Tudat, the time defined inside the numerical propagation is always defined using J2000 epoch (01-01-2000, 12:00:00) as reference epoch, in TDB scale. This choice and definition is 'inherited' from SPICE, which is typically used in Tudat to determine the state and orientation of solar system bodies. When defining or providing a ``time`` to any function in Tudat, this can typically be either simply a ``float`` (or ``double`` in C++) or a :class:`~tudatpy.astro.time_conversion.Time` object (see :ref:`below <internal_time>`), both of which denote the seconds since J2000 epoch in TDB scale. Note that the difference between TDB (dynamical barycentric time) and TT (terrestrial time) is purely periodic and on the order of millisecond. For many applications, the two can be see as equivalent.

However, seconds since J2000 in TDB is not a very intuitive quantity to provide for a user. Therefore, functionality is provided to convert between different time scale and representations:

* Conversion between calendar dates and times and seconds since J2000
* Conversion of time between different time scales (UTC, UT1, TAI, TDB, TT)

Calendar dates and times
========================

Tudat comes with its own class to represent an epoch as a calendar date and time, which is driven by the need for extremely accurate representations of time that occur in some astrodynamics applications, in particular with regards to tracking data (10 picoseconds of light-time error corresponds to 3 mm of range error).
The specifics are described in the :class:`~tudatpy.astro.time_conversion.DateTime` documentation. In summary, this class allows the definition of epochs with approximately femtosecond resolution. For compatibility, a conversion between the ``datetime`` class from Python's ``datetime`` library is provided in Tudat, with the note that this class can represent time to microsecond resolution. The :class:`~tudatpy.astro.time_conversion.DateTime` class in Tudat contains member functions that allow it to be converted to seconds since J2000, Julian day, modified Julian day, or an ISO string representing time. An overview is given on the API documentation. 

Below is an example of defining the current date and time through the Python ``datetime`` class, or through Tudat's :class:`~tudatpy.astro.time_conversion.DateTime` class.

.. code-block:: python

  from datetime import datetime
  from tudatpy.astro import time_conversion

  # Create Python datetime object
  python_datetime = datetime.fromisoformat('2023-06-20T00:05:23.281765')

  # Convert to Tudat DateTime object
  tudat_datetime = time_conversion.datetime_to_tudat( python_datetime )

  # Extract single-valued epoch in different scales from Tudat object
  seconds_since_j2000 = tudat_datetime.epoch( )
  julian_day = tudat_datetime.julian_day( )
  modified_julian_day = tudat_datetime.modified_julian_day( )

Note that the inverse operations, creating a :class:`~tudatpy.astro.time_conversion.DateTime` object from an epoch (:func:`~tudatpy.astro.time_conversion.date_time_from_epoch`),
an iso string (:func:`~tudatpy.astro.time_conversion.date_time_from_iso_string`), or directly from the year, month, day and time
(:class:`~tudatpy.astro.time_conversion.DateTime`  constructor) are also available.

In the above, the ``epoch`` is a floating point value, that can be used as input to (for instance) a numerical propagation.
Note that this epoch may need to be converted to a different time scale (see below).

Julian days
===========

In astrodynamics, the use of a Julian day (full days since 12:00 on 01-01-4713BC of the Julian calendar) or modified Julian day (full days since 00:00 of 17-11-1858 of the Gregorian calendar)
continues to be prevalent. Although these time representations are not used directly inside Tudat, we do offer a number of useful conversion functions
to support (modified) Julian days as input or output. Both quantities can be extracted directly as attributes from the :class:`~tudatpy.astro.time_conversion.DateTime` class.
The function :func:`~tudatpy.astro.time_conversion.seconds_since_epoch_to_julian_day` can be used to convert the typical Tudat time of seconds since J2000 epoch to a Julian day,
and :func:`~tudatpy.astro.time_conversion.julian_day_to_seconds_since_epoch` the inverse operation.

Conversion between time scales
==============================

Users will often define epochs in UTC scale, whereas the Tudat propagation requires time in TDB scale. The different time scales are described very well in `USNO circular 179 <https://aa.usno.navy.mil/downloads/Circular_179.pdf>`_. The Tudat methods for converting between time scales rely heavily in the SOFA software, for which the documentation on `SOFA Time Scale and Calendar Tools <https://www.iausofa.org/sofa_ts_c.pdf>`_ provides additional useful information.

Tudat supports the automatic conversion between the following time scales:

* Universal Time UT1, based on Earth rotation
* Coordinated Universal Time UTC, the primary time standard used globally
* International Atomic Time TAI, which differs from UTC through leap seconds (UTC incorporates leap seconds, TAI does not)
* Terrestrial Time TT, equivalent to TAI with an offset of 32.184 seconds
* Barycentric Dynamical Time TDB, the time scale in which solar system ephemerides are often disseminated, related to TT through a four-dimensional relativistic conversion linear scaling
* Geocentric coordinate time TCG, a coordinate time for 'geocentric' applications, related to TT by a linear scaling
* Barycentric coordinate time TCB, a coordinate time for 'barycentric' applications, related to TDB by a linear scaling

Conversion between each of these time scales can be done using the :class:`~tudatpy.astro.time_conversion.TimeScaleConverter`, which can convert an epoch from and to any one of the above time scales. Below is an example of how to convert an epoch from one time scale to another:

.. code-block:: python

  from tudatpy.astro import time_conversion

  # Create time scale converter object
  time_scale_converter = time_conversion.default_time_scale_converter( )

  # Set the epoch in UTC scale (for instance from the above example using DateTime)
  epoch_utc = tudat_datetime.epoch( )
  epoch_tdb = time_scale_converter.convert_time( 
    input_scale = time_conversion.utc_scale, 
    output_scale = time_conversion.tdb_scale,
    input_value = epoch_utc )

The conversion between UTC and UT1 (the latter of which is used directly to compute Earth rotation) is based on the detailed Earth rotation model as defined in the `IERS 2010 Conventions <https://www.iers.org/SharedDocs/Publikationen/EN/IERS/Publications/tn/TechnNote36/tn36.pdf>`_. The :func:`~tudatpy.astro.time_conversion.default_time_scale_converter` is initialized using default settings for small variations to Earth rotation (see :doc:`the notes here <rotation_model>` on high-accuracy Earth rotation model and the function :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.gcrs_to_itrs`). The conversion between geocentric scales (TT/TCG) and barycentric scales (TDB/TCB) is performed using the model implemented in SOFA for TT-TDB, which is a series expansion with about 800 terms, based on a numerical solution to the governing equation of the transformation. This conversion is accurate to the level of several nanoseconds. For higher accuracy in this conversion, numerical computation of these time scales, consistent with a given solar system ephemeris, should be used. Data for such conversions is shipped with recent INPOP ephemerides (for instance).

Formally, the conversion from TT to TDB (and therefore also UTC to TDB) depends on the geocentric position at which the time in TT/UTC is registered. This effect is very small, with the largest effect a daily periodic variation on the order of several microseconds.

.. _internal_time:

Using time representations
==========================

The :class:`~tudatpy.astro.time_conversion.DateTime` class described above is used for converting between typical representations of time and a single numerical epoch. It is not used as the representation of time in the propagation, simulation of obsevations *etc.* For this, we have a dedicated :class:`~tudatpy.astro.time_conversion.Time` class. This class provides a numerical representation of time (both epochs and intervals) with a better resolution that what is provided by a simple ``float``. Using a ``float``, we can represent time over a period of 100 years with a resolution of a microsecond. For some applications, this is insufficient, since it also means that the representation of time intervals (from the subtraction of two epochs) is limited to the same resolution. The :class:`~tudatpy.astro.time_conversion.Time` class provides a two-component representation of time (integer hours since J2000, and number of seconds into the current hour). This provides sub-picosecond resolution in time over essentially arbitrary time intervals.

Unlike the :class:`~tudatpy.astro.time_conversion.DateTime` class, the :class:`~tudatpy.astro.time_conversion.Time` class supports arithmetic operations, so that it can be used to represent an epoch (with the 0 value defined as J2000) or a time interval. It can also be down-converted to a ``float`` to be used, and conversely be created from a ``float``. The ``Time`` class is implemented in C++, and using pybind11's functionality, it can be implicitly coverted to/from a ``float``. This means that any function that takes a ``float`` as input can take a ``Time`` as input (and vice versa). For instance, the following code (to create translational state propagator settings)

.. code-block:: python

    # Define translational propagator settings
    translational_propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_state,
        simulation_start_epoch,
        integrator_settings,
        termination_settings )
    ]

can be called with ``simulation_start_epoch`` being an object of type ``Time`` (as is technically required by :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational`), but also using a ``float`` as input. In the latter case, it will be automatically converted to a ``Time`` object. Although this would provide the initial time a the lower resolution provided by ``float``, it will ensure that all subsequent operations are performed at high numerical resolution. Therefore, by default the time representation there is a ``float``.

A typical input for a simulation is a calendar day and time in UTC. This needs to be converted to TDB before being input to a Tudat simulation for (for instance) an observation or propagation epoch. This conversion can be done in either type (``float`` and ``Time``) Below is an example code block using a ``Time`` object

.. code-block:: python

    # Create current date/time object in utc
    date_time_utc = DateTime(2025, 7, 21, 11, 4, 45.2)

    # Convert date/time UTC to an epoch with full resolution (as Time object)
    epoch_utc = date_time_utc.epoch_time_object()

    # Convert epoch to TDB (as Time object)
    epoch_tdb = time_scale_converter.convert_time_object(
        input_scale = time_conversion.utc_scale,
        output_scale = time_conversion.tdb_scale,
        input_value = epoch_utc )

and using a ``float``

.. code-block:: python

    # Create current date/time object in utc
    date_time_utc = DateTime(2025, 7, 21, 11, 4, 45.2)

    # Convert date/time UTC to an epoch with float resolution
    epoch_utc = date_time_utc.epoch()

    # Convert epoch to TDB (as float)
    epoch_tdb = time_scale_converter.convert_time(
        input_scale = time_conversion.utc_scale,
        output_scale = time_conversion.tdb_scale,
        input_value = epoch_utc )

In both cases, the ``epoch_tdb`` can be used as input to determine (for instance) propagator settings. The functional differences between the two will typically be minimal (in both cases ``Time`` is used internally for all computations in the propagation), but using the ``Time`` object when defining input ensures no unforeseen rounding errors result in slightly offset results.

Similarly, although internal operations in propagation, *etc.* will be done at high resolution time representation, typical post-processing and analysis of results does not require such resolution. Moreover, using a ``float`` as time representation is easier for plotting, interacting with other libraries and data structures, *etc.* Therefore, the default time representation in output data is a ``float``. For instance, the type of the propagation state history in :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.state_history` is a ``dict[float, np.ndarray]``, where it must be stresses that this is down-converted from the internal representation that uses ``Time`` as independent variable. For users requiring the high-precision time representation as output, the :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.state_history_time_object` is available. A similar structure (functions seemingly duplicated, with one having the ``_time_object`` suffix) can be found in a number of places, which is provided to allow (i) easy interation with output data in ``float`` representation (ii) full resolution data using ``Time`` when users require it.




