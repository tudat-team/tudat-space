
==========================
Transfer trajectory design
==========================

Multiple Gravity Assists and Deep Space Maneuvers (MGA-DSM)
###########################################################
.. warning::
    TODO: Link Paul Musegaas' thesis

An MGA-DSM trajectory is defined as a series of nodes (i.e. the planets where the gravity assists are executed) connected
by a series of legs. These legs may or may not contain DSMs.





.. note::

    | Both problems *with* and *without* DSMs have the departure date and time of flight per leg as parameters.
    | Problems *without* DSMs have no additional parameters.
    | Problems *with* DSMs have the following as additional parameters:
    - fraction of the time of flight at which the DSM takes place per leg

    - magnitude of the relative velocity w.r.t. the departure planet after departure

    - in-plane angle of the relative velocity

    - out-of-plane angle of the relative velocity

    - the pericenter radius per gravity assist

    - the rotation angle per gravity assist

    - the magnitude of :math:`\Delta V` applied per gravity assists

.. End of note

Semi-major axes and eccentricities are optional
===============================================
Here, one can specify the semi-major axis and eccentricity of both the departure and insertion orbits. Do note that this
is optional, by default it is assumed :math:`a = \infty` and :math:`e=0`, which means that the spacecraft
departs from/arrives at the edge of the sphere of influence of the departure/arrival planet.


