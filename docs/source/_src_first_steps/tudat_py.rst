******************************
Getting Started with Tudat(Py)
******************************

Installation
############

The installation of packages from the ``tudat-space`` ecosystem is supported exclusively through the use of the ``conda``
package manager. This includes ``Miniconda`` and ``Anaconda``. Additional installation procedures are not currently
supported by the team, although there are plans to add additional support in the future. If this does not satisfy your
application then please make a feature request at the respective package at https://github.com/tudat-team or show
support for an existing request.

.. note::

    This procedure requires that Anaconda or Miniconda is installed. For
    information regarding the use of the conda ecosystem, please see :ref:`Getting Started with Conda`.

1. Ensure that ``conda`` is updated.

.. code:: bash

    conda update conda

2. Download and create an environment from this ``environment.yaml`` (:download:`pdf <_static/environment.yaml>`).
Ensure that the current working directory is set to the one containing the ``environment.yaml`` file.

.. code:: bash

    conda env create -f environment.yaml

.. note::

    **New to the command-line?** The following commands may be useful to you:

    +-------------------------------------------------------+-----------------------+-----------------------+-----------------------+
    | **Command effect**                                    | **Linux**             | **macOS**             | **Windows**           |
    +-------------------------------------------------------+-----------------------+-----------------------+-----------------------+
    | Enter a directory using a path (relative or absolute) | ``cd <abs/rel path>`` | ``cd <abs/rel path>`` | ``cd <abs/rel path>`` |
    +-------------------------------------------------------+-----------------------+-----------------------+-----------------------+
    | Step back to the previous directory                   | ``cd ..``             | ``cd ..``             | ``cd ..``             |
    +-------------------------------------------------------+-----------------------+-----------------------+-----------------------+
    | List the contents of the current working directory    | ``ls``                | ``ls``                | ``dir``               |
    +-------------------------------------------------------+-----------------------+-----------------------+-----------------------+

.. warning::

    **Are you a macOS user**? There is currently a known issue while installing tudatpy via conda.
    If you have issues installing via the ``environment.yml`` in the form of conflicts when installing, please inform us `on tudatpy-feedstock (#2)`_.

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

Choosing a Development Environment
##################################

.. note::

    Your choice of development environment will differ greatly depending on your intended development purpose. **For
    students of Numerical Astrodynamics**, PyCharm and Jupyter(Lab/Notebook) will be used in classes.

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

Setting up PyCharm to use Python from a Conda Environment
---------------------------------------------------------

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



