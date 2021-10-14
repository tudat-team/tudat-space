***********
Mathematics
***********

.. _interpolators:

Interpolators
=============

Tudat contains a number of interpolators for discrete data sets. The input to an interpolator is a set of combinations of independent variables :math:`t_{i}`, and state variables :math:`\mathbf{x}_{i}`, where :math:`\mathbf{x}` may be a scalar, vector or matrix. A data sets that is often interpolated using tudat is the the state history, as generated from the propagation of dynamics (TODO: add link). The general operation of an interpolator is to take a set of combinations :math:`[t_{i},\mathbf{x}_{i}]` and turn this into a continuous function :math:`\mathbf{x}(t)`. 

The manner in which to use the tudat interpolators is similar to that of the various models for numerical propagation: settings for the interpolation are to be created, which are then processed along with the data that is to be interpolated to create the interpolator. An example, for the case of a linear interpolator, is shown below:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/math/interpolators/interpolator_import.py
                :language: python

          .. literalinclude:: /_src_snippets/math/interpolators/basic_interpolation.py
             :language: python


         .. tab:: C++

The data that is to be interpolated must be provided as a ``dict`` (in Python) with a float as independent variable, and the data that is to be interpolated as values. In the above example, the linear scheme is used to interpolate the ``data_to_interpolate`` data set at  :math:`t=100` (where typically, but not necesarilly, the independent variable in interpolation will represent time, in the context of Tudat).

Tudat includes the following interpolators for a data set with a single independent variable (TODO: insert API links):

* Piecewise constant interpolation
* Linear interpolation
* Cubic spline interpolation
* Hermite spline interpolation
* Lagrange interpolation

To use the Hermite spline interpolator, the user must provide not only the states :math:`\mathbf{x}_{i}` *and* the state derivatives :math:`d\mathbf{x}_{i}/dt` at the independent variable values :math:`t_{i}`:s 

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/math/interpolators/interpolator_import.py
                :language: python

          .. literalinclude:: /_src_snippets/math/interpolators/hermite_interpolation.py
             :language: python


         .. tab:: C++

Finally, Tudat contains a single interpolator for multi-dimensional interpolation: a multi-linear interpolation scheme. This interpolator is not yet exposed to Python, however.

To create interpolators, there are a number of additional settings that a user may want to modify. These are listed below:

Extrapolation/Boundary handling
-------------------------------

Typically, an interpolation of data at independent variables :math:`t_{0}...t_{N}` is only used within this range of independent variables. However, sometimes the interpolator is called beyond this range of values. The default behaviour of Tudat is that the interpolation scheme is extrapolated beyond this range *without warning*. The user can choose to override this behaviour, with one of the following five options (all defined by an entry of the ``BoundaryInterpolationType`` variable TODO):

* Throw exception: in this case the program will terminate with an error message when the interpolator is interrogated beyond the range :math:`[t_{0}...t_{N}]`
* Use boundary value: in this case, the value :math:`\mathbf{x}_{0}` is returned for :math:`t<t_{0}` (and :math:`\mathbf{x}_{N}` if :math:`t>t_{N}`).
* Use boundary value with warning: same as previous, but a warning is printed
* Extrapolate at boundary: the interpolation scheme is extended beyond the range `t_{0}...t_{N}` without any warning
* Extrapolate at boundary with warning: same as previous, but a warning is printed

Lookup scheme
-------------

When the ``interpolate`` function of the interpolator is called, the interpolator scheme will typically start by find the nearest neighbour of :math:`t` in the data set :math:`[t_{i}]`. Two options are implemented  (both defined by an entry of the ``AvailableLookupScheme`` variable TODO), with the so-called *hunting algorithm* being the default. The choice of lookup scheme may have an influence on computational efficiency for extremely large data sets

* Hunting algorithm: here, the interpolator 'remembers' which value of :math:`t_{i}` was the nearest neighbour during the previous call to the interpolate function, and starts looking at/near this entry of the data set :math:`[t_{i}]` to find the nearest neighbour
* Binary algorithm: the algorithm uses a binary search algorithm to find the nearest neighbour (see Press at al.)

.. _lagrange_interpolator_issues:

Special considerations: Lagrange interpolator
---------------------------------------------

The Lagrange interpolator that is implemented in Tudat warrants some additional discussion, as it is typically the interpolator of highest accuracy that is available, but has a number of features which may lead to unexpected behaviour, that a user must be aware of. To understand the issues, we briefly outline the algorithm that is used (see TODO for mathematical details):

* The Lagrange interpolator uses :math:`m` consecutive points to from the data set :math:`[t_{0}...t_{N}]` to create the polynomial of order :math:`m-1` that interpolates these points. From here on, we assume :math:`m` is even
* Let the nearest lower neighbour of the data point :math:`t` at which the state :math:`\mathbf{x}` is to be interpolated be :math:`t_{i}`
* The interpolating polynomial is constructed from the consecutive data points :math:`[t_{i-(m/2-1)}...t_{i+m}]` 
* This interpolating polynomial is known to experience strong fluctuations near the boundaries of this range (Runge's phenomenon), and the interpolating polynomial should ideally not be used outside of the range :math:`[t_{i}..t_{i+1}]`

In most situations, the above behaviour is followed without problem. For instance, if :math:`m=8` we use a :math:`7^{th}` order polynomial that interpolates a contiguous set of 8 data points out of the full data set (see figure, TODO). Normally, the interpolating polynomial is only used between the :math:`4^{th}` and :math:`5^{th}` data point, where it will typically be of good accuracy. However, issues occur if the data point :math:`t` at which the interpolation is to be performed is close to :math:`t_{0}` or :math:`t_{N}`. In those case, there is not sufficient data to constuct the interpolating polynomial *and* to only use this interpolating polynomial between the middle two data points that were used to it. In these cases, the user has a number of options (all defined by an entry of the ``LagrangeInterpolatorBoundaryHandling`` variable TODO):

* A cubic-spline interpolator is created from the first and last :math:`\max(m/2-1,4)` data points of the full data set, and these cubic spline interpolators are used when an interpolation at :math:`t<t_{(m/2-1)}` or :math:`t<t_{N-(m/2)}` is called
* The program will terminate with an error message when the :agrange interpolator is interrogated beyond its valid range

Integrators
===========

Root Finders
============

Filters
=======

Quadrature
==========

Statistics
==========

Geometric
=========


