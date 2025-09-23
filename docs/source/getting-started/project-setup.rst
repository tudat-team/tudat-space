
.. _tudat_ecosystem:

=================================
Understanding the Tudat ecosystem
=================================

The Tudat project consists of a variety of repositories, packages, pipelines, etc. that also relies on various external dependencies. This page will give an overview of the different component of the project, and how these are connected together.

The code for Tudat is housed on Github, which details provided here: :ref:`using_tudat_source`. The majority of the functionality is implemented in C++, and exposed to Python using the `pybind11 <https://pybind11.readthedocs.io/en/stable/index.html>`_ package. Some functionality in Tudat is implemented in Python only, primarily those that rely on the use of existing Python packages to facilitate data retrieval (for instance using `astroquery <https://astroquery.readthedocs.io/en/latest/>`_). A typical user will use the conda packages for tudatpy (see below) that contain the compiled C++ libraries and header files, but will not have to directly interact with C++ code. To facilitate user independence from C++, Tudat has a broad variety of options for implementing :ref:`custom_models` in Python, which during a simulation or analysis are interfaced with the compiled C++ libraries. However, for computationally intensive tasks, we recommend to implement models in C++. To do so, you can download and modify the source code of Tudat, compile it locally and use your own compiled libraries rather than the conda packages. If the implemented functionality may also be useful for others, we recommend you to open a pull request!

Tudat contains many tests to ensure the continued validity of the implemented functionality. These are primarily included in the C++ side of the code (with close to 300 unit tests). The source code of these tests can be found `here <https://github.com/tudat-team/tudatpy/tree/develop/tests/test_tudat/src>`_. Every time a new pull request or merge is made onto the master or develop branches of the tudat repository, all tests are automatically rebuilt and run (see ``Build and Test`` actions `here <https://github.com/tudat-team/tudatpy/actions>`_.

The Tudat repositories typically have (in addition to feature branches, bug fix branches etc. that are under development) a ``master`` branch and a ``develop`` branch.  The ``master`` branch gets updated once or twice per year, whenever we release a new minor or major version. Any new features or bug fixes are first merged into our ``develop`` branch. To use the most up-to-date version of the code, or when developing a new feature, we recommend to use this ``develop`` branch. On a daily basis, a Github action checks whether there have been any modifications to this branch and, if so, modifies the version tag (for instance from 0.9.0.dev34 to 0.9.0.dev35), and triggers a rebuild of the associated conda package (see below).

The Tudat conda packages are built on `Azure <https://dev.azure.com/tudat-team/feedstock-builds/_build>`_, for Ubuntu, Windows and Mac (for both Intel and Apple Silicon processors). Several Python-native tests are run when building the packages on Azure, and the package is only published if the tests pass succesfully. This set of tests is much smaller than the C++-based one, since it only concerns the Python-native implementation in Tudat (which is much more limited) in addition to small tests validating the Python exposure. Once successfully built, the conda packages are published on our `Anaconda channel <https://anaconda.org/tudat-team/>`_. We provide two types of packages. Firstly, we have our ``main`` package. This is the version that gets installed when following our regular installation guide. We also provide ``dev`` packages, which is built from the ``develop`` branch on Github. The installation of both packages is described on our installation guide.

The setup of the builds on Azure is handled by so-called feedstock repositories. For instance, the build of the `tudat repository <https://github.com/tudat-team/tudatpy>`_ is handled by the `tudat-feedstock <https://github.com/tudat-team/tudatpy-feedstock>`_ repository. Any push to any branch of the feedstock automatically triggers a build on Azure and (if enabled and the tests are successful) a new conda package.







