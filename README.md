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
In an effort to modernised the repositories and provide capability to host prebuilt libraries on contemporary package
managers, many changes have been made. Some minor corrections, some styling and most related to the build process. 
(See [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html))

## Conda support
- Conda package manager support for all repositories has been added (See [Anaconda Cloud](https://anaconda.org/tudat-team)). 

## Styling
- Directory naming has been changed throughout the tudat source code.
- The `tudat::electro_magnetism` namespace has been changed to `tudat::electromagnetism`. 


## CMake
- CMakeList.cmake files have been changed throughout the entirety of the tudat source code to provide relocatability
in addition the an install step.
- `yolo` cmake archive added which provided consistent functions to add tudat libraries, tests and executables. 
(See [Github](https://github.com/tudat-team/tudat/tree/master/cmake_modules/yolo))


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

Minconda is solely the conda repository management system without packages, whereas Anaconda is the repository management 
system packaged with some built in packages. If you want the bare minimum (bare in mind you will be installing some of
what comes with the base distribution in Anaconda), then install Miniconda 
([Miniconda download](https://docs.conda.io/en/latest/miniconda.html)), otherwise you can install
the Graphical, or command line installer of Anaconda ([Anaconda download](https://www.anaconda.com/products/individual)).

### Building ([conda-build](https://docs.conda.io/projects/conda-build/en/latest/))
When designing the specifics of a build process for a repository across platforms, to be install by the `conda` package 
manager, `conda-build` is concerned. From the [`conda-build`](https://docs.conda.io/projects/conda-build/en/latest/) 
documentation:

> Conda-build contains commands and tools to use conda to build your own packages. It also provides helpful tools to constrain or pin versions in recipes. Building a conda package requires installing conda-build and creating a conda recipe. You then use the conda build command to build the conda package from the conda recipe.

At the heart of `conda-build` are `conda-recipes`. Within the `tudat-team` repositories, these can be found in the source
code as `.conda`. The `.conda` recipes are used for development purposes, whereas releases on conda are invoked by making
a PR to the master branches of any of the `feedstock` repositories (see below). For more information on `conda-build` 
see their [docs](https://docs.conda.io/projects/conda-build/en/latest/index.html). 

Please see [`conda-build` recipes](https://docs.conda.io/projects/conda-build/en/latest/concepts/recipe.html) in
conjunction with the following examples.

**Example 1**: [cspice-cmake](https://github.com/tudat-team/cspice-cmake) repository recipe. 

````$xslt
.conda
├── bld.bat
├── build.sh
├── conda_build_config.yaml
└── meta.yaml
````

The `build.sh` contains the build process for Linux and macOS. Worth noticing is the definition of `CMAKE_PREFIX_PATH`.
This tells `CMake` to install the build into `conda-build`'s `$PREFIX` path. The `$PREFIX` path is an important concept
and is equivalent to the `$CONDA_PREFIX` environment variable following installation of Anaconda or Miniconda. 

````$xslt
#!/usr/bin/env bash

mkdir build

cd build

cmake \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="$PREFIX" \
    -DCMAKE_PREFIX_PATH="$PREFIX" \
    -DCSPICE_BUILD_STATIC_LIBRARY=1 \
    ..

make -j2

ctest

make install
````

The `$PREFIX` path definition fixes the following install tree structure in the compressed package on Anaconda Cloud. 
(see the [cspice-cmake package](https://anaconda.org/tudat-team/cspice-cmake/files)).

## Result
````$xslt
.
├── data
│   └── cspice
│       ├── cook_01.tc
|       ...
|
├── include
│   └── cspice
│       ├── f2c.h
|       ...
|
├── info
│   ├── about.json
│   ├── files
│   ├── git
│   ├── hash_input.json
│   ├── has_prefix
│   ├── index.json
│   ├── paths.json
│   └── recipe
│       ├── bld.bat
│       ├── build.sh
│       ├── conda_build_config.yaml
│       ├── meta.yaml
│       └── meta.yaml.template
└── lib
    ├── cmake
    │   └── cspice
    │       ├── cspice-config.cmake
    │       ├── cspice-config-version.cmake
    │       ├── cspice_export.cmake
    │       └── cspice_export-release.cmake
    └── libcspice.a

````




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
