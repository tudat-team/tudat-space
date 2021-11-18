.. _`mga_dsm_trajectory`:

******************************************
Analysis of MGA-DSM trajectories
******************************************

In the following sections the definition and analysis of MGA-DSM trajectories within the context of the CDL is
explained. The code that would be used when studying these trajectories is presented, and the differences between
the definition of trajectories with and without DSMs are highlighted. The full codes can be downloaded through:

| :download:`Trajectory without DSMs <_static/mga_noDsm_test.py>`
| :download:`Trajectory with DSMs <_static/mga_dsm_test.py>`

An MGA-DSM trajectory is defined using the ``MgaDsmTrajectory`` class, thus requiring the following import statement

.. code-block:: python

    from MgaDsmTrajectory import MgaDsmTrajectory
.. End of code block

Although not strictly necessary, the following import statement is also used here, as the constants defined in TudatPy
are helpful when selecting some parameters.

.. code-block:: python

    from tudatpy.kernel import constants
.. End of code block


Each trajectory is defined as a series of nodes (the planets where the gravity-assists are executed) connected by a
series of legs (which may or may not have DSMs).


1. Selection of trajectory settings
-------------------------------------------------

The first step necessary is the creation of an object of the ``MgaDsmTrajectory`` class. This requires defining the
sequence of planets for the gravity-assists and the type of legs used. The leg type can either be
``'unpowered_unperturbed_leg_type'`` (legs without DSMs) or
``'dsm_velocity_based_leg_type'`` (legs with DSMs defined using the velocity formulation).

.. note::
    The leg types are specified as strings, therefore they should be defined using apostrophes (``'...'``).
.. End of note

Additionally, one may also specify the semi-major axis (:math:`a`) and eccentricity (:math:`e`) of the departure and insertion orbits.
Do note that this is optional, by default it is assumed :math:`a = \infty` and :math:`e=0` (since the patched conics approximation
is used, this means that the spacecraft departs/arrives from/at the edge of the sphere of influence of the departure/arrival planet).

.. warning::
    TODO: SOI explanation necessary?

    TODO: Add some reference for SOI thing

    TODO: worth mentioning here the definition of bodies?
.. End of warning

.. tabs::

    .. tab:: without DSM

        .. literalinclude:: _static/mga_noDsm_test.py
            :language: python
            :lines: 31-49

    .. tab:: with DSM

        .. literalinclude:: _static/mga_dsm_test.py
            :language: python
            :lines: 31-49

.. end of tab


2. Selection of trajectory parameters
-------------------------------------------------

After creating the ``MgaDsmTrajectory`` object, it is necessary to select the various parameters that define the
gravity-assists and DSMs that are executed during the transfer. The number of parameters that needs to be defined and their
meaning can be retrieved with

.. code-block:: python

    transfer_trajectory.print_parameter_definitions()
.. End of code block

In the case of a transfer **without** DSMs one needs to define:

1. Time at departure node
2. Time of flight between each of the following nodes

In the case of a transfer **with** DSMs one needs to define:

1. Time at departure node
2. Time of flight between each of the following nodes
3. Node free-parameters
4. Leg free-parametes

.. note::
    The trajectory free-parameters must always be specified according to the order given above.
.. End of note

.. warning::
    TODO: More detailed definition of free parameters?

    TODO: Musegaas reference
.. End of warning

The selection of the trajectory parameters is done through the ``evaluate()`` function:

.. tabs::

    .. tab:: without DSM

        .. code-block:: python

            # Retrieving duration of julian day from TudatPy's constants
            julian_day = constants.JULIAN_DAY
        .. End of code block

        .. literalinclude:: _static/mga_noDsm_test.py
            :language: python
            :lines: 59-66

    .. tab:: with DSM

        .. code-block:: python

            # Retrieving duration of julian day from TudatPy's constants
            julian_day = constants.JULIAN_DAY
        .. End of code block

        .. literalinclude:: _static/mga_dsm_test.py
            :language: python
            :lines: 59-74

.. end of tab

3. Retrieving transfer trajectory data
--------------------------------------------------------

Having selected the trajectory parameters, it is then possible to retrieve various data from the ``MgaDsmTrajectory``
object. From this point onwards, there is no difference between a trajectory with DSMs and one without.

3.1. Calculation of :math:`\Delta V` and time of flight
==========================================================

The :math:`\Delta V`, :math:`\Delta V` per node (i.e. per gravity-assist), :math:`\Delta V` per leg
(i.e. per DSM) and time of flight can be retrieved via:

.. code-block:: python

    # Delta V
    delta_v = transfer_trajectory.delta_v()
    # Delta V per node
    delta_v_per_node = transfer_trajectory.delta_v_per_node()
    # Delta V per leg
    delta_v_per_leg = transfer_trajectory.delta_v_per_leg()
    # Time of flight
    time_of_flight = transfer_trajectory.time_of_flight()
.. End of code block

3.2. State history and other variables history
==========================================================

Finally, there is a series of functions which allow retrieving the value of different variables throughout the transfer.
Each of these functions returns two objects, both of type ``np.ndarray``, in the form ``variable_history, time_history``.
Although not showed in the examples below, if desired, most of these functions also allow the selection of the number
of values outputted per leg.

.. warning::
    TODO: Is the previous sentence understandable?
.. End of warning

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