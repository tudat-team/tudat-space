*****************************
Using Github with Tudat Space
*****************************


This page outlines some useful workflows when using Github to add

Gitflow Workflow
################

- https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

Initialize (if not already) Git-Flow
************************************

Initialize a Repository for git-flow

.. code-block:: base
    :linenos:

    git flow init -d

(Omit `-d` if you want to select values other than the defaults.)

.. code-block:: base
    :linenos:

    $ git flow init
    Initialized empty Git repository in ~/project/.git/
    No branches exist yet. Base branches must be created now.
    Branch name for production releases: [master]
    Branch name for "next release" development: [develop]

    How to name your supporting branch prefixes?
    Feature branches? [feature/]
    Release branches? [release/]
    Hotfix branches? [hotfix/]
    Support branches? [support/]
    Version tag prefix? []

Start a New Feature
*******************

This creates a new branch based on `develop` and switches to it:

.. code-block:: base
    :linenos:

    git flow feature start feature_branch

Publish a Feature
*****************

Push a feature branch to remote repository:

.. code-block:: base
    :linenos:

    git flow feature publish feature_branch

Get a feature published by another user from remote repository:

.. code-block:: base
    :linenos:

    git flow feature pull origin feature_branch

Finish a Feature
****************

This merges the feature into `develop`, removes the feature branch, and switches to `develop`:

.. code-block:: base
    :linenos:

    git flow feature finish feature_branch

Start a Release
***************

Create release branch from `develop`:

.. code-block:: base
    :linenos:

    git flow release start release_branch

Publish release branch:

.. code-block:: base
    :linenos:

    git flow release publish release_branch

Create a local tracking branch for a remote release:

.. code-block:: base
    :linenos:

    git flow release track release_branch

Finish a Release
****************

Merge release branch into `master`, tag it, merge back into `develop`, and remove the release branch:

.. code-block:: base
    :linenos:

    git flow release finish release_branch
    git push --tags

Start a Hotfix
**************

Create hotfix branch from `master`:

.. code-block:: base
    :linenos:

    git flow hotfix start VERSIONNAME

Create hotfix branch from some other commit:

.. code-block:: base
    :linenos:

    git flow hotfix start VERSIONNAME BASENAME

Finish a Hotfix
***************

Merge hotfix back into develop and master, and tag:

.. code-block:: base
    :linenos:

    git flow hotfix finish VERSIONNAME

Command-line
############

CLion Github Integration
########################

Releases using Rever
####################