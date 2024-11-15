.. _observationModelSetup:

Observation Model Setup
=======================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   observation_model_setup/observation_models

Having defined the :ref:`link ends <linkEndSetup>`, you can now define and create the observation models. Below the general workflow for this is discussed. The observation models can play two roles in Tudat:

* To generate simulated data inside Tudat, instead of loading real data.
* For use in a (least-squares) estimation loop, to create the observation models used to fit input data (real or simulated) to observations provided

Before providing any specifics, we need to distinguish several different types of settings/models/data structures in Tudat, which will be elaborated upon in
the following pages:

* **Observation Model Settings**, which are presented :ref:`below <observationTypes>` containing settings for the *types* of observations that are to be used. These objects do not perform any calculation, but defined the properties of the observation simulators that are created
* **Observation Simulators**, which are discussed :ref:`below <observationSimulators>`. These objects compute the actual observations from the current properties of the environment. As input, these objects require observation times (and possibly additional metadata).
* **Observation Simulation Settings**, which are discussed on the :ref:`following page<observationTypes2>`. These objects define *how to use the observation simulators* by providing the required settings for observation times, etc.
* **Observation Collection**, which are discussed on the :ref:`following page<accessing_observations>`. These objects store the full set of observations and associated data used in a single estimation/covariance analysis in Tudat

.. _observationTypes:

Defining observation settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tudat supports a diverse set of observation types.
The creation of an observation model is done in a similar manner as models used for the numerical propagation:
an object defining the settings of each observation model is created (of type :class:`~tudatpy.numerical_simulation.estimation_setup.observation.ObservationModelSettings`),
which is then processed to create the actual observation model. The full list of available observation models
is discussed :ref:`here <observation_model_overview>`, including links to the API documentation

A basic observation model is defined by:

* The type of the observation
* The link ends involved in the observation (e.g. transmitter, receiver)

Below is a basic example of creating settings for two observation models. Note that the below code snippet defines a o
ne-way range and one-way Doppler (open-loop) observable, each with the New Norcia ESTRACK station/Mars Express as transmitter/receiver
(see :ref:`linkEndSetup`). These settings are put into the ``observation_settings_list`` list.
Note that this list of observation model settings can be extended with any number of entries, with any number of link ends.
The only limitation is that you may not have duplicate entries of link ends *and* observable type
(as this would essentially define an identical type of observation).


.. code-block:: python

    # Define link ends
    one_way_nno_mex_link_ends = dict( )
    one_way_nno_mex_link_ends[ transmitter ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "NNO" )
    one_way_nno_mex_link_ends[ receiver ] = estimation_setup.observation.body_origin_link_end_id( "MeX" )
    one_way_nno_mex_link_definition = estimation_setup.link_definition( one_way_nno_mex_link_ends )

    
    # Create list of observation settings
    observation_settings_list = list()
    observation_settings_list.append( observation_setup.one_way_range( one_way_nno_mex_link_ends ) )
    observation_settings_list.append( observation_setup.one_way_open_loop_doppler( one_way_nno_mex_link_ends ) )
                
                

When defining observation models, you can for most types of models define settings for:

* **Biases:** A bias in Tudat is applied to the observable after its 'ideal' value computed from the environment is computed. You can find a list of settings for observation biases in our :doc:`API documentation <observation>`.
* **Light-time corrections:** When using an observable that involves the observation of one point/body in space by another (including any observable that involves the exchange of electromagnetic signals), it is automatically assumed that the signal travels at the speed of light, and the associated light-time is determined when calculating the observable. Deviations from the signal's ideal trajectory (straight line at speed of light) may be defined by adding light-time correction settings, as listed in our :doc:`API documentation <observation>`.
* **Light-time convergence settings:** Calculating the light time between two link ends requires the iterative solution of the light-time equation. Default settings for convergence criteria for this solution are implemented, but a user may modify these settings if so desired. The associated settings object can be created using the :func:`~tudatpy.numerical_simulation.estimation_setup.observation.light_time_convergence_settings` function.

Observation biases are used to add any systematic deviations from the 'physical' value of the computed observation
(due to unmodelled electronic delays, or unmodelled propagation effects of the electromagnetic signals). A list of available biases
can be found TODO. In short, for a bias :math:`\Delta h` (which may be a function of time, or properties of the environment),
an 'ideal' computed observation :math:`\bar{h}`, the actual computed observation becomes:

.. math::

  h(t)=\bar{h}(t)+\Delta h(t)

Note that the *random* noise is not yet considered here, as this is typically not modelled as part of the observation itself during the estimation.

The light-time correction and light-time convergence settings influence how the light time in one 'leg' (e.g. between two link ends, here with indices 0 and 1) is calculated.
To compute the light time, the following implicit equation has to be solved:

.. math::

  \frac{||\mathbf{r}_{1}(t_{1}) - \mathbf{r}_{0}(t_{0})||}{c}=\left(t_{1}-t_{0}\right)+\Delta t(t_{0},t_{1};\mathbf{r}_{1}(t_{1}),\mathbf{r}_{0}(t_{0}))

where, depending on the reference link end, the time :math:`t_{0}` at link end 0 is kept fixed, or the time :math:`t_{1}` at link end 1 is kept fixed.
The :math:`\mathbf{r}_{0}` and :math:`\mathbf{r}_{1}` functions define the positions of link end 0 and 1 as a function of time. The function :math:`\Delta t`
collects all effects that cause the propagation of the signal to deviate from propagation in a straight line at the speed of light.

.. note::
    The light time equation is *always* solved when using an observable that involved the transmission/reception of a signal. The "light time corrections"
    only refer to deviations from the straight-line speed of light propagation of the signal.

The above options are added to the calls of the observation model settings factory functions. Below is an example

.. code-block:: python

    # Define link ends
    one_way_nno_mex_link_ends = dict( )
    one_way_nno_mex_link_ends[ transmitter ] = estimation_setup.observation.body_reference_point_link_end_id( "Earth", "NNO" )
    one_way_nno_mex_link_ends[ receiver ] = estimation_setup.observation.body_origin_link_end_id( "MeX" )
    one_way_nno_mex_link_definition = estimation_setup.link_definition( one_way_nno_mex_link_ends )
    
    # Define settings for light-time calculations
    light_time_correction_settings = [ observation_setup.first_order_relativistic_correction( [ 'Sun' ] )]
    
    # Define settings for range bias
    range_bias_settings = observation_setup.absolute_bias( 0.01 )
    
    # Create list of observation settings
    observation_settings_list = list()
    observation_settings_list.append( observation_setup.one_way_range( 
        one_way_nno_mex_link_ends,
        light_time_correction_settings = light_time_correction_settings,
        bias_settings = range_bias_settings ) )
    observation_settings_list.append( observation_setup.one_way_open_loop_doppler( 
        one_way_nno_mex_link_ends, 
        light_time_correction_settings = light_time_correction_settings ) )
                
where we have defined that, for both observation models for which settings are created, the light-time calculation will take into account the first-order relativistic correction of the Sun, by using the :func:`~tudatpy.numerical_simulation.estimation_setup.observation.first_order_relativistic_light_time_correction` function. For the range observable, we have defined an absolute bias of 1 cm (0.01 m) using the :func:`~tudatpy.numerical_simulation.estimation_setup.observation.absolute_bias`, while leaving the Doppler observable unbiased.

.. _observationSimulators:

Creating the observation models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``observation_settings_list`` in the above examples (a ``list[ObservationModelSettings]``) is used to create the observation
simulators, which compute the actual values of the observables in Tudat. Depending on the your use case, a user may or may not interact
with the observation simulators directly:

* **Simulated observations** In this case, the user must interact with the observation simulators created from the ``observation_settings_list`` (which can be done in several ways), as discussed in more detail below
* **Real observations** In this case, the ``observation_settings_list`` is used inside the estimation to create the observation simulators and generated the 'computed observations' from which the residuals are computed

Therefore, the rest of this section is only relevant for the first part: using simulated observations in Tudat.

.. note::
    This section only discusses the *creation* of the observation simulators. The use of these simulators to generate observations is discussed on the :ref:`next page<observation_simulation>`

In what follows, we distinguish two different kinds of observation models:

* The **truth model**, which is the one used to simulate the observations which we use as input to the estimation. When using real observations, the 'truth model' is our physical reality
* The **estimation model**, which is the model used inside the estimator to fit the real or simulated observations (which are generated from the truth model)

In other words, when computing the residuals from 'observed minus computed' (or 'O-C') data, the truth model is the source of the 'observed* data, and the estimation model is the source of the *computed* data.

When using simulated observations, one can therefore choose between two different approaches

* The *truth model* and *estimation model* are identical to one another, so that the observation model(s) used to fit the observations is mathematically identical to the one used to generate them
* The *truth model* and *estimation model* are different from one another, so that there are physical effects present in the mathematical model used to simulate the observations which are not present in the model used to do the estimation

Same truth and estimation model
"""""""""""""""""""""""""""""""

The first case (equal truth and estimation model) is obviously a simplification of reality: when processing real data there are *always* effects present in our physical reality that are not incorporated into our models
However, the first case can be very useful for a number of cases. Firstly, when only performing a :ref:`covariance analysis<covarianceSettings>`, the estimation model *is never used*, so we can dispense with
its definition altogether (greatly simplifying the setup!) Secondly, doing a :ref:`full estimation<fullEstimationSettings>` with the truth and estimation model equal to one another allows one to study the influence that
different data types, their noise levels, etc. have on the final estimation, with some more flexibility than what is the case in the covariance analysis. More specifically,
in a covariance analysis one is limited to Gaussian uncorrelated noise, which in a full estimation you can add any noise you like to the observations.

When taking this approach, one makes use of the fact that observation simulators for the estimation are created anyway when creating an :class:`~tudatpy.numerical_simulation.Estimator` object (discussed further :ref:`here <perform_estimation>`).
You can extract these ``observation_simulators`` as follows, and use them to :ref:`simulate observations <observationSimulation>` as follows:

.. code-block:: python

  # Create physical environment (as set of physical bodies)
  estimator = Estimator(
      bodies,
      parameters_to_estimate,
      observation_settings_list,
      propagator_settings)

  # Extract observation simulators
  observation_simulators = estimator.observation_simulators


Different truth and estimation model
""""""""""""""""""""""""""""""""""""

The second case above, where the truth and estimation model are different from one another, opens up a broad range of options. In principle, any and all settings
of the bodies, the propagation model, and the observation models can be made different between the two. A challenge is often in choosing the difference that one
wants to implement to study the case at hand. In this case, the observation simulators are created directly, using the :func:`~tudatpy.numerical_simulation.estimation_setup.create_observation_simulators` function:

.. code-block:: python

  # Create physical environment (a set of physical bodies)
  bodies = ...

  # Create settings for observation models
  observation_settings_list = list( )
  ...

  # Create observation simulators
  observation_simulators = create_observation_simulators( observation_settings_list, bodies )       

When subsequently creating the :class:`~tudatpy.numerical_simulation.Estimator` object (discussed further :ref:`here <perform_estimation>`)
to perform the estimation, one can then provide a different ``observation_settings_list`` to ensure a difference between the truth
and estimation models. One can also choose to provide different ``bodies``, so that the physical environment from which
the observations are simulated, and the one to which they are fit, are different. Finally, even when using the same ``bodies``,
one can choose a different model for the states of the estimated bodies to ensure a difference in truth and estimation model.

The observation simulators
""""""""""""""""""""""""""

In either case, the ``observation_simulators`` variable is a list of objects derived from
:class:`~tudatpy.numerical_simulation.estimation.ObservationSimulator`, with a single object responsible for the simulation
of a single *type* of observable (*e.g.* one-way range, one-way Doppler, *etc.*). The ``observation_simulators``
is then used for simulating the actual observations to be used in the analysis, as described in :ref:`observationSimulation`.
Note that the ``ObservationSimulator`` is responsible for *all* observations of a given kind (e.g. each set of link ends),
the ``ObservationModel`` simulates observations of a single kind, for a single set of link ends
(e.g. one-way range observations between a given ground station and a single spacecraft).
Details on the associated options can be found in the API documentation.

For 'manual' simulation of observations, you can extract an :class:`~tudatpy.ObservationModel` object from the ``ObservationSimulator`` (TODO example).
