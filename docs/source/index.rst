======================================
Welcome to Tudat Space!
======================================

The TU Delft Astrodynamics Toolbox (Tudat) is a powerful set of libraries that support astrodynamics and space research.
Such framework can be used for a wide variety of purposes, ranging from the study of reentry dynamic to interplanetary
missions. The core functionality of Tudat is implemented in C++ and exposed to Python using an interface called Tudat(Py).
Tudat and Tudat(Py) are entirely open-source and disseminated using conda packages.

.. grid:: 1 1 2 2
    :gutter: 2 3 4 4

    .. grid-item-card::
        :img-top: _static/rocket-solid.svg
        :text-align: center

        Getting started
        ^^^

        Launch your mission with Tudat(Py) using the Quickstart guide and installation instructions.
        The Getting Started section also contains some example applications to see TudatPy in action and a primer on related coding tools.

        +++

        .. button-ref:: getting_started_quickstart
            :expand:
            :color: secondary
            :click-parent:

            To the quickstart guide

    .. grid-item-card::
        :img-top: _static/user-astronaut-solid.svg
        :text-align: center

        User guide
        ^^^

        Our user guide provides in-depth information on the functionalities and concepts of Tudat(Py).
        This also includes the mathematical description of the models implemented in Tudat(Py).

        +++

        .. button-ref:: _src_user_guide/index
            :expand:
            :color: secondary
            :click-parent:

            To the user guide

    .. grid-item-card::
        :img-top: _static/laptop-code-solid.svg
        :text-align: center

        API reference
        ^^^

        The API reference provides the documentation of the functionality exposed in the Python interface.

        +++

        .. button-link:: https://py.api.tudat.space/en/latest/
            :expand:
            :color: secondary
            :click-parent:

            To the API reference

    .. grid-item-card::
        :img-top: _static/code-solid.svg
        :text-align: center

        Contributor's guide
        ^^^

        Learn more about where you can find the source code of Tudat(Py), upcoming developments and how you can contribute.

        +++

        .. button-ref:: contribute_to_tudat
            :expand:
            :color: secondary
            :click-parent:

            To the contributor's guide



.. toctree::
   :hidden:

   _src_getting_started/index
   _src_user_guide/index
   _src_advanced_topics/index

.. toctree::
   :hidden:

   API Reference <https://py.api.tudat.space/en/latest/>

.. toctree::
   :hidden:

   _src_about/index

.. nblinkgallery::
   :caption: Take a look at some examples!

   /_src_getting_started/_src_examples/propagation.rst
   /_src_getting_started/_src_examples/estimation.rst
   /_src_getting_started/_src_examples/mission_design.rst
   /_src_getting_started/_src_examples/pygmo.rst