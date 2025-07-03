
.. _mission_design_examples:

=======================
Mission Design
=======================

Performance evaluation
**********************

The following examples compute the performance (e.g. Delta V, time of flight, etc.) at one or more points in the design space, and visualize the results for the user.

.. nbgallery::

  ./tudatpy-examples/mission_design/mga_trajectories.ipynb
  ./tudatpy-examples/mission_design/earth_mars_transfer_window.ipynb
  ./tudatpy-examples/mission_design/low_thrust_earth_mars_transfer_window
  
.. _trajectory_optimization_examples:
  
Trajectory optimization
***********************
  
The following examples optimize the performance (e.g. Delta V, time of flight, etc.) of transfer trajectories using the Pygmo toolbox. See :ref:`pygmo_examples` for more examples/links on the use of Pygmo

.. nbgallery::
  
  ./tudatpy-examples/mission_design/hodographic_shaping_mga_optimization.ipynb
  ./tudatpy-examples/mission_design/cassini1_mga_optimization.ipynb
