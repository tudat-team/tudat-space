
.. _getting_started_examples:

************************
Examples
************************

There are several example applications disseminated in various forms.



.. panels::
    :body: text-left
    :header: text-center

    ---
    :column: col-lg-4 p-3

    **Mybinder**
    ^^^

    Here examples written as Jupyter notebooks can be run online, without the need of installing tudatpy and/or an IDE.

    +++

    .. link-button:: https://mybinder.org/v2/gh/tudat-team/tudatpy-examples/master
        :text: Try it out
        :classes: btn-outline-primary btn-block stretched-link

    ---
    :column: col-lg-4 p-3

    **Github repo**
    ^^^

    The same examples are available on Github, both as Jupyter notebooks and regular *.py* files.

    +++

    .. link-button:: https://github.com/tudat-team/tudatpy-examples
        :text: Go to the repo
        :classes: btn-outline-primary btn-block stretched-link

    ---
    :column: col-lg-4 p-3

    **Online documentation**
    ^^^

    Alternatively, you can go through the examples directly from this website.

    +++

    .. link-button:: examples
        :type: ref
        :text: See below
        :classes: btn-outline-primary btn-block stretched-link




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
