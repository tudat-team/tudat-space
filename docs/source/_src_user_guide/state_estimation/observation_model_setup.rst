.. _observationModelSetup:

Observation Model Setup
=======================

Having defined the :ref:`link ends <linkEndSetup>`, you can now define and create the observation models, below the top-level workflow for this is discussed.

.. _observationTypes:

Defining observation settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tudat supports a diverse set of observation types, you can find the list of functions to create settings for obsevation models in our API documentation: :mod:`~tudatpy.observation_setup`. Below is an example of creating a list of settings for observation models.

.. code-block:: python

    # Define link ends
    one_way_nno_mex_link_ends = dict( );
    one_way_nno_mex_link_ends[ transmitter ] = ( "Earth", "NNO" );
    one_way_nno_mex_link_ends[ receiver ] = ( "MeX", "" );
    
    # Create list of observation settings
    observation_settings_list = list()
    observation_settings_list.append( observation_setup.one_way_range( one_way_nno_mex_link_ends ) )
    observation_settings_list.append( observation_setup.one_way_open_loop_doppler( one_way_nno_mex_link_ends ) )
                
                
This defines a one-way range and one-way Doppler (open-loop) observable, each with the same transmitter/receiver (see :ref:`linkEndSetup`). Note that you can extend a list of observation model settings with any number of entries, with any number of link ends. The only limitation is that you may not have duplicate entries of link ends *and* observable type. The full list of observation types supported by Tudat can be found at :mod:`~tudatpy.observation_setup`.

When defining observation models, you can for most types of models define settings for:

* **Biases:** A bias in TudatPy is applied to the observable after its 'ideal' value computed from the environment is computed. You can find a list of settings for observation biases in our API documentation: :mod:`~tudatpy.observation_setup.bias`
* **Light-time corrections:** When using an observable that involves the observation of one point/body in space by another (including any observable that involves the exchange of elecromagnetic signals), it is automatically taken into account that the signal travels at a finite speed (in vacuum: the speed of light). Unless a user specifies additional corrections, using the list of options in our API documentation: :mod:`~tudatpy.observation_setup.light_time_corrections`, this light time is calculated as taking place in a straight line with the speed of light. This involves the implicit solution of the light-time equation, as outlines :ref:`here <lighttime>`.

The above options are added to the calls of the observation model settings factory functions. Below is an example 

.. code-block:: python

    # Define link ends
    one_way_nno_mex_link_ends = dict( );
    one_way_nno_mex_link_ends[ transmitter ] = ( "Earth", "NNO" );
    one_way_nno_mex_link_ends[ receiver ] = ( "MeX", "" );
    
    # Define settings for light-time calculations
    light_time_correction_settings = [ observation_setup.first_order_relativistic_correction( [ 'Sun' ] )]
    
    # Define settings for range bias
    range_bias_settings = observation_setup.bias( 0.01 )
    
    # Create list of observation settings
    observation_settings_list = list()
    observation_settings_list.append( observation_setup.one_way_range( 
        one_way_nno_mex_link_ends
        light_time_correction_settings = light_time_correction_settings,
        bias_settings = range_bias_settings ) )
    observation_settings_list.append( observation_setup.one_way_open_loop_doppler( 
        one_way_nno_mex_link_ends, 
        light_time_correction_settings = light_time_correction_settings ) )
                
where we have defined that, for both observation models for which settings are created, the light-time calculation will take into account the first order relativistic correction of the Sun, by using the :func:`~tudatpy.first_order_relativistic_correction` function. For the range observable, we have defined an absolute bias of 1 cm (0.01 m), while leaving the Doppler observable unbiased.


Creating the models
~~~~~~~~~~~~~~~~~~~

Depending on the type of simulation you are using, you can use one of two manners in which to create the observation simulators from the observation settings:

* Create dedicated set of observation simulators, using the :ref:`~tudatpy.create_observation_simulators` function (TODO)

    .. code-block:: python

        # Create physical environment (as set of physical bodies)
        bodies = ...

        # Create settings for observation models
        observation_settings_list = list( )
        ...
        
        # Create observation simulators
        observation_simulators = create_observation_simulators( observation_settings_list, bodies )       
  
* Create the :ref:`~tudatpy.Estimator` object (TODO API and user guide), which creates the observation simulators automatically

    .. code-block:: python

       
        # Create physical environment (as set of physical bodies)
        estimator = Estimator(...)
        
        # Exract observation simulators
        observation_simulators = estimator.observation_simulators
        
In either case, the ``observation_simulators`` variable is a list of objects derived from :class:`~tudatpy.ObservationSimulator`, with a single object responsible for the simulation of a single *type* of observable (*e.g.* one-way range, one-way Doppler, *etc.*). The ``observation_simulators`` list of simulators can then be used when :ref:`simulating observations` (TODO). For 'manual' simulation of observations, you can extract an :class:`~tudatpy.ObservationModel` object from the ``ObservationSimulator``. Whereas the latter is responsible for *all* observations of a given kind, the former simualtes observations of a single kind, for a single set of link ends (e.g. one-way range observations between a given ground station and a single spacecraft). Details on the associated options can be found in the API documentation.



 


