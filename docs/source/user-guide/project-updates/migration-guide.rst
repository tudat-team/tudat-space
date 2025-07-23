.. _migration-guide:

******************************
Migration Guide
******************************

TudatPy v1.0
-----------------

This section provides a guide for users migrating from TudatPy v0.9 and older to v1.0.

Have questions or feedback? As always, let us know in our `Github Discussion forum <https://github.com/orgs/tudat-team/discussions?discussions_q=>`_!

Installation
^^^^^^^^^^^^

How to obtain the new version: ...

New module structure
^^^^^^^^^^^^^^^^^^^^

Explain what was changed ...

Why was this needed?
===================

...

How does it effect users?
=========================

...

How to migrate?
====================

...


New ``Time`` type
^^^^^^^^^^^^^^^^^

Explain what was changed ...

Why was this needed?
===================

...

How does it affect users?
=========================

...

How to migrate?
====================

...


Merging of ``tudatpy`` repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The previous tudat-bundle structure (where tudat, tudatpy, and tudatpy-examples were maintained as separate repositories) has been simplified. The core tudat codebase is now included as a subdirectory within the tudatpy repository, which contains both the C++ source code and the Python bindings. The tudatpy-examples repository still exists, now as a submodule within tudatpy. The tudat-bundle repository has been deprecated and is effectively replaced by tudatpy.

The CMake configuration from tudat has been merged into the main CMakeLists.txt of tudatpy, resulting in a unified build system. The tudatpy repository now follows a mirrored structure: each component has its own tudat (for C++) and tudatpy (for Python) subdirectories. In general, the core logic is located in the tudat folders, while Python bindings and Python-only functionality are placed under the tudatpy folders.

Where files were previously duplicated or mirrored between tudat and tudatpy, they have now been consolidated—typically by keeping the version from tudatpy when the content was identical.

[WHAT ELSE IS WORTH MENTIONING, @ALFONSO? PERHAPS THE AZURE BUILD, and something else...]

Why was this needed?
===================
The decision to merge the tudat and tudatpy repositories was driven by the need to simplify development, testing, and packaging workflows. Maintaining them separately had become increasingly cumbersome, and the original motivation for the split no longer reflects how the project is used today.

Here are the main reasons behind the merge:

Simpler build process:
Previously, the tudat and tudatpy conda packages had to be built in sequence, which made the setup more fragile and added unnecessary overhead—especially for contributors and automated packaging.

More effective testing:
With separate repositories, the continuous integration pipelines were also split. This made it difficult to test changes to tudatpy until corresponding changes in tudat were merged, since the PRs weren’t linked. A single repo ensures all components can be tested together.

Reduced complexity:
Developers were expected to build from the tudat-bundle repository, even though the actual source code lived in tudat and tudatpy. This indirection often caused confusion, particularly for new contributors. The merge removes this extra layer.

Consistent configuration:
Maintaining separate build systems (CMake and conda feedstock) for two repositories sometimes led to inconsistencies or duplication of effort. A unified repo makes it easier to keep things aligned.

Changing usage patterns:
The repositories were originally split to support C++-only users. However, most users now rely on the Python interface. With the merged setup, C++-only workflows are still fully supported, but there's no longer a strong reason to keep the two codebases apart.

In short, the merge makes Tudat easier to work with, more robust to maintain, and better aligned with how it's actually used by the community.


How does it effect users?
=========================

The repository restructuring introduces a cleaner and more unified layout, but all core functionalities remain unchanged. Most users will continue working with tudatpy as before.

However, developers who were actively working on branches in the old tudat repository will need to migrate their work to the new combined repository. This typically involves rebasing or transplanting their changes into the appropriate location within the new structure (e.g. moving C++ code to the tudat/ subdirectory within tudatpy).

To preserve commit history and ensure smooth integration, we recommend carefully following the steps outlined in the "How to Migrate?" section below. If you encounter any issues or are unsure how to proceed, feel free to reach out to the core development team at [ADD EMAILS].

How to migrate?
====================
...

