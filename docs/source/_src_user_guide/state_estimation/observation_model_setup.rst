.. _observationModelSetup:

Setting up Observation Models
=============================

.. _observationTypes:

Observation Types
~~~~~~~~~~~~~~~~~

Tudat supports a diverse set of observation types, you can find the list of functions to create settings for obsevation models in our API documentation: :mod:`~tudatpy.observation_setup`. Below is an example of creating a list of settings for observation models.

.. code-block:: python

        AAAA
                
This defines a one-way range, one-way Doppler and angular position observable, each with the same  transmitter/receiver. Note that you can extend a list of observation model settings with any number of entries, wih any number of link ends. The only limitation is that you may not have duplicate entries of link ends *and* observable type.

When defining observation models, you can often define settings for:

* Biases A bias in TudatPy is applied to the observable after its 'ideal' value computed from the environment is computed. You can find a list of settings for observation biases in our API documentation: :mod:`~tudatpy.observation_setup.bias`
* Light-time corrections When using an observable that involves the observation of one point/body in space by another (including any observable that involves the exchange of elecromagnetic signals), it is automatically taken into account that the signal travels at a finite speed (in vacuum: the speed of light). Unless a user specifies additional corrections, using the list of options in our API documentation: :mod:`~tudatpy.observation_setup.light_time_corrections`, this light time is calculated as taking place in a straight line with the speed of light. This involves the implicit solution of the light-time equation, as outlines :ref:`here <lighttime>`

