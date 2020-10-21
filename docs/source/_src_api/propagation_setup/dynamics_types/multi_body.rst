===================
Multi-body Dynamics
===================

The propagation framework in Tudat is implemented such that any number of bodies may be propagated numerically. Taking the translational dynamics as an example, propagating multiple bodies is achieved simply by extending the list of propagated bodies and central bodies:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_multi_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cp

Where the ``acceleration_models`` should contain a set of acceleration models acting upon each propagated body (if one or more of the bodies is omitted from the ``acceleration_models``, no accelerations are assumed to act on this body, without warning or error).

The use of a 'hierarchical' system is also supported by Tudat. For instance, one can propagate the Earth and Mars w.r.t. the Sun, the Sun w.r.t. the barycenter, the Moon w.r.t the Earth:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_multi_hierarchy_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cp

In either case, any and all physical interactions are automatically formulated as required for the specific dynamical system under consideration. Specifically, the use of direct and third-body gravitational accelerations, and the definition of the correct effective gravitational parameter, are automatically handled. See TODO for details on this process
