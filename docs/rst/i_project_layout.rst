Python Project Layout
---------------------

The file structure for this Python project follows the ``src``, ``tests``, ``docs`` and ``devtools`` folders layout.

The src layout
~~~~~~~~~~~~~~

I discovered storing the project's source code underneath a ``src`` directory layer instead of directly in the project's root folder is one of the most controversial discussions regarding organization of Python projects. Here I adopted the ``src``-based layout discussed by `ionel`_ in his `blog post`_. After more than one year using ``src`` I have nothing to complain about, on the contrary, it saved many issues related with ``import`` statements. Are you importing from the repository? Are you importing the installed version? The ``src`` guarantees stable imports. More on ionel's blog (see also `src-nosrc example`_.

Testing
~~~~~~~

Tests are nicely encapsulated in a separate ``tests`` folder. With this encapsulation, outside the main library folder, it is easier to control that tests do not import from relative paths and can only access the library code after library installation (whatever the installation mode is). Also, having ``tests`` in a separated folder facilitates the configuration files layout on excluding tests from deployment (``MANIFEST.in``) and code quality (``.codacy.yaml``) or coverage (``.coveragerc``).

Documentation
~~~~~~~~~~~~~

All documentation related files are stored in a ``docs`` folder. These include all files related to the library documentation, as well as, development process, like: ``AUTHORS``, ``CONTRIBUTING``, ``CHANGELOG``, etc.

devtools
~~~~~~~~

The ``devtools`` folder hosts the files related to development. In this case, I used the idea explained by `Chodera Lab`_ in their `structuring your project`_ guidelines.

.. _ionel: https://github.com/ionelmc
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _src-nosrc example: https://github.com/ionelmc/python-packaging-blunders
.. _Chodera lab: https://github.com/choderalab
.. _structuring your project: https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md
