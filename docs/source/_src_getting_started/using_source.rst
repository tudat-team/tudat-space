===========================
Using the Tudat source code
===========================

For normal/simple applicationss, a user will not need to view or interact directly with the underlying C++ source code, but will only use the conda package that has the Python exposure of the C++ code. But, for various reasons, it can be very advantageous to view, search or modify the source code, to for instance:

* Understand where/why an exception is thrown during a simulatioin
* Understand how exactly a model is implemented
* Find functionality that is not (yet) exposed to Python, but which does exist
* Find clarification for incomplete/incorrect documentation
* Extend the underlying C++ functionality
* Have fun with C++ :) 

.. note::
   You can read and navigate through the code in your IDE without having to compile! The advantage of using an IDE is then that there are a whole bunch of built-in code analysis features that allow you to easily find where a function is defined, where it is used, etc., which is very helpful when understanding how a codebase is set up.

If you only want to view and navigate through the source code, but not compile it, you only need to go through the README up to step 4. We've created a video (TODO VIDEO) to showcase how to use an IDE (in this case CLion) to navigate through the code, starting from the Python exposure of a Tudatpy function that you would normally use.

The Tudat sources code is hosted on Github, in a number of repositories, which can be found here: `https://github.com/tudat-team/ <https://github.com/tudat-team/>`_. To build both tudat and tudatpy, while installing all dependencies for the installation with a single conda environment, we have created the 'tudat-bundle' repository: `https://github.com/tudat-team/tudat-bundle <https://github.com/tudat-team/tudat-bundle>`_. The README of this repository walks you through the steps of downloading and (if you want!) compiling tudat. The tudat-bundle includes two repositories:

  * The tudat repository, which contains the code for the functionality in C++, and the (~250) unit tests: `https://github.com/tudat-team/tudat <https://github.com/tudat-team/tudat>`_
  * The tudatpy repository, which contains the code for creating the Python exposures from the C++ code, and a number of small tests: `https://github.com/tudat-team/tudatpy <https://github.com/tudat-team/tudatpy>`_
  
To assist new users/developers in understanding the link between the Python code and the C++ code, we have taken a number of the example applications, and have translated them into C++, as an example of how the interfaces in the two languages compare to one another (TODO EXAMPLES).




