*********************************
Post-processing Results in Python
*********************************

The ``tudat`` C++ libraries were build around the use of a ``std::map<double, Eigen::vectorXd>`` as the data type of the
state and dependent variable histories. In Python, this is returned as a ``dict[float, np.ndarray]``.

.. code-block::

    # ...

    # Create simulation object and propagate dynamics.
    dynamics_simulator = propagation_setup.SingleArcDynamicsSimulator(
        bodies,
        integrator_settings,
        propagator_settings,
        True
    )
    state_history = dynamics_simulator.state_history

The returned data type from the simulator is returned as (for a single translational popagation):

.. code-block::

    state_history = {
        t[0]: np.array([pos_x[0], pos_y[0], pos_z[0], vel_x[0], vel_y[0], vel_z[0]]),
        t[1]: np.array([pos_x[1], pos_y[1], pos_z[1], vel_x[1], vel_y[1], vel_z[1]]),
        t[2]: np.array([pos_x[2], pos_y[2], pos_z[2], vel_x[2], vel_y[2], vel_z[2]]),
        # ...
        t[-1]: np.array([pos_x[-1], pos_y[-1], pos_z[-1], vel_x[-1], vel_y[-1], vel_z[-1]]),
    }

.. note::

    ``vel`` is a shortening of "velocity" & ``pos`` is a shortening of "position".


Using NumPy Arrays
==================

Converting simulator results to ``numpy.ndarray``
-------------------------------------------------

The provided utility ``result2array`` converts the ``dict[float, numpy.ndarray]`` to a ``numpy.ndarray`` as:

.. code-block::

    # Required: Import for result conversion.
    # from tudatpy.util import result2array

    # the use of the utility function:
    states_array = result2array(state_history)

This returns the equivalent expanded expression:

.. code-block::

    states_array = np.array([
        [t[0], pos_x[0], pos_y[0], pos_z[0], vel_x[0], vel_y[0], vel_z[0]],
        [t[1], pos_x[1], pos_y[1], pos_z[1], vel_x[1], vel_y[1], vel_z[1]],
        [t[2], pos_x[2], pos_y[2], pos_z[2], vel_x[2], vel_y[2], vel_z[2]],
        # ...
        [t[-1], pos_x[-1], pos_y[-1], pos_z[-1], vel_x[-1], vel_y[-1], vel_z[-1]],
    ])

Subset observations from a ``numpy.ndarray``
--------------------------------------------

The following examples deal with specific cases that may arise during post-processing of simulator results.
In some cases, you may wish to combine multiple examples for your desired processing step.

1. Extract state/dependent variables at a given time point:

.. code-block:: python

    t_0_state = states_array[states_array[:, 0] == 0] # returns a 2d array with one row

    t_0_state = t_0_state[0] # extracts a 1d array from the 2d array

    t_0_state = t_0_state[1:] # slices the array, ignoring the time value

As a one-liner:

.. code-block:: python

    t_0_state = states_array[states_array[:, 0] == 0][0][1:0]

2. Extract state/dependent variables within a time period:

.. code-block:: python

    t_start = 100
    t_end = 1000
    t_period_array = states_array[(states_array[:, 0] > t_start) & (states_array[:, 0] < t_end)]

Converting simulator results to ``numpy.ndarray``
-------------------------------------------------

Using pandas DataFrames
=======================

.. tip::
    Download the ``pandas`` cheatsheet!
    :download:`pdf <_static/Pandas_Cheat_Sheet.pdf>`

Converting simulator results to ``pandas.DataFrame``
----------------------------------------------------

The following examples demonstrate how ``pandas`` can be used in post-processing of simulation results from ``tudatpy``.
The examples assume ``tutorial 1`` of ``tudatpy`` is being used. In this case, a single satellite translational state is propagated.

.. code-block:: python

    from tudatpy.util import result2array
    import pandas as pd

    # the use of the utility function:
    df = pd.DataFrame(data=result2array(state_history),
                      columns="t pos_x pos_y pos_x vel_x vel_y vel_z".split())

+------+-------+--------------+--------------+-------------+----------+------------+----------+
|      |     t |        pos_x |        pos_y |       pos_z |    vel_x |      vel_y |    vel_z |
+======+=======+==============+==============+=============+==========+============+==========+
|    0 |     0 |  7.03748e+06 |  3.23806e+06 | 2.15072e+06 | -1465.66 |   -40.9584 |  6622.8  |
+------+-------+--------------+--------------+-------------+----------+------------+----------+
|    1 |    10 |  7.02256e+06 |  3.23753e+06 | 2.21687e+06 | -1519.53 |   -65.7719 |  6606.06 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+
|    2 |    20 |  7.00709e+06 |  3.23674e+06 | 2.28284e+06 | -1573.2  |   -90.5372 |  6588.85 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+
| ...  | ...   | ...          | ...          | ...         | ...      | ...        | ...      |
+------+-------+--------------+--------------+-------------+----------+------------+----------+
| 8638 | 86380 | -4.46865e+06 | -1.38981e+06 | 6.07194e+06 | -4630.32 | -2437.64   | -4843.76 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+
| 8639 | 86390 | -4.51475e+06 | -1.41413e+06 | 6.02323e+06 | -4590.52 | -2425.21   | -4897.34 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+
| 8640 | 86400 | -4.56045e+06 | -1.43832e+06 | 5.97399e+06 | -4550.21 | -2412.54   | -4950.63 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+


Printing the DataFrame will output:

.. code-block:: bash

    >> print(df)

                t         pos_x  ...        vel_y        vel_z
    0         0.0  7.037484e+06  ...   -40.958395  6622.797609
    1        10.0  7.022558e+06  ...   -65.771910  6606.061690
    2        20.0  7.007094e+06  ...   -90.537171  6588.849542
    3        30.0  6.991095e+06  ...  -115.252840  6571.163857
    4        40.0  6.974562e+06  ...  -139.917596  6553.007326
    ...       ...           ...  ...          ...          ...
    8636  86360.0 -4.375255e+06  ... -2461.730180 -4735.762481
    8637  86370.0 -4.422146e+06  ... -2449.807206 -4789.899972
    8638  86380.0 -4.468646e+06  ... -2437.635419 -4843.761214
    8639  86390.0 -4.514750e+06  ... -2425.214496 -4897.340123
    8640  86400.0 -4.560454e+06  ... -2412.544139 -4950.630569

Adjusting the print options of a  ``pandas.DataFrame``
------------------------------------------------------

The print of the DataFrame can be adjusted using the following (adjust the values as needed):

.. code-block:: python

    import pandas as pd
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

.. code-block:: bash

    >> print(df)

                t         pos_x         pos_y         pos_x        vel_x        vel_y        vel_z
    0         0.0  7.037484e+06  3.238059e+06  2.150724e+06 -1465.657627   -40.958395  6622.797609
    1        10.0  7.022558e+06  3.237525e+06  2.216869e+06 -1519.533718   -65.771910  6606.061690
    2        20.0  7.007094e+06  3.236744e+06  2.282844e+06 -1573.199711   -90.537171  6588.849542
    3        30.0  6.991095e+06  3.235715e+06  2.348644e+06 -1626.653078  -115.252840  6571.163857
    4        40.0  6.974562e+06  3.234439e+06  2.414266e+06 -1679.891319  -139.917596  6553.007326
    ...       ...           ...           ...           ...          ...          ...          ...
    8636  86360.0 -4.375255e+06 -1.340820e+06  6.167734e+06 -4708.356140 -2461.730180 -4735.762481
    8637  86370.0 -4.422146e+06 -1.365378e+06  6.120105e+06 -4669.596584 -2449.807206 -4789.899972
    8638  86380.0 -4.468646e+06 -1.389815e+06  6.071937e+06 -4630.319239 -2437.635419 -4843.761214
    8639  86390.0 -4.514750e+06 -1.414129e+06  6.023231e+06 -4590.524624 -2425.214496 -4897.340123
    8640  86400.0 -4.560454e+06 -1.438318e+06  5.973991e+06 -4550.213316 -2412.544139 -4950.630569


Subset observations from a ``pandas.DataFrame``
-----------------------------------------------

Adding dependent columns to a  ``pandas.DataFrame``
---------------------------------------------------

.. code-block:: python

    # the use of the utility function:
    df["r"] = np.sqrt(np.square(df[["pos_x", "pos_y", "pos_z"]]).sum(axis=1))


+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+
|      |     t |        pos_x |        pos_y |       pos_z |    vel_x |      vel_y |    vel_z |           r |
+======+=======+==============+==============+=============+==========+============+==========+=============+
|    0 |     0 |  7.03748e+06 |  3.23806e+06 | 2.15072e+06 | -1465.66 |   -40.9584 |  6622.8  | 8.0397e+06  |
+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+
|    1 |    10 |  7.02256e+06 |  3.23753e+06 | 2.21687e+06 | -1519.53 |   -65.7719 |  6606.06 | 8.0444e+06  |
+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+
|    2 |    20 |  7.00709e+06 |  3.23674e+06 | 2.28284e+06 | -1573.2  |   -90.5372 |  6588.85 | 8.04905e+06 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+
| ...  | ...   | ...          | ...          | ...         | ...      | ...        | ...      | ...         |
+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+
| 8638 | 86380 | -4.46865e+06 | -1.38981e+06 | 6.07194e+06 | -4630.32 | -2437.64   | -4843.76 | 7.66608e+06 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+
| 8639 | 86390 | -4.51475e+06 | -1.41413e+06 | 6.02323e+06 | -4590.52 | -2425.21   | -4897.34 | 7.65912e+06 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+
| 8640 | 86400 | -4.56045e+06 | -1.43832e+06 | 5.97399e+06 | -4550.21 | -2412.54   | -4950.63 | 7.65213e+06 |
+------+-------+--------------+--------------+-------------+----------+------------+----------+-------------+

Outputting a LaTeX table from a ``pandas.DataFrame``
----------------------------------------------------

.. code-block:: python

    print(pd.concat([df.head(3), df.tail(3)]).to_latex())

.. code-block:: latex

    \begin{tabular}{lrrrrrrrr}
    \toprule
    {} &        t &         pos_x &         pos_y &         pos_z &        vel_x &        vel_y &        vel_z &             r \\
    \midrule
    0    &      0.0 &  7.037484e+06 &  3.238059e+06 &  2.150724e+06 & -1465.657627 &   -40.958395 &  6622.797609 &  8.039703e+06 \\
    1    &     10.0 &  7.022558e+06 &  3.237525e+06 &  2.216869e+06 & -1519.533718 &   -65.771910 &  6606.061690 &  8.044402e+06 \\
    2    &     20.0 &  7.007094e+06 &  3.236744e+06 &  2.282844e+06 & -1573.199711 &   -90.537171 &  6588.849542 &  8.049053e+06 \\
    8638 &  86380.0 & -4.468646e+06 & -1.389815e+06 &  6.071937e+06 & -4630.319239 & -2437.635419 & -4843.761214 &  7.666081e+06 \\
    8639 &  86390.0 & -4.514750e+06 & -1.414129e+06 &  6.023231e+06 & -4590.524624 & -2425.214496 & -4897.340123 &  7.659115e+06 \\
    8640 &  86400.0 & -4.560454e+06 & -1.438318e+06 &  5.973991e+06 & -4550.213316 & -2412.544139 & -4950.630569 &  7.652129e+06 \\
    \bottomrule
    \end{tabular}
