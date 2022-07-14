Python Package Skeleton Template
================================

.. image:: https://github.com/joaomcteixeira/python-project-skeleton/workflows/ci/badge.svg?branch=main
    :target: https://github.com/joaomcteixeira/python-project-skeleton/actions?workflow=ci
    :alt: CI

.. image:: https://codecov.io/gh/joaomcteixeira/python-project-skeleton/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/joaomcteixeira/python-project-skeleton
    :alt: Codecov

.. image:: https://api.codeclimate.com/v1/badges/d96cc9a1841a819cd4f5/maintainability
   :target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/codeclimate/tech-debt/joaomcteixeira/python-project-skeleton
    :target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton
    :alt: Code Climate technical debt

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/latest?label=Read%20the%20Docs
    :target: https://python-project-skeleton.readthedocs.io/en/latest/index.html
    :alt: Read the Docs

Summary
-------

This repository is a **skeleton template** for a **Python application/library**
compliant with the latest team-development and software deployment practices
within a continuous integration (CI) framework. You can use this repository as a
source of information and a resource to study CI. Also, you can use this
repository as a direct template for your repositories.

**Note** that this repository reflects the setup I like the most and that covers
the CI needs for my Python projects, which include:

* A robust Python library/application file hierarchy with packages, modules, clients, and documentation:
    * detailed, yet simple, ``setup.py``
    * retrievable ``README`` and ``CHANGELOG``
    * documentation deployed in `ReadTheDocs`_
    * the unusual adoption of the ``src`` directory layer (love it)
    * examples of packages and modules hierarchy
    * examples of Python command-line interfaces
* A unique testing framework for developers with `tox`_ and `pytest`_
    * guarantees tests are reproducible for all developers
    * ensures same lint rules are always applied (local and remotely)
    * ensures all desired Python versions are covered
    * adopts `hypothesis`_
* Fully automated continuous integration services with `GitHub Actions`_
    * automatic testing on Linux, MacOS, and Windows
    * automatic testing simulated upon deployment with ``tox``
    * test coverage report to Codecov
    * automated version bump with `bump2version`_, git tagging, and Python packaging to PyPI on Pull Request merge

Motivation
----------

I developed this repository to understand how to implement the best practices
for team-based development and automatic deployment of a scientific software
written in Python. Nonetheless, I believe the strategy reviewed here can be
applied to most general-purpose Python libraries.

This repository does **not** intend to be a `cookiecutter`_-like repository.
There are very well documented cookiecutters, `even for scientific software`_,
if you are looking for one of those. However, when I started developing Python
libraries, I decided that blindly using a cookiecutter would not provide me the
learning insights from configuring CI services because I would miss the details
of what was actually being implemented. Hence, assembling this *template* from
scratch as a full working repository was my best approach to obtain a useful
understanding of CI.  Now, this repository serves as a reference guide for all
my projects and hopefully will serve you, too. I keep constantly updating this
repository, expect one to two updates/reviews per year.

Acknowledgments
---------------

I want to acknowledge `ionel`_ discussions about *Packaging a python library*.
They are a pillar in my understanding and decisions on this matter, and I really
recommend reading his `blog post`_ and references herein.

I configured the CI pipeline to my needs by taking bits and pieces from many
places. Kudos to `python-nameless`_ and `cookiecutter-pylibrary`_; two primary
sources of information for the *python-project-skeleton* repository, especially
in the first versions using Travis and Appveyor.

When migrating to GitHub Actions, I based my choices on the version bump and
deploying workflows `@JoaoRodrigues <https://github.com/JoaoRodrigues>`_
assembled for `pdb-tools`_; on the `tox-gh-actions`_ package; and on
`structlog`_. Implementation details have evolved with newest versions.

I refer to other important sources of information as comments in the specific
files. Thanks, everyone, for keeping open discussions on internet.

How to use this repository
--------------------------

The `documentation`_ pages explain how to use this template for your projects
and the implementation details adopted here. The documentation pages also serve
to demonstrate how to compile documentation with Sphinx and deploy it online
with `ReadTheDocs`_.

Issues and Discussions
----------------------

As usual for any GitHub-based project, raise an `issue`_ if you find any bug or
want to suggest an improvement, or open a `discussion`_ if you want to discuss
or chat :wink:

Projects using this skeleton
----------------------------

Below, a list of the projects using this repository as template or as base for
their CI implementations:

* `julie-forman-kay-lab/IDPConformerGenerator <https://github.com/julie-forman-kay-lab/IDPConformerGenerator>`_
* `haddocking/HADDOCK3 <https://github.com/haddocking/haddock3>`_
* `THGLab/MCSCE <https://github.com/THGLab/MCSCE>`_
* `joaomcteixeira/taurenmd <https://github.com/joaomcteixeira/taurenmd>`_
* `MDAnalysis/mdacli <https://github.com/MDAnalysis/mdacli>`_

If you use this repository as a reference for your works, let me know, so I
list your work above, as well.

Version
-------

v0.11.1

.. _GitHub Actions: https://github.com/features/actions
.. _PyPI: https://pypi.org
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _bump2version: https://github.com/c4urself/bump2version
.. _cookiecutter-pylibrary: https://github.com/ionelmc/cookiecutter-pylibrary
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/index.html
.. _discussion: https://github.com/joaomcteixeira/python-project-skeleton/discussions
.. _documentation: https://python-project-skeleton.readthedocs.io/
.. _even for scientific software: https://github.com/MolSSI/cookiecutter-cms
.. _hypothesis: https://hypothesis.readthedocs.io/en/latest/
.. _ionel: https://github.com/ionelmc
.. _issue: https://github.com/joaomcteixeira/python-project-skeleton/issues
.. _latest branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/latest
.. _master branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/master
.. _pdb-tools: https://github.com/haddocking/pdb-tools/blob/2a070bbacee9d6608b44bb6d2f749beefd6a7690/.github/workflows/bump-version-on-push.yml
.. _project's documentation: https://python-project-skeleton.readthedocs.io/en/latest/index.html
.. _pytest: https://docs.pytest.org/en/stable/
.. _python-nameless: https://github.com/ionelmc/python-nameless
.. _structlog: https://github.com/hynek/structlog
.. _test.pypi.org: https://test.pypi.org
.. _tox-gh-actions: https://github.com/ymyzk/tox-gh-actions
.. _tox: https://tox.readthedocs.io/en/latest/
.. _ReadTheDocs: https://readthedocs.org/
