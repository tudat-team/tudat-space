
.. _getting_started_tudatpy:

******************************
Getting Started with Tudat(Py)
******************************

This page will guide you through the installation of Tudat(Py). The installation is supported exclusively through the use of the ``conda``
package manager, such as ``Anaconda``. Additional installation procedures are not currently
supported by the team, although there are plans to add additional support in the future. If the current situation does not satisfy your
application then please make a feature request at the respective package at https://github.com/tudat-team or show
support for an existing request.




Installing Anaconda
###################

Install Anaconda on your system, see the `Installation`_ guide provided by the Anaconda documentation.

.. _`Installation`: https://docs.anaconda.com/anaconda/install/

.. note::

    **macOS users are advised to use `homebrew`_**: this is an excellent packet manager, with the added advantage of making it exceedingly easy to install Anaconda:

    .. code:: bash

        brew install anaconda

    ... or `Miniconda`_, a lighter alternative to Anaconda:

    .. code:: bash

        brew install miniconda

.. _`homebrew`: https://brew.sh
.. _`Miniconda`: https://docs.conda.io/en/latest/miniconda.html


Installing Tudat(Py)
####################

To install Tudat(Py), we recommend the use of a terminal (command line) interface. On Unix system (Linux and Mac), ``conda`` should be integrated with the terminal, and you can open your terminal directly. On Windows, you can find a program called ``Anaconda Prompt`` in the Windows search. The ``Anaconda Prompt`` is equivalent to the terminal use of ``conda`` on Unix. Some Unix commands are made available in this prompt, although most usage is equivalent to the Windows shell (see below for some useful terminal commands).

Open a terminal. Then, first verify that Conda is Installed via using the following command:

.. code-block::

    conda --version

Then, ensure that ``conda`` is updated.

.. code:: bash

    conda update conda

Download this ``environment.yaml`` (:download:`yaml <_static/environment.yaml>`), or use wget to this for you (downloading it to the current directory):

.. code:: bash

    wget https://tudat-space.readthedocs.io/en/latest/_downloads/2ff196b0ef4830f53d754f6a3972d2e8/environment.yaml

In your terminal navigate to the directory containing this file, and use the following command (see below for tips on using the command line):

.. code:: bash

    conda env create -f environment.yaml

Congratulations! You have now installed Tudat and TudatPy, and are ready to get started running your simulations and analyses!

.. note::

    **New to the command-line?** The following commands may be useful to you:

    +-------------------------------------------------------+--------------------------+-----------------------+
    | **Command effect**                                    | **Unix (Linux & macOS)** | **Windows**           |
    +-------------------------------------------------------+--------------------------+-----------------------+
    | Enter a directory using a path (relative or absolute) | ``cd <abs/rel path>``    | ``cd <abs/rel path>`` |
    +-------------------------------------------------------+--------------------------+-----------------------+
    | Step back to the previous directory                   | ``cd ..``                | ``cd ..``             |
    +-------------------------------------------------------+--------------------------+-----------------------+
    | List the contents of the current working directory    | ``ls``                   | ``dir``               |
    +-------------------------------------------------------+--------------------------+-----------------------+

.. warning::

    **Are you a macOS user**? You may encounter an issue while installing tudatpy via conda.
    If you have issues installing via the ``environment.yaml`` in the form of conflicts when installing, please inform us `on tudatpy-feedstock (#2)`_.

    If this is the case, then you can attempt to install tudatpy with this alternative procedure:

    1. Create a new environment.

    .. code:: bash

        conda create --name tudat-space

    In case you need to specify the python version to be used with TudatPy (which is irrespective and independent of the python version you may have installed in your system), you can do this with:

    .. code:: bash

        conda create --name tudat-space python=3.8

    Be aware that the tudat-space environment has a certain number of pre-defined python versions that it can work with; you can check which ones in the `conda_build_config.yaml`_ file.

    2. Activate the environment.

    .. code:: bash

        conda activate tudat-space

    3. Install tudatpy & matplotlib with a manual definition of channels.

    .. code:: bash

        conda install tudatpy matplotlib -c tudat-team -c conda-forge -c defaults

    If conda complains there is no tudat-team channel, just add it:

    .. code:: bash

        conda config --add channels tudat-team

    then re-run the command in item 3.

    If this alternative fix did not work, please inform us `on tudatpy-feedstock (#2)`_.

    You can also try the macOS install (:download:`install-osx.sh <_static/install-osx.sh>`) and uninstall (:download:`uninstall-osx.sh <_static/uninstall-osx.sh>`) scripts.

.. _`on tudatpy-feedstock (#2)`: https://github.com/tudat-team/tudatpy-feedstock/issues/2
.. _`tudatpy-feedstock`: https://github.com/tudat-team/tudatpy-feedstock
.. _`tudatpy`: https://github.com/tudat-team/tudatpy
.. _`conda_build_config.yaml`: https://github.com/tudat-team/tudatpy-feedstock/blob/master/recipe/conda_build_config.yaml

.. note::

    - If there are any other issues with the installation process, please submit an issue
    on the `tudatpy-feedstock`_.
    - If there are issues running tutorials please submit an issue on the `tudatpy`_ repository.