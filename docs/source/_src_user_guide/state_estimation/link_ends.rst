.. _linkEndSetup:

Link ends setup
===============

In TudatPy, an observation model is referred to a set of of link ends. For a one-way range model, for instance, a receiver and transmitter are required, both of which are termed a 'link end'. The :class:`~tudatpy.LinkEndType` defines the full list of possible kinds of link ends. A full list of observation models, as well as the link ends that they require, is given on the page on :ref:`observationModelSetup`, and the associated API documentation page (TODO)

.. _groundStationCreation:

Ground Station Creation
~~~~~~~~~~~~~~~~~~~~~~~

Often, you will need to define the positions of ground stations on celestial bodies to/from which observations are made. Note that in TudatPy, a planetary lander is treated identically to a terrestrial ground station. Presently, the position of a ground station is fixed in the body-fixed frame of the body on which it is located, but modifications to allow a time-varying position (due to tides, continental drift, *etc.*) are planned.

To create a ground station, you provide only its name and position (in one of several coordinate types) to the :func:`~tudatpy.add_ground_station` function. Once created, you may add additional properties to a ground station. See details in (TODO)

Creating a Set of Link Ends
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A set of link ends used for a given observable are stored in a dictionary (in Python). In this dictionary:
 - The key represents the :class:`~tudatpy.LinkEndType`.
 - The value represents the identifier of the link end (spacecraft, ground station, *etc.*) ss a pair of strings. The first entry of the string is the body on which the link end is placed, the second entry the reference point on this body (typically the ground station). In the case where the second entry is empty, the body's center of mass is used. Although using a center of mass is unrealistic for data analysis, such a setup can often be useful for a simulated analysis. An example of defining link ends is given below:

Each type of observable requires a specific combination of *types* of link ends. Below, a number of examples are given for one-, two- and three-way observables

.. code-block:: python
                
    one_way_link_ends = dict( );
    one_way_link_ends[ transmitter ] = ( "Earth", "Graz" );
    one_way_link_ends[ receiver ] = ( "LRO", "" );
    
This defines a link for which the ground station termed Graz on the body called Earth acts as transmitter, and the body called LRO is used as the receiver (in this case placed at the body's center of mass).

An example of link-ends for a two-way link from Graz to LRO and back to Graz is:

.. code-block:: python

    two_way_link_ends = dict( );
    two_way_link_ends[ transmitter ] = ( "Earth", "Graz" );
    two_way_link_ends[ reflector ] = ( "LRO", "" );
    two_way_link_ends[ receiver ] = ( "Earth", "Graz" );

Where the Graz station now acts as both transmitter and receiver. Similarly, the receiver may be different from the transmitter (in what is typically called a three-way observable in Deep Space tracking ), so:

.. code-block:: python

    two_way_link_ends = dict( );
    two_way_link_ends[ transmitter ] = ( "Earth", "Graz" );
    two_way_link_ends[ reflector ] = ( "LRO", "" );
    two_way_link_ends[ receiver ] = ( "Earth", "Matera" );
    
where the signal is transmitter by Graz station, retransmitter or reflected by LRO, and then received by the Matera station.

In addition to this manual creation of link ends, we also have a number of functions that allow you to generate a list of link ends for one- two- and three-way observables (:func:`~tudatpy.one_way_downlink_link_ends`, :func:`~tudatpy.one_way_uplink_link_ends`, :func:`~tudatpy.two_way_link_ends`, :func:`~tudatpy.three_way_link_ends`)