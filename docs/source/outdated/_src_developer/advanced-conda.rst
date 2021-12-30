*************************
Advanced Usage with Conda
*************************

.. tip::
    This page follows directly from :ref:`Getting Started with Conda`, so make
    sure to have gone through that first.

Getting Started with conda-build
################################

.. note::
    The documentation found here will be complementary to the official
    `conda-build_` documentation and will assume that that has been covered.

Conda-build contains commands and tools to use conda to build your own
packages. It also provides helpful tools to constrain or pin versions in
recipes. Building a conda package requires installing conda-build and creating
a conda recipe. You then use the conda build command to build the conda package
from the conda recipe.

.. note::
    If you are planning to upload your packages to Anaconda Cloud, you will
    need an Anaconda Cloud account and client.

Installing and Updating conda-build
***********************************

Concepts
********

- Conda-

********

Getting Started with conda-forge
################################

.. image:: _static/conda-forge-square.png

.. _conda-build: https://docs.conda.io/projects/conda-build/en/latest/

   conda-forge is a GitHub organization containing repositories of conda
   recipes. Thanks to some awesome continuous integration providers (AppVeyor,
   Azure Pipelines, CircleCI and TravisCI), also known as a feedstock,
   automatically builds its own recipe in a clean and repeatable way on
   Windows, Linux and OSX.

