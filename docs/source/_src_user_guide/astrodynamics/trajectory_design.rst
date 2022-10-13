.. _`transfer_trajectory`:

=================================
Multiple Gravity Assists Transfer
=================================

In this section, the design of multiple-leg interplanetary transfer trajectories is discussed. This module
provides the functionalities for creating transfer trajectories consisting of multiple transfer legs with powered
and unpowered gravity assists. This allows defining high-, low-, and hybrid-thrust transfers.

The module is defined under the assumptions of the patched-conics approximation. As such, it allows the flexible design
of transfers using only analytical and semi-analytical methods, without any required numerical integration. This is
particularly useful for preliminary mission design, where having a fast method is particularly important.

A multiple gravity-assist transfer (MGA) is constituted by a series of nodes and legs. The nodes correspond to the departure,
gravity assist, and arrival planets. The legs to the trajectories between the nodes. A transfer can be constituted by
a minimum of one leg and two nodes (there is always one more node than legs).

General Procedure
==============================================================

The transfer trajectory module can be imported with:

.. code-block:: python

    from tudatpy.kernel.trajectory_design import transfer_trajectory

In general, the procedure for analyzing an MGA transfer consists of:

- **Define transfer settings**: These include the body order (bodies through which the spacecraft will pass), the
  settings of each transfer leg, and the settings of each transfer node. The leg and node settings can either be created
  manually or using a factory function.
- **Create the transfer trajectory object**: Through :func:`~tudatpy.trajectory_design.transfer_trajectory.create_transfer_trajectory`.
- **Evaluate the transfer**: Select the node times, node parameters, and leg parameters, and use them to evaluate the
  transfer through :func:`~tudatpy.trajectory_design.transfer_trajectory.TransferTrajectory.evaluate`.
- **Retrieve the results**: Use :class:`~tudatpy.trajectory_design.transfer_trajectory.TransferTrajectory`'s
  properties or functions to retrieve the :math:`\Delta V`, time of flight, state history, acceleration history, etc.

All available functions and classes are described in detail in the relevant entry of the `API reference`_.
For example applications see :ref:`mga_dsm_analysis`.

.. _`API reference`: https://tudatpy.readthedocs.io/en/latest/transfer_trajectory.html#

Transfer Model Description
==============================================================

To evaluate the transfer one needs to select a series of transfer parameters: node times, leg parameters, and node
parameters. The node times always need to be specified, and correspond to the epoch when the spacecraft reaches each
planet/body. The node and leg parameters depend on the specific node and leg type, which are described next.

Legs
--------------------------------------------------------------

The following types of legs are support:

- :func:`~tudatpy.trajectory_design.transfer_trajectory.unpowered_leg`. Unpowered leg, does not have leg parameters.

- :func:`~tudatpy.trajectory_design.transfer_trajectory.dsm_velocity_based_leg`: High-thrust leg with one impulsive
  deep space maneuver (DSM). Its leg parameters are:

      - Fraction of the leg's time-of-flight at which DSM is applied (:math:`\in [0,1]`).

- :func:`~tudatpy.trajectory_design.transfer_trajectory.dsm_position_based_leg`. High-thrust leg with one impulsive
  DSM. Its leg parameters are:

      - Fraction of the leg's time-of-flight at which DSM is applied (:math:`\in [0,1]`).
      - Position of the DSM in spherical coordinates, with respect to a frame with the x-axis aligned with the position
        of the departure body, z-axis aligned with the angular momentum of the departure body, y-axis selected to form a
        right-handed frame. The spherical position is specified as: dimensionless radial position (using as unit of length
        the radial position of the departure body), in-plane angle, out-of-plane angle.

- :func:`~tudatpy.trajectory_design.transfer_trajectory.spherical_shaping_leg`. Low-thrust leg. Its leg parameters are:

      - Integer number of revolution (:math:`\geq 0`).

- :func:`~tudatpy.trajectory_design.transfer_trajectory.hodographic_shaping_leg`. Low-thrust leg. Its leg parameters are:

      - Integer number of revolution (:math:`\geq 0`).
      - Free coefficients of shaping functions (number of coefficients in :math:`\geq 0`).

The inputs and outputs associated with each of these leg types are summarized in the following table.

+----------------------+-----------------------+-----------------------+---------------------+---------------------+
|                      | Leg initial position  | Leg initial velocity  | Leg final position  | Leg final velocity  |
+======================+=======================+=======================+=====================+=====================+
| Unpowered            | Input                 | Output                | Input               | Output              |
+----------------------+-----------------------+-----------------------+---------------------+---------------------+
| DSM-Velocity         | Input                 | Input                 | Input               | Output              |
+----------------------+-----------------------+-----------------------+---------------------+---------------------+
| DSM-Position         | Input                 | Output                | Input               | Output              |
+----------------------+-----------------------+-----------------------+---------------------+---------------------+
| Spherical shaping    | Input                 | Input                 | Input               | Input               |
+----------------------+-----------------------+-----------------------+---------------------+---------------------+
| Hodographic shaping  | Input                 | Input                 | Input               | Input               |
+----------------------+-----------------------+-----------------------+---------------------+---------------------+

Nodes
--------------------------------------------------------------

