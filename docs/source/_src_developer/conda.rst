***********************
Advanced Usage of Conda
***********************

.. image:: _static/conda_logo.svg

.. tip::
    This page follows directly from :ref:`Getting Started with Conda`, so make
    sure to have gone through that first.

:ref:`Getting Started with Conda`

Choosing an Installer
#####################

When using the conda package manager, you have three options to choose from:

- Miniconda_, Command Line Installer
- Anaconda_, Command Line Installer
- Anaconda_, Graphical Installer

.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _Anaconda: https://www.anaconda.com/products/individual

.. warning::
    Python 3.X version of the installer **must** be chosen.
    Python 2 has reached its End Of Life (EOL) and therefore we do not support
    it and do not plan to.

The following table summarises the differences between available installers. We
recommend you to choose what you feel most comfortable with.

+--------------------------+----------------+---------------+---------------+
| Component/Feature        | Miniconda, CLI | Anaconda, CLI | Anaconda, GUI |
+--------------------------+----------------+---------------+---------------+
| Conda Package Manager    |        ✔       |       ✔       |       ✔       |
+--------------------------+----------------+---------------+---------------+
| Bundled Packages [info_] |        ✗       |       ✔       |       ✔       |
+--------------------------+----------------+---------------+---------------+
| Graphical User Interface |        ✗       |       ✗       |       ✔       |
+--------------------------+----------------+---------------+---------------+

.. _info: https://docs.anaconda.com/anaconda/packages/pkg-docs/

Integrating with CMake
######################

There are two points of interaction between CMake and Conda.

******************
