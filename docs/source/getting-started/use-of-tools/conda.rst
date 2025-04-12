.. _getting_started_with_conda:

**************************
Getting Started with Conda
**************************

.. image:: _static/conda_logo.svg

This page outlines the fundamentals in using the ``conda`` package manager.

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

.. note::
    **For students of Numerical Astrodynamics** it is recommended that you install Anaconda.

.. _info: https://docs.anaconda.com/anaconda/packages/pkg-docs/
.. _Source: https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/

Installation
############

Please see the `Installation`_ guide provided by the Anaconda documentation.

.. _`Installation`: https://docs.anaconda.com/anaconda/install/

Managing Conda
##############

Command-line & GUI use
----------------------

On Unix system (Linux and Mac), conda should be integrated with the terminal. On Windows, you can find
a program called ``Anaconda Navigator`` and ``Anaconda Prompt`` in the Windows search. The ``Anaconda Prompt`` is
equivalent to the terminal use of ``conda`` on Unix. Some Unix commands are made available in this prompt, although
most usage is equivalent to the Windows shell. On Unix you can start ``Anaconda Navigator`` with the following command:

.. code-block::

    anaconda-navigator    # base environment should be active

Verify Conda is Installed via ``Terminal/Anaconda Prompt``.

.. code-block::

    conda --version

Managing Environments
#####################

Create a new environment
------------------------

Generally Python 3.7 is preferred when using the ``tudat-space`` ecosystem.

.. code-block::

    conda create --name myenv python=3.7

Create an environment from an environment.yml file
__________________________________________________

An environment can be defined in an ``environment.yml`` file as:

.. code-block:: yaml

    name: tudat-space
    channels:
      - conda-forge
      - tudat-team
    dependencies:   # these are available on anaconda.org
      - tudatpy
      - matplotlib
      - pip         # pip can be added as a dependency!
      - pip:        # packages only available on PyPi can be added:
        - rtcat_sphinx_theme
        - sphinxcontrib-contentui

1. Create the environment from the ``environment.yml`` file in the current directory:

.. code-block:: bash

    conda env create -f environment.yml

2. Activate the environment (the name of the environment is defined on the first line of the ``environment.yml``):

.. code-block:: bash

    conda activate tudat-space

3. Verify the installation of the packages listed in ``environment.yml``.

.. code-block:: bash

    conda env list

Export an environment
---------------------

1. Your current active environment can be exported into the current directory as follows:

.. code-block::

    conda env export > environment.yml

Delete an environment
---------------------

.. warning::
    The following command is not reversible unless the environment has been exported beforehand.

1. Remove the environment and all its packages:

.. code-block:: bash

    conda remove --name myenv --all

2. Verify that the environment has been removed:

.. code-block:: bash

    conda env list

Managing Packages
#################

Installing a package
---------------------

1. Add the channel indexing the package (if required):

.. code-block:: bash

    conda config --append channels tudat-team

2. Install the package:

.. code-block:: bash

    conda install tudatpy

.. note::

    Alternatively, if you do not want to add a channel and potentially cause package conflicts, if available
    on multiple sources, you can isolate the channel for the package search as follows:

(1&2). Install a package from a specific channel:

.. code-block:: bash

    conda install tudatpy -c tudat-team
