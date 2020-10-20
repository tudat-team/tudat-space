******************************
Getting Started with Tudat(Py)
******************************

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


Choosing a Development Environment
##################################

.. note::

    Your choice of development environment will differ greatly depending on your intended development purpose

    **PyCharm**

    * Brilliant for developing pure Python code.
    * Extensive number of plugins to improve experience.
    * For debugging **Python** code, it is superior.
    * Execution will go through an entire script, unless debug mode is used. Not always desirable with data-science and numerical analysis.

    **CLion**

    * Close to on-par with PyCharm, although PyCharm is still superior for pure Python projects.
    * If your workflow involves C++, even if just to browse source code, then CLion would be superior unless you decide to use both PyCharm and CLion.
    *

    **JupyterLab**
    *


Setting up JupyterLab (Python)
------------------------------

Setting up PyCharm (Python with some optional C++)
--------------------------------------------------

Setting up CLion (C++ with some optional Python)
------------------------------------------------


