================================
Python Package Skeleton Template
================================

.. image:: https://github.com/joaomcteixeira/python-project-skeleton/workflows/Tests/badge.svg?branch=master
    :target: https://github.com/joaomcteixeira/python-project-skeleton/actions?workflow=Tests
    :alt: Test Status

.. image:: https://github.com/joaomcteixeira/python-project-skeleton/workflows/Package%20Build/badge.svg?branch=master
    :target: https://github.com/joaomcteixeira/python-project-skeleton/actions?workflow=Package%20Build
    :alt: Package Build

.. image:: https://codecov.io/gh/joaomcteixeira/python-project-skeleton/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/joaomcteixeira/python-project-skeleton
    :alt: Codecov

.. image:: https://img.shields.io/codacy/grade/ae042ac066554bfab398024b0beea6a5/master?label=Codacy
    :target: https://app.codacy.com/manual/joaomcteixeira/python-project-skeleton/dashboard
    :alt: Codacy

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
=======

This repository is a **skeleton template** for a **Python application/library** compliant with the latest team-development and software deployment practices within a continuous integration (CI) framework. It can be used as a source of information/study to emulate or as a direct template for your repositories. **Note** I can't cover all strategies available in the wild. This repository reflects the setup I like the most and covers the CI needs of my Python projects, which includes:

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
==========

To understand and implement the best practices for team-based development and automatic deployment of scientific software in Python. Also, I believe the strategy reviewed here can be applied to most general-purpose Python libraries.

This repository does **not** intend to be a `cookiecutter`_-like repository. There are very well documented cookiecutters, `even for scientific software`_, if you are looking for one of those.

When I started developing Python libraries, I decided that using a cookiecutter as a shortcut would lead me nowhere in the learning process of configuring CI services because I would miss the details of what was actually being implemented. Hence, assembling this *template* from scratch as a full working repository was the only best approach to achieve a minimum understanding of CI. Now, this repository serves as a reference guide for all my projects and hopefully will serve you too. I try to keep it up to date with my needs and the ever-evolving CI ecosystem.

Acknowledgments
===============

I want to acknowledge `ionel`_ discussions about *Packaging a python library*. They are a pillar in my understanding and decisions on this matter, and I really recommend reading his `blog post`_ and references herein.

I configured the CI pipeline to my needs by taking bits and pieces from many places. Kudos to `python-nameless`_ and `cookiecutter-pylibrary`_; two primary sources of information for the *python-project-skeleton* repository, especially in the first versions using Travis and Appveyor. When migrating to GitHub Actions, I fed on the workflows `@JoaoRodrigues <https://python-project-skeleton.readthedocs.io/>`_ assembled for `pdb-tools`_; on the `tox-gh-actions`_ package; and on `structlog`_, which was also a repository I used as a reference to build test latest version here.

I refer to other important sources of information as comments in the specific files. Thanks, everyone, for keeping discussions out there open.

How to use this repository
==========================

The `documentation`_ pages explain how to use this template for your projects and the implementation details adopted here. Use the documentation as a reference to learn the rationale behind this repository and also as a demonstration of how to deploy documentation in ReadTheDocs.

Issues and Discussions
======================

As usual in any GitHub based project, raise an `issue`_ if you find any bug or room for improvement (certainly there are many), or open a `discussion`_ (new feature!!) if you want to discuss or talk :-)

Version
=======

v0.8.1

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
.. _pdb-tools: https://github.com/haddocking/pdb-tools
.. _project's documentation: https://python-project-skeleton.readthedocs.io/en/latest/index.html
.. _pytest: https://docs.pytest.org/en/stable/
.. _python-nameless: https://github.com/ionelmc/python-nameless
.. _structlog: https://github.com/hynek/structlog
.. _test.pypi.org: https://test.pypi.org
.. _tox-gh-actions: https://github.com/ymyzk/tox-gh-actions
.. _tox: https://tox.readthedocs.io/en/latest/
.. _ReadTheDocs: https://readthedocs.org/
