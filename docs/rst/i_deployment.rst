Deployment
----------

Deployment of the Python package is automated using `Github actions`_.
The YML file configure the workflow `is here`_. The idea of this implementation
is to support an agile development framework where every new commit to the `master` or `latest`,
depending on the maintainer preferences is automatically deployed as a new package version
in PyPI.

.. _Github actions: https://docs.github.com/en/actions
.. _is here: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.github/workflows/python-publish.yml
