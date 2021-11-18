.. _`CDL`:

*************
CDL Specifics
*************

.. warning::
    TODO: have a look at the old mga_dsm_analysis_OLD.rst for useful things


State history
#########################################################

The state history with respect to the Sun or the planets of the Solar System can be retrieved via ``state_history()``:

.. code-block:: python

    # State history with respect to the Sun
    state_history_wrt_sun,time_history = transfer_trajectory.state_history()
    # State history with respect to the Sun
    state_history_wrt_sun,time_history = transfer_trajectory.state_history('Sun')
    # State history with respect to Earth
    state_history_wrt_earth, time_history = transfer_trajectory.state_history('Earth')
.. End of code block


Solar flux
#########################################################
The total incident solar flux in the location of the spacecraft can be retrieved with ``total_solar_flux()``:

.. code-block:: python

    # Total solar flux
    total_solar_flux_history, time_history = transfer_trajectory.total_solar_flux()
.. End of code block

Do note that the total solar flux does not take into account the angle of the incident solar radiation, only the
distance between the Sun and the spacecraft.

Additionally, it is possible to compute the effective solar flux, i.e. the solar flux perpendicular to the solar arrays.
Currently, this is done by assuming the solar arrays are always perpendicular to some reference direction.
The options for this reference direction are the Sun-spacecraft vector, planets-spacecraft vectors and the velocity vector.
Thus, the effective solar flux is computed, using ``effective_solar_flux()``, according to:

.. code-block:: python

    # Solar flux perpendicular to spacecraft-Sun vector, which is the same as total_solar_flux()
    effective_solar_flux_history, time_history = transfer_trajectory.effective_solar_flux('Sun')
    # Solar flux perpendicular to velocity vector
    effective_solar_flux_history, time_history = transfer_trajectory.effective_solar_flux('Velocity')
    # Solar flux perpendicular to spacecraft-Earth vector
    effective_solar_flux_history, time_history = transfer_trajectory.effective_solar_flux('Earth')
.. End of code block

.. warning::
    TODO: Check if effective solar flux is ok
.. End of warning

Link budget
#########################################################

The link budget can be retrieved using the ``link_budget()`` function. It requires the definition of:

* Power of the transmitter antenna
* Gain of the transmitter antenna
* Gain of the receiver antenna
* Frequency of the signal

.. code-block:: python

    transmited_power = 27           # [W]
    transmiter_antenna_gain = 10    # [-]
    receiver_antenna_gain = 1       # [-]
    frequency = 1.57542e9           # [Hz]

    # Link budget
    link_budget_history, time_history = transfer_trajectory.link_budget(frequency,
                                                                        transmited_power,
                                                                        transmiter_antenna_gain,
                                                                        receiver_antenna_gain)
.. End of code block

Communications time per day
#########################################################

To calculate the time available for communications per day it is first necessary to define a
ground station, through the ``add_ground_station_simple()`` function.
The ground station is defined by its latitude and longitude, assuming a spherical Earth.

.. code-block:: python

    # Retrieving value of pi from TudatPy's constants
    pi = constants.PI
    # Selecting position of ground station
    station_name = 'Delft'
    station_latitude = 52.0115769 * pi / 180        # [rad]
    station_longitude = 4.3570677 * pi / 180        # [rad]

    # Add ground station
    transfer_trajectory.add_ground_station_simple(station_name,
                                                  station_latitude,
                                                  station_longitude)

.. End of code block

Next, one can retrieve the time available for communications using the ``communications_time_per_day()`` function.
This function requires as input the name of the station being used and the minimum elevation from which
communications with the spacecraft are possible.

.. code-block:: python

    # Selecting minimum elevation
    minimum_elevation = 10 * pi / 180       # [rad]

    # Communications time per day
    comms_time_per_day, time_history = transfer_trajectory.communications_time_per_day(station_name,
                                                                                       minimum_elevation)

.. End of code block