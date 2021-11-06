.. _create_celestial_body_settings:

===============================================
Creation of celestial body settings
===============================================

The usual workflow to create celestial body settings is composed of two subsequent steps, described separately:

1. :ref:`default_body_settings`
2. :ref:`custom_body_settings`

.. warning::
   Body settings are not used in the propagation: they are only useful to create body objects. This procedure is
   described in the separate page :ref:`create_bodies_from_settings`.


.. _default_body_settings:

Generation of default body settings
===============================================

Generating default settings prevents a user from having to manually define a variety of 'typical' models for
solar-system bodies. The 'default' settings can be retrieved as follows, using the
:func:`~tudatpy.numerical_simulation.environment_setup.get_default_body_settings` function:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

where the ``global_frame_origin`` and ``global_frame_orientation`` define the reference frame in which state vectors
stored in the environment `during` propagation are represented. For more details about reference frames, see
:ref:`reference_frames`.

In general, it is recommended to choose this as the most 'intuitive' frame origin for your propagation
(e.g. SSB or Sun for solar system scale propagations, Earth for an Earth orbiter, Mars for a Martian mission, etc.).

.. warning::
   This frame definition is *distinct* from the center of propagation that you can define in the propagation setup.
   For more information, see :ref:`simulation_propagator_setup`.


The full list of default body settings is available at :ref:`default_environment_models`.

.. note::
   Note that the ephemerides that are used by default are only valid for a somewhat limited time interval
   (on the order of a century, depending on the specific body).


In addition to the above method of creating default bodies, we offer an alternative which is more computationally efficient, at the expense of higher RAM usage and a more limited time interval in which the environment is valid. Such an approach is typically only used when computational speed is very important, and is described in more detail :ref:`here<valid_time_range>`.


.. _custom_body_settings:

Customization of body settings
================================


Default settings may be overridden as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

Where the above example overrides the default setting for the Sun's gravity field, and sets a point-mass gravity field
with a gravitational parameter of 1.32712440042 :math:`\cdot` 10 :superscript:`20` m :superscript:`3` / s :superscript:`2`.

.. seealso::
   A comprehensive list of *all* environment models, and how their settings can be defined and overridden as above, is
   given in the page about :ref:`available_environment_models`.


