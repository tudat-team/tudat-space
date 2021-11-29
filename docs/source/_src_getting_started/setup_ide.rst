####################################
Setting Up a Development Environment
####################################


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

Getting started with Jupyter Notebooks
---------------------------------------

Your default browser will now open a localhost page in your current directory, as given in the following figure:

.. figure:: _static/jupyterlab_launch.png

Search and open your notebook. Once opened, you should see, for example, the following screen (Numerical Astrodynamics Assignment 1)

.. figure:: _static/jupyterlab_notebook.png

The notebook consists of blocks. There are three types of blocks, two of which are important for us: Markdown and Code. Markdown blocks contain mostly text, while Code blocks contain and run python code.

Setting up PyCharm
------------------

PyCharm is a famous Integrated Development Environment (IDE) to work with Python, widely used by developers and
professionals. It is available for download `here`_. The open-source, basic version ("Community") is free to download
and sufficient to write and run Python code; however, if you have a TU Delft account (or another educational email),
you can download and activate the professional version as well. To activate your educational license, please visit this
`webpage`_.

.. _`here`: https://www.jetbrains.com/pycharm/download
.. _`webpage`: https://www.jetbrains.com/shop/eform/students

To start working with PyCharm, you can create a new project. It is possible to set the conda environment to be used
directly from PyCharm. You can follow this procedure to create a new project and use your conda installation of Tudat:

1. Go to ``File`` > ``New project...``

2. From the tab ``PurePython``, select the location of your project (i.e. provide the path to the directory of interest, named ``yourProjectFolderPath`` in the figure below).

.. figure:: _static/pycharm_new_project.png

3. Select ``Existing interpreter`` and click on the three dots to the right to provide the path to the interpreter.

4. Select ``Conda Environment`` on the left bar.

5. Select ``Existing Environment`` and tell Pycharm where the environment ``python(.exe)`` is.

.. note::

    The location of the python interpreter in your active conda environment is the output of the ``which python`` command.

.. figure:: _static/pycharm_set_environment.png

The project interpreter can be viewed and/or modified at any time, even after the project is created, by
navigating to ``File`` > ``Settings`` > ``Project`` > ``Python Interpreter`` (Windows/Linux) or ``PyCharm`` >
``Preferences`` > ``Project`` > ``Python Interpreter`` (macOS). The figure below shows the interpreter panel on
Windows.

.. figure:: _static/pycharm_interpreter.png

After a project is created, it can happen that the *run* button is disabled. This issue can be caused by two reasons:

*   PyCharm is parsing and indexing the source files. This can take a few minutes, depending on the size of the project;
    the processes run in the background by PyCharm can be viewed and monitored from the bar at the bottom of the screen.

*   A *run configuration* is missing. This can be added manually by clicking on ``Add configuration`` next to the *run*
    button in the bar at the top of the editor (not explained here), but it is also possible to let PyCharm set up a
    predefined run configuration by right-clicking on a script and select ``Run`` from the context menu. This is the
    recommended procedure, if the user does not have specific requirements on the run configuration.

If you are working with multiple source files (e.g. your code is split into multiple modules), the best practice is to
let PyCharm know about this, so it will retrieve all the dependencies present in your modules. Otherwise, the IDE will
parse the source code and complain about potential errors, especially while importing other modules: even if the code
runs fine, PyCharm does not know where to look for them. This can be done as follows:

1. Navigate to ``File`` > ``Settings`` > ``Project`` > ``Project Structure``.

2. Select the directory containing your source code and mark it as ``Sources`` (blue folder).

.. note::

    The students of AE4866 Propagation and Optimization in Astrodynamics are encouraged to follow all the steps
    presented above.

