**************************
Exposing C++ with Pybind11
**************************

This guide on exposing ``C++`` using ``pybind11`` is centered around the
architecture of the ``tudatpy/kernel`` source directory. This is done in
order to provider developers with a practical guide that introduces the
implementation and design of the current architecture.

.. note::
    This also allows developers to see motivations for the current design,
    should convention change, or deprecation of classes/functions occur.

The entirety of exposed C++ functionality in ``tudatpy`` is contained within
the ``tudatpy/kernel`` source directory. For reference during this guide, the
architecture of this directory is as follows:

.. code-block:: base
    :linenos:

Module Definition
#################

The following folded code shows the core elements of the
level ``kernel`` module definition in ``tudatpy``. It would serve the reader to
have glance through before we walk through the elements in detail.

.. code-block:: cpp
    :caption: ``tudatpy/kernel/kernel.cpp``
    :linenos:

    // expose tudat versioning
    #include <tudat/config.hpp>

    // include all exposition headers
    #include "expose_simulation.h"
    // other submodule headers...

    // standard pybind11 usage
    #include <pybind11/pybind11.h>
    namespace py = pybind11;

    PYBIND11_MODULE(kernel, m) {

        // Disable automatic function signatures in the docs.
        // NOTE: the 'options' object needs to stay alive
        // throughout the whole definition of the module.
        py::options options;
        options.disable_function_signatures();
        options.enable_user_defined_docstrings();

        // export the tudat version.
        m.attr("_tudat_version_major") = TUDAT_VERSION_MAJOR;
        m.attr("_tudat_version_minor") = TUDAT_VERSION_MINOR;
        m.attr("_tudat_version_patch") = TUDAT_VERSION_PATCH;

        // simulation module definition
        auto simulation = m.def_submodule("simulation");
        tudatpy::expose_simulation(simulation);

        // other submodule definitions...

        // versioning of kernel module
        #ifdef VERSION_INFO
          m.attr("__version__") = VERSION_INFO;
        #else
          m.attr("__version__") = "dev";
        #endif

    }

.. note::

    Starting with the end in mind, compiling the previous will result in a
    shared library named ``kernel.so``.

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



