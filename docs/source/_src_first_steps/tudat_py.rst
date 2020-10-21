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

Installing Tudat(Py) 
####################

To install Tudat(Py), we recommend the use of a terminal (command line) interface. On Unix system (Linux and Mac), ``conda`` should be integrated with the terminal, and you can open your terminal directly. On Windows, you can find a program called ``Anaconda Prompt`` in the Windows search. The ``Anaconda Prompt`` is equivalent to the terminal use of ``conda`` on Unix. Some Unix commands are made available in this prompt, although most usage is equivalent to the Windows shell (see below for some useful terminal commands). 

Open a terminal. Then, first verify that Conda is Installed via using the following command:

.. code-block::

    conda --version

Then, ensure that ``conda`` is updated.

.. code:: bash

    conda update conda

Download this ``environment.yaml`` (:download:`yaml <_static/environment.yaml>`). In your terminal navigate to the directory containing this file, and use the following command (see below for tips on using the command line):

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

    **Are you a macOS user**? There is currently a known issue while installing tudatpy via conda.
    If you have issues installing via the ``environment.yaml`` in the form of conflicts when installing, please inform us `on tudatpy-feedstock (#2)`_.

    If this is the case, then you will need to follow this procedure:

    1. Create a new environment.

    .. code:: bash

        conda create --name tudat-space python=3.7

    2. Activate the environment.

    .. code:: bash

        conda activate tudat-space

    3. Install tudatpy & matplotlib with manual definition of channels.

    .. code:: bash

        conda install tudatpy matplotlib -c tudat-team -c conda-forge -c defaults

    Furthermore, if this fix did not work, please inform us `on tudatpy-feedstock (#2)`_.

.. _`on tudatpy-feedstock (#2)`: https://github.com/tudat-team/tudatpy-feedstock/issues/2
.. _`tudatpy-feedstock`: https://github.com/tudat-team/tudatpy-feedstock
.. _`tudatpy`: https://github.com/tudat-team/tudatpy

.. note::

    If there are any other issues with the installation process, please submit an issue
    on the `tudatpy-feedstock`_. If there are issues running tutorials please submit an issue on the `tudatpy`_ repository.

Setting Up a Development Environment
####################################

.. note::

    Your choice of development environment will differ greatly depending on your intended development purpose. **For
    students of Numerical Astrodynamics**, Jupyter(Lab/Notebook) will be used for assignments, and for examples during lectures. PyCharm may be used for examples during lectures.

Setting up JupyterLab in a Conda Environment
--------------------------------------------

1. Activate your desired conda environment to be used by JupyterLab:

.. code-block:: bash

    conda activate tudat-space

2. Install JupyterLab on the desired environment:

.. code-block:: bash

    conda install jupyterlab

3. Launch JupyterLab with its entry-point:

.. code-block:: bash

    jupyter-lab

OR

.. code-block:: bash

    jupyter lab

Setting up PyCharm to use a Conda Environment
---------------------------------------------

After installing PyCharm, use the following procedure to use your conda installation of Tudat:

1. Navigate to ``File`` > ``Settings`` > ``Project`` > ``Python Interpreter``

2. Drop down the menu for Python selection.

3. Click ``Show all``.

4. Click ``+`` to add an intepreter not listed.

5. Select ``Conda Environment`` on the left bar.

6. Select ``Existing Environment`` and tell Pycharm where the environment ``python(.exe)`` is.

.. note::

    On Unix, Anaconda and Miniconda are by default installed under ``~/Anaconda3/`` and ``~/Miniconda3`` respectively. This
    is also the ``$CONDA_PREFIX`` env variable in the terminal on Unix or ``%CONDA_PREFIX`` on Windows in the Anaconda
    prompt. The base environment Python interpreter is located as ``$CONDA_PREFIX/python`` (dev note: this must be verified on Unix)
    and ``%CONDA_PREFIX%/python.exe`` on Windows. The Python Interpreter of any contained environment can be found under a directory
    with their name as ``$CONDA_PREFIX/envs/<name>``.



