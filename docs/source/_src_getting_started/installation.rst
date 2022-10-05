
.. _getting_started_tudatpy:

******************************
Installation
******************************

.. contents:: Content of this page
   :local:

This page will guide you through the installation of Tudat(Py). The installation is supported exclusively through the use of a ``conda``
package manager, such as ``miniconda`` or ``Anaconda``. Alternative installation procedures are not currently
supported, although support for alternatives may be added in the future. If the current procedure is not suitable for your
application, then please make a feature request under the respective package at https://github.com/tudat-team or show
support for an existing request.

For more details on how to use ``conda``, please refer to our detailed guide (:ref:`getting_started_with_conda`) and the references therein.

.. note::

    `Miniconda`_ or `Anaconda`_: when refering to a ``conda`` package manager, "Anaconda" will be used regardless of whether you are using the ``Miniconda`` or ``Anaconda`` interface to ``conda``. See also `Anaconda or Miniconda?`_.

.. _`Miniconda`: https://docs.conda.io/en/latest/miniconda.html
.. _`Anaconda`: https://docs.anaconda.com/anaconda/navigator/#anaconda-navigator
.. _`Anaconda or Miniconda?`: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda

Installing Anaconda
###################

To install Anaconda on your system, see the `Installation`_ guide provided in the Anaconda documentation.

.. _`Installation`: https://docs.anaconda.com/anaconda/install/


Installing Tudat(Py)
####################

.. attention::

  As of TudatPy version 0.7, a number of modifications have been made to how TudatPy deals with vehicle orientations,
  in particular in the context of thrust and aerodynamic guidance. These changes are, in part, not backwards compatible.
  See :ref:`this page <backwards_incompatibility>` for more details. To continue to use the last older version of Tudat, install
  version 0.6.3.

To install Tudat(Py), we recommend the use of a terminal (command line) interface. On Unix system (Linux and Mac), ``conda`` should already be available within the terminal; you can open your terminal directly. On Windows, you can find a program called ``Anaconda Prompt`` in the Windows search. Using ``conda`` in the ``Anaconda Prompt`` is equivalent to the terminal use of ``conda`` on Unix. Some Unix commands are made available in this prompt, although most usage is equivalent to the Windows shell (see below for some useful terminal commands).

Open a terminal. Then first verify that ``conda`` is installed by executing the following command:

.. code-block::

    conda --version

Next ensure that ``conda`` is up-to-date.

.. code:: bash

    conda update conda

Download this ``environment.yaml`` (:download:`yaml <_static/environment.yaml>`) or use ``curl`` or ``wget`` to do this for you; download it to the current directory:

.. code:: bash

    wget https://tudat-space.readthedocs.io/en/latest/_downloads/dfbbca18599275c2afb33b6393e89994/environment.yaml

In your terminal, navigate to the directory containing this file and execute the following command (see below for tips on using the command line):

.. code:: bash

    conda env create -f environment.yaml

With the ``conda`` environment now installed, you can activate it to work in it using:

.. code:: bash

        conda activate tudat-space

.. note::
    At this point, you may choose to install the **development version of TudatPy**, which is a conda package that is updated as soon as changes are merged to the development branch of the code on GitHub. 
    To do so, you can run the following command:

    .. code:: bash

        conda install -c tudat-team/label/dev tudatpy


Congratulations! You have now installed Tudat and TudatPy and are ready to start running your simulations and analyses! We recommend you get started by having a look at our :ref:`getting_started_examples`.

If there are any issues with the installation process, please submit an issue on the `tudatpy-feedstock`_. If there are issues running examples, please submit an issue on the `tudatpy`_ repository.


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


Updating Tudat(Py)
##################

To update an existing installation of ``tudatpy``, activate your ``tudat-space`` environment:

    .. code:: bash

        conda activate tudat-space

Then execute the following command to install the latest version of ``tudatpy``:

    .. code:: bash

        conda install -c tudat-team tudatpy

Note that using this command may also update additional packages (such as ``tudat``) that are needed to run the latest version of ``tudatpy``.


.. warning::

    It can happen that running the install command above does not update ``tudatpy`` to the latest version (which can be checked on the `Anaconda website <https://anaconda.org/tudat-team/tudatpy>`_). In that case it is recommended to execute the following command (while still in the ``tudat-space`` environment):

       .. code:: bash

           conda install --update-deps -c tudat-team tudatpy
