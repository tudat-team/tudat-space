.. _`mga_dsm_optimization`:

*****************************
Optimize MGA-DSM trajectories
*****************************

In the following sections the optimization of MGA-DSM trajectories within the context of the CDL is explained through an
example. If you are unfamiliar with optimizations within Tudat(py) and/or Pygmo, please refer to :ref:`pygmo_basics` first.
The optimizer will search for optimal solutions in terms of two objectives: :math:`\Delta V` and time of flight. The Pareto
fronts that result from the optimization are always saved and can be viewed in order to identify specific solutions that
are to be analyzed further, in terms of available communication time, incident solar flux and other quantities.

.. warning::
    TODO: link to pygmo documentation


1. Definition of inputs and optimization settings
-------------------------------------------------
First and foremost, the input for the transfer trajectory and the optimization settings are to be defined. The settings
which are to be specified are the same, for transfers *with* or *without* DSMs, although the exact values are to be chosen
according to the specific transfer type:

.. literalinclude:: _static/transfer_trajectory_inputs.py
    :language: python
    :lines: 9-44

Download: :download:`Inputs <_static/transfer_trajectory_inputs.py>`

1.1. Transfer body order(s)
==========================================================
``transfer_body_orders`` specifies the sequence in which planets are visited. Each planet is denoted with a string (with
capital first letter) in a list of lists. This enables the subsequent and automatic optimization of multiple planet sequences.

.. note::
    If you only want to optimize one planet sequence, do make sure to keep the outer list: ``transfer_body_orders = [['Earth',
    'Venus', 'Venus', 'Earth', 'Jupiter', 'Saturn']]``
.. End of note

1.2. Leg type
===========================================================

``leg_type`` specifies whether the transfer will utilize DSMs or not. This is denoted by a ``trajectory_design`` attribute
imported from Tudat.

| To not use DSMs: ``leg_type = trajectory_design.unpowered_unperturbed_leg_type``.
| To use DSMs: ``leg_type = trajectory_design.dsm_velocity_based_leg_type``.

1.3. Departure date and margin
===========================================================
The ``departure_date`` is to be specified in J2000 (Julian days since 1 January 2000, 12:00 UTC). ``departure_date_margin``
indicates the time added and subtracted from the nominal departure date to define the departure time boundaries for the
optimization. In the above example this means that the departure will occur within half a year before and half a
year after the nominal date.

1.4. Semi-major axes and eccentricities (optional)
===========================================================
As explained in the introductory guide to :ref:`Transfer trajectory design`, specifying the semi-major axis and eccentricity
of the departure and insertion orbits is optional. By default it is assumed :math:`a = \infty` and :math:`e=0`, which means
that the spacecraft departs from/arrives at the edge of the sphere of influence of the departure/arrival planet.

1.5. Number of evolutions and population size
===========================================================
The optimization settings include the ``number_of_evolutions``, ``population_size``, ``optimization_seed`` and ``maximum_delta_v``,
of which the first two are most crucial. Good values for these parameters are heavily dependent on your problem definition,
i.e.  mostly on ``transfer_body_orders`` and ``leg_type``. Moreover, it is important to consider the number of parameters
in your problem before choosing these values. In general, the more parameters in your problem, the larger the population
size and the more evolutions are required to obtain good results.

The number of parameters within a problem *without* DSMs is equal to the number of planets that are flown by (including the
departure and destination planet). In contrast, the number of parameters within a problem *with* DSMs is equal to the number
of planets that are flown by (including the departure and destination planet) *plus* four times the number of legs that are
flown. The number of parameters for a problem *with* DSMs is thus significantly larger than for one *without*. This more
elaborate problem definition makes it computationally more expensive to optimize.

The following table presents a good choice of optimization settings for two case studies along with their problem characteristics:

========  ================================================  ============================ ========================= ===================== =====================
  DSM?     Planet sequence                                   Number of parameters         Number of evolutions      Population size       Optimization runtime
========  ================================================  ============================ ========================= ===================== =====================
   No       Earth, Venus, Venus, Earth, Jupiter, Saturn      6                            3000                      500                    ~3 minutes
   Yes      Earth, Earth, Venus, Venus, Mercury              21                           2000                      2000                   ~15 minutes
========  ================================================  ============================ ========================= ===================== =====================

This shows that it is significantly more effective to increase the population size to optimize a more complex problem, than to perform
more evolutions.

Do note, for a problem *without* DSMs it is recommended to pick a large value for the number of generations and be
on the 'safe side' for the optimization, as the cost in runtime is not too large. This is not the case for a problem *with*
DSMs, where an evolution costs significantly more time.


1.6. Tricks to help the optimization
===========================================================
It may occur that the optimization does not yield expected or even satisfactory results. This may be because the problem
definition is not ideal, but it may also be that the optimal solutions are simply not found. In the latter case there are a
few things that can be done to 'manipulate' the optimization:

* *Pick a different*  ``optimization_seed``
    The seed is used for two purposes: to create the initial population and to initialize the optimization algorithm. By
    specifying a different seed, the starting point for the optimizaton is different and the final results may be better.

* *Set* ``maximum_delta_v``
    It is possible to try and force the optimization towards solutions with lower :math:`\Delta V`. This can be done by specifying
    a maximum :math:`\Delta V`. This value is used in the optimization to apply a penalty to all solutions that exceed it,
    thereby forcing it to continue to search for better solutions. There is a risk involved here, if this maximum
    :math:`\Delta V` is too low, the optimization may not find any solutions satisfying it at all and won't give you any
    solutions that are not penalized. The default is set to :math:`2e8` m/s, so that it is practically ineffective.

* *Increase population size*
    Increasing the population size (even only slightly) will yield a different initial population, thereby affecting
    the entire evolution and may therefore yield better solutions (maybe even in less evolutions).

* *Reduce number of parameters*
    It may be the case that a problem *with* DSMs is simply too complex to be optimized efficiently. In that case it may
    be better to reduce the number of parameters, either by not using DSMs or by reducing the number of planets that are
    visited.

Lastly, it was noted that the time of flight range in the Pareto front is rather limited in some cases. In this case it
may be that the optimization has found optimal solutions for this range, but that these are not acceptable and that larger
times of flight need to be explored. This may be achieved with the above tricks (e.g. it is adviced to try setting a maximum
:math:`\Delta V` first), but there is one more trick:

* *Increase minimum times of flight* in :download:`Constants <_static/constants.py>`
    In this file the boundaries as used in the optimization regarding time of flight are defined in days, depending on the planet
    that defines the end of a leg. One can increase the minima (and possibly increase the maxima) to move (and extend) the
    time of flight range of the Pareto front.

2. Perform the optimization
-------------------------------------------------
The optimization can be run with the settings as defined before, without any further modifications or other settings to
be defined, with the following file:

:download:`Optimization of MGA-DSM trajectories <_static/transfer_trajectory_optimization.py>`

This script imports the required packages, modules, functions and variables. First, a problem class is defined,
as required by Pygmo to perform the optimization. Subsequently, the optimization is run and the parameters and fitness of
every 100th generation are saved to text files, which can be used for reference later on, for example to check convergence
of the optimization. Afterwards, the Pareto front is obtained from the final generation, plotted and saved in PDF format.
The corresponding parameters and fitness values are also saved to text files. If multiple planet sequences are given in
``transfer_body_orders``, the next planet sequence is optimized next. Otherwise, the script terminates and the Pareto front(s)
can be analyzed in order to choose solutions that are interesting for further analysis.

.. warning::
    TODO: Include some code here to demonstrate?