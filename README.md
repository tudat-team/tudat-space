![alt text](cover.png "Logo Title Text 1")

# Foreword

To the ongoing developers of tudat and its ecosystem: I apologise sincerely. The codebases have gone through a complete refractoring, but I will motviate and go through each and every one of them. I also give you my word that I will be here be here to ensure a smooth transition to the accepted changes of the codebase (I will refractor specific changes if it is so desired by the majority). There are changes to the development workflow and user workflow which concern both performance and conventions. Also, for the first time in my memory of the environment, we have versioning!

# Table of Contents
1. [Repositories](#repositories)
2. [Changes](#changes)
2. [Users](#users)
3. [Developers](#developers)
4. [Goals](#goals)

# Repositories

- **[[tudat]](https://github.com/tudat-team/tudat) A C++ platform to perform astrodynamics and space research.**
> If the tudat-environment were Io, the most geolocially active object in the solar system, then tudat would be its iron constiuent of its core. It comprises of a powerful set of C++ libraries aimed towards facilliating astrodynamics and space research. 

- **[[tudat-resources]](https://github.com/tudat-team/tudat-resources) A curated resource manager to facilitate astrodynamics and space research.** 

> There is a continuous demand to incorporate readily available and accessible resources for tudat, as well as allow for unique analyses that may be rare. For this purpose, all spice kernels, space weather data, gravity models (everything that can be classified as data outside of a header file) have been separated from tudat. The end goal is to eventually have the package retrieve resources on the fly, as requested, from the original source. (e.g. the spice kernels path will mirror the original [source](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/), downloading artefacts only when requested, or in advance with user configuration)

- **[[sofa-cmake]](https://github.com/tudat-team/sofa-cmake)** [dependency] 
> Required for the tudat spice_interface library.

- **[[cspice-cmake]](https://github.com/tudat-team/cspice-cmake)** [dependency] 
> Required for the tudat cspice_interface library.

- **[[nrlmsise-00-cmake]](https://github.com/tudat-team/nrlmsise-00-cmake)** [dependency]

- **[[tudatpy]](https://github.com/tudat-team/tudatpy)** 


- **[[tudat-bundle]](https://github.com/tudat-team/tudat-bundle) A developers repository for the tudat environment.**
> If you're used to the original way of working with tudat, this will be familiar. This repository bundles together all dependencies that are maintained by the tudat-team, with the addition of pybind11. Boost and Eigen have well maintained packages on conda-forge which reduces compile time (w.r.t. Boost), so their dependencies are met through specifying the `CMAKE_PREFIX_PATH=$CONDA_PREFIX`, for your chosen conda environment.

# Changes

# Users

## Documentation

## Feature requests

## Submit an issue

# Developers

## Packaging ([conda](https://docs.conda.io/en/latest/))

### Building ([conda-build](https://docs.conda.io/projects/conda-build/en/latest/))

### Deployment ([conda-smithy](https://github.com/conda-forge/conda-smithy))

### Peer-review ([conda-forge](https://conda-forge.org/))

## Versioning ([rever](https://regro.github.io/rever-docs/index.html))

# Goals

- Ease of Accessibility:
- Educational Environment:
- Research and Development:
- Machine Learning Integration:
