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

In the context of Tudat(Py), having a Linux environment is required as of v0.9, as no more Windows conda packages are provided.


Installing WSL
##############

.. important::
    Before you start, make sure that the Windows Subsystem for Linux (WSL) feature is enabled on your Windows machine.
    
    To check this, open the Control Panel -> Programs -> Programs and Features -> "Turn Windows features on or off" and make sure that the Windows Subsystem for Linux feature is enabled.

- Follow the installation guide on the `Microsoft website <https://learn.microsoft.com/en-us/windows/wsl/install>`_ to install WSL.
- By default, this will install Ubuntu as a Linux distribution. This is a common choice and recommended for beginners as you will find plenty of support, but you can also `install other distributions <https://learn.microsoft.com/en-us/windows/wsl/install#change-the-default-linux-distribution-installed>`_.

.. note::
    If you run into any issues during the installation, you can find help in the `WSL troubleshooting guide <https://learn.microsoft.com/en-us/windows/wsl/troubleshooting>`_.

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

- To access your Windows files from the Linux environment, you can navigate to ``/mnt/c/`` in the terminal. This is where your Windows files are mounted and accessible from inside Linux.
- To access the Linux files from Windows, you can navigate to ``\\wsl$\`` in the file explorer.
- You can also access the Linux environment from the Windows terminal by running ``wsl``.
- To access the Linux environment from the Windows file explorer, you can run ``explorer.exe .`` in the Linux terminal.

.. tip::
    While it is possible to access files stored in the Windows environment from within WSL (and vice-versa), it is not recommended! Instead, store your files in the environment you are planning to use them in.

    In any case, make sure you have backups of your files in case something goes wrong! If something goes wrong, it will be in the worst moment possible. Don't ask how we know 🤐

Preparing WSL to use Tudat(Py)
#################################
In principle, you are now ready to use WSL.
However, you might want to install some additional packages to make your life easier.

Install Conda
================
Tudat(Py) uses Conda to manage its dependencies.
If you have used Conda before in your Windows environment, you will still have to install it in your WSL environment.
As we will mainly use the command-line in WSL, Miniconda is recommended.
The instructions in the following are based on the `official Anaconda documentation <https://docs.anaconda.com/miniconda/install//>`_.

1. Open the terminal in WSL and download the latest Miniconda installer by running:

   .. code-block:: bash

       wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

2. Install Miniconda by running the following command in the same directory:

   .. code-block:: bash

       bash Miniconda3-latest-Linux-x86_64.sh

3. Read through the Terms of Service and accept them.

4. In the next step, it is recommended to install Miniconda in the default location.

5. In the final step, you can configure the initialization of conda.
   It is recommended to add conda to your PATH, but not activate the base environment automatically upon opening a new terminal, to avoid accidentally installing packages in the base environment.

   You can configure this by typing ``yes`` when prompted for the initialization option.
   Then, restart your terminal and run the following command:

   .. code-block:: bash

       conda config --set auto_activate_base false

   Next time you open a terminal, the ``base`` environment will not be activated.
   You can activate any environment by running ``conda activate <ENVIRONMENT_NAME>``.

6. Lastly, make sure that conda is installed correctly by running:

   .. code-block:: bash

       conda --version

   This should return the installed Conda version.

From there on, you can follow the instructions in the :ref:`Conda primer <getting_started_with_conda>` to set up your Conda environment and :ref:`install Tudat(Py) <getting_started_installation>`.

.. dropdown:: Quick TudatPy installation
    :color: secondary

    In case you want to install TudatPy quickly, you can run the following commands from inside your WSL environment:

    Download ``environment.yaml`` file inside your WSL environment:

    .. code-block:: bash

        wget https://raw.githubusercontent.com/tudat-team/tudat-space/refs/heads/develop/docs/source/_src_getting_started/_static/environment.yaml
    
    Create a new Conda environment from the ``environment.yaml`` file:

    .. code-block:: bash

        conda env create -f environment.yaml

    Activate the new Conda environment:

    .. code-block:: bash

        conda activate tudat-space

    For more information on the installation and issues you might encounter, see the :ref:`installation page <getting_started_installation>`.

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

In the following, it is assumed that you have installed PyCharm Professional and have a Conda environment set up in WSL.
See also the `PyCharm documentation <https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html>`_.

To connect PyCharm to your WSL environment and set it up for TudatPy, follow these steps:

1. Open PyCharm and create a new project inside WSL.

   .. figure:: _static/wsl_create_project.png

   Choose your WSL instance in the following dialog (Ubuntu by default).

2. If you haven't done so already, create a new project directory. Make sure that the project path starts with ``\\wsl$\``, indicating that your project is stored in the WSL environment.

   .. figure:: _static/wsl_select_project.png

   Click ``OK`` and ``Start IDE and Connect`` to open your project. This might take some time, as the JetBrains client is downloaded.

3. Finally, we can set up the Conda environment in PyCharm. Click on the Python version and add a new interpreter on WSL:
   
   .. figure:: _static/wsl_pycharm_interpreter.png

   After the introspection was successful, click next and select the Conda environment you want to use.
   For TudatPy, you should select the Conda environment you created in the WSL environment.

   .. figure:: _static/wsl_pycharm_conda.png

You are now ready to use PyCharm with your WSL environment.
Make sure to follow the last step to :ref:`setup Git <wsl_setup_git>` in the WSL environment.

Setting up Visual Studio Code
-----------------------------

Visual Studio Code (VS Code) is freely available and supports WSL using official extensions.

To connect VS Code to your WSL environment and set it up for TudatPy, follow these steps:

1. If you haven't done so already, install VS Code from the `official website <https://code.visualstudio.com/Download>`_.
2. Open VS Code and install the `Remote - WSL <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`_ extension by Microsoft. You can also search for the extension in the Extensions tab in VS Code.

   - Remote - WSL: Identifier ``ms-vscode-remote.remote-wsl``
  
   .. figure:: _static/wsl_vscode_install_extension.png

3. Open the command palette by pressing ``Ctrl+Shift+P`` and type ``WSL: Connect to WSL``.
   You should now see being connected to your WSL environment.

   .. figure:: _static/wsl_vscode_connected.png

   Alternatively, you can also navigate from the command line to your project directory and type ``code .``. This will open VS Code directly in the WSL environment. In this case, you can skip the next step.

4. Open your project folder in VS Code.
   
   .. figure:: _static/wsl_vscode_open_project.png

5. Install the `Python extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_ by Microsoft. You can also use the identifier ``ms-python.python`` in the Extensions tab.

6. Create a new Python file and select the Python interpreter. You should now see the Conda environment you set up in WSL.

   .. figure:: _static/wsl_vscode_python_file.png

   .. figure:: _static/wsl_vscode_conda_environment.png

You are now ready to use VS Code with your WSL environment.
Make sure to follow the last step to :ref:`setup Git <wsl_setup_git>` in the WSL environment.
For more information on how to use VS Code with WSL, see the `official documentation <https://code.visualstudio.com/docs/remote/wsl>`_.

.. _wsl_setup_git:

Setting up Git
==============

Lastly, you will likely want to use source control for your projects.
In order to use Git in WSL, you will have to install it inside your Linux environment, even if you have installed it previously in your Windows environment.
Follow the `setup instructions by Microsoft <https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git>`_, in particular the setup instructions of the `Git Credential Manager <https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git#git-credential-manager-setup>`_.

Next steps
##########

Congratulations!
You are now all set to use WSL with Tudat(Py).
If you would like to learn more about how to use the Tudat source code, which is written in C++, have a look at the :ref:`using_tudat_source` page.
You can also make use of your new environment to contribute to the Tudat project on GitHub, see :ref:`this page <contribute_to_tudat>` for more information.