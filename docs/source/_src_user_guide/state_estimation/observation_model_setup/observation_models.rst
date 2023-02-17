
.. _observation_model_overview:

==================
Observation models
==================

On this page, we provide an overview of the categories of observation models that are available (with links to API documentation), as well as some general notes on their usages, typical pitfalls, hints, etc.

.. _available_observation_models:

Available Model Types
=====================

Below is a list with the different observation models is given. It is important to realize that Tudat does *not* make an a priori distinction between different manners in which the same observation may be realized. For instance, a VLBI observation of a spacecraft, referenced to the geocenter, and an optical astrometric observation of Io by a spacecraft, are both modelled as an ``angular_position`` observable. The difference between the different realization lies in the different noise levels, link  ends, biases, etc., while using the same observation model.

* Range observations: 

  * **One-way range**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.one_way_range`
  * **Two- (and three-)way range**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.two_way_range`, or  :func:`~tudatpy.numerical_simulation.estimation_setup.observation.two_way_range_from_one_way_links`. The latter function provided more fine-grained control of the settings for the up- and downlink (e.g. using different light-time corrections for each). See :ref:`two_three_way_observables` for the manner in which Tudat distinguishes between two- and three-way observations. Note that the two-way functions is idenical to the n-way function, with a check on the number of link ends added.
  * **N-way range**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.n_way_range` or :func:`~tudatpy.numerical_simulation.estimation_setup.observation.n_way_range_from_one_way_links`. This observable provides a generalization of the two-way range, and can have any number of constituent links.


* Averaged Doppler observables (see :ref:`doppler_types` for the distinction with instantaneous Doppler)

  * **One-way averaged Doppler**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.one_way_doppler_averaged`
  * **Two- (and three-)way averaged Doppler**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.two_way_doppler_averaged`, or  :func:`~tudatpy.numerical_simulation.estimation_setup.observation.two_way_doppler_averaged_from_one_way_links`. The latter function provided more fine-grained control of the settings for the up- and downlink (e.g. using different light-time corrections for each). See :ref:`two_three_way_observables` for the manner in which Tudat distinguishes between two- and three-way observations. Note that the two-way functions is idenical to the n-way function, with a check on the number of link ends added.
  * **N-way averaged Doppler**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.n_way_doppler_averaged` ( or  :func:`~tudatpy.numerical_simulation.estimation_setup.observation.n_way_doppler_averaged_from_one_way_links`). This observable provides a generalization of the two-way averaged Doppler, and can have any number of constituent links.


* Instantenous doppler observables (see :ref:`doppler_types` for the distinction with averaged Doppler)

  * **One-way instantaneous Doppler**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.one_way_doppler_instantaneous`
  * **Two-way (and three-way) instantaneous Doppler**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.two_doppler_instantaneous`, or  :func:`~tudatpy.numerical_simulation.estimation_setup.observation.two_way_doppler_instantaneous_from_one_way_links`. The latter function provided more fine-grained control of the settings for the up- and downlink (e.g. using different light-time corrections for each). See :ref:`two_three_way_observables` for the manner in which Tudat distinguishes between two- and three-way observations.


* Angular observables 

  * **Angular position** right ascension and declination in inertial frame of a body, as observed by another body, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.angular_position`
  * **Relative angular position** relative right ascension and declination of two bodies, as observed by another body, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.relatives_angular_position`


* Direct state observables. These observations are typically not generated directly, but are used for idealized simulations, or to fit a model to an existing orbit.

  * Three-dimensional **Cartesian position**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.cartesian_position`
  * Three-dimensional **Cartesian velocity**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.cartesian_velocity`
  * Orientation of body w.r.t. inertial frame as **3-1-3 Euler angles**, defined using :func:`~tudatpy.numerical_simulation.estimation_setup.observation.313_euler_angles`


.. _specific_observation_considerations:

Points of attention
===================

Here, we give a brief overview of some specific aspects of the obserevation models that may be useful for a user to
know, in order to properly select and understand their choice of obserevation models.
This page is meant to supplement the API documentation, and is *not* a comprehensive overview of all obserevation models.


.. _two_three_way_observables:

Two- and three-way observables  
------------------------------

In the typical terminology of (deep-)space tracking, an observable denoted as 'two-way', with an uplink and downlink to (typically) a space segment has the same transmitter for the uplink, and receiver for the downlink (e.g. only a single ground station involved in the observation). An observable that is denoted as 'three-way' on the other hand, is used for a two-way observable (e.g. a single uplink and a single downlink) where the transmitting and receiving ground station are *not* the same. In Tudat, both types of observations are defined using the 'two-way' functions (e.g. :func:`~tudatpy.numerical_simulation.estimation_setup.observation.two_way_range`), with the distinction between the typical naming convention of two- and three-way observations made in the ``link_ends`` that are provided as input (``transmitter`` and ``receiver`` sthe same entry, or not). The n-way observations in Tudat, such as :func:`~tudatpy.numerical_simulation.estimation_setup.observation.n_way_range`, define observations with :math:`n` links (e.g. ground station -> spacecraft 1 -> spacecraft 2 -> spacecraft 1  -> ground station would be an example for :math:`n=4`). 


.. _doppler_types:

Doppler types
-------------

A typical Doppler observable from e.g. the Deep Space Network does not provide the instantaneous observed range-rate. Instead, it provides an observable that is equivalent to the range-rate averaged over an integration time :math:`\Delta t`. At present, this is implemented in Tudat as the difference between two range observations, offset in time by :math:`\Delta t`. These observables are provided by the ``..._doppler_averaged`` obserevables. To compute the instantanous Doppler observable, such as those for instance generated by a tracking station in open-loop mode, use the ``..._doppler_instantaneous`` observable. 


Instantaneous Doppler Implementation
------------------------------------

The instantaneous Doppler observables are all derived from the one-way observable :math:`h`:

.. math::
    h=\frac{d\tau_{T}}{d\tau_{R}}=\left(\left(\frac{d\tau}{dt}\right)_{T}\frac{dt_{T}}{dt_{R}}\left(\frac{dt}{d\tau}\right)_{R} - 1\right)c

where the :math:`T` and :math:`R` subscripts denote the transmitter and receiver, :math:`\tau` denotes the proper time as experience by an observed, and :math:`t` denotes coordinate time. The multiplication by :math:`c` (speed of light) may be omitted by selecting a non-dimensionalized observable in the factory function. In the present context, :math:`t` is taken as dynamical barycentric time (TDB). Note that, unless otherwise specified, all times used in Tudat are in TDB. Even though TDB is not technically a coordinate time, in the above equation :math:`t` may be referred to TDB, as the constant scaling offset between TDB and TCB (barycentric coordinat time) drops out of the above equation.

For basic simulations. The :math:`\frac{d\tau}{dt}` terms can be omitted (by not providing the proper time rate settings in the factory function), so that the observable becomes:

.. math::
    h=\left(\frac{dt_{T}}{dt_{R}} - 1\right)c
    
In this formulation, the ``..._doppler_averaged`` observables reduce exactly to the time average of the ``..._doppler_instantaneous`` observables. The full formulation of the Doppler observable (including the proper time rates) is typically used either when processing real (open-loop Doppler) data, or when analyzing the influence of physical parameters on the propet ime rate, for instance for simulating relativistic experiments.

The second and third the terms in the first equation for the instantaneous Doppler observables are expanded in a Taylor series (at present, hardcoded to :math:`N=3`), to prevent excessive rounding errors (as a result of each of the constituent derivaties being :math:`\approx 1`. By setting :math:`\Delta\tau=\tau-t`, we have:

.. math::
    \frac{d\tau}{dt}&=1+\frac{d\Delta\tau}{dt}\\
    \frac{dt}{d\tau}&\approx 1+\sum_{i}^{N}(-1)^i\frac{d\tau}{dt}

Similarly, we can expand the coordinate time derivative as, seting :math:`T=t_{R}-t_{T}`:

.. math::
    s_{T}&=-\frac{dT}{d\mathbf{r}_{T}}\cdot\left(\frac{\mathbf{v_{T}}}{c}\right)\\
    s_{R}&=\frac{dT}{d\mathbf{r}_{R}}\cdot\left(\frac{\mathbf{v_{R}}}{c}\right)\\
    \frac{dt_{T}}{dt_{R}}&=\frac{1-s_{R}}{1+s_{T}}+1\\
    \frac{1}{1+s_{T}}&\approx 1+\sum_{i}^{N}s_{T}

Using these approximations, the complete observable is then computed. Note that, when calculating the partial derivatives of the observables for estimation, only the first-order Taylor series terms are retained.

    











