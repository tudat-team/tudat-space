**************************
tudat-bundle
**************************

This guide shows how ``C++``-based tudat code can be exposed to python and how it can be made available in a local ``tudatpy`` module.
This topic is relevant for developers who want to expose updated tudat code to a new tudatpy module and for users who like to extend tudatpy functionality via modification of the ``C++``-based tudat code.

The interface between tudat and tudatpy is managed via ``pybind11`` in the ``tudat-bundle`` environment.
%! Check version number


Setting up tudat-bundle
########################

%! Getting tudat bundle
%! Setting up Cmake


Introduction to tudat-bundle
#############################

The tudat-bundle consists of three subdirectories:

- ``tudat``, containing the tudat ``C++`` source code
- ``tudatpy``, containing the ``tudatpy/kernel`` directory in which the ``pybind`` exposure is facilitated
- ``cmake-build-XXX``, the build directory containing the compiled ``C++`` tudat code (cmake-build-XXX/tudat), as well as the compiled tudatpy kernels at cmake-build-XXX/tudatpy/tudatpy/kernel.so



The entirety of exposed C++ functionality in ``tudatpy`` is contained within
the ``tudatpy/kernel`` source directory. For reference during this guide, the
architecture of this directory is as follows:

.. code-block:: base
    :linenos:

%! insert architecture


Module Definition
#################

The following folded code shows the core elements of the module definition on level ``kernel`` in ``tudatpy``.
It would serve the reader to have glance through before we walk through the elements in detail.


.. literalinclude:: /_src_tudatpy/snippets/kernel.cpp
        :caption: ``tudatpy/kernel/kernel.cpp``
        :language: cpp

.. note::

    Starting with the end in mind, compiling the previous will create a shared library named ``kernel.so``, making available all submodules included in ``kernel.cpp``.

.. note::

    With the ``kernel.so`` library added to the Python path variable, users
    can then execute ``from kernel import simulation` successfully.

.. warning::

    The Python interpreter searches the ``sys.path`` in its order. Inspect
    the ``sys.path`` list to determine which variant of a module is imported.

Submodule Definition
####################

.. code-block:: cpp
    :caption: ``tudatpy/kernel/expose_simulation.hpp``
    :linenos:

    namespace tudatpy {

    void expose_simulation(py::module &m) {

    }

    }

.. code-block:: cpp
    :caption: ``tudatpy/kernel/expose_simulation.cpp``
    :linenos:

    namespace tudatpy {

    void expose_simulation(py::module &m) {

    }

    }

Function Definition
###################

With Overloads
--------------

With Custom Resource Management
-------------------------------

Class Definition
################

This section walks through the process of exposing C++ classes into Python
using Pybind11. An accompanying example is used and extended to certain
situations that may be encountered.

.. code-block:: cpp
    :linenos:

    class Animal {
    public:
        virtual ~Animal() { }
        virtual std::string go(int n_times) = 0;
    };

    class Dog : public Animal {
    public:
        std::string go(int n_times) override {
            std::string result;
            for (int i=0; i<n_times; ++i)
                result += "woof! ";
            return result;
        }
    };

Managed by ``std::shared_ptr<>``
--------------------------------

With Inheritance
----------------

Containing


Satisfying Conversions
######################

STL Containers
--------------

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

NumPy and Eigen
---------------

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



