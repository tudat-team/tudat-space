# ``tudat-space``

This repository contains the source code for the `tudat-space` website, found under [docs.tudat.space](https://docs.tudat.space/). The website contains a getting-started section for new users, a comprehensive user-guide along with some background information on the Tudat project. It is built using Sphinx.

For more details on the Tudat project, we refer to the [project website](https://docs.tudat.space/en/latest/) and our [project Github page](https://github.com/tudat-team).

## Structure of `tudat-space`

The `tudat-space` repository contains the `docs` directory, which hosts all information required to build the `tudat-space` website:
1. `tudat-space/docs/source`, where the source of the website is written in `.rst` files.
2. `tudat-space/docs/environment.yaml`, which holds information to create the `tudat-docs` environment. This environment is used to build the website locally and on [ReadtheDocs](https://readthedocs.org/projects/tudat-space/).
3. `tudat-space/.readthedocs.yml` contains the configuration for the online build on [ReadtheDocs](https://readthedocs.org/projects/tudat-space/).
4. (If the documentation has been built locally): `tudat-space/docs/build`, which contains the local build in `.html` files.
   

## How to build the `tudat-space` website locally 

The Sphinx build process is documented in the [tudat-developer-docs](https://tudat-developer.readthedocs.io/en/latest/primer/docs/sphinx.html).

In short, the `tudat-space` website can be built as follows:

1. Install the `tudat-docs` conda environment:

```bash
conda env create -f docs/environment.yaml
```

2. Activate the `tudat-docs` environment:

```bash
conda activate tudat-docs
```

3. Build the website:

The local build can be triggered from the command-line or using an IDE. For IDE-specific instructions, see the [tudat-developer-docs](https://tudat-developer.readthedocs.io/en/latest/primer/docs/sphinx.html#compiling-documentation-in-pycharm).

The website is built using the `sphinx-build` command, specifying `html` as desired output.

```bash
sphinx-build -b html docs/source docs/build
```

By default, this will only trigger a partial rebuild of the files with changes.
This might lead to issues when changing file names or after switching branches.
In that case, a full rebuild can be triggered by adding a `-E` flag:

```bash
sphinx-build -b html docs/source docs/build -E
```

For additional troubleshooting see the [Troubleshooting section](https://tudat-developer.readthedocs.io/en/latest/primer/docs/sphinx.html#troubleshooting) in the `tudat-developer-docs`.

4. View the local build:

You can check your local build by opening the newly created `docs/build/index.html` with your preferred browser and navigating as desired.

## How to trigger a build of the online `tudat-space` website

The `tudat-space` website resides at [docs.tudat.space](https://docs.tudat.space/), where the ``stable`` version (see menu at lower left of this page) contains the docs of the `tudat-space` master branch, and the ``latest`` version of the `tudat-space` develop branch.
The website is rebuilt every time a new commit is pushed on one of the branches.
The progress and log of the online docs build can be found [here](https://readthedocs.org/projects/tudat-space/).