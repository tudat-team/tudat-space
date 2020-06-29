# start-here
An introduction and guide to the new tudat environment.

<p align="center">
  <img src="tudat-team.png" width="300" height="300">
  <em>
  <br>Big thanks to a childhood friend, <a href="https://www.instagram.com/neiltf/?hl=en">Neil Tiou-Fat</a>, for throwing this concept together
    </em>
</p>

# Foreword

To the ongoing developers of tudat and its ecosystem: I apologise sincerely. The codebases have gone through a complete refractoring, but I will motviate and go through each and every one of them. I also give you my word that I will be here be here to ensure a smooth transition to the accepted changes of the codebase (I will refractor specific changes if it is so desired by the majority). There are changes to the development workflow and user workflow which concern both performance and conventions. Also, for the first time in my memory of the environment, we have versioning!

# Repositories

- **[[tudat]](https://github.com/tudat-team/tudat) A C++ platform to perform astrodynamics and space research.**
> If the tudat-environment were Io, the most geolocially active object in the solar system, then tudat would be its iron constitued core. It comprises of a powerful set of C++ libraries aimed towards facilliating astrodynamics and space research. 

- **[[tudat-resources]](https://github.com/tudat-team/tudat-resources) A curated resource manager to facilitate astrodynamics and space research.** 

> There is a continuous demand to incorporate readily available and accessible resources for tudat, as well as allow for unique analyses that may be rare. For this purpose, all spice kernels, space weather data, gravity models (everything that can be classified as data outside of a header file) have been separated from tudat. The end goal is to eventually have the package retrieve resources on the fly, as requested, from the original source.

- **[[sofa-cmake]](https://github.com/tudat-team/sofa-cmake)** [dependency] 
> Required for the tudat spice_interface library.

- **[[cspice-cmake]](https://github.com/tudat-team/cspice-cmake)** [dependency] 
> Required for the tudat cspice_interface library.

- **[[nrlmsise-00-cmake]](https://github.com/tudat-team/nrlmsise-00-cmake)** [dependency]

- **[[tudatpy]](https://github.com/tudat-team/tudatpy)** 
