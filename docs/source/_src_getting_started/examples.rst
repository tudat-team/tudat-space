
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

.. attention::

  As of Tudatpy version 0.7, a number of modifications have been made to how Tudatpy deals with vehicle orientations,
  in particular in the context of thrust and aerodynamic guidance. These changes are, in part,
  :ref:`not backwards compatible<backwards_incompatibility>`. The examples below dealing with thrust and aerodynamics
  are **not yet up-to-date**. This will be corrected by the first week of October.

.. nbgallery::
   :caption: Numerical propagation of dynamics
   :glob:

   _src_examples/notebooks/propagation/*

.. nbgallery::
   :caption: Estimation of dynamics and parameters
   :glob:

   _src_examples/notebooks/estimation/*

.. nbgallery::
   :caption: Optimization with PyGMO
   :glob:

   _src_examples/notebooks/pygmo/*

.. note::
   If you have never used PyGMO before, please
   consider reading our introductory guide: :ref:`Optimization with PyGMO`.
