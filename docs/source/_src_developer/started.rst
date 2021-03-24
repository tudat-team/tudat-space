Getting Started
===============

.. note:: Developing tudat/tudatpy **features** on Windows? Please follow :ref:`Development on Windows` as
            first.

Installing Dependencies
-----------------------

In order to develop for ``tudat`` or ``tudatpy``, the dependencies must be
satisfied for building each project. To make this consistent, the following
environment files are provided.

- If developing ``tudatpy``, install ``tudatpy-devel.yaml`` (:download:`yaml <_static/tudatpy-devel.yaml>`)
- If developing ``tudat``, install ``tudat-devel.yaml`` (:download:`yaml <_static/tudat-devel.yaml>`)

.. note::

    You can install a conda environment by navigating to the containing directory and executing:

    .. code-block:: bash

        conda env create -f <file-name>.yml

.. toctree::
   :maxdepth: 2
   :caption: Intermediate Steps

   conda-smithy

Where next?
-----------

- Creating a new feedstock for tudat-space?
- Developing documentation?
- Developing source code?
    - Developing tudat
    - Developing tudatpy
    - Developing tudat and tudatpy simultaneously (tudat-bundle configuration).
- Working with Azure pipelines?

Repositories
------------






