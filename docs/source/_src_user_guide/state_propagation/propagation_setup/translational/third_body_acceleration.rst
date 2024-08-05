.. _third_body_acceleration:

========================
Third-body accelerations
========================

Settings for a third-body and central gravitational acceleration are defined identically to direct gravitational
accelerations. During the creation and processing of the acceleration models, Tudat distinguishes three different
cases, for the body :math:`A` undergoing the acceleration, the body :math:`B` exerting the acceleration,
and the body :math:`C` as the center of propagation.


.. contents:: Contents:
    :depth: 3

Third-body perturbation
==================================

The central body is non-inertial (e.g. is not the SSB), and the acceleration *is not* exerted by central body. The acceleration is then computed from:

.. math::

 \mathbf{a}=\nabla U_{B}(\mathbf{r}_{A})-\nabla U_{B}(\mathbf{r}_{C})

This is the typical *third body* perturbation, for instance for the case where :math:`A` is a spacecraft orbiting the Moon, :math:`B` is the Earth and :math:`C` is the Moon.


Central gravitational acceleration
==================================

The central body is non-inertial (e.g. is not the SSB), and the acceleration *is* exerted by the central body. If the body undergoing the acceleration itself possesses a gravity field, the gravitational back-reaction is accounted for when setting up the gravitational acceleration.

.. math::

 \mathbf{a}=\nabla U_{B}(\mathbf{r}_{A})-\nabla U_{A}(\mathbf{r}_{B})

The backreaction (accounted for by the second term) becomes relevant when computing the mutual dynamics of two natural bodies. For instance, when propagating the Moon w.r.t. the Earth, and adding the point-mass gravitational acceleration of the Earth on the Moon, the following acceleration will be used:

.. math::

 \mathbf{a}=-\frac{\mu_{A}+\mu_{B}}{||\mathbf{r}||^{2}}\hat{\mathbf{r}}

with :math:`\mathbf{r}` the position of the Moon w.r.t. the Earth. The backreaction is taken into account by using the sum of the gravitational parameters (as opposed to only the gravitational parameter of the Earth).


Direct gravitational acceleration
==================================

The central body is inertial (e.g. is the SSB). In this case, the direct acceleration is used:

.. math::

 \mathbf{a}=\nabla U_{B}(\mathbf{r}_{A})

.. note::
   We stress that the above works equally well for **point-mass**, **spherical-harmonic** and
   **mutual-spherical-harmonic** accelerations (see examples below).

Examples
========

When propagating the dynamics of a spacecraft w.r.t. the Moon, the following will add the third-body point-mass
acceleration of the Earth:

.. tabs::

     .. tab:: Python

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/point_mass_gravity.py
         :language: python

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/point_mass_gravity.cpp
         :language: cpp

while the following will add the third-body spherical-harmonic acceleration of the Earth (zonal coefficients up to degree 4):

.. tabs::

   .. tab:: Python

    .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/spherical_harmonic_gravity_zonal.py
       :language: python

   .. tab:: C++

       :language: cpp

Note that above two code blocks are identical to those given as example in the API documentation
entries of :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.point_mass_gravity` and
:func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.spherical_harmonic_gravity`. It is through the definition
*of the central body* that a direct, central or third-body acceleration is created.
