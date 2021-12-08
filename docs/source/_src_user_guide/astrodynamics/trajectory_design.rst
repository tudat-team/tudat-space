.. _`transfer_trajectory`:

==========================
Transfer trajectory design
==========================

Multiple Gravity Assists and Deep Space Maneuvers
==============================================================

In this section, the TudapPy module that is used for the design and analysis of high thrust transfer trajectories is
described. The module considers multiple (powered) gravity assists (MGA) and deep space maneuvers (DSM). An MGA-DSM
trajectory is defined by a series of nodes, i.e. the planets where the GAs are executed, connected
by a series of legs, i.e. the trajectories in between the nodes. A maximum of 1 DSM can be executed per leg.

For details about the theory behind this module, please see `Musegaas`_.

.. _`Musegaas`:  http://resolver.tudelft.nl/uuid:02468c77-5c64-4df8-9a24-1ed7ad9d1408


The module
------------------

The transfer trajectory module can be imported with:

.. code-block:: python

    from tudatpy.kernel.trajectory_design import transfer_trajectory

The transfer trajectory module contains of a set of methods, factory functions, enumerations and classes. Here, the
most important functionality of the module is explained. For more details about the module, please see the `API`_.

.. _`API`: https://tudatpy.readthedocs.io/en/latest/transfer_trajectory.html#

The :func:`~tudatpy.trajectory_design.transfer_trajectory.mga_transfer_settings` method is used to create the settings
of the transfer trajectory. The module also provides the possibility to retrieve only the settings of a specific type,
e.g. :func:`~tudatpy.trajectory_design.transfer_trajectory.dsm_velocity_based_leg` and
:class:`~tudatpy.trajectory_design.transfer_trajectory.EscapeAndDepartureNodeSettings`. The resulting leg and node
settings are required to create a transfer trajectory object through
:func:`~tudatpy.trajectory_design.transfer_trajectory.create_transfer_trajectory`. This transfer trajectory object can
be used to analyze various implementations of the defined transfer trajectory. This can be done through the object's
:func:`~tudatpy.trajectory_design.transfer_trajectory.TransferTrajectory.evaluate` method. Having done this, various
transfer characteristics can be retrieved, such as the total :math:`\Delta V`, time of flight and :math:`\Delta V` per
leg.

Inputs
----------

The general inputs required to define an MGA-DSM transfer trajectory are:

- *body order*: order of the bodies that are visited for GAs (the nodes)
- *leg type*: type of the legs, either excluding or including DSMs
- *departure and arrival orbit semi-major axes and eccentricities*: departure and arrival orbit characteristics

``leg_type`` must be of the ``tudatpy.kernel.trajectory_design.transfer_trajectory.TransferLegTypes`` type and can be
retrieved from the module directly:

.. code-block:: python

    no_dsm_leg_type = transfer_trajectory.unpowered_unperturbed_leg_type
    dsm_velocity_based_leg_type = transfer_trajectory.dsm_velocity_based_leg_type
    dsm_position_based_leg_type = transfer_trajectory.dsm_position_based_leg_type


The departure and arrival orbit characteristics are optional inputs. By default it is assumed :math:`a = \infty` and
:math:`e=0`, which means that the spacecraft departs from / arrives at the edge of the SOI of the
departure / arrival planet.

Besides the general inputs, trajectory specific inputs are required, which are called transfer parameters. Which
transfer parameters need to be defined, depends on the leg type. For all trajectories, *with* and *without* DSMs, it is
required to define the ``node_times``, which indicate when the spacecraft is at the periapsis of the GA at each planet.
Through a simple conversion these can be obtained from a departure date and times of flight per leg. The table below
presents the additional parameters, so called leg and node free parameters, required per leg type.

+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
| Parameter type                        | No DSM                | DSM Velocity based                                    | DSM Position based                                                           |
+=======================================+=======================+=======================================================+==============================================================================+
| Node times *(per node)*               | Node times            | Node times                                            | Node times                                                                   |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
| Leg free parameters                   |                       | Time of flight fraction at                            | Time of flight fraction at                                                   |
|                                       |                       |                                                       |                                                                              |
| *(per leg)*                           |                       | which the DSM takes place                             | which the DSM takes place                                                    |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
|                                       |                       |                                                       | The dimensionless distance of the DSM to the Sun, which                      |
|                                       |                       |                                                       |                                                                              |
|                                       |                       |                                                       | which is scaled to the distance of the departure planet to the Sun           |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
|                                       |                       |                                                       | In-plane angle, defined as the angle between the position of the departure   |
|                                       |                       |                                                       |                                                                              |
|                                       |                       |                                                       | planet and the projection of the DSM location in the orbital plane of the    |
|                                       |                       |                                                       |                                                                              |
|                                       |                       |                                                       | departure planet                                                             |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
|                                       |                       |                                                       | Out-of-plane angle, defined as the angle between the DSM location and the    |
|                                       |                       |                                                       |                                                                              |
|                                       |                       |                                                       | orbital plane of the departure planet                                        |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
| Node free parameters                  |                       | Magnitude of the relative velocity w.r.t.             |                                                                              |
|                                       |                       |                                                       |                                                                              |
| *(departure node only)*               |                       | the departure planet after departure                  |                                                                              |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
|                                       |                       | In-plane angle of the relative velocity w.r.t.        |                                                                              |
|                                       |                       |                                                       |                                                                              |
|                                       |                       | the departure planet after departure                  |                                                                              |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
|                                       |                       | Out-of-plane angle of the relative velocity           |                                                                              |
|                                       |                       |                                                       |                                                                              |
|                                       |                       | w.r.t. the departure  planet after departure          |                                                                              |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
| Node free parameters                  |                       | Periapsis radius                                      |                                                                              |
|                                       |                       |                                                       |                                                                              |
| *(per swing-by node)*                 |                       |                                                       |                                                                              |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
|                                       |                       | Rotation angle                                        |                                                                              |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
|                                       |                       | Magnitude of :math:`\Delta V` applied at periapsis    |                                                                              |
+---------------------------------------+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+


General procedure
-----------------

In general, the procedure for analyzing an MGA-DSM transfer trajectory constitutes the following steps:

* *Define settings*
    Use a body order, leg type and optionally departure/arrival orbit characteristics to define settings, e.g. through
    :func:`~tudatpy.trajectory_design.transfer_trajectory.mga_transfer_settings`.

* *Create and evaluate transfer object*
    Use the settings in :func:`~tudatpy.trajectory_design.transfer_trajectory.create_transfer_trajectory` and apply
    user-defined transfer parameters to :func:`~tudatpy.trajectory_design.transfer_trajectory.TransferTrajectory.evaluate`
    the transfer trajectory object.

* *Retrieve the desired results from the evaluated object*
    Use any of :class:`~tudatpy.trajectory_design.transfer_trajectory.TransferTrajectory`'s properties or functions to
    retrieve :math:`\Delta V`, time of flight, spacecraft state during the transfer, etc.


For example applications of this module, please see :ref:`mga_dsm_analysis`.