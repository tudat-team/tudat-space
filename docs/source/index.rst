======================================
Tudat Space
======================================


Tudat Space is a platform and community for astrodynamics and space research.
Our mission is to provide educators, researchers, students, and
enthusiasts access to a powerful toolkit, fuelling careers and
passions in astrodynamics and space. It contains user guides and tutorials to use Tudat.

**Content of Tudat Space**

- *Getting Started:* all the information for new users, including how to install tudatpy and some examples
  showcasing its functionalities.
- *User Guide:* several guides explaining how different parts of tudatpy code are used together to create a simulation.
- *Resources:* guides for external tools that a user might need when using Tudat.
- *About:* additional information about Tudat and its ecosystem.



What is Tudat?
===========================================

The TU Delft Astrodynamics Toolbox (Tudat) is a powerful set of libraries that support astrodynamics and space research.
Such framework can be used for a wide variety of purposes, ranging from the study of reentry dynamic to interplanetary
missions. The functionality of Tudat is implemented in C++, but a Python interface, called Tudatpy, is now available,
through which the core simulation functionality can be accessed. Tudat and Tudatpy are disseminated as conda packages;
to get started with them, have a look at our
:ref:`installation guide<getting_started_tudatpy>`.



.. panels::

    **TudatPy API reference**
    ^^^

    Documentation of the tudatpy Application Programming Interface.

    +++

    .. link-button:: https://tudatpy.readthedocs.io
        :text: Tudatpy API reference
        :classes: btn-outline-primary btn-block stretched-link

    ---

    **Developer Documentation**
    ^^^

    A separate website with guides and resources to develop Tudat and TudatPy code and documentation.

    +++

    .. link-button:: https://tudat-developer.readthedocs.io/en/latest/
        :text: Tudat Developer Docs
        :classes: btn-outline-primary btn-block stretched-link


.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: Getting started
   :hidden:

   _src_getting_started/installation
   _src_getting_started/setup_ide
   _src_getting_started/examples

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: User guide
   :hidden:

   _src_user_guide/state_propagation
   _src_user_guide/state_estimation
   _src_user_guide/astrodynamics
   _src_user_guide/mathematics

.. toctree::
   :maxdepth: 2
   :caption: Resources
   :hidden:

   _src_resources/post_processing
   _src_resources/pygmo_basics
   _src_resources/use_of_tools

.. toctree::
   :maxdepth: 2
   :caption: About
   :hidden:

   _src_about/about
   _src_about/api
   _src_about/developer_docs
   _src_about/documentation

