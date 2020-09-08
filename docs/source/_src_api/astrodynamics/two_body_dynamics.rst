=================
Two body dynamics
=================

Clohessy-Wiltshire
##################

Capture and Escape ΔV
#####################

.. tabs::

    .. tab:: Python

      .. toggle-header::
         :header: Required (Beginner) **Show/Hide**

          In this basic example, ``EARTH_R`` and ``EARTH_GM`` are parameters
          originating from the default ``tudat`` spice kernels.

          .. literalinclude:: ../../_src_snippets/astrodynamics/two_body_dynamics/req_capture_escape_beginner.py
             :language: python

      .. toggle-header::
         :header: Required (Advanced) **Show/Hide**

          More advanced users can interact directly with ``spice`` through the
          ``spiceypy`` package available on ``conda``. This library can be used
          to complement the internal ``cspice`` wrappings present in
          ``tudat``.

          .. literalinclude:: ../../_src_snippets/astrodynamics/two_body_dynamics/req_capture_escape_advanced.py
             :language: python

          .. note:: The use of the internal loading of ``spice`` kernels
             through ``tudat`` bindings does not make the kernel available
             for use through ``spiceypy``.

      .. literalinclude:: ../../_src_snippets/astrodynamics/two_body_dynamics/capture_escape.py
         :language: python

    .. tab:: C++

Gravity Assist ΔV
#################


Lambert Targeting
#################

.. tabs::

    .. tab:: Python

      .. toggle-header::
         :header: Required (Beginner) **Show/Hide**

          .. literalinclude:: ../../_src_snippets/astrodynamics/two_body_dynamics/req_lambert_targeter_beginner.py
             :language: python

      .. toggle-header::
         :header: Required (Advanced) **Show/Hide**

          .. literalinclude:: ../../_src_snippets/astrodynamics/two_body_dynamics/req_lambert_targeter_advanced.py
             :language: python

          .. note:: The use of the internal loading of ``spice`` kernels
             through ``tudat`` bindings does not make the kernel available
             for use through ``spiceypy``.

      .. literalinclude:: ../../_src_snippets/astrodynamics/two_body_dynamics/lambert_targeter.py
         :language: python

    .. tab:: C++
