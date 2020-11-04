==========================
Creating Artificial Bodies
==========================

After creating a set of bodies (see :ref:`creating_celestial_bodies`), any number of additional custom bodies may be added to the simulation. Typically, such an approach is used for artificial bodies

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

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

which creates a new body, with no properties. Properties can then be added to this body one-by-one. For an artificial body, typical properties are a mass, aerodynamic coefficients, and radiation pressure properties. 

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

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

In this example, the settings for the aerodynamic coefficients and radiation pressure are defined as the most simple models available (constant drag-only aerodynamic coefficients, and cannonball radiation pressure). A comprehensive list of settings for both types of models can be found here :ref:`available_environment_models`.
