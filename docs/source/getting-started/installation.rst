.. meta::
    :description lang=en:
        Installation instructions for the open-source TU Delft Astrodynamics toolbox (Tudat), disseminated as a conda package that provides a Python interface wrapping C++ functionality.

.. _getting_started_installation:

******************************
Installation
******************************

.. contents:: Content of this page
   :local:

This page will guide you through the installation of Tudat(Py).
At the moment the installation is supported exclusively through the use of a ``conda`` package manager, such as Miniconda or Anaconda.
To install Anaconda or Miniconda on your system, see the `Anaconda Installation`_  of `Miniconda Installation`_ guide provided in their documentation.
For more details on how to use ``conda``, please refer to our detailed guide (:ref:`getting_started_with_conda`) and the references therein.

.. _`Anaconda Installation`: https://docs.anaconda.com/anaconda/install/
.. _`Miniconda Installation`: https://docs.conda.io/en/latest/miniconda.html

.. note::

    **New to the command-line?** The following commands may be useful to you:

    +-------------------------------------------------------+--------------------------+-----------------------+
    | **Command effect**                                    | **Unix (Linux & macOS)** | **Windows**           |
    +-------------------------------------------------------+--------------------------+-----------------------+
    | Enter a directory using a path (relative or absolute) | ``cd <abs/rel path>``    | ``cd <abs/rel path>`` |
    +-------------------------------------------------------+--------------------------+-----------------------+
    | Go back to the parent directory                       | ``cd ..``                | ``cd ..``             |
    +-------------------------------------------------------+--------------------------+-----------------------+
    | List the contents of the current working directory    | ``ls``                   | ``dir``               |
    +-------------------------------------------------------+--------------------------+-----------------------+

    For more help on getting started with the command-line interface (CLI), you could start with a `tutorial`_.
           
.. _`tutorial`: https://blog.balthazar-rouberol.com/discovering-the-terminal


Installing Tudat(Py)
####################

To install Tudat(Py), we recommend the use of a terminal (command line) interface. On Unix system (Linux and Mac), ``conda`` should already be available within the terminal; you can open your terminal directly.  On Windows, you can find a program called ``Anaconda Prompt`` in the Windows search. Using ``conda`` in the ``Anaconda Prompt`` is equivalent to the terminal use of ``conda`` in a Unix terminal.

Open a terminal. Then first verify that ``conda`` is installed by executing the following command:

.. code-block:: bash

    conda --version

Next ensure that ``conda`` is up-to-date.

.. code-block:: bash

    conda update conda

Stable Version
--------------

If you are starting a new project, we recommend creating a new conda environment for TudatPy to avoid conflicts with other packages.
You can do this and install TudatPy in one step by downloading the :download:`environment.yaml <_static/environment.yaml>` file.
Then, in your terminal navigate to the directory containing this file and execute the following command (see above for tips on using the command line):

.. code-block:: bash

    conda env create -f environment.yaml

With the ``conda`` environment now installed, you can activate it using:

.. code-block:: bash

    conda activate tudat-space

Alternatively, if you already have a conda environment that you would like to use, you can install TudatPy in that environment using the following command:

.. code-block:: bash

    conda install -c tudat-team -c conda-forge tudatpy

Congratulations! You have now installed tudatpy and are ready to start running your simulations and analyses! We recommend you get started by having a look at our :ref:`getting_started_examples`.

If there are any issues with the installation, the examples, or if you have any question or comments on Tudat, please use our `Github discussion forum <https://github.com/orgs/tudat-team/discussions>`_.

Development Version
-------------------

You may choose to install the **development version of TudatPy**, which is a conda package that is typically build weekly from the ``develop`` branch of the https://github.com/tudat-team/tudatpy repository.
To do so, you can again download the :download:`environment-dev.yaml <_static/environment-dev.yaml>` file and create a new conda environment with the development version of TudatPy by using the following commands:

.. code-block:: bash

    conda env create -f environment-dev.yaml
    conda activate tudat-space-dev

This installs and activates the ``tudat-space-dev`` environment.

Alternatively, you can install the development version of TudatPy in an existing conda environment using the following command:

.. code-block:: bash

    conda install -c tudat-team/label/dev -c tudat-team -c conda-forge "tudatpy>1.0.0.dev"


Building your own TudatPy kernel
################################

.. note::

    This workflow is not recommended for new users.

If you would prefer to not use a pre-built conda package, but instead build your own tudatpy kernel from the source code, clone the ``tudatpy`` repository from https://github.com/tudat-team/tudatpy and follow the instructions in the README. To build the latest version of the kernel, ensure that you are on the ``develop`` branch in step 3 of the README.
