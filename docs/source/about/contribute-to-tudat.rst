.. _contribute_to_tudat:

===================
Contribute to Tudat
===================

Any contribution you have to Tudat is very welcome! This can come in the form of code contributions in C++ or Python, additions to our website, extensions to the API documentation, the writing of example applications, *etc.* Also, any general advice, ideas, comments, feature request are most welcome! You can use any of the following to work on Tudat and/or reach out:

* Send an `e-mail <https://www.tudelft.nl/staff/d.dirkx/>`_ to get in touch. We're always open and eager to discuss contributions to and use of Tudat!
* Post an issue on one of our Github repositories:
  
  * `Tudatpy code (C++ and Python) <https://github.com/tudat-team/tudatpy>`_ where our functionality is implemented, and the C++ functionality is exposed to Python using `pybind11 <https://pybind11.readthedocs.io/en/stable/index.html>`_
  * `Tudatpy examples code (Python/Jupyter) <https://github.com/tudat-team/tudatpy-examples>`_ where the :ref:`getting_started_examples` of our project are located
  * `Tudat space (sphinx) <https://github.com/tudat-team/tudat-space>`_ where the markup language that generates this website is located

* Part of our development workflow is documented on our `developer docs <https://github.com/tudat-team/tudatpy/wiki>`_.

Ongoing and planned developments
================================

Below is a (not entirely comprehensive) list of features and functionalities that are under active development, or or our near(ish)-term wishlist. For some of them, the required development would be Python-only. If you're interested in the status of these points, in contributing, or in proposing additional ones, please feel free to contact us!

* Extension of Tudat estimation functionality for real tracking data analysis, with a focus on planetary missions

  * Reading additional typical radio tracking data files (TDF) into Tudat-compatible data structures (in addition to ODF, TNF, IFMS files, which are currently supported)
  * Adding albedo and surface temperature models for specific solar system bodies
  * Flexible and automated setup for high-fidelity propagation and estimation of planetary spacecraft
  * ...

* Adding better functionality to automate the plotting of numerical propagation results (**Python**)
* Linking the preliminary mission design module to the numerical propagation, including automated differential corrections
* Supporting events during the propagation (i.e. modify models when a specific condition is met)
* Implementing regularized propagators (e.g. Dromo)
* Extend CR3BP propagation and mission design functionality (including differential correction to account for perturbations)
* Rigorous relativistic effects for orbit propagation (e.g. acceleration derived from metric tensor)
* ...

We're also always looking for new example applications, and good ideas for example applications, please feel free to share any ideas and code you may have!

.. _contributors:

Contributor list
================

Below, there is a list of contributors to Tudat. Mostly, these have been staff and students of TU Delft who have worked on Tudat as part of their research project(s) and/or as TAs. Many of them have put a lot of their free time and research time into making Tudat what it is. If you think your name is missing here, please let us know! 

**Currently and recently active contributors**

* Riva Alkahal
* Kevin Cowan
* `Dominic Dirkx <https://www.linkedin.com/in/dominic-dirkx-2806a5b6>`_
* Sam Fayolle
* Valerio Filice
* Jonas Hener
* Lars Hinüber
* Luigi Gisolfi
* Nicolò Maistri
* Andrea Minervino Amodio
* Michael Plumaris
* Markus Reichel
* Alfonso Sanchez Rodriguez

**Tudat Alumni Hall-of-fame**

* `Kartik Kumar <https://www.linkedin.com/in/kumarkartik/>`_ - For starting it all, developing numerous core features, and leading the project through the crucial first few years with huge passion and commitment
* `Jacco Geul <https://jacco.geul.net/>`_ - For supporting Tudat for the duration of his Ph.D. project, resolving more bugs and answering more questions than we can count and professionalizing the setup of the project
* `Jeroen Melman <https://www.linkedin.com/in/jeroen-melman-9533148>`_ - For helping to build up the Tudat project in its very first years with code development and project setup, without which it may never have survived 
* Miguel Avillez - For developing the current loading and processing functionality allowing Tudat to handle real radio tracking data
* `Geoffrey Garrett <https://www.linkedin.com/in/ghgarrett/>`_ - For setting up the Python interface of Tudat, the building of the conda packages, and making an important step in professionalizing the project

**Past Contributors**

* `Giacomo Aciarini <https://www.linkedin.com/in/giacomo-acciarini-470712151/>`_
* `Evianne Brandon <https://www.linkedin.com/in/eviannebrandon/>`_
* Sean Cowan
* Fabien Dahmani
* Tristan Dijkstra
* `Frank Engelen <https://www.linkedin.com/in/frankengelen/>`_
* `Michele Facchinelli <https://www.linkedin.com/in/mfacchinelli/>`_
* `Iosto Fodde <https://www.linkedin.com/in/iosto-fodde-572b81129/>`_
* Carlos Fortuny Lombrana
* Jeremie Gaffarel
* `Jacco Geul <https://jacco.geul.net/>`_
* `David Gondelach <https://www.linkedin.com/in/david-gondelach/>`_
* `Alejandro Gonzalez Puerta <https://www.linkedin.com/in/alejandrogonzalezpuerta/>`_
* `Linda van der Ham <https://www.linkedin.com/in/linda-van-der-ham-1606594a/>`_
* Jonas Hener
* `Frank Hogervorst <https://www.linkedin.com/in/frankhogervorst/>`_
* `René Hoogendoorn <https://www.linkedin.com/in/rene-hoogendoorn-107/>`_
* `Elisabetta Iorfida <https://www.linkedin.com/in/elisabettaiorfida>`_
* `Kartik Kumar <https://www.linkedin.com/in/kumarkartik/>`_
* `Jonatan Leloux <https://www.linkedin.com/in/jonatanleloux/>`_
* Antonio Lopez Rivera
* `Francesco Lupi <https://www.linkedin.com/in/francesco-lupi-b23a658/>`_
* Gregorio Marchesini
* Jorge Martinez
* Maarten van Nistelrooij
* Filippo Oggionni
* `Aleix Pinardell <https://www.linkedin.com/in/aleixpinardell/>`_
* `Bart Römgens <https://www.linkedin.com/in/bart-r%C3%B6mgens-b7a19314/>`_
* `Tineke Roegiers <https://www.linkedin.com/in/roegiers/>`_
* `Alexander Ronse <https://www.linkedin.com/in/alexander-ronse-1401a5b/>`_
* `Dominik Stiller <https://www.linkedin.com/in/dominikstiller/>`_
* `Mattia Topini <https://www.linkedin.com/in/mattia-topini-796448175/>`_
* Simon Van Hulle
* Rens van der Zwaard

..
   * Elmar Puts
   * Bryan Tong Minh
   * Sebastian Villamil
