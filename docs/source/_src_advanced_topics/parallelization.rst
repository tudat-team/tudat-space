.. _`parallelization`:

***************************
Parallelization with Python
***************************

This file is an introduction to the realm of parallelization, and specifically for use with tudatpy. Tudatpy has many
applications and many can be parallelized. For parallelization specifically in combination with PyGMO, further reading
is available under :ref:`parallelization_with_pygmo`.

.. contents:: Content of this page
   :local:


General parallelization with Python
####################################

In Python, you can parallelize data processing in various ways. One possible way is to use GPU's, but this is not
discussed here. For Python CPU-based parallelization, there are generally two types: multi-processing and
multi-threading. Multi-processing is a method that initializes multiple processes. This means that different processes
are running on independent CPU's, with independent memory management. Multi-threading is a method that uses multiple
threads for a single parent process with shared memory. Child processes can be run on separate threads. There are
generally two threads per CPU, and each computer system has their own amount of CPU's with their own specs. The amount
of parallellity is therefore determined by the system you want to run on.

It should be noted that it does not always make sense to parallelize your simulations. The initialization of parallel
tasks takes longer, so there is a break even point beyond which it is worthwhile, shown in :ref:`multi_threading_with_batch_fitness_evaluation`. To enable parallel behavior with Python, the ``multiprocessing`` module is used. Other
alternatives exist as well that are more modern, but they are not as widely spread or as thoroughly documented. Ray, for
instance, is one of these packages, it is arguably more seamless, but it is also rather new and focused on AI
applications.

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

.. use manually synchronized tabs instead of tabbed code to allow dropdowns
.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. code-block:: python

            import multiprocessing as mp
            import numpy as np

            from tudatpy.kernel.numerical_simulation import environment_setup, propagation_setup
            from tudatpy.kernel.interface import spice

      .. literalinclude:: /_src_snippets/simulation/parallelization/general_bfe_example.py
         :language: python

   .. tab-item:: C++
      :sync: cpp
         
      .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
         :language: cpp


.. note::

    The memory will be freed only after all the outputs are collected. It may be wise to split the list of
    inputs into smaller batches in case a high number of simulations are run, to avoid overflowing the memory.

.. seealso::
    Other ways to specify the context or create a Pool object are also possible, more can be read on `the multiprocessing
    documentation page <https://docs.python.org/3/library/multiprocessing.html>`_.

Batch Fitness Evaluation for Monte-Carlo analysis
#################################################

In this section, the basic structure is presented that can allow for a simple, parallel Monte-Carlo analysis of any
problem. An astrodynamics example is used for obvious reasons: the :ref:`Kepler satellite orbit
</_src_getting_started/_src_examples/tudatpy-examples/propagation/keplerian_satellite_orbit.ipynb>`. Using
this, we can change any parameter, let the Monte-Carlo simulations run in parallel, and enjoy the power.

BFE Monte Carlo code structure
------------------------------

In the snippet below, the implementation can be seen. It is straightforward, and looks surprisingly similar to
`General parallelization with Python`_. The ``run_simulation()`` function is shown below as ``run_dynamics()``. The
same concepts are applied, but rather than two integers being returned without further calculations, the inputs are the
Semi-major Axis and Eccentricity elements of the initial state which has a profound influence on the final results of
the orbit. 

.. use manually synchronized tabs instead of tabbed code to allow dropdowns
.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. code-block:: python

            # Load bfe modules
            import multiprocessing as mp

            # Load standard modules
            import numpy as np
            from matplotlib import pyplot as plt

            # Load tudatpy modules
            from tudatpy.kernel.interface import spice
            from tudatpy.kernel import numerical_simulation
            from tudatpy.kernel.numerical_simulation import environment_setup, propagation_setup
            from tudatpy.kernel.astro import element_conversion
            from tudatpy.kernel import constants
            from tudatpy.util import result2array

      .. literalinclude:: /_src_snippets/simulation/parallelization/mc_bfe_run.py
         :language: python

   .. tab-item:: C++
      :sync: cpp
         
      .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
         :language: cpp

The basic BFE structure can be seen above. Below the ``run_dynamics()`` function is shown, which is almost identical to
code from the :ref:`Kepler satellite orbit
</_src_getting_started/_src_examples/tudatpy-examples/propagation/keplerian_satellite_orbit.ipynb>`, with the small
adjustment that the initial state definition is given by the input arguments to the function rather than defined
manually.

.. use manually synchronized tabs instead of tabbed code to allow dropdowns
.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. code-block:: python

            # Load bfe modules
            import multiprocessing as mp

            # Load standard modules
            import numpy as np
            from matplotlib import pyplot as plt

            # Load tudatpy modules
            from tudatpy.kernel.interface import spice
            from tudatpy.kernel import numerical_simulation
            from tudatpy.kernel.numerical_simulation import environment_setup, propagation_setup
            from tudatpy.kernel.astro import element_conversion
            from tudatpy.kernel import constants
            from tudatpy.util import result2array

      .. literalinclude:: /_src_snippets/simulation/parallelization/mc_bfe_dynamics.py
         :language: python

   .. tab-item:: C++
      :sync: cpp
         
      .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
         :language: cpp


BFE Monte Carlo results
-----------------------

Regarding the performance of the BFE, a few results are shown in the table below. Once again, a substantial improvement
is observed when conducting Monte Carlo analyses using tudatpy. 

.. note::

   These simulations are tested on macOS Ventura 13.1 with a 3.1 GHz Quad-Core Intel Core i7 processor only. Four cores
   (CPU's) are used during the BFE.

+-----------------------+---------------------------+---------------+----------------+--------------------+
| Number of experiments | Batch Fitness Evaluation  | CPU time [s]  | CPU usage [-]  | Clock time [s]     |
+=======================+===========================+===============+================+====================+
| 500                   | no                        | 107.94        | 99%            | 110.51             |
|                       +---------------------------+---------------+----------------+--------------------+
|                       | yes                       | 118.07        | 381%           | 32.07              |
+-----------------------+---------------------------+---------------+----------------+--------------------+
| 2000                  | no                        | 443.83        | 99%            | 457.35             |
|                       +---------------------------+---------------+----------------+--------------------+
|                       | yes                       | 475.32        | 385%           | 127.11             |
+-----------------------+---------------------------+---------------+----------------+--------------------+

.. note::

    Other applications are possible and may be documented in the future. If you happen to implement any yourself, feel
    free to contact the developers or open a pull-request.

