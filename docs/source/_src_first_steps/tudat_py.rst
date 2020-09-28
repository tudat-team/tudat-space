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

2. Add the ``tudat-team`` channel to your conda channel list.

.. code:: bash

    conda config --append channels tudat-team

3. Install the desired package for developing in Python (``tudatpy``) or C++ (``tudat``). The installation of ``tudatpy``
will automatically include ``tudat`` as a dependency.

.. code:: bash

    conda install tudatpy

.. code:: bash

    conda install tudat

.. warning::

    **[macOS users]** There is currently an issue with the package metadata defined for the ``tudatpy-feedstock``.
    You will require definition of the channels as follows to install successfully:

    .. code:: bash

        conda install tudatpy -c tudat-team -c conda-forge -c defaults

    If this was not required, or did not work, please inform us `on tudatpy-feedstock (#2)`_

.. _`on tudatpy-feedstock (#2)`: https://github.com/tudat-team/tudatpy-feedstock/issues/2

.. note::

    If there are any issues regarding the installation process on the side of ``conda``, please submit an issue
    on the respective package's feedstock (suffixed with ``feedstock``).
    If there are issues running tutorials in the form of import errors, failing tests, or symbol errors, please
    submit an issue on the package repository itself. This can be done at https://github.com/tudat-team.

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



