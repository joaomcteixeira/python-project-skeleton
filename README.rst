================================
Python Package Skeleton Template
================================

.. start-badges

.. image:: https://github.com/joaomcteixeira/python-project-skeleton/workflows/CI/badge.svg?branch=master
:target: https://github.com/joaomcteixeira/python-project-skeleton/actions?workflow=CI
:alt: CI Status

.. image:: https://codecov.io/gh/joaomcteixeira/python-project-skeleton/branch/master/graph/badge.svg
:target: https://codecov.io/gh/joaomcteixeira/python-project-skeleton
:alt: Codecov master branch

.. image:: https://img.shields.io/codacy/grade/ae042ac066554bfab398024b0beea6a5/master?label=Codacy
:target: https://app.codacy.com/manual/joaomcteixeira/python-project-skeleton/dashboard
:alt: Codacy master branch

.. image:: https://api.codeclimate.com/v1/badges/d96cc9a1841a819cd4f5/maintainability
:target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton
:alt: Code Climate

.. image:: https://img.shields.io/codeclimate/tech-debt/joaomcteixeira/python-project-skeleton?label=Code%20Climate%20tech%20debt
:target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton
:alt: Code Climate technical debt

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/stable?label=Read%20the%20Docs
:target: https://python-project-skeleton.readthedocs.io/en/latest/index.html
:alt: Read the Docs

.. end-badges

Summary
=======

This is a **project skeleton template** for a **Python project/library**. This repository implements and explains the latest practices in team software development and deployment within a continuous integration framework. **Note** that is impossible for me to cover all strategies available in the wild. This repository covers the needs of my Python projects, which include:

* a robust Python library/application file hierarchy with packages, modules, clients
    * detailed, yet simple, ``setup.py``
    * the special use of the ``src`` directory
    * examples of Python command-line interfaces
* unique testing framework for developers with `tox`_ and `pytest`_
    * assures tests are reproducible across developers platforms
    * assures same lint rules are always applied
    * assures all desired Python versions are covered
* continuous integration with `GitHub Actions`_
    * automatic testing on Linux, MacOS, and Windows
    * automatic testing upon deployment with tox
    * test coverage report to `Codecov`_
    * automatic version bump with `bump2version`_
    * automatic git tagging and Python packaging to `PyPI`_

Motivation
==========

To understand and implement in the best practices in software development and deployment for scientific software. Actually, I believe the strategy reviewed here can be applied to most Python library projects.

This repository does **not** intent to be a `cookiecutter`_-like repository. Though there are many and very well documented cookiecutter templates out there, `even for scientific software`_, when I initiated my adventure in developing Python libraries I decided that using a cookiecutter would lead me to nowhere because I would miss what was actually being automatized. Hence, assembling this *template* repository from scratch was the only and best approach to achieve a minimum understanding of the best practices and protocols on the matter. Now, this repository serves as a reference guide for all my projects and I try to keep it up to date to my needs and changes in the CI ecosystem.

Acknowledgments
===============

The Python library organization itself was strongly influenced by `ionel`_ discussions in his `blog post`_ about *Packaging a python library*. I really recommend reading through that post and the related posts in his blog.

I setup the CI pipeline with bits from many places. Kudos to `python-nameless`_ and `cookiecutter-pylibrary`_ two repositories that served as main source of information for the *python-project-skeleton* repository, specially in the first versions with Travis and Appveyor.

When migrating to GitHub Actions, I want to thank `Joao Rodrigues`_ for the workflows in `pdb-tools`_, ``ymyzk`` for the `tox-gh-actions`_ package, and `structlog`_, which was also a repository I used as a reference to build test latest version here.

I reference other important sources of information as comments in the specific files. Thanks everyone for keeping discussions out there open.

How to use this repository
==========================

The repository simulates the implementation of a :code:`sampleproject`. Here, ``sampleproject`` is the Python name of your project, that which will be `import sampleproject`. So everywhere you find ``sampleproject`` just replace with the name of your project.

In ``setup.py`` the project has the name ``jmct-sampleproject`` because ``sampleprojet`` was already in use in `test.pypi.org`_, as expected. Substitute that by the name of you package. Normally, it as the same name as ``sampleproject``.

You will find in the `project's documentation`_ all references that motivated the current configuration as well as detailed explanation on the different configuration files.

I intent to keep this repository up to date to my knowledge and needs. Your feedback and suggestions are highly appreciated, please raise an `issue`_ and share your thoughts.

Version
=======

v0.2.2

.. _project's documentation: https://python-project-skeleton.readthedocs.io/en/latest/index.html
.. _issue: https://github.com/joaomcteixeira/python-project-skeleton/issues
.. _master branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/master
.. _latest branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/latest
.. _python-nameless: https://github.com/ionelmc/python-nameless
.. _cookiecutter-pylibrary: https://github.com/ionelmc/cookiecutter-pylibrary
.. _even for scientific software: https://github.com/MolSSI/cookiecutter-cms
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/index.html
.. _ionel: https://github.com/ionelmc
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _pytest: https://docs.pytest.org/en/stable/
.. _GitHub Actions: https://github.com/features/actions
.. _Codecov: https://about.codecov.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _PyPI: https://pypi.org
.. _structlog: https://github.com/hynek/structlog
.. _tox-gh-actions: https://github.com/ymyzk/tox-gh-actions
.. _pdb-tools: https://github.com/haddocking/pdb-tools
.. _Joao Rodriges: https://github.com/JoaoRodrigues
.. _test.pypi.org: https://test.pypi.org
