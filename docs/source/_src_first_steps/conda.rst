  .. _getting_started_with_conda:

**************************
Getting Started with Conda
**************************

.. image:: _static/conda_logo.svg

This page outlines the fundamentals in using the `conda` package manager.

  Package, dependency and environment management for any language—Python, R,
  Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more.

.. tip::
    Conda has its own cheat sheet available for download
    :download:`pdf <_static/conda-cheatsheet.pdf>`

Choosing a Conda Flavour
########################

When using the conda package manager, you have two options to choose from:

- Miniconda_
- Anaconda_

.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _Anaconda: https://www.anaconda.com/products/individual

.. warning::
    Python 3.X version of the installer **must** be chosen.
    Python 2 has reached its End Of Life (EOL) and therefore we do not support
    it, and do not plan to.

The following table summarises the differences between available installers. We
recommend you to choose what you feel most comfortable with.

+--------------------------+----------------+---------------+
| Component/Feature        | Miniconda      | Anaconda      |
+--------------------------+----------------+---------------+
| Conda Package Manager    |        ✔       |       ✔       |
+--------------------------+----------------+---------------+
| Bundled Packages [info_] |        ✗       |       ✔       |
+--------------------------+----------------+---------------+
| Graphical User Interface |        ✗       |       ✔       |
+--------------------------+----------------+---------------+

.. note::
    The Graphical User Interface (Anaconda Navigator) can be installed
    separately in Miniconda.

.. _info: https://docs.anaconda.com/anaconda/packages/pkg-docs/
.. _Source: https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/

Managing Conda
##############

Managing Environments
#####################

Managing Packages
#################

Conda Configuration File
########################

A conda configuration file can be found
