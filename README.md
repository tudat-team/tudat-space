# ``tudat-space``

This repository contains the source code for the `tudat-space` website, found under [docs.tudat.space](https://docs.tudat.space/). The website contains a getting-started section for new users, a comprehensive user-guide along with some background information on the Tudat project. It is built using Sphinx.

For more details on the Tudat project, we refer to the [project website](https://docs.tudat.space/en/latest/) and our [project Github page](https://github.com/tudat-team).

## Structure of `tudat-space`

The `tudat-space` repository contains the `docs` directory, which hosts all information required to build the `tudat-space` website:
1. `tudat-space/docs/source`, where the source of the website is written in `.rst` files.
2. `tudat-space/docs/environment.yaml`, which holds information to create the `tudat-docs` environment. This environment is used to build the website locally and on [ReadtheDocs](https://readthedocs.org/projects/tudat-space/).
3. `tudat-space/.readthedocs.yml` contains the configuration for the online build on [ReadtheDocs](https://readthedocs.org/projects/tudat-space/).
4. (If the documentation has been built locally): `tudat-space/docs/build`, which contains the local build in `.html` files.

The [examples on the website](https://docs.tudat.space/en/latest/_src_getting_started/examples.html) are integrated using the [tudatpy-examples repository](https://github.com/tudat-team/tudatpy-examples) as a submodule.
If you would like to add examples or make changes, please contribute in the `tudatpy-examples` repository.
This repository will be automatically updated from the [Sync tudat-space submodule](https://github.com/tudat-team/tudatpy-examples/actions/workflows/sync-tudat-space.yml) action.

## Contributing to the website

If you see anything on the website you would like to improve, you can leave your thoughts on our [discussion board](https://github.com/orgs/tudat-team/discussions/categories/ideas-and-suggestions) or make the modifications yourself and open a pull request. Detailed instruction for developing and building the website (locally or online) are provide on our [wiki](https://github.com/tudat-team/tudat-space/wiki)
