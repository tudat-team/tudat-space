.. _valid_time_range:

==============================================
Default bodies with a limited valid time range
==============================================

The regular default body settings use the spice toolbox to determine the ephemerides of solar system bodies. Consequently, when using these defaults, each time the state of a solar system body is required, the corresponding spice function is called, and a celestial body state is computed. The downside of this is that the process of extracting a state from spice is fairly slow, and may present a computational bottleneck in certain cases. This is especially true when the dynamics you are using is fairly simple (no high-order spherical harmonics, no complex guidance model, no detailed atmosphere model), in which you require the states of numerous solar system bodies, for instance for the computation of third-body perturbations. To mitigate this, we offer an alternative method of defining default body settings: 

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies_time_interval.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

The difference w.r.t. the `regular creation<creating_celestial_bodies>` of default body settings being the use of the ``get_default_body_settings_time_limited`` function (instead of ``get_default_body_settings``). What is done when using this alternative setup:

 * When *creating* the bodies, spice is queried at a linearly spaced set of times (defined by the ``initial_time``, ``final_time`` and ``time_step``, the latter of which has a default of 300 s), resulting in a table of states for each body that is to be created
 * A 6-step Lagrange interpolator (TODO link) is created for each body using these tables of states, and is used to define the ephemeris of the body
 * When requiring the state of a body during the simulation, the interpolator is queried, instead of spice

Extracting a state from the interpolator is significantly faster than extracting it from spice. However, this approach comes with a number of downsides:

* This setup require large tables of states (and associated data for the interpolator) to be stored in active memory, leading to significant memory usage when used for large simulation time intervals
* Using the interpolator will produce a *slightly* different result for the states that if they would be extracted from spice directly. For most solar system bodies, this is limited, but for bodies with short orbital periods (*e.g.* solar system moons), the interpolation error may be excessive. In such cases, users can define a different ``time_step`` for a single body by using the ``get_default_single_body_settings_time_limited`` (TODO: API link) function.
* The ephemeris that is created in this manner is *only* valid within a given time range, which means that you need to know beforehand which the time interval of your simulation will be

.. warning::
    The Lagrange interpolator that is created in the above flow is *not* valid within the full range [``initial_time``, ``final_time``]. At the edges of this domain, it will return unreliable results, due to the onset of Runge's phenomenon. See `this page<lagrange_interpolator_issues>` for a more detailed description. In short, the interpolator is only valid in the range [``initial_time`` + 3 :math:`\cdot` ``time_step``, ``final_time`` - 3 :math:`\cdot` ``time_step``]   