There are three main types of nodes: departure, swingby, and arrival nodes (these types are specified by the user).
The nodes connect the legs, computing the inputs for each leg based on the
outputs of the other legs or the user-specified node parameters. As such, depending on the inputs/outputs of the legs
that precede and follow a node, different variants of the previous three node types are used (these variants are
selected automatically). Each of these variants is described next, including a summary of their node
parameters and the operations executed by them.

Based on the following description and on
the table specifying the inputs and output of each leg, it is possible to predict exactly which nodes are used
for a given set of legs, as well as the required node parameters. Note that the incoming velocity of a node corresponds to the
final velocity of the previous leg and the outgoing velocity of a node to the initial velocity of the following leg.

- :func:`~tudatpy.trajectory_design.transfer_trajectory.departure_node`
    Usually, this is the initial node of the
    transfer. The outgoing relative velocity at the node (i.e. the excess velocity) is either
    retrieved from the following leg or specified by the user. The node computes the impulsive :math:`\Delta V` that
    needs to be applied at the periapsis of the departure elliptic orbit to enter a hyperbolic orbit with the target excess velocity.
    This node is subdivided into the following types:

    - **Node with leg-defined outgoing velocity**: Does not require node parameters.
    - **Node with user-defined outgoing velocity**: Node parameters:

      - Outgoing velocity vector relative to the node, specified with respect to a TNW reference frame defined using the node's
        inertial state. The outgoing relative velocity is specified in spherical coordinates: norm of the velocity,
        in-plane angle, out-of-plane angle.

- :func:`~tudatpy.trajectory_design.transfer_trajectory.capture_node`
      Usually, this is the final node of the
      transfer. The incoming relative velocity at the node (i.e. the excess velocity) is either
      retrieved from the previous leg or specified by the user. The node computes the impulsive :math:`\Delta V` that
      needs to be applied at the periapsis of the hyperbolic orbit with the specified excess velocity to enter the
      arrival elliptical orbit. This node is subdivided into the following types:

      - **Node with leg-defined incoming velocity**: Does not require node parameters.
      - **Node with user-defined incoming velocity**: Node parameters:

        - Incoming velocity vector relative to the node, specified with respect to a TNW reference frame defined using the node's
          inertial state. The incoming relative velocity is specified in spherical coordinates: norm  of the velocity, in-plane angle,
          out-of-plane angle.


- :func:`~tudatpy.trajectory_design.transfer_trajectory.swingby_node`

      These are usually the intermediate nodes of the
      transfer. However, the initial and final nodes might also be selected to be swingby nodes; this is useful when individually
      analyzing different parts of a transfer or when a mission's objective is to do a swingby of the final body.
      The swingby node is subdivided into the following types:

      - **Node with leg-defined incoming and outgoing velocity**: Does not require node parameters. Computes the
        :math:`\Delta V \geq 0` that needs to be applied during the swingby to patch the incoming and outgoing
        velocities, according to section 4.5.2 of `Musegaas (2012)`_.

      - **Node with leg-defined incoming velocity, user-defined swingby**: Given the known incoming velocity,
        the node forward propagates the swingby using the user-specified parameters, according to sections 4.4.2/3
        of `Musegaas (2012)`_. Node parameters:

            - Swingby periapsis radius
            - Swingby :math:`\Delta V` (applied at the periapsis)
            - Outgoing-velocity rotation angle. Defined according to Appendix 7a of "Spacecraft Trajectory Optimization",
              `Conway (2010)`_. This angle defines the plane in which the swingby occurs (different from the bending angle,
              which is defined inside that plane). This angle can take values in :math:`[0, 2\pi]`.

      - **Node with user-defined swingby, leg-defined outgoing velocity**: Given the known outgoing velocity,
        the node backward propagates the swingby using the user-specified parameters. Analogous to sections 4.4.2/3
        of `Musegaas (2012)`_. Node parameters:

            - Swingby periapsis radius
            - Swingby :math:`\Delta V` (applied at the periapsis)
            - Incoming-velocity rotation angle. Defined analogously to the outgoing-velocity rotation angle, which in turn is
              defined according to Appendix 7a of "Spacecraft Trajectory Optimization",
              `Conway (2010)`_. This angle defines the plane in which the swingby occurs (different from the bending angle,
              which is defined inside that plane). This angle can take values in :math:`[0, 2\pi]`.

      - **Node with user-defined incoming, user-defined swingby**: Given the known incoming velocity,
        the node forward propagates the swingby using the user-specified parameters, according to sections 4.4.2/3
        of `Musegaas (2012)`_. Node parameters:

            - Incoming velocity vector relative to the node, specified with respect to a TNW reference frame defined using the node's
              inertial state. The incoming relative velocity is specified in spherical coordinates: norm of the velocity, in-plane angle,
              out-of-plane angle.
            - Swingby periapsis radius
            - Swingby :math:`\Delta V` (applied at the periapsis)
            - Outgoing-velocity rotation angle. Defined according to Appendix 7a of "Spacecraft Trajectory Optimization",
              `Conway (2010)`_. This angle defines the plane in which the swingby occurs (different from the bending angle,
              which is defined inside that plane). This angle can take values in :math:`[0, 2\pi]`.

.. _`Musegaas (2012)`:  http://resolver.tudelft.nl/uuid:02468c77-5c64-4df8-9a24-1ed7ad9d1408
.. _`Conway (2010)`:  https://doi.org/10.1017/CBO9780511778025