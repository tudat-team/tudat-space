======================================
Tudat Space
======================================


Tudat is a platform and community for astrodynamics and space research.
Our mission is to provide educators, researchers, students, and
enthusiasts access to a powerful toolkit, fuelling careers and
passions in astrodynamics and space. 

..
	Just a number of the key features of Tudat are the following: 

	- **Modular propagation** of orbital dynamics 

	  - Simulation the ascent of a space plane, or all planets in the solar system, using the same interfaces
	  - Swap out environment and acceleration models to smoothly go from preliminary design to high-fidelity models
	  - Use custom models (implemented in Python or C++) for guidance systems, or models not (yet) in Tudat    

	- **Concurrent propagation** of the coupled dynamics of any number of bodies 
	  
	  - Propagate the orbit and attitude dynamics of a spacecraft, re-entry vehicle or space plane
	  - Propagate the coupled dynamics of a natural satellite system, including the possibility for rotational dynamics
	  - Propagate dynamics and variational equations for any type of dynamics

	- **Simulated state estimation** using a wide variety of tracking data and parameters
	  
	  - From high-accuracy Mars gravity field determination, to coupled spacecraft-natural-body dynamics estimation
	  - Fuse radio tracking data, astrometric data, and other data types for either a covariance analysis or a full simulated estimation
	  - Single-arc, multi-arc, or a combination of the tow

	- **Estimation from real data** under active development! Coming soon:
	  
	  - Spacecraft orbit determination from DSN radio tracking data
	  - Processing of Minor Planet Center data for minor solar system body estimation  
	  - Incorporation of Planetary Radio Interferometry and Doppler Experiment (PRIDE) data into an estimation       

	- Perform **preliminary interplanetary transfer** trajectory design with patched conic methods   
	- All model **implementation in C++**, all **interfaces in Python**, using the pybind11 library
	- Extensively verified by **more than 200 unit tests**
	- Used as the core tool for **more than 20 peer-reviewed articles**, and more than 100 M.Sc. thesis projects
	- An extensive `API description <https://py.api.tudat.space/en/latest/>`_
	- Everything **open-source**!



What is Tudat?
===========================================

The TU Delft Astrodynamics Toolbox (Tudat) is a powerful set of libraries that support astrodynamics and space research.
Such framework can be used for a wide variety of purposes, ranging from the study of reentry dynamic to interplanetary
missions. The functionality of Tudat is implemented in C++, but a Python interface, called Tudatpy, is now available,
through which the core simulation functionality can be accessed. Tudat and Tudatpy are disseminated as conda packages;
to get started with them, have a look at our
:ref:`installation guide<getting_started_installation>`.


.. grid:: 1 1 3 3
  :gutter: 2

  .. grid-item-card::
    :text-align: center

    **Different dynamics types**
    ^^^

    Numerical propagation of different state types (translational state, rotational state, and mass) and their associated variational equations through built-in or user-defined acceleration and torque models.

    +++

    .. button-ref:: propagation_setup
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Find out more

  .. grid-item-card::
    :text-align: center

    **Flexible modeling of simulated bodies**
    ^^^

    Numerous built-in, extendable solar-system body models, together with user-friendly interfaces to create and customize new bodies, such as vehicles.

    +++

    .. button-ref:: environment_setup
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Find out more

  .. grid-item-card::
    :text-align: center

    **State estimation capabilities**
    ^^^

    A powerful framework where state propagation and observations can be combined to simulate the trajectory determination process.

    +++

    .. button-ref:: state_estimation
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Find out more

  .. grid-item-card::
    :text-align: center

    **Large choice of numerical integrators**
    ^^^

    Various fixed and variable step-size built-in integrators, including Runge-Kutta 4, Runge-Kutta variable step-size (various orders), Bulirsch-Stoer, and Adams-Bashfort-Moulton.

    +++

    .. button-ref:: integrator_setup
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Find out more

  .. grid-item-card::
    :text-align: center

    **Preliminary mission design tools**
    ^^^

    Several tools for preliminary mission design, including Lambert targeters, patched conic multiple-gravity assists, and shape-based low-thrust models. Extended documentation

    +++

    .. button-ref:: transfer_trajectory
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Find out more

  .. grid-item-card::
    :text-align: center

    **Guidance models**
    ^^^

    Possibility to embed built-in or user-defined aerodynamic, thrust, and other guidance models in the simulation.

    +++

    .. button-ref:: custom_models
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Find out more


Quickstart
==========

.. grid:: 1 1 3 3
  :gutter: 2

  .. grid-item-card::
    :text-align: center

    **Installation**
    ^^^

    Learn how to install the tudatpy package via conda.

    +++

    .. button-ref:: getting_started_installation
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Read our guide


  .. grid-item-card::
    :text-align: center

    **Online examples**
    ^^^

    Run the examples on mybinder and see how tudatpy works: you don't need to install any package or IDE.

    +++

    .. button-link:: <https://mybinder.org/v2/gh/tudat-team/tudatpy-examples/master>
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Try it out


  .. grid-item-card::
    :text-align: center

    **Research output**
    ^^^

    Find out some state-of-the-art examples of what you can do with tudat(py) by having a look at our list of publications.

    +++

    .. button-ref:: research_output
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Have a look


This website contains user guides and tutorials to use Tudat and it is organized as follows:

- *Getting Started:* all the information for new users, including how to install tudatpy and some examples
  showcasing its functionalities.
- *User Guide:* several guides explaining how different parts of tudatpy code are used together to create a simulation.
- *Advanced topics*: guides for more advanced topics (e.g., optimization with Tudat).
- *Resources from Tudat ecosystem:* links to other Tudat resources (API reference, developer documentation, etc...)
  not hosted directly on tudat-space.
- *About:* additional information about Tudat and its ecosystem.


Additional resources
============================

Some resources related to Tudatpy are located elsewhere. See below!

.. grid:: 1 1 3 3
  :gutter: 2

  .. grid-item-card::
    :text-align: center

    **TudatPy API reference**
    ^^^

    Documentation of the tudatpy Application Programming Interface.

    +++

    .. button-link:: https://py.api.tudat.space
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Go to the website

  .. grid-item-card::
    :text-align: center

    **Developer Documentation**
    ^^^

    A separate website with guides and resources to develop Tudat and TudatPy code and documentation.

    +++

    .. button-link:: https://tudat-developer.readthedocs.io/en/latest/
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Go to the website


  .. grid-item-card::
    :text-align: center

    **Mathematical model definition**
    ^^^

    A manual containing definitions of mathematical models implemented in Tudat.

    +++

    .. button-link:: https://github.com/tudat-team/tudat-space/raw/master/Tudat_mathematical_model_definition.pdf
       :expand:
       :color: primary
       :click-parent:
       :outline:

       Download the manual


.. toctree::
   :titlesonly:
   :maxdepth: 3
   :caption: Getting started
   :hidden:

   _src_getting_started/quickstart
   _src_getting_started/installation
   _src_getting_started/examples
   _src_getting_started/primers_coding_tools
   _src_getting_started/faq
   _src_getting_started/using_source

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: User guide
   :hidden:

   _src_user_guide/tudatpy_submodules
   _src_user_guide/state_propagation
   _src_user_guide/state_estimation
   _src_user_guide/prelim_mission_design
   _src_user_guide/mathematics

.. toctree::
   :maxdepth: 2
   :caption: Advanced topics
   :hidden:

   _src_advanced_topics/sphinx-linking
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

