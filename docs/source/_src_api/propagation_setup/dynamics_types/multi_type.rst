===================
Multi-type Dynamics
===================

Tudat permits the propagation of any combination of types of dynamics, for any number of bodies
One example is the simulation of coupled translational-rotational dynamics of one or more bodies, or the combined translational and mass dynamics of a body (e.g. spacecraft under thrust). N

To define multi-type propagator settings, you must first define the propagaor settings for each type of dynamics separately, after which you combine these using the function as follows: 

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/full_rotational_setup.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/full_mass_setup.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_multitype_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

This example shows the use of the translational, rotational and mass dynamics of a single body ``Vehicle``. However, the framework is not limited to propagating the differnet types of dynamics for only one body. You may for instance propagate the translational state and mass of a spacecraft concurrently with the rotational state of the Earth. Also, you may propagate any number of any type of dynamics of any body, e.g. translational dynamics of 6 bodies, rotational dynamics of 4 bodies and mass of 2 bodies, where these three sets of bodies may but need not fully or partially overlap)
   
 .. Warning:: 

    When using multi-type propagator settings, the output variables, termination settings, and print interval defined through the ``propagation_setup.propagator.multi_type`` function are used. Settings of the same kind are also stored in the constituent single-type propagator settings, but these are fully ignored when using multi-type settings 

