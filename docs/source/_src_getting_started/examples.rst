
.. _getting_started_examples:

************************
Examples
************************

There are several example applications available in `this repository`_, in the form of Python scripts.
At the top of each `.py` example file, the topic and goals of such example application are explained in detail.

In addition, to facilitate the understanding of tudat(py) code, a selection of the example applications are
illustrated in more detail in the pages linked below.

.. _`this repository`: https://github.com/tudat-team/tudatpy-examples

.. contents:: Categories of example applications
   :local:


=================================
Numerical Propagation of Dynamics
=================================

Below you can find examples of numerical simulations that you can achieve with TudatPy.

.. toctree::
   :titlesonly:
   :maxdepth: 1

   _src_examples/simulation_examples/delfi_simple_example_page
   _src_examples/simulation_examples/var_equation_example_page
   _src_examples/simulation_examples/multi_body_propagation_inner_SS
   
=====================================
Estimation of Dynamics and Parameters
=====================================

Below you can find examples of estimation that you can achieve with TudatPy.

.. toctree::
   :maxdepth: 1

   _src_examples/estimation_examples/basic_estimation


===================
Examples with PyGMO
===================

Below you can find general examples, explained in detail, about optimizing an astrodynamical problem simulated in
TudatPy through `Pygmo <https://esa.github.io/pygmo2/index.html>`_. If you have never used PyGMO before, please
consider reading our introductory guide: :ref:`Optimization with PyGMO`.

.. toctree::
   :maxdepth: 1

   _src_examples/pygmo_examples/pygmo_orbit_optimization

=========================================
Examples of MGA-DSM transfer trajectories
=========================================

Below you can find general examples, explained in detail, about using the tools available for analyzing Multiple Gravity
Assist transfer trajectories with Deep Space Maneuvers (MGA-DSM).

.. toctree::
   :maxdepth: 1

   _src_examples/mga_dsm_examples/mga_dsm_analysis
   _src_examples/mga_dsm_examples/mga_dsm_optimization
