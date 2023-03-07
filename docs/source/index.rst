======================================
Tudat Space
======================================


Tudat Space is a platform and community for astrodynamics and space research.
Our mission is to provide educators, researchers, students, and
enthusiasts access to a powerful toolkit, fuelling careers and
passions in astrodynamics and space. It contains user guides and tutorials to use Tudat and it is organized as follows:

- *Getting Started:* all the information for new users, including how to install tudatpy and some examples
  showcasing its functionalities.
- *User Guide:* several guides explaining how different parts of tudatpy code are used together to create a simulation.
- *Advanced topics*: guides for more advanced topics (e.g., optimization with Tudat).
- *Resources from Tudat ecosystem:* links to other Tudat resources (API reference, developer documentation, etc...)
  not hosted directly on tudat-space.
- *About:* additional information about Tudat and its ecosystem.

.. attention::

  As of Tudatpy version 0.7, a number of modifications have been made to how Tudatpy deals with vehicle orientations,
  in particular in the context of thrust and aerodynamic guidance. These changes are, in part, not backwards compatible.
  See :ref:`this page <backwards_incompatibility>` for more details. To continue to use the last older version of Tudat, install
  version 0.6.3.

Quickstart
==========

.. panels::
    :body: text-left
    :header: text-center

    ---
    :column: col-lg-4 p-3

    **Installation**
    ^^^

    Learn how to install the tudatpy package via conda.

    +++

    .. link-button:: _src_getting_started/installation
        :type: ref
        :text: Read our guide
        :classes: btn-outline-primary btn-block stretched-link

    ---
    :column: col-lg-4 p-3

    **Online examples**
    ^^^

    Run the examples on mybinder and see how tudatpy works: you don't need to install any package or IDE.

    +++

    .. link-button:: https://mybinder.org/v2/gh/tudat-team/tudatpy-examples/master
        :text: Try it out
        :classes: btn-outline-primary btn-block stretched-link

    ---
    :column: col-lg-4 p-3

    **Research output**
    ^^^

    Find out some state-of-the-art examples of what you can do with tudat(py) by having a look at our list of publications

    +++

    .. link-button:: _src_about/research_output
        :type: ref
        :text: Have a look
        :classes: btn-outline-primary btn-block stretched-link


External resources
============================

Some resources related to Tudatpy are located elsewhere. See below!

.. panels::
    :body: text-left
    :header: text-center

    ---
    :column: col-lg-4 p-3

    **TudatPy API reference**
    ^^^

    Documentation of the tudatpy Application Programming Interface.

    +++

    .. link-button:: https://tudatpy.readthedocs.io
        :text: Go to the website
        :classes: btn-outline-primary btn-block stretched-link

    ---
    :column: col-lg-4 p-3

    **Developer Documentation**
    ^^^

    A separate website with guides and resources to develop Tudat and TudatPy code and documentation.

    +++

    .. link-button:: https://tudat-developer.readthedocs.io/en/latest/
        :text: Go to the website
        :classes: btn-outline-primary btn-block stretched-link

    ---
    :column: col-lg-4 p-3

    **Mathematical model definition**
    ^^^

    A manual containing definitions of mathematical models implemented in Tudat.

    +++

    .. link-button:: https://github.com/tudat-team/tudat-space/raw/master/Tudat_mathematical_model_definition.pdf
        :text: Download the manual
        :classes: btn-outline-primary btn-block stretched-link




What is Tudat?
===========================================

The TU Delft Astrodynamics Toolbox (Tudat) is a powerful set of libraries that support astrodynamics and space research.
Such framework can be used for a wide variety of purposes, ranging from the study of reentry dynamic to interplanetary
missions. The functionality of Tudat is implemented in C++, but a Python interface, called Tudatpy, is now available,
through which the core simulation functionality can be accessed. Tudat and Tudatpy are disseminated as conda packages;
to get started with them, have a look at our
:ref:`installation guide<getting_started_installation>`.

.. panels::
    :body: text-left
    :header: text-center
    :footer: text-center
    :container: container-lg pb-3


    ---
    :column: col-lg-4 p-3

    **Different dynamics types**
    ^^^

    Numerical propagation of different state types (translational state, rotational
    state, and mass) and their associated variational equations through built-in or user-defined acceleration and
    torque models.

    +++
    .. link-button:: _src_user_guide/state_propagation/propagation_setup
            :type: ref
            :text: Find out more
            :classes: stretched-link btn-outline-primary

    ---
    :column: col-lg-4 p-3

    **Flexible modeling of simulated bodies**
    ^^^

    Numerous built-in, extendable solar-system body models, together with user-friendly interfaces to create
    and customize new bodies, such as vehicles.


    +++
    .. link-button:: _src_user_guide/state_propagation/environment_setup
            :type: ref
            :text: Find out more
            :classes: stretched-link btn-outline-primary

    ---
    :column: col-lg-4 p-3

    **State estimation capabilities**
    ^^^

    A powerful framework where state propagation and observations can be combined to simulate the trajectory
    determination process.

    +++
    .. link-button:: _src_user_guide/state_estimation
            :type: ref
            :text: Find out more
            :classes: stretched-link btn-outline-primary

    ---
    :column: col-lg-4 p-3

    **Large choice of numerical integrators**
    ^^^

    Various fixed and variable step-size built-in integrators, including Runge-Kutta 4, Runge-Kutta variable step-size
    (various orders), Bulirsch-Stoer, and Adams-Bashfort-Moulton.

    +++
    .. link-button:: _src_user_guide/state_propagation/propagation_setup/integration_setup
            :type: ref
            :text: Find out more
            :classes: stretched-link btn-outline-primary

    ---
    :column: col-lg-4 p-3

    **Preliminary mission design tools**
    ^^^

    Several tools for preliminary mission design, including Lambert targeters, patched conic multiple-gravity
    assists, and shape-based low-thrust models. Extended documentation

    +++
    .. link-button:: _src_user_guide/prelim_mission_design/mga_transfer
            :type: ref
            :text: Find out more
            :classes: stretched-link btn-outline-primary

    ---
    :column: col-lg-4 p-3

    **Guidance models**
    ^^^

    Possibility to embed built-in or user-defined aerodynamic, thrust, and other guidance models in the simulation.


    +++
    .. link-button:: _src_user_guide/state_propagation/environment_setup/custom_models
            :type: ref
            :text: Find out more
            :classes: stretched-link btn-outline-primary




.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: Getting started
   :hidden:

   _src_getting_started/installation
   _src_getting_started/setup_dev_environment
   _src_getting_started/primers_coding_tools
   _src_getting_started/examples
   _src_getting_started/tudatpy_submodules

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: User guide
   :hidden:

   _src_user_guide/state_propagation
   _src_user_guide/state_estimation
   _src_user_guide/prelim_mission_design
   _src_user_guide/mathematics

.. toctree::
   :maxdepth: 2
   :caption: Advanced topics
   :hidden:

   _src_advanced_topics/post_processing_python
   _src_advanced_topics/parallelization
   _src_advanced_topics/optimization_pygmo

.. toctree::
   :maxdepth: 2
   :caption: About
   :hidden:

   _src_about/contribute_to_tudat
   _src_about/research_output
   _src_about/history

