**************************
Exposing C++ with Pybind11
**************************

Common Errors Encountered
#########################

Relating to Eigen
-----------------

.. code-block:: base
    :linenos:

    python: /home/ggarrett/miniconda3/envs/tudat-env/include/eigen3/Eigen/src/Core/DenseStorage.h:109: Eigen::internal::plain_array<T, Size, MatrixOrArrayOptions, 16>::plain_array() [with T = double; int Size = 6; int MatrixOrArrayOptions = 0]: Assertion `(internal::UIntPtr(eigen_unaligned_array_assert_workaround_gcc47(array)) & (15)) == 0 && "this assertion is explained here: " "http://eigen.tuxfamily.org/dox-devel/group__TopicUnalignedArrayAssert.html" " **** READ THIS WEB PAGE !!! ****"' failed.

Please see :ref:`Missing Standard Conversions`

Missing Conversions
-------------------

The following conversion table for ``STL`` containers in C++ can be satisfied
by adding ``#include <pybind11/stl.h>`` to your header file while using
Pybind11 [source_].

+----------+---------------------------------------------------------------------+
| Python   |                                 C++                                 |
+----------+---------------------------------------------------------------------+
| ``list`` | ``std::vector<>``/``std::deque<>``/``std::list<>``/``std::array<>`` |
+----------+---------------------------------------------------------------------+
| ``set``  |               ``std::set<>``/``std::unordered_set<>``               |
+----------+---------------------------------------------------------------------+
| ``dict`` |               ``std::map<>``/``std::unordered_map<>``               |
+----------+---------------------------------------------------------------------+

.. tip::
    For dealing with conversions between Python lists, NumPy ndarrays and Eigen
    arrays in C++, the following lines cover all bases.
    .. code-block:: cpp
        :linenos:

        // Conversion for standard types (e.g. list->vector)
        #include <pybind11/stl.h>
        // Limited conversion for numpy<->eigen
        #include <pybind11/eigen.h>
        #include <pybind11/numpy.h>



