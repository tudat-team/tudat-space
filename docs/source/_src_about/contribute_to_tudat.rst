===================
Contribute to Tudat
===================

Any contribution you have to Tudat is very welcome! This can come in the form of code contributions in C++ or Python, additions to our website, extensions to the API documentation, the writing of example applications,  *etc.* Also, any general advice, ideas, comments, feature request are most welcome! You can use any of the following to work on Tudat and/or reach out:

* Post on `gitter chat <https://gitter.im/tudat-space/tudatpy>`_ with any question you may have
* Post an issue on one of our Github repositories:
  
  * `Tudat code (C++) <https://github.com/tudat-team/tudat>`_ in which our functionality is implemented
  * `Tudatpy code (C++) <https://github.com/tudat-team/tudatpy>`_ where the C++ functionality is exposed to Python using `pybind11 <https://pybind11.readthedocs.io/en/stable/index.html>`_
  * `Tudatpy examples code (Python/Jupyter) <https://github.com/tudat-team/tudatpy-examples>`_ where the :ref:`getting_started_examples` of our project are located
  * `Tudat space (sphinx) <https://github.com/tudat-team/tudat-space>`_ where the markup language that generates this website is located
  * `Tudat space (docstings) <https://github.com/tudat-team/tudat-multidocs>`_ where the entries of our `API documentation <https://py.api.tudat.space/en/latest/>`_ are located

* Join our Slack chat! This is where most of our coding discussion takes place. Send an `e-mail <https://www.tudelft.nl/staff/d.dirkx/>`_ to get an invite. 
* Part of our development workflow is documented on our `developer docs <https://tudat-developer.readthedocs.io/en/latest/>`_. This site is still under construction, and any input is more than welcome!

Ongoing and planned developments
================================

Below is a (non enirely comprehensive) list of features and functionalities that are under active development, or or our near(ish)-term wishlist. For some of them, the requied development would be ython-only. If you're interested in the status of these points, in contributing, or in proposing additional ones, please feel free to contact us!

* Extension of Tudat estimation functionality for real tracking data analysis, with a focus on planetary missions

  * Reading typical radio tracking data files (ODF, TNF, TDF) into Tudat-compatible data structures (**Python**?)
  * Linking JPL Horizons and Minor Planet Center databases to Tudat environment, to make setup of planetary mission scenarios easier, both will use the astroquery package (**Python**)
  * Adding models for media corrections for radio tracking (troposphere, ionosphere, corona)
  * Implement sparse matrices for partials matrices
  * ...

* Adding better functionality to automate the plotting of numerical propagation results, including easier access to specific dependent variables (**Python**)
* Linking SGP4 propagator to Tudat (**Python**?)
* Use a dedicated Time object to represent time (rather than just a double)
* Linking the preliminary mission design module to the numerical propagation, including automated differential corrections
* Supporting events during the propagation (i.e. modify models when a specific condition is met)
* Implementing regularized propagators (e.g. Dromo)
* Implement detailed radiation pressure models
* Extend CR3BP propagation and mission design functionality (including differential correction to account for perturbations)
* ...

.. _contributors:

Contributor list
================

Below, there is a list of contributors to Tudat. Mostly, these have been staff and students of TU Delft who have worked on Tudat as part of their research project(s) and/or as TAs. Many of them have put a lot of their free time and research time into making Tudat what it is. If you think your name is missing here, please let us know! 

**Currently and recently active contributors**

* `Dominic Dirkx <https://www.linkedin.com/in/dominic-dirkx-2806a5b6>`_
* `Geoffrey Garrett <https://www.linkedin.com/in/ghgarrett/>`_
* Marie Fayolle
* Miguel Avillez
* Sean Cowan
* Kevin Cowan
* `João Encarnação <https://www.linkedin.com/in/joaoencarnacao/>`_
* Carlos Fortuny Lombrana
* Jeremie Gaffarel
* Jonas Hener
* Gregorio Marchesini
* Maarten van Nistelrooij
* Filippo Oggionni
* Michael Plumaris

**Tudat Alumni Hall-of-fame**

* `Kartik Kumar <https://www.linkedin.com/in/kumarkartik/>`_ - For starting it all, developing numerous core features, and leading the project through the crucial first few years with huge passion and commitment
* `Jacco Geul <https://jacco.geul.net/>`_ - For supporting Tudat for the duration of his Ph.D. project, resolving more bugs and answering more questions than we can count and professionalizing the setup of the project
* `Jeroen Melman <https://www.linkedin.com/in/jeroen-melman-9533148>`_ - For helping to build up the Tudat project in its very first years with code development and project setup, without which it may never have survived 

**Past Contributors**

* `Giacomo Aciarini <https://www.linkedin.com/in/giacomo-acciarini-470712151/>`_
* `Evianne Brandon <https://www.linkedin.com/in/eviannebrandon/>`_
* `Frank Engelen <https://www.linkedin.com/in/frankengelen/>`_
* `Michele Facchinelli <https://www.linkedin.com/in/mfacchinelli/>`_
* `Iosto Fodde <https://www.linkedin.com/in/iosto-fodde-572b81129/>`_
* `Jacco Geul <https://jacco.geul.net/>`_
* `David Gondelach <https://www.linkedin.com/in/david-gondelach/>`_
* `Alejandro Gonzalez Puerta <https://www.linkedin.com/in/alejandrogonzalezpuerta/>`_
* `Linda van der Ham <https://www.linkedin.com/in/linda-van-der-ham-1606594a/>`_
* `Frank Hogervorst <https://www.linkedin.com/in/frankhogervorst/>`_
* `René Hoogendoorn <https://www.linkedin.com/in/rene-hoogendoorn-107/>`_
* `Kartik Kumar <https://www.linkedin.com/in/kumarkartik/>`_
* `Jonatan Leloux <https://www.linkedin.com/in/jonatanleloux/>`_
* `Francesco Lupi <https://www.linkedin.com/in/francesco-lupi-b23a658/>`_
* `Aleix Pinardell <https://www.linkedin.com/in/aleixpinardell/>`_
* `Bart Römgens <https://www.linkedin.com/in/bart-r%C3%B6mgens-b7a19314/>`_
* `Tineke Roegiers <https://www.linkedin.com/in/roegiers/>`_
* `Alexander Ronse <https://www.linkedin.com/in/alexander-ronse-1401a5b/>`_


..
   * Elmar Puts
   * Bryan Tong Minh
   * Sebastian Villamil
