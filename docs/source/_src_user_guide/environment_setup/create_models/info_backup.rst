.. class:: Exponential Atmosphere

   Custom wind models can be created via the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_wind_model` function.


  Simple atmosphere model independent of time, latitude and longitude based on an exponentially decaying density profile with a constant temperature and composition.

  For example for an exponential atmosphere with a scale height of 7200 m, a constant temperature of 290 K, a density at 0 m altitude of 1.225 kg/m^3 and a specific gas constant of 287.06 J/(kg K):

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/exponential_atmosphere.py
             :language: python

          .. toggle-header::
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/exponential_atmosphere.cpp
               :language: cpp

  The value of pressure is computed by assuming hydrostatic equilibrium, whereas temperature, gas constant and the ratio of specific heats are assumed to be constant.

  For cases where only the atmospheric density is relevant, you can use:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/exponential_atmosphere.py
             :language: python

          .. toggle-header::
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

               :language: cpp

  When using this interface, all other properties are set to NaN, and it is not possible to extract any other property besides the density from the atmosphere model.




.. class:: Tabulated Atmosphere

  Due to the extensive customization available for the tabulated atmosphere, you can find the settings for this class in a separate page: (coming soon) :ref:`tabulated-atmosphere-settings`.



Time-variations of the Gravity Field
####################################

Unlike most other environment models, gravity field variations are provided as a *list* for a single body: multiple gravity field variation settings may be defined. Their summation is then applied to the spherical harmonic gravity field.

.. class:: Basic Solid Body Gravity Field Variation

  Variations of the gravity field due to solid body tides, using the model provide (for instance) by `Eq. 6.6 of this document <https://www.iers.org/SharedDocs/Publikationen/EN/IERS/Publications/tn/TechnNote36/tn36_079.pdf?__blob=publicationFile&v=1>`_). Several options, using various levels of simplification, can be used:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/gravity_field_tides_simple.py
             :language: python

          .. toggle-header::
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

             :language: cpp

  This interface defines a single Love number for a full degree. Specifically, the above case computes tides raised by the Moon, for the case where :math:`k_{2}=k_{20}=k_{21}=k_{22}=0.3`. The ``love_number`` variable may be provided as a float or complex type.

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/gravity_field_tides_multiple_degrees.py
             :language: python

          .. toggle-header::
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

             :language: cpp

  This interface defines a separate Love number for multiple full degrees. Specifically, the above case computes tides raised by the Moon, for the case where :math:`k_{2}=k_{20}=k_{21}=k_{22}=0.3` and :math:`k_{3}=k_{30}=k_{31}=k_{32}=k_{33}=0.1`. The values of :math:`k_{2}` and :math:`k_{3}`  may be provided as a float or complex type.

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/gravity_field_tides_multiple_orders.py
             :language: python

          .. toggle-header::
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

             :language: cpp

  This interface defines a separate Love number at each order for a single degree. the above case computes tides raised by the Moon :math:`k_{20}=0.31`, :math:`k_{21}=0.305` and :math:`k_{22}=0.308`. The entries of ``love_numbers`` may be provided as a float or complex type.


.. class:: Tabulated Gravity Field Variation

  Variations in spherical harmonic coefficients tabulated as a function of time.

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/tabulate_gravity_variations.py
             :language: python

          .. toggle-header::
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

             :language: cpp

  where the ``cosine_variations_table``  and ``sine_variations_table`` variables contain the tabulated data for the variations of the spherical harmonic coefficients. Both are dictionaries (keys: floats representing time - values: numpy arrays, size :math:`N\times M`, representing variation in gravity field coefficients at given time). Each value in these two dictionaries must be the same size array. The ``minimum_degree`` and ``minimum_degree`` inputs define how the data in the table is processed: they denote the degree and order of the variation that the (0,0) entry in each value in the dictionaries represent. For instance, for array sizes :math:`N=2` and :math:`M=3`, the above would provide variations in gravity field at degree 2 and 3 (up to order 3)



.. _environment_inertia_tensor:

Inertia Tensors
################

This section is WIP and will be updated soon.