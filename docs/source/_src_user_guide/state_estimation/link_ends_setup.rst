.. _linkEndSetup:

Link Ends Setup
===============

To define an observation model, the various bodies, spacecraft, ground stations, etc. involved in the observation, and their role in the observation, must be defined. For a one-way range model, for instance, the definition of a transmitter and a receiver is required. In Tudat, the transmitter and receiver are both referred to as 'link ends'. The full set of link ends in the observable, and their role in the observable, are stored in the :class:`~tudatpy.numerical_simulation.estimation.LinkDefinition`. Below, we describe the steps that are (or may be) required to set up this object.

.. note::

    A :class:`~tudatpy.numerical_simulation.estimation.LinkDefinition` object does *not* define the observation model itself, but only the various reference points (link ends) that are required for it. For instance, a one-way range, one-way Doppler and angular position observation may all use an identical ``LinkDefinition`` (containing a transmitter and a receiver). 

.. _groundStationCreation:

Ground Station Creation
~~~~~~~~~~~~~~~~~~~~~~~

Often, you will need to define the positions of ground stations on celestial bodies to/from which observations are made. Note that in Tudat, a planetary lander is treated identically to a terrestrial ground station. The creation of a ground station is described in the :ref:`environment setup <ground_stations>`.

Creating a Set of Link Ends
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The creation of the link definition requires the definition of a set of link ends used for a given observable. These are stored in a dictionary as follows:

 - The dictionary key denotes the role in the observation (e.g. receiver, transmitter, *etc.*), given by an entry from the :class:`~tudatpy.numerical_simulation.estimation_setup.LinkEndType` enum. For each observation model in the `API documentation <https://py.api.tudat.space/en/latest/observation.html>`_, it is specified which link end types are required.
 - The dictionary value represents the identifier of the link end (spacecraft, ground station, *etc.*), as a :class:`~tudatpy.numerical_simulation.estimation_setup.LinkEndId` object.  To use a reference point on a body (for instance, a ground station on Earth), the :func:`~tudatpy.numerical_simulation.estimation_setup.observation.body_reference_point_link_end_id` function can be used to create an object of this type. To use the origin (typically, but not necessarily its center of mass) of a body as link end, use the :func:`~tudatpy.numerical_simulation.estimation_setup.observation.body_origin_link_end_id` function.  Although using a center of mass is unrealistic for data analysis, such a setup can often be useful for a simulated analysis. Example of defining link ends are given below:

Each type of observable requires a specific combination of *types* of link ends. Below, a number of examples are given for one-, two- and three-way observables (see :ref:`here <two_three_way_observables>` for the distinction between two- and three-way observables when creating observation models):

.. code-block:: python
                
    one_way_link_ends = dict( );
    one_way_link_ends[ transmitter ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "Graz" );
    one_way_link_ends[ receiver ] = estimation_setup.observation.body_origin_link_end_id( "LRO" );
    
This defines a link for which the ground station termed Graz on the body called Earth acts as transmitter, and the body called LRO is used as the receiver (in this case placed at the body's center of mass).

An example of link-ends for a two-way link from Graz to LRO and back to Graz is identified below. Note that below example is a representation of the manual creation of link ends. There are also a number of functions that allow you to generate a list of link ends for one- two- and three-way observables (:func:`~tudatpy.one_way_downlink_link_ends`, :func:`~tudatpy.numerical_simulation.estimation_setup.one_way_uplink_link_ends`, :func:`~tudatpy.numerical_simulation.estimation_setup.two_way_link_ends`, :func:`~tudatpy.numerical_simulation.estimation_setup.three_way_link_ends`).


.. code-block:: python

    two_way_link_ends = dict( );
    two_way_link_ends[ transmitter ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "Graz" );
    two_way_link_ends[ reflector ] = estimation_setup.observation.body_origin_link_end_id( "LRO" );
    two_way_link_ends[ receiver ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "Graz" );

Where the Graz station now acts as both transmitter and receiver. Similarly, the receiver may be different from the transmitter (in what is typically called a three-way observable in Deep Space tracking ), so:

.. code-block:: python

    two_way_link_ends = dict( );
    two_way_link_ends[ transmitter ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "Graz" )
    two_way_link_ends[ reflector ] = estimation_setup.observation.body_origin_link_end_id( "LRO" )
    two_way_link_ends[ receiver ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "Matera" )
    
where the signal is transmitter by Graz station, retransmitter or reflected by LRO, and then received by the Matera station.

After the creation of the link ends dictionary, the :class:`~tudatpy.numerical_simulation.estimation.LinkDefinition` object can be created as:

.. code-block:: python

    two_way_link_ends[ transmitter ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "Graz" )
    two_way_link_ends[ reflector ] = estimation_setup.observation.body_origin_link_end_id( "LRO" )
    two_way_link_ends[ receiver ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "Matera" )
    two_way_link_definition = estimation_setup.link_definition( two_way_link_ends )
    
where, for this basic example, the link definition is simply a wrapper class for the link ends.

Having defined the link definition, we can :ref:`create the observation model <observationModelSetup>`.
