Python Project Layout
---------------------

The file structure for this Python project follows the ``src``, ``tests``,
``docs`` and ``devtools`` folders layout.

The src layout
~~~~~~~~~~~~~~

I discovered storing the project's source code underneath a ``src`` directory
layer instead of directly in the project's root folder is one of the most
controversial discussions regarding the organization of Python projects. Here, I
adopted the ``src``-based layout discussed by `ionel`_ in his `blog post`_.
After more than one year of using ``src``, I have nothing to complain about; on
the contrary, it saved many issues related to ``import`` statements. Either
importing from the repository or the installed version? The ``src`` guarantees
stable imports. More on ionel's blog (see also `src-nosrc example`_).

The ``src/sampleproject`` folder hosts the actual source of the project. In the
current version of this template, I don't discuss how to organize a source code
of a project. I am looking forward doing that in future versions.

Testing
~~~~~~~

Here, tests are encapsulated in a separate ``tests`` folder. With this
encapsulation, outside the main library folder, it is easier to control that
tests do not import from relative paths and can only access the library code
after library installation (regardless of the installation mode). Also, having
``tests`` in a separated folder facilitates the configuration files layout on
excluding tests from deployment (``MANIFEST.in``) and code quality
(``.codacy.yaml``) or coverage (``.coveragerc``).

Documentation
~~~~~~~~~~~~~

All documentation related files are stored in a ``docs`` folder. Files in
``docs`` will be compiled using Sphinx to generate the HTML documentation web
pages. You can follow the file and folder structure in this repository as an
example of how to assemble the documentation. You will see files that contain
text and others that import text from relative files. The latter strategy avoids
repeating information.

devtools
~~~~~~~~

The ``devtools`` folder hosts the files related to development. In this case, I
used the idea explained by `Chodera Lab`_ in their `structuring your project`_
guidelines.

.. _ionel: https://github.com/ionelmc
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _src-nosrc example: https://github.com/ionelmc/python-packaging-blunders
.. _Chodera lab: https://github.com/choderalab
.. _structuring your project: https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md
