.. _torque_model_setup:


==================
Torque Model Setup
==================


In Tudat, a torque model setup works similarly to the translational acceleration setup.
The torque acting on a body is defined by

*  The body upon which the torque is acting
*  The body exerting the torque
*  The type and settings of the torque

The user defines these settings for each torque in their simulation. These settings are then used to create the torque models:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/torque_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

where second degree gravitational torques are exerted by the Sun and the Moon, as well as spherical harmonic gravity torques (to degree and order 4) by the Earth and aerodynamic torques by the Earth's atmosphere.
The variable ``torque_settings_vehicle`` denotes the list of bodies exerting torques, and the types of torques, and the variable ``torque_settings`` associates this list with the body upon which the torques are acting.
The function ``create_torque_models`` creates the list of models that compute the torques during the propagation.

When propagating multiple bodies (see :ref:`multi_body_propagation`), the same list of settings may be re-used for multiple bodies. Below, an example is given for the definition of ``torque_settings`` for multiple bodies (``Vehicle1`` and ``Vehicle2``) which are acted upon by identical torques:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/torque_setup_multi_vehicle.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

Or separate acceleration settings may be defined for separate bodies, and then combined into a ``acceleration_settings`` variable. Below, an example for such a case is given when propagating the Earth and Moon:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/torque_setup_multi.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp