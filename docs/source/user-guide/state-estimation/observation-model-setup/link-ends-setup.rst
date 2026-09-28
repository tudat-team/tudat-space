.. _linkEndSetup:

Link Ends Setup
===============

To define an observation model, the various bodies, spacecraft, ground stations, etc. involved in the observation, and their role in the observation, must be defined. For a one-way range model, for instance, the definition of a transmitter and a receiver is required. In Tudat, the transmitter and receiver are both referred to as 'link ends'. The full set of link ends in the observable, and their role in the observable, are stored in the :class:`~tudatpy.estimation.observable_models_setup.links.LinkDefinition`. Below, we describe the steps that are (or may be) required to set up this object.

.. note::

    A :class:`~tudatpy.estimation.observable_models_setup.links.LinkDefinition` object does *not* define the observation model itself, but only the various reference points (link ends) that are required for it. For instance, a one-way range, one-way Doppler and angular position observation may all use an identical :class:`~tudatpy.estimation.observable_models_setup.links.LinkDefinition` (containing a transmitter and a receiver).

.. _groundStationCreation:

Creating Ground Station Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often, you will need to define the positions of ground stations on celestial bodies to/from which observations are made. Note that in Tudat, a planetary lander is treated identically to a terrestrial ground station. The creation of a ground station is done when creating the environment, as one of the properties of a body. See  the :ref:`tudatpy:ground_station` module for available ground station settings.

Below we create settings for a ground station in ``Graz`` and add it to the settings of body ``Earth``:


.. code-block:: python
                
    from tudatpy.dynamics import environment_setup

    body_settings = ...

    graz_station_cartesian_position = [4194426.1, 1162694.5, 4647246.9]
    graz_station_settings = environment_setup.ground_station.basic_station(
        "Graz", graz_station_cartesian_position
    )

    earth_ground_station_settings_list = [graz_station_settings]

    body_settings.get("Earth").ground_station_settings = earth_ground_station_settings_list

You can also define the station position in geodetic or spherical position elements. For instance:

.. code-block:: python

    from tudatpy.astro import element_conversion
    from tudatpy.dynamics import environment_setup

    body_settings = ...

    graz_station_geodetic_position = [539.4, 0.821475864, 0.270409097]
    graz_station_settings = environment_setup.ground_station.basic_station(
        "Graz",
        graz_station_geodetic_position,
        element_conversion.PositionElementTypes.geodetic_position_type,
    )

    earth_ground_station_settings_list = [graz_station_settings]

    body_settings.get("Earth").ground_station_settings = earth_ground_station_settings_list

Besides manually creating ground station settings, we also offer default settings for a number of ground station networks, see the :ref:`tudatpy:ground_station` module for a comprehensive list.
Below we create settings for all DSN stations:

.. code-block:: python

    body_settings.get("Earth").ground_station_settings = environment_setup.ground_station.dsn_stations()

Creating a Link Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The creation of the link definition requires the definition of a set of link ends used for a given observable. These are stored in a dictionary as follows:

- The dictionary key denotes the role in the observation (e.g. receiver, transmitter, *etc.*), given by an entry from the :class:`~tudatpy.estimation.observable_models_setup.links.LinkEndType` enum. For each observation model in the :ref:`API documentation <tudatpy:model_settings>`, it is specified which link end types are required.
- The dictionary value represents the identifier of the link end (spacecraft, ground station, *etc.*), as a :class:`~tudatpy.estimation.observable_models_setup.links.LinkEndId` object.  To use a reference point on a body (for instance, a ground station on Earth or an antenna on a spacecraft), the :func:`~tudatpy.estimation.observable_models_setup.links.body_reference_point_link_end_id` function can be used to create an object of this type. To use the origin (typically, but not necessarily its center of mass) of a body as link end, use the :func:`~tudatpy.estimation.observable_models_setup.links.body_origin_link_end_id` function.  Although using a center of mass is unrealistic for data analysis, such a setup can often be useful for a simulated analysis. Example of defining link ends are given below.

Each type of observable requires a specific combination of *types* of link ends. Below, a number of examples are given for one-, two- and three-way observables (see :ref:`here <two_three_way_observables>` for the distinction between two- and three-way observables when creating observation models):

.. code-block:: python
                
    from tudatpy.estimation.observable_models_setup import links

    one_way_link_ends = {
        links.LinkEndType.transmitter: links.body_reference_point_link_end_id(
            "Earth", "Graz"
        ),
        links.LinkEndType.receiver: links.body_origin_link_end_id("LRO"),
    }

This defines a link for which the ground station termed Graz on the body called Earth acts as transmitter, and the body called LRO is used as the receiver (in this case placed at the body's center of mass).

An example of link-ends for a two-way link from Graz to LRO and back to Graz is shown below, where the Graz station now acts as both transmitter and receiver.

.. Note that below example is a representation of the manual creation of link ends. There are also a number of functions that allow you to generate a list of link ends for one- two- and three-way observables (:func:`~tudatpy.estimation.observable_models_setup.links.one_way_downlink_link_ends`, :func:`~tudatpy.estimation.observable_models_setup.links.one_way_uplink_link_ends`, :func:`~tudatpy.estimation.observable_models_setup.links.two_way_link_ends`, :func:`~tudatpy.estimation.observable_models_setup.links.three_way_link_ends`).


.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links

    two_way_link_ends = {
        links.LinkEndType.transmitter: links.body_reference_point_link_end_id(
            "Earth", "Graz"
        ),
        links.LinkEndType.reflector1: links.body_origin_link_end_id("LRO"),
        links.LinkEndType.receiver: links.body_reference_point_link_end_id("Earth", "Graz"),
    }

Similarly, the receiver may be different from the transmitter (in what is typically called a three-way observable in Deep Space tracking), so:

.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links

    three_way_link_ends = {
        links.LinkEndType.transmitter: links.body_reference_point_link_end_id(
            "Earth", "Graz"
        ),
        links.LinkEndType.reflector1: links.body_origin_link_end_id("LRO"),
        links.LinkEndType.receiver: links.body_reference_point_link_end_id("Earth", "Matera"),
    }
    
where the signal is transmitter by Graz station, retransmitter or reflected by LRO, and then received by the Matera station.

After the creation of the link ends dictionary, the :class:`~tudatpy.estimation.observable_models_setup.links.LinkDefinition` object can be created as:

.. code-block:: python

    from tudatpy.estimation.observable_models_setup import links

    three_way_link_ends = {
        links.LinkEndType.transmitter: links.body_reference_point_link_end_id(
            "Earth", "Graz"
        ),
        links.LinkEndType.reflector1: links.body_origin_link_end_id("LRO"),
        links.LinkEndType.receiver: links.body_reference_point_link_end_id("Earth", "Matera"),
    }
    three_way_link_definition = links.link_definition(three_way_link_ends)
    
where, for this basic example, the link definition is simply a wrapper class for the link ends.

Having defined the link definition, we can :ref:`create the observation model <observationModelSetup>`.
