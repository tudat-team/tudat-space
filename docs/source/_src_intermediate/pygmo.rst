*********************************
Optimizating a problem with PyGMO
*********************************

The following sections will provide some information on how to
optimize an astrodynamics problem written with tudatpy through the
usage of `PyGMO`_.

.. _`PyGMO`: https://esa.github.io/pygmo2/index.html

About PyGMO
######################

The "basic" idea
----------------

PyGMO is a Python scientific library derived by `PaGMO`_ (Parallel Global Multiobjective Optimization),
an open-source software developed at the European Space Agency by F. Biscani and D. Izzo [Biscani2020]_.
The flexible and complete framework of PaGMO (and of its equivalent PyGMO) can be applied to
"single-objective, multiple-objective, continuous, integer, box-constrained, non linear constrained, stochastic,
deterministic optimization problems".
Both programs are based on the concept of the *island model*, which in short is a computational strategy that allows to
run the optimization process in parallel (hence its name) by using multithreading techniques.

.. _`PaGMO`: https://esa.github.io/pagmo2/index.html

First steps
-----------

There are a number of basic elements concurring to the solution of an optimization problem using PyGMO.
These will be listed below and briefly explained; each of them correspond to an equivalent base class in PyGMO.

1. *A problem*. This represents the problem for which an optimal solution must be found.
This is usually known, in PyGMO terminology, as User-Defined Problem (UDP);
it is usually more interesting to code and solve a custom problem, but there are certain problems that
are defined within PyGMO and can be readily used.

2. *An algorithm*. This is the procedure to solve the optimization problem.
Similarly, this is known as User-Defined Algorithm (UDA); differently from the problem,
it is often more convenient to take advantage of the many UDAs offered by PyGMO. Nonetheless, it is always
possible to code a custom solver.

3. *One (or more) individuals*. Optimizers rely not on one, but many decision vectors that may interact (heuristic
optimizers) or may not (analytical solvers) interact with each other. A set of individuals form a *population*.
In PyGMO, it is more frequent to deal with an entire population, rather than with a single individual.

There are also two other fundamental blocks that conclude the structure of the island model.
One is the *island* itself, which represents the main parallelization block to achieve simultaneous
computation; the other one is the *archipelago*, consisting of a set of islands. These are useful
to solve more advanced and computationally-demanding problems, therefore their usage will not be analyzed in
detail here.


Optimizing a simple problem
###########################

write steps for the Himmelblau function


.. [Biscani2020] Biscani et al., (2020). A parallel global multiobjective framework for optimization: pagmo. Journal of Open Source Software, 5(53), 2338, https://doi.org/10.21105/joss.02338.