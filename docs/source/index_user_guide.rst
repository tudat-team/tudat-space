.. _user_guide:

******************************
User Guide
******************************
This section provides a detailed guide on how to use the functionalities of Tudat(Py).

.. grid:: 1 1 2 2
    :gutter: 2 3 4 4

    .. grid-item-card::
        :text-align: center

        **Propagation**
        ^^^

        Learn how to setup a propagation problem and simulation it with Tudat(Py).
        This includes the environment setup, dynamical models, and numerical integration of a state or state transition matrix.

        +++

        .. button-ref:: state_propagation
            :expand:
            :color: secondary
            :click-parent:

            To the propagation section

    .. grid-item-card::
        :text-align: center

        **Estimation**
        ^^^

        Learn how to setup an estimation problem with Tudat(Py).
        The section includes background information on how to setup observation models, simulate observations, load real data and perform the estimation.

        +++

        .. button-ref:: state_estimation
            :expand:
            :color: secondary
            :click-parent:

            To the estimation section

    .. grid-item-card::
        :text-align: center

        **Preliminary mission design**
        ^^^

        The preliminary mission design section introduces the transfer trajectory module of Tudat(Py).
        This includes the setup of powered and unpowered trajectories, in addition to swingby maneuvers.

        +++

        .. button-ref:: prelim_mission_design
            :expand:
            :color: secondary
            :click-parent:

            To the mission design section

    .. grid-item-card::
        :text-align: center

        **Mathematics**
        ^^^

        The mathematics section holds information about the interpolators implemented in Tudat(Py).

        +++

        .. button-ref:: mathematics
            :expand:
            :color: secondary
            :click-parent:

            To the mathematics section


The :ref:`tudatpy_submodules` section provides an overview of all modules available in TudatPy.

For more information on how to use TudatPy with other libraries, see the :ref:`optimization_pygmo` or :ref:`parallelization` sections.

.. toctree::
   :caption: Tudat(Py) user guide
   :hidden:

   /_src_user_guide/state_propagation
   /_src_user_guide/state_estimation
   /_src_user_guide/prelim_mission_design
   /_src_user_guide/mathematics
   Mathematical model definition <https://raw.githubusercontent.com/tudat-team/tudat-space/master/Tudat_mathematical_model_definition.pdf>
   /_src_user_guide/tudatpy_submodules

.. toctree::
   :caption: Interface with other libraries
   :hidden:

   /_src_advanced_topics/optimization_pygmo
   /_src_advanced_topics/parallelization
   /_src_advanced_topics/post_processing_python
