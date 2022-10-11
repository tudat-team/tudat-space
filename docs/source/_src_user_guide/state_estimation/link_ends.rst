.. _linkEndSetup:

Link ends setup
===============

To define an observation model, the various bodies, spacecraft, ground stations, etc. involved in the observation, and their role in the observation, must be defined. For a one-way range model, for instance, a definition of a receiver and a transmitter is required. In Tudat, the transmitter and receiver are both referred to as 'link ends'. The full set of link ends in the observable, and their role in the observable, are stored in the :class:`~tudatpy.numerical_simulation.estimation.LinkDefinition`. Below, we describe the steps that are (or may be) required to set up this object. 

.. note::
A :class:`~tudatpy.numerical_simulation.estimation.LinkDefinition` object does *not* define the observation model itself, but only the various reference points (link ends) that are required for it. For instance, a one-way range, one-way Doppler and angular position observation may all use an identical ``LinkDefinition`` (containing a transmitter and a receiver). 

.. _groundStationCreation:

Ground Station Creation
~~~~~~~~~~~~~~~~~~~~~~~

Often, you will need to define the positions of ground stations on celestial bodies to/from which observations are made. Note that in Tudat, a planetary lander is treated identically to a terrestrial ground station. The creation of a ground station is described in the :ref:`environment setup <ground_stations>`.

Creating a Set of Link Ends
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The creation of the link definition requires the definition of a set of link ends used for a given observable. These are stored in a dictionary as follows:

 - The dictitonary key represents the :class:`~tudatpy.numerical_simulation.estimation_setup.LinkEndType`, denoting the role in the observation (e.g. receiver, transmitter, *setc.*)
 - The dictitonary  value represents the identifier of the link end (spacecraft, ground station, *etc.*). The basic creation of a link definition requires a pair of strings for each link end. The first entry of the string is the body on which the link end is placed, the second entry the reference point on this body (typically the ground station). In the case where the second entry is empty, the body's center of mass is used. Although using a center of mass is unrealistic for data analysis, such a setup can often be useful for a simulated analysis. An example of defining link ends is given below:

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

In addition to this manual creation of link ends, we also have a number of functions that allow you to generate a list of link ends for one- two- and three-way observables (:func:`~tudatpy.one_way_downlink_link_ends`, :func:`~tudatpy.numerical_simulation.estimation_setup.one_way_uplink_link_ends`, :func:`~tudatpy.numerical_simulation.estimation_setup.two_way_link_ends`, :func:`~tudatpy.numerical_simulation.estimation_setup.three_way_link_ends`).

After the creation of the link ends dictionary, the :class:`~tudatpy.numerical_simulation.estimation.LinkDefinition` object can be created as:

.. code-block:: python

    two_way_link_ends = ..
    two_way_link_definition = estimation_setup.link_definition( two_way_link_ends )
    
where, for this basic example, the link definition is simply a wrapper class for the link ends.

Having defined the link definition, we can :ref:`create the observation model <observationModelSetup>`
