![alt text](cover.png "Logo Title Text 1")

# Foreword

To the ongoing developers of tudat and its ecosystem: I apologise sincerely. The codebases have gone through a complete refractoring, but I will motivate and go through each and every one of them. I also give you my word that I will be here be here to ensure a smooth transition to the accepted changes of the codebase (I will refractor specific changes if it is so desired by the majority). There are changes to the development workflow and user workflow which concern both performance and conventions. Also, for the first time in my memory of the environment, we have versioning!

# Table of Contents
1. [Repositories](#repositories)
2. [Changes](#changes)
2. [Users](#users)
3. [Developers](#developers)
4. [Goals](#goals)

# Repositories

This section briefly describes all repositories contained within the `tudat-team` organization. 

## **[tudat-bundle](https://github.com/tudat-team/tudat-bundle)**
**A developers repository for the tudat environment.** If you're used to the original way of working with tudat, this 
will be familiar. This repository bundles together all dependencies that are maintained by the tudat-team, with the 
addition of pybind11. Boost and Eigen have well maintained packages on conda-forge which reduces compile time 
(w.r.t. Boost), so their dependencies are met through specifying the `CMAKE_PREFIX_PATH=$CONDA_PREFIX`, for your chosen 
conda environment.

## **[tudatpy](https://github.com/tudat-team/tudatpy)**
**A Python platform to perform astrodynamics and space research.** 

## **[tudat](https://github.com/tudat-team/tudat)**
**A C++ platform to perform astrodynamics and space research.** If the tudat environment were Io, the most geologically 
active object in the solar system, then tudat would be the iron constituent of its core. It comprises of a powerful set 
of C++ libraries aimed towards facilitating astrodynamics and space research. 

## **[tudat-resources](https://github.com/tudat-team/tudat-resources)** 
**A curated resource manager to facilitate astrodynamics and space research.** There is a continuous demand to 
incorporate readily available and accessible resources for tudat, as well as allow for unique analyses that may be rare. 
For this purpose, all spice kernels, space weather data, gravity models (everything that can be classified as data 
outside of a header file) have been separated from tudat. The end goal is to eventually have the package retrieve 
resources on the fly, as requested, from the original source. (e.g. the spice kernels path will mirror the original 
[source](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/), downloading artifacts only when requested, or in advance 
with user configuration). When `tudat-resources` is complete, it will:

- Ensure resources specified in a `resource-manifest.json` are downloaded and ready to use when requested.
- Download resources upon request.
- Provide a C++ and Python library to access the resources.

## **[sofa-cmake](https://github.com/tudat-team/sofa-cmake)**
`sofa-cmake` is a repository which contains the `SOFA` ANSI C source code, with additional 
cmake files in order to interface with `tudat`. From The International Astronomical Union's SOFA service website:

> The International Astronomical Union's SOFA service has the task of establishing and maintaining an accessible and 
> authoritative set of algorithms and procedures that implement standard models used in fundamental astronomy. The 
> service is managed by an international panel, the SOFA Board, appointed through IAU Division A — Fundamental Astronomy.
> SOFA also works closely with the International Earth Rotation and Reference Systems Service (IERS).

Bundled documentation from the source code is hosted at [tudat.space](http://tudat.space/). For further information on 
`SOFA`, please see [iausofa.org](http://www.iausofa.org/).

## **[cspice-cmake](https://github.com/tudat-team/cspice-cmake)**
`cspice-cmake` is a repository which contains the `SPICE` toolkits for C, with additional 
cmake files in order to interface with `tudat`. From the Navigation and Ancillary Information Facility (NAIF) website:

> NASA's Navigation and Ancillary Information Facility (NAIF) offers NASA flight projects and NASA funded researchers 
> the "SPICE" observation geometry information system to assist scientists in planning and interpreting scientific
> observations from space-based instruments aboard robotic planetary spacecraft. SPICE is also used in support of
> engineering tasks associated with these missions. While planetary missions were the original focus, today SPICE is
> also used on some heliophysics and earth science missions.

Bundled documentation from the source code is hosted at [tudat.space](http://tudat.space/). For further information on 
`SPICE`, please see [naif.jpl.nasa.gov](https://naif.jpl.nasa.gov/naif/index.html).

## **[nrlmsise-00-cmake](https://github.com/tudat-team/nrlmsise-00-cmake)**
`nrlmsise-00-cmake` is a repository which contains the `NRLMSISE-00` Atmosphere Model in C, with additional 
cmake files in order to interface with `tudat`. From wikipedia's 
[paraphrasing](https://en.wikipedia.org/wiki/NRLMSISE-00) of 
[J. M. Picone et al.](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2002JA009430):

> NRLMSISE-00 is an empirical, global reference atmospheric model of the Earth from ground to space. It models the 
> temperatures and densities of the atmosphere's components. A primary use of this model is to aid predictions of 
> satellite orbital decay due to atmospheric drag. This model has also been used by astronomers to calculate the mass
> of air between telescopes and laser beams in order to assess the impact of laser guide stars on the non-lasing
> telescopes.

# Changes

# Users

1. Download either the graphical *or* command line Anaconda installer [[link](https://www.anaconda.com/products/individual)].
2. 
 

## Documentation

## Feature requests

## Submit an issue

# Developers

## Packaging ([conda](https://docs.conda.io/en/latest/))
From the [`conda`](https://docs.conda.io/en/latest/) website, `conda` is a:

> Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more.

Minconda is solely the repository management system without packages, whereas Anaconda is the repository management 
system packaged with some built in packages. If you want the bare minimum (bare in mind you will be installing a lot of
what comes with the base distribution in Anaconda), then install Miniconda ([download links]), otherwise you can install
the Graphical, or command line installer of Anaconda ([download links](https://www.anaconda.com/products/individual)).

### Building ([conda-build](https://docs.conda.io/projects/conda-build/en/latest/))
From the [`conda-build`](https://docs.conda.io/projects/conda-build/en/latest/) documentation:

> Conda-build contains commands and tools to use conda to build your own packages. It also provides helpful tools to constrain or pin versions in recipes. Building a conda package requires installing conda-build and creating a conda recipe. You then use the conda build command to build the conda package from the conda recipe.

### Deployment ([conda-smithy](https://github.com/conda-forge/conda-smithy))
From the [`conda-smithy`](https://github.com/conda-forge/conda-smithy) repository:

> `conda-smithy` is a tool for combining a conda recipe with configurations to build using freely hosted CI services into a single repository, also known as a feedstock.

### Peer-review ([conda-forge](https://conda-forge.org/))
From the [`conda-forge`](https://conda-forge.org/) website:

> conda-forge is a GitHub organization containing repositories of conda recipes.

## Versioning ([rever](https://regro.github.io/rever-docs/index.html))
From the [`rever`](https://regro.github.io/rever-docs/index.html) documentation:

> Rever is a xonsh-powered, cross-platform software release tool. The goal of rever is to provide sofware projects a standard mechanism for dealing with code releases. Rever aims to make the process of releasing a new version of a code base as easy as running a single command.

Initiating `rever` in a repository:



# Goals

- Ease of Accessibility:
- Educational Environment:
- Research and Development:
- Machine Learning Integration:
