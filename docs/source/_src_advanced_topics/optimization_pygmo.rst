.. _`optimization_pygmo`:

***********************
Optimization with PyGMO
***********************

The following paragraphs will give some information on how to
optimize an astrodynamics problem written with tudatpy through the
usage of `PyGMO`_. The aim of this page is not to provide comprehensive
documentation to the usage of PyGMO (such a guide already exists, see previous link),
but rather to introduce the reader to the logic behind PyGMO and illustrate how
to employ it jointly with tudatpy.

.. _`PyGMO`: https://esa.github.io/pygmo2/index.html

.. contents:: Content of this page
   :local:

About PyGMO
######################

The "basic" idea
----------------

PyGMO is a Python scientific library derived from `PaGMO`_ (Parallel Global Multiobjective Optimization),
an open-source software developed at the European Space Agency by F. Biscani and D. Izzo [Biscani2020]_.
The flexible and complete framework of PaGMO (and of its equivalent PyGMO) can be applied to
"single-objective, multiple-objective, continuous, integer, box-constrained, non linear constrained, stochastic,
deterministic optimization problems".
Both programs are based on the concept of the *island model*, which in short is a computational strategy that allows to
run the optimization process in parallel (hence its name) by using multithreading techniques.

.. _`PaGMO`: https://esa.github.io/pagmo2/index.html


Installing PyGMO
----------------
PyGMO is not part of the standard tudatpy distribution, but it can easily be added to any tudatpy environment.
Here we will assume that you already have a standard tudatpy environment (called ``tudat-space``) installed.
If that is not the case, please follow the "Installing Tudat(Py)" instructions in :ref:`installation`.

In order to make PyGMO available inside the ``tudat-space`` environment, the following steps need to be taken.
First, activate the ``tudat-space`` environment:

.. code:: bash

    $ conda activate tudat-space

Next, use conda to install the PyGMO package *to this environment*:

.. code:: bash

    (tudat-space) $ conda install pygmo

.. warning::

    Please ensure to install PyGMO in your given tudatpy environment. Do not add the PyGMO package to your base environment.


Lastly, you should verify that the package is now available in your tudatpy environment.
You can do so via your IDE or by using the following command in your terminal:

.. code:: bash

    (tudat-space) $ conda list | grep pygmo

which should return the name, version, build and channel of the pygmo installation in the given environment.



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

In this example, we will attempt to optimize a simple problem: the minimization of a
known analytical function. We chose `Himmelblau's function`_  as it is often employed
to test the performance of optimization algorithms:

.. _`Himmelblau's function`: https://en.wikipedia.org/wiki/Himmelblau%27s_function


.. math:: f(x,y) = (x^2 + y - 11)^2 + (x + y^2 - 7)

subject to the bounds:

.. math:: \begin{align*} &-5 < x < 5 \\ &-5 < y < 5 \end{align*}

There are four equal minima which can be found analytically. These are:

.. math:: \begin{align*} f(3, 2) &= 0 \\ f(−2.805118,3.283186) &= 0 \\ f(−3.779310,−3.283186) &= 0 \\ f(3.584458,−1.848126) &= 0 \end{align*}

Below, we will explain how to write the code for this specific UDP and solve it with PyGMO.
The original code, which is broken down into parts for the sake of clarity, is available :download:`here <_static/pygmo_himmelblau_test.py>`.

1. Creation of the UDP class
----------------------------

First, we create a Python class to describe the problem. This class will be fed later
to PyGMO, therefore it must be compatible. To be PyGMO-compatible, a UDP class must
have two methods:

- ``fitness(np.array)``: it takes a vector of size :math:`n` as input and returns a list with :math:`p` values
  as output. :math:`n` and :math:`p` are respectively the dimension of the problem (in our case, :math:`n = 2`)
  and the number of objectives (in our case, :math:`p = 1` because it is a single-objective optimization).

- ``get_bounds()``: it takes no input and returns a tuple of two :math:`n`-dimensional lists, defining respectively the
  lower and upper boundaries of each variable. The dimension of the problem (i.e. the value of :math:`n`) is
  automatically inferred by the return type of the this function.

.. literalinclude:: ./_static/himmelblau_udp.py
             :language: python

.. seealso::
   For more information, see the PyGMO documentation about
   `defining an UDP class <https://esa.github.io/pygmo2/tutorials/coding_udp_simple.html>`_.

2. Creation of a PyGMO problem
------------------------------

Once the UDP class is created, we must create a PyGMO problem object by passing
an instance of our class to ``pygmo.problem``. Note that an instance of the UDP class
must be passed as input to pygmo.problem() and NOT the class itself. It is also possible to use a PyGMO UDP, i.e.
a problem that is already defined in PyGMO, but it will not be shown in this tutorial. In this example,
we will use only one generation. More information about the PyGMO problem class is available
`on the PyGMO website <https://esa.github.io/pygmo2/tutorials/using_problem.html>`_.

.. literalinclude:: ./_static/pygmo_problem.py
             :language: python

3. Selection of the algorithm
-----------------------------

Now we must choose a specific optimization algorithm to be passed to ``pygmo.algorithm``. For this example, we will use
the Differential Evolution algorithm (DE). Many different algorithms are available
through PyGMO, including heuristic methods and local optimizers. It is also possible to create a User-Defined Algorithm
(UDA), but in this tutorial we will use an algorithm readily available in PyGMO. Since the algorithm internally uses a
random number generator, a seed can be passed as an optional input argument to ensure reproducibility.

.. seealso::
   For more information, see the PyGMO documentation about `available algorithms <https://esa.github.io/pygmo2/overview
   .html#list-of-algorithms>`_ and the `PyGMO algorithm class <https://esa.github.io/pygmo2/tutorials/using_algorithm.html>`_.

.. note::
    During the actual optimization process, fixing the seed is probably what you do **not** want to do.


.. literalinclude:: ./_static/pygmo_algorithm.py
             :language: python

4. Initialization of a population
---------------------------------

As a final preliminary step, a population of individuals must be initialized with ``pygmo.population``. Each individual has an associated
decision vector which can change (evolution), the resulting fitness vector, and an unique ID to allow their tracking.
The population is initialized starting from a specific problem to ensure that all individuals are
compatible with the UDP. The default population size is 0; in this example, we use 1000 individuals.
Similarly to what was done for the algorithm, since the population initialization is random,
a seed can be passed as an optional input argument to ensure reproducibility.

.. literalinclude:: ./_static/pygmo_population.py
             :language: python

.. seealso::
   For more information, see the page from the PyGMO documentation about
   `the PyGMO population class <https://esa.github.io/pygmo2/tutorials/using_population.html>`_.

5. Evolve the population
------------------------

To actually solve the problem, it is necessary to *evolve* the population.
This can be done by calling the ``evolve()`` method of the ``pygmo.algorithm`` object. We do so 100 times
in a recursive manner. At each evolution stage, it is possible to retrieve the full population through the ``get_x()``
method and, analogously, the related fitness values with ``get_f()``. If we are only interested in the best individual
of each evolution stage, we can find its index through the ``pop.best_idx()`` method. On the contrary, the ``champion_x``
(and the related ``champion_f``) attributes retrieves the decision variable vector and its fitness value. Note that the
*champion* is the best individual across all evolutionary stages (not necessarily the best individual found at the last
evolution).

.. literalinclude:: ./_static/pygmo_evolution.py
             :language: python

.. seealso::
   For more information, see the PyGMO documentation about
   `evolving a PyGMO population <https://esa.github.io/pygmo2/tutorials/evolving_a_population.html>`_.

6. Visualization of the results
-------------------------------

In the following figure, a contour plot of the Himmelblau's function is reported, where the red X represent the best
individuals of each generation. As it can be seen, the algorithm manages to locate all four identical minima.

.. figure:: _static/contour_himmelblau.png

In the plot below, instead, we can see how the fitness of the best individual improves while the population is evolved.
It can be seen, as anticipated before, that the champion is found a few generations before the last one.

.. figure:: _static/fitness_himmelblau.png

The figure below illustrates indicatively the performance of the algorithm in the vicinity of one of the four minima.

.. figure:: _static/one_minimum_himmelblau.png

7. Performance of the algorithm
-------------------------------

Since this is supposed to be an introductory example, a performance analysis of the algorithm is not presented here.
However, it is interesting to provide a quick comparison between the optimization conducted with PyGMO's DE algorithm
two other simple analytical methods, namely a grid search and a Monte-Carlo search (both of them were run with 1000
points per variable). In the table below, referred to the minimum located at (3,2), the results are summarized in terms
of accuracy and computational expenses.
As it can be noticed, the DE algorithm reaches a fitness level several orders of magnitude below the other two methods,
despite using only 10% of the computational resources.

.. tabularcolumns:: |l|c|c|c|

+-----------------------------------------------+------------------------------+-----------------------------------------------------+----------------------------+
| **Optimization method**                       | **Fitness value**            | **Decision variable difference wrt (3,2)**          | **Function evaluations**   |
+-----------------------------------------------+------------------------------+-----------------------------------------------------+----------------------------+
| PyGMO's DE (100 gens, 1000 individuals)       | :math:`1.292 \cdot 10^{-11}` | :math:`(-6.365 \cdot 10^{-7}, +2.382 \cdot 10^{-7})`| :math:`1.01 \cdot 10^{5}`  |
+-----------------------------------------------+------------------------------+-----------------------------------------------------+----------------------------+
| Grid search (1000 points per variable)        | :math:`4.215 \cdot 10^{-4}`  | :math:`(-2.002 \cdot 10^{-3}, -3.003 \cdot 10^{-3})`| :math:`1.00 \cdot 10^{6}`  |
+-----------------------------------------------+------------------------------+-----------------------------------------------------+----------------------------+
| Monte-Carlo search (1000 points per variable) | :math:`7.095 \cdot 10^{-4}`  | :math:`(+4.595 \cdot 10^{-3}, -9.645 \cdot 10^{-4})`| :math:`1.00 \cdot 10^{6}`  |
+-----------------------------------------------+------------------------------+-----------------------------------------------------+----------------------------+

.. [Biscani2020] Biscani et al., (2020). A parallel global multiobjective framework for optimization: pagmo.
   Journal of Open Source Software, 5(53), 2338, https://doi.org/10.21105/joss.02338.


Parallelization with Python and PyGMO
#########################################

In this section, a short guide is given on the parallelization of tasks in Python, and specifically for application with
PyGMO.


General parallelization with Python
------------------------------------

In Python, you can parallelize data processing in various ways. One possible way is to use GPU's, but this is not
discussed here. For Python CPU-based parallelization, there are generally two types: multi-processing and
multi-threading. Multi-processing is a method that initializes multiple processes. This means that different processes
are running on independent CPU's, with independent memory management. Multi-threading is a method that uses multiple
threads for a single parent process with shared memory. Child processes can be run on separate threads. There are
generally two threads per CPU, and each computer system has their own amount of CPU's with their own specs. The amount
of parallellity is therefore determined by the system you want to run on.

To start, parallelization does not have to be within PyGMO, it can be used for any simulation. Though, it should be
noted that it does not always make sense to parallelize your simulations. The initialization takes longer, so there is a
break even point beyond which it is worthwhile, which is discussed in :ref:`Multi-threading with Batch Fitness
Evaluation`. Below is a code snippet that shows in pseudo code how one can implement parallelization without PyGMO. To
enable this behavior with Python, the ``multiprocessing`` module is used. Other alternatives exist as well that are more
modern, but they are not as widely spread or as thoroughly documented. Ray, for instance, is one of these packages, it
is arguably more seemless, but it is also rather new and focused on AI applications.

All parallel processing should be put under ``if __name__ == "__main__" :``. This line ensures that the code is only run
if that file is the file being executed directly (so not imported, for example). This prevents an infinite loop when
creating new child processes -- or starting calculations on other threads.  If this line is omitted, child processes
import the python script, which then run the same script again, thereby spawning more child processes. This results in
an infinite loop. Next, ``mp.get_context("spawn")`` is  a context object that has the attributes of the multiprocessing
module. Here, the ``"spawn"`` argument refers to the method that creates a new Python process. ``"spawn"`` specifically
starts a fresh Python interpreter process -- which is default on macOS and Windows. ``"fork"`` copies a Python process
using ``os.fork()``-- which is the default on Linux. ``"forkserver"`` creates a server process; a new process is then
requested and the server uses ``"fork"`` to create it. This method can generally be left at the default value.

A ``Pool`` object is temporarily created, which is just a collection of available processes that can be allocated to
computational tasks. The number of cores you would like to appoint to the ``Pool`` is given as an argument.
Subsequently, the ``map()`` or ``starmap`` method allows for a function to be applied to an iterable, rather than a
single argument. ``map()`` allows for a single argument to be passed to the function, ``starmap()`` allows for multiple
arguments. The inputs are all the sets of input arguments in the form of a list of tuples, which constitutes the
iterable mentioned previously. The outputs are formatted analogously, where the tuples are the various outputs rather
than the input arguments. 

.. note::

    The memory will be freed only after all the outputs are collected. It may be wise to split the list of
    inputs into smaller batches in case a high number of simulations are run, to avoid overflowing the memory.

Other ways to specify the context or create a Pool object are also possible, more can be read on `the multiprocessing
documentation page <https://docs.python.org/3/library/multiprocessing.html>`_.

.. code:: python
    
    # Imports
    import multiprocessing as mp
    import numpy as np
    
    from tudatpy.kernel.numerical_simulation import environment_setup, propagation_setup
    from tudatpy.kernel.interface import spice
    
    # Functions
    def run_simulation(arg_1, arg_2):
        # Do some tudat things...
        return 1, arg_1 + arg_2
    
    # Main script
    if __name__ == "__main__":
        # Number of simulations to run
        N = 500
        arg_1_list = np.random.normal(-100, 50, size=N)
        arg_2_list = np.random.normal(1e6, 2e5, size=N)
    
        # Combine list of inputs
        inputs = []
        for i in range(N):
            inputs.append((arg_1_list[i], arg_2_list[i]))
    
        # Run simulations in parallel, using half the available cores
        n_cores = mp.cpu_count()//2
        with mp.get_context("spawn").Pool(n_cores) as pool:
            outputs = pool.starmap(run_simulation, inputs)

Parallelization with PyGMO User-Defined Problem (UDP)
-----------------------------------------------------

Parallelization is also very useful for optimization problems, because optimizations are generally quite resource
intensive processes, and this can be curbed by applying some form of parallellity. There are two flavors of parallelity
in PyGMO. One utilizing multi-processing, one multi-threading, presented in :ref:`Multi-threading with Batch Fitness
Evaluation` and :ref:`Multi-processing with Archipelagos`, respectively.


Multi-threading with Batch Fitness Evaluation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multi-threading in PyGMO is used with so-called Batch Fitness Evaluation (BFE); simply evaluating some fitness function
in a batch, similar to the examples explained before. For this, PyGMO has classes and methods to help setup a
multi-threaded optimisation. For this section, code snippets are used from an adapted version of `the hodographic
shaping MGA trajectory example
<https://github.com/tudat-team/tudatpy-examples/blob/master/pygmo/hodographic_shaping_mga_optimization.py>`_, seen
below. You can either define your own User-Defined Batch Fitness Evaluator (UDBFE), explained `here
<https://esa.github.io/pygmo2/bfe.html>`_, but here the `batch_fitness()` method is explained, as this follows more
naturally from :ref:`1. Creation of the UDP class` above. Furthermore, you have no control over exactly what happens
with using UDBFE's implemented in PyGMO, though it can be easier in some cases.

In a UDP, BFE can be enabled by adding a `batch_fitness()` method to the class, as seen below. This method receives as
input a 1D flattened array of all the design parameter vectors -- the first vector ranges from index [0, n], the second
from [n, 2n] and so on, with a design variable vector of length n. The output is constructed analogously, where the
length n is equal to the number of objectives. The `batch_fitness` method is somewhat of a wrapper for the `fitness()`
method, all it has to do is convert the input array into a list of lists, then create a pool of worker processes that
can be used.

.. code:: python

    def batch_fitness(self,
                design_parameter_vectors: np.ndarray) -> List[float]:
        """
        Function to evaluate the fitness. A single-objective optimization is used, in which the objective is the deltaV
        necessary to execute the transfer.
        """

        # Compute the final index of each type of parameters
        time_of_flight_index = 3 + self.no_of_legs
        incoming_velocity_index = time_of_flight_index + self.no_of_swingbys
        swingby_periapsis_index = incoming_velocity_index + self.no_of_swingbys
        shaping_free_coefficient_index = swingby_periapsis_index + self.total_no_shaping_free_coefficients
        revolution_index = shaping_free_coefficient_index + self.no_of_legs

        len_single_dpv = revolution_index
        dpvs = design_parameter_vectors.reshape(len(design_parameter_vectors)//len_single_dpv, len_single_dpv)

        inputs, fitnesses = [], []
        for dpv in dpvs:
            inputs.append([list(dpv)])

        # cpu_count = len(os.sched_getaffinity(0))
        cpu_count = mp.cpu_count()
        with mp.get_context("spawn").Pool(processes=int(cpu_count-4)) as pool:
            outputs = pool.map(self.fitness, inputs)

        for output in outputs:
            fitnesses.append(output)

        return fitnesses

Next, a code snippet is shown that invokes the BFE capabilities. The `batch_fitness()` function is part of the UDP,
which is called. There are two distinct things to do. 

.. code:: python

    bfe = True

    seed = 42
    pop_size = 500

    # Create Pygmo problem
    transfer_optimization_problem = MGAHodographicShapingTrajectoryOptimizationProblem(
        central_body, transfer_body_order, bounds, departure_semi_major_axis, departure_eccentricity,
        arrival_semi_major_axis, arrival_eccentricity)
    prob= pg.problem(transfer_optimization_problem)

    # Create algorithm and define its seed
    algo = pg.gaco()
    if bfe:
        algo.set_bfe(pg.bfe())
    algo = pg.algorithm(algo)

    bfe_pop = pg.default_bfe() if bfe else None
    pop = pg.population(prob=prob, size=pop_size, seed=seed, b=bfe_pop)

    num_gen = 150

    # Initialize lists with the best individual per generation
    list_of_champion_f = [pop.champion_f]
    list_of_champion_x = [pop.champion_x]

    # mp.freeze_support() needs to be called when using multiprocessing on windows
    # mp.freeze_support()

    for i in range(num_gen):
        print(f'Evolution: {i+1} / {num_gen}', end='\r')
        pop =algo.evolve(pop)

        # Save current champion
        list_of_champion_x.append(pop.champion_x)
        list_of_champion_f.append(pop.champion_f)
    print('Evolution finished')


To show that this actually works well, a few tests are done with various complexities. Normally, the number of function
evaluations would be a good indication of runtime complexity, however this parallellity does not change that number. CPU
time can be and clock time to show that it makes a difference, though this should be taken with a grain of.

.. note::

   These simulations are tested on macOS Ventura 13.1 with a 3.1 GHz Quad-Core Intel Core i7 processor.


+--------------------+-------------------------+---------------------------+---------------+----------------+-----------------+
| Transfer Sequence  | Gen count and Pop size  | Batch Fitness Evaluation  | CPU time [s]  | CPU usage [-]  | Clock time [s]  |
+====================+=========================+===========================+===============+================+=================+
| EJ                 | gen30pop100             | no                        | 17.6          | 106%           | 16.7            |
|                    |                         +---------------------------+---------------+----------------+-----------------+
|                    |                         | yes                       | 130.7         | 443%           | 29.5            |
|                    +-------------------------+---------------------------+---------------+----------------+-----------------+
|                    | gen300pop1000           | no                        | 4500          | 78%            | 5770            |
|                    |                         +---------------------------+---------------+----------------+-----------------+
|                    |                         | yes                       | 3000          | 405%           | 735             |
+--------------------+-------------------------+---------------------------+---------------+----------------+-----------------+
| EMEJ               | gen30pop100             | no                        | 70.1          | 97%            | 72.3            |
|                    |                         +---------------------------+---------------+----------------+-----------------+
|                    |                         | yes                       | 159.2         | 428%           | 37.2            |
|                    +-------------------------+---------------------------+---------------+----------------+-----------------+
|                    | gen300pop1000           | no                        | 4440          | 60%            | 7440            |
|                    |                         +---------------------------+---------------+----------------+-----------------+
|                    |                         | yes                       | 5946          | 404%           | 1470            |
+--------------------+-------------------------+---------------------------+---------------+----------------+-----------------+

Multi-processing with Islands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section presents multi-processing with PyGMO using the ``pg.island`` and/or ``pg.archipelago`` class. An island is
an object that enables asynchronous optimization of its population. An archipelago is a network that connects multiple
islands -- `pg.island` objects -- through a topology. Islands can exchange individuals with one another through a
topology -- a `pg.topology` object. This topology can configure the exchange of individuals between islands in an
archipelago. 

.. Finally, the optimization can be executed by successively evolving the island. To do so, the method
.. `island.evolve()` is called the desired number of times inside a loop. After starting each evolution of the island,
.. the method `island.wait_check()` is called, which makes the program wait for all the evolutions running in parallel
.. to finish. After each evolution is finished, the best fitness and parameters vector are saved.

.. code:: python

    seed = 42
    pop_size = 1000

    # Create Pygmo problem
    transfer_optimization_problem = MGAHodographicShapingTrajectoryOptimizationProblem(
        central_body, transfer_body_order, bounds, departure_semi_major_axis, departure_eccentricity,
        arrival_semi_major_axis, arrival_eccentricity)
    problem = pg.problem(transfer_optimization_problem)

    # Create algorithm and define its seed
    algorithm = pg.algorithm(pg.sga(gen=1))
    algorithm.set_seed(seed)

    # Create island
    island = pg.island(algo=algorithm, prob=problem, size=pop_size, seed=seed)

    num_gen = 40

    # Initialize lists with the best individual per generation
    list_of_champion_f = [island.get_population().champion_f]
    list_of_champion_x = [island.get_population().champion_x]

    # mp.freeze_support() needs to be called when using multiprocessing on windows
    # mp.freeze_support()

    for i in range(num_gen):
        print('Evolution: %i / %i' % (i+1, num_gen))

        island.evolve() # Evolve island
        island.wait_check() # Wait until all evolution tasks in the island finish

        # Save current champion
        list_of_champion_x.append(island.get_population().champion_x)
        list_of_champion_f.append(island.get_population().champion_f)

    print('Evolution finished')


TBC.

