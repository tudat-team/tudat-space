.. _getting_started_with_wsl:

********************************************
Setting Up Windows Subsystem for Linux (WSL)
********************************************

.. contents:: Table of Contents
   :local:
   :depth: 2

If you would like to use Linux on a Windows machine, you can set up the Windows Subsystem for Linux (WSL).
This allows you to run a Linux distribution in parallel to your regular Windows environment.
Compared to a dual-boot setup or virtual machine, WSL is more lightweight and integrates well with a number of IDEs.
It is primarily based on the command-line, although you can also run graphical applications.

In the context of Tudat(Py), having a Linux environment is recommended for the development and testing of new features in the Tudat and Tudat(Py) libraries.


Installing WSL
##############

- Follow the installation guide on the `Microsoft website <https://learn.microsoft.com/en-us/windows/wsl/install>`_ to install WSL.
- By default, this will install Ubuntu as a Linux distribution. This is a common choice and recommended for beginners as you will find plenty of support, but you can also `install other distributions <https://learn.microsoft.com/en-us/windows/wsl/install#change-the-default-linux-distribution-installed>`_.

Setting up WSL
##############
In the following steps, we will assume that you have installed Ubuntu as your Linux distribution.
Other distributions may have slightly different steps.

- After installing WSL, open Ubuntu from the start menu and `follow the instructions <https://learn.microsoft.com/en-us/windows/wsl/setup/environment>`_ to set up your Linux distribution.
- You can now run Linux commands in the terminal. For example, you can check the installed Ubuntu version by typing

.. code-block:: bash

    lsb_release -a

This should return something like the following::

    No LSB modules are available.
    Distributor ID: Ubuntu
    Description:    Ubuntu 20.04.2 LTS
    Release:        20.04
    Codename:       focal

.. tip::
    If this is your first time using a Linux environment, take a look at the `Linux and Bash tutorial <https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux#working-with-files-and-directories>`_ in the WSL documentation or the `Linux command line basics tutorial <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>`_ for a more extensive background.

    In short, some basic commands you might need to know are:

    - ``ls`` to **l**\i\ **s**\t files in a directory,
    - ``cd my_directory/`` to **c**\hange **d**\irectories to the directory called ``my_directory``, use ``cd ..`` to go up one directory,
    - ``mkdir new_directory`` to create (**m**\a\ **k**\e) a new **dir**\ectory called ``new_directory``,
    - ``rm old_file.txt`` to **r**\e\ **m**\ove the file called ``old_file.txt``,
    - ``cat environment.yaml`` to display the contents of the file ``environment.yaml``,
    - ``sudo`` to run a command as an administrator,
    - ``apt-get`` to install packages.
    
    .. - ``cp`` to **c**\o\ **p**\y files,
    .. - ``mv`` to **m**\o\ **v**\e files,


- Update your package list and upgrade your packages by running the following commands:

  .. code-block:: bash

      sudo apt-get update && sudo apt-get upgrade

Using WSL with Windows
######################

- To access your Windows files from the Linux environment, you can navigate to ``/mnt/c/`` in the terminal. This is where your Windows files are mounted.
- To access the Linux files from Windows, you can navigate to ``\\wsl$\`` in the file explorer.
- You can also access the Linux environment from the Windows terminal by running ``wsl``.
- To access the Linux environment from the Windows file explorer, you can run ``explorer.exe .`` in the Linux terminal.

.. tip::
    While it is possible to access files stored in the Windows environment from within WSL (and vice-versa), it is not recommended! Instead, store your files in the environment you are planning to use them in.

    In any case, make sure you have backups of your files in case something goes wrong! If something goes wrong, it will be in the worst moment possible. Don't ask how we know 🤐

Preparing WSL to use Tudat(Py)
#################################
In principle, you are now ready to use WSL with Tudat(Py).
However, you might want to install some additional packages to make your life easier.

Install Conda
================
Tudat(Py) uses Conda to manage its dependencies.
If you have used Conda before in your Windows environment, you will still have to install it in your WSL environment.
As we will mainly use the command-line in WSL, Miniconda is recommended.
Follow the `installation instructions <https://docs.anaconda.com/miniconda/#quick-command-line-install>`_ and make sure conda is installed in your WSL environment:

.. code-block:: bash

    conda --version

This should return the installed Conda version.
From there on, you can follow the instructions in the :ref:`Conda primer <getting_started_with_conda>` to set up your Conda environment and :ref:`install Tudat(Py) <getting_started_installation>`.

Setting up an IDE
=================
As mentioned before, WSL is primarily based on the command-line.
While you can run graphical applications, it is not recommended to run a full-fledged IDE in WSL.
Instead, you can use an IDE on your Windows machine and connect it to the WSL environment.
If you have a preference for a specific IDE, have a look if it supports WSL.

In the following, two options will be presented: PyCharm and Visual Studio Code.

Setting up PyCharm
------------------

.. warning::
    At the time of writing, only the PyCharm Professional version but not the Community version supports WSL natively. As a student you can get a free license for the Professional version. If you do not have access to the Professional version, Visual Studio Code is a good alternative.

Setting up Visual Studio Code
-----------------------------

Setting up Git
==============