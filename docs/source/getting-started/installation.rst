.. meta::
    :description lang=en:
        Installation instructions for the open-source TU Delft Astrodynamics toolbox (Tudat), disseminated as a conda package that provides a Python interface wrapping C++ functionality.

.. _getting_started_installation:

******************************
Installation
******************************

.. contents:: Content of this page
   :local:

This page will guide you through the installation of Tudat(Py). The installation is supported exclusively through the use of a ``conda``
package manager, such as Miniconda or Anaconda.

.. attention::

    **Windows users** must install Anaconda; for new users in general we recommend Anaconda

To install Anaconda or Miniconda on your system, see the `Anaconda Installation`_  of `Miniconda Installation`_ guide provided in their documentation.

.. _`Anaconda Installation`: https://docs.anaconda.com/anaconda/install/
.. _`Miniconda Installation`: https://docs.conda.io/en/latest/miniconda.html

For more details on how to use ``conda``, please refer to our detailed guide (:ref:`getting_started_with_conda`) and the references therein.

.. _`Miniconda`: https://docs.conda.io/en/latest/miniconda.html
.. _`Anaconda`: https://docs.anaconda.com/navigator
.. _`Anaconda or Miniconda?`: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda

Installing Tudat(Py)
####################

To install Tudat(Py), we recommend the use of a terminal (command line) interface. On Unix system (Linux and Mac), ``conda`` should already be available within the terminal; you can open your terminal directly.  On Windows, you can find a program called ``Anaconda Prompt`` in the Windows search. Using ``conda`` in the ``Anaconda Prompt`` is equivalent to the terminal use of ``conda`` in a Unix terminal.

Open a terminal. Then first verify that ``conda`` is installed by executing the following command:

.. code-block:: bash

    conda --version

Next ensure that ``conda`` is up-to-date.

.. code-block:: bash

    conda update conda

Download this ``environment.yaml`` (:download:`yaml <_static/environment.yaml>`). Then, in your terminal navigate to the directory containing this file and execute the following command (see below for tips on using the command line):

.. code-block:: bash

    conda env create -f environment.yaml

With the ``conda`` environment now installed, you can activate it to work in it using:

.. code-block:: bash

    conda activate tudat-space

.. note::
    At this point, you may choose to install the **development version of TudatPy**, which is a conda package that is updated as soon as changes are merged to the development branch of the code on GitHub. 
    To do so, you can download the ``environment-dev.yaml`` (:download:`yaml <_static/environment-dev.yaml>`), and use:

    .. code-block:: bash

        conda env create -f environment-dev.yaml
        conda activate tudat-space-dev

    to install and activate the ``tudat-space-dev`` environment.


For more help on getting started with the command-line interface (CLI), you could start with a `tutorial`_.

.. _`tutorial`: https://blog.balthazar-rouberol.com/discovering-the-terminal

Congratulations! You have now installed tudatpy and are ready to start running your simulations and analyses! We recommend you get started by having a look at our :ref:`getting_started_examples`.

If there are any issues with the installation, the examples, or if you have any question or comments on Tudat, please use our `Github discussion forum <https://github.com/orgs/tudat-team/discussions>`_.

.. _`tudatpy-feedstock`: https://github.com/tudat-team/tudatpy-feedstock
.. _`tudatpy`: https://github.com/tudat-team/tudatpy

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
           
Building your own TudatPy kernel
################################

If you would prefer to not use a conda package, but instead build your own tudatpy kernel from the source code, clone the ``tudatpy`` repository from `here <https://github.com/tudat-team/tudatpy>`_ and follow the instructions in the README. To build the latest version of the kernel, switch the tudatpy repository to the ``develop`` branch in step 3 of the README.

.. note::

    This workflow is not recommended for new users.










