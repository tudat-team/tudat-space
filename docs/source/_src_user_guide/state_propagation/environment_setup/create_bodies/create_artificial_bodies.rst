.. _create_artificial_bodies:

==============================
Creation of artificial bodies
==============================

After creating a set of bodies from default settings (see :ref:`default_body_settings`), any number of additional
custom bodies may
be added to the simulation. Typically, such an approach is used for artificial bodies. This process can be done in
two steps:

1. :ref:`create_empty_body`
2. :ref:`decorate_empty_body`

.. note::
   Unlike celestial bodies that have default settings, the creation of artificial bodies does *not* require creating
   body settings. On the other hand, first an empty body is created: only after its creation, its properties can be
   modified.

.. _create_empty_body:

Creation of empty body
==============================

The first step is to add an empty :class:`~tudatpy.numerical_simulation.environment.Body` object to the existing
:class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object through its
:meth:`~tudatpy.numerical_simulation.environment.SystemOfBodies.create_empty_body` method:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/create_system_of_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

which adds a body with no properties to the system.


.. _decorate_empty_body:

Addition of properties to a body
=================================

Properties can then be added to this body one-by-one. For an artificial body, typical properties are:

- mass
- aerodynamic coefficients
- radiation pressure properties

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/create_system_of_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body_properties.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

In this example, the settings for the aerodynamic coefficients and radiation pressure are defined as the most simple models available (constant drag-only aerodynamic coefficients, and cannonball radiation pressure).

.. seealso::
   A comprehensive list of settings for both types of models can be found in :ref:`available_environment_models`.
