.. _interpolators:

=============
Interpolators
=============

Tudat contains a number of interpolators for discrete data sets. The input to an interpolator is a set of combinations
of independent variables :math:`t_{i}`, and state variables :math:`\mathbf{x}_{i}`, where :math:`\mathbf{x}` may be a
scalar, vector or matrix. A data sets that is often interpolated using tudat is the the state history, as generated
from the propagation of dynamics (see :ref:`single_arc_propagation`). The general operation of an interpolator is to
take a set of combinations :math:`[t_{i},\mathbf{x}_{i}]` and turn this into a continuous function
:math:`\mathbf{x}(t)`.

.. seealso::
   The full API documentation for interpolators
   can be found here `here <https://tudatpy.readthedocs.io/en/latest/interpolators.html>`_.

General procedure
-----------------

The manner in which to use the tudat interpolators is similar to that of the various models for numerical propagation:

1. create settings for the interpolation (see :ref:`interpolator_types`);
2. create interpolator based on the settings and the data that is to be
   interpolated.

An example, for the case of a linear interpolator, is shown below:

.. use manually synchronized tabs instead of tabbed code to allow dropdowns
.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. literalinclude:: /_src_snippets/math/interpolators/interpolator_import.py
            :language: python

      .. literalinclude:: /_src_snippets/math/interpolators/basic_interpolation.py
         :language: python


In the example above, the linear scheme is used to interpolate the ``data_to_interpolate`` data set at  :math:`t=100`
(where typically, but not necessarily, the independent variable in interpolation will represent time, in the context of Tudat).

The data that is to be interpolated must be provided as a ``dict`` (in Python) or a ``std::map`` (in C++):

- ``key``: independent variable
- ``value``: dependent variable to be interpolated

Based on the type of independent variable, different functions to create the interpolator are available:

- *scalar* interpolator (see the
  :func:`~tudatpy.math.interpolators.create_one_dimensional_scalar_interpolator` function, as in the example above)
- *vector* interpolator (see the
  :func:`~tudatpy.math.interpolators.create_one_dimensional_vector_interpolator` function)
- *matrix* interpolator (see the
  :func:`~tudatpy.math.interpolators.create_one_dimensional_matrix_interpolator` function)


.. _interpolator_types:

Available types of interpolators
--------------------------------

Tudat includes the following interpolators for a data set with a single independent variable:

* :func:`~tudatpy.math.interpolators.piecewise_constant_interpolation`
* :func:`~tudatpy.math.interpolators.linear_interpolation`
* :func:`~tudatpy.math.interpolators.cubic_spline_interpolation`
* :func:`~tudatpy.math.interpolators.hermite_spline_interpolation`
* :func:`~tudatpy.math.interpolators.lagrange_interpolation`

To use the Hermite spline interpolator, the user must provide not only the states :math:`\mathbf{x}_{i}` *and*
the state derivatives :math:`d\mathbf{x}_{i}/dt` at the independent variable values :math:`t_{i}`:

.. use manually synchronized tabs instead of tabbed code to allow dropdowns
.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. literalinclude:: /_src_snippets/math/interpolators/interpolator_import.py
            :language: python

      .. literalinclude:: /_src_snippets/math/interpolators/hermite_interpolation.py
         :language: python

Additional settings
--------------------

To create interpolator settings, there are a number of additional settings that a user may want to modify
(these have default values in the factory functions for the interpolator settings), related to:

* the look-up scheme, through the enum :class:`~tudatpy.math.interpolators.AvailableLookupScheme`;
* the behaviour beyond the boundaries of the domain, through the enum :class:`~tudatpy.math.interpolators.BoundaryInterpolationType`;
* the behaviour close to the boundaries of the domain, through the enum :class:`~tudatpy.math.interpolators.LagrangeInterpolatorBoundaryHandling`
  (for the :func:`~tudatpy.math.interpolators.lagrange_interpolation` only).
