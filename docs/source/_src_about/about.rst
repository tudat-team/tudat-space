====================
About Tudat
====================

Tudat's core functionality is in everything related to numerical progation of dynamics, including functionality such as:

- Choices of various, fixed and variable step-size, integrators, including: Runge-Kutta 4, Runge-Kutta variable step-size (various orders), Bulirsch-Stoer, and Adams-Bashfort-Moulton.
- Propagation of the **diverse state types**: translational state, rotational state, mass, or any user defined state derivative function.
- Flexible options for the **termination conditions** of a propagation
- Options to **save environment and system properties** during the propagation
- Propagation of not only the state, but also the **variational equations **associated with the dynamics, over a single arc, multiple arcs, or a combination.
- Numerous **built-in and customizable solar-system body models**, e.g. gravity fields, atmosphere, orbits and rotations of various planets.
- Options to include acceleration models, e.g. point mass gravity, spherical harmonics gravity, aerodynamics, radiation pressure, and thrust.
- Building of a custom made, or pre-defined, aerodynamic guidance model and/or thrust guidance model.
- Defining a vehicle to be used in the simulation, for which the mass, aerodynamic coefficients, reference area, orientation, and various other parameters can be defined by the user.
- Preliminary mission design functionality, including Lambert targeters, patched conic multiple-gravity assist, shape-based low-thrust models, and more.
- Interface to the orbit simulation functionality through JSON files
- Extensive documentation and tutorials found on this website.

Tudat has also been used extensively in research projects, a few of them are listed below:

- `Propagation and estimation of the dynamical behaviour of gravitationally interacting rigid bodies <https://link.springer.com/article/10.1007/s10509-019-3521-4>`_, Dirkx, D., Mooij, E., & Root, B. Astrophysics and Space Science, 364(2), 2019, 37.
- `Ariane 5 GTO debris mitigation using natural perturbations <https://www.sciencedirect.com/science/article/pii/S0273117718308792?dgcid=coauthor>`_, Pinardell Pons, A., and Noomen, R. Advances in Space Research (in press) 2019.
- `Laser and radio tracking for planetary science missions—a comparison <https://link.springer.com/article/10.1007/s00190-018-1171-x>`_, Dirkx, D., Prochazka, I., Bauer, S., Visser, P., Noomen, R., Gurvits, L. I., & Vermeersen, B. Journal of Geodesy (in press), 2018
- `Uncertainty propagation for statistical impact prediction of space debris <https://www.sciencedirect.com/science/article/pii/S0273117717307305>`_, Hoogendoorn, R., Mooij, E., and Geul, J., Advances in Space Research, 61(1), (2018, 167-181.
- `On the contribution of PRIDE-JUICE to Jovian system ephemerides <https://www.sciencedirect.com/science/article/pii/S0032063317302301>`_, D. Dirkx, L.I. Gurvits, V. Lainey, G. Lari, A. Milani, G. Cimò, T.M. Bocanegra-Bahamon, P.N.A.M. Visser. Planetary and Space Science, Volume 147, 2017, Pages 14-27, ISSN 0032-0633.
- `Dynamical modelling of the Galilean moons for the JUICE mission <https://www.sciencedirect.com/science/article/pii/S0032063316301143>`_, D. Dirkx, V. Lainey, L.I. Gurvits, P.N.A.M. Visser. Planetary and Space Science, Volume 134, 2016, Pages 82-95, ISSN 0032-0633.
- `Demonstration of orbit determination for the Lunar Reconnaissance Orbiter using one-way laser ranging data <https://www.sciencedirect.com/science/article/pii/S0032063316300319>`_, S. Bauer, H. Hussmann, J. Oberst, D. Dirkx, D. Mao, G.A. Neumann, E. Mazarico, M.H. Torrence, J.F. McGarry, D.E. Smith, M.T. Zuber. Planetary and Space Science, Volume 129, 2016, Pages 32-46, ISSN 0032-0633.
- `Comparative analysis of one- and two-way planetary laser ranging concepts <https://www.sciencedirect.com/science/article/pii/S0032063315001798>`_, D. Dirkx, R. Noomen, P.N.A.M. Visser, S. Bauer, L.L.A. Vermeersen. Planetary and Space Science, Volume 117, 2015, Pages 159-176, ISSN 0032-0633.
- `Phobos laser ranging: Numerical Geodesy experiments for Martian system science <https://www.sciencedirect.com/science/article/pii/S0032063314000907>`_, D. Dirkx, L.L.A. Vermeersen, R. Noomen, P.N.A.M. Visser. Planetary and Space Science, Volume 99, 2014, Pages 84-102, ISSN 0032-0633.
- `Mab’s orbital motion explained <https://www.sciencedirect.com/science/article/pii/S0019103515000950>`_, K. Kumar, I. de Pater, M.R. Showalter. Icarus, Volume 254, 2015, Pages 102-121, ISSN 0019-1035.
- `Statistical Impact Prediction of Decaying Objects <https://arc.aiaa.org/doi/abs/10.2514/1.A32832>`_, A. L. A. B. Ronse and E. Mooij. Journal of Spacecraft and Rockets, Vol. 51, No. 6 (2014), pp. 1797-1810.
- `Node Control and Numerical Optimization of Aerogravity-Assist Trajectories <https://arc.aiaa.org/doi/abs/10.2514/6.2017-0471>`_, Jaimy Hess and Erwin Mooij. AIAA Atmospheric Flight Mechanics Conference, AIAA SciTech Forum, (AIAA 2017-0471).
- `Reachability Analysis to Design Zero-Wait Entry Guidance <https://arc.aiaa.org/doi/abs/10.2514/6.2018-1316>`_, Alejandro Gonzalez-Puerta, Erwin Mooij, and Celia Yabar Valles. 2018 AIAA Guidance, Navigation, and Control Conference, AIAA SciTech Forum, (AIAA 2018-1316).
