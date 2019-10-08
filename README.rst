================================
Python Package Skeleton Template
================================

This is a skeleton template for a Python project aimed at distribution and continuous integration. The repository intents to implement the latest best practices in team software development, continuous integration and deployment.

You will find in this README all the references that motivated the current configuration.

I intent to keep this repository up to date to my knowledge and needs. To give your feedback or suggestion please raise an `issue`_.

Stable version
==============
.. image:: https://img.shields.io/travis/joaomcteixeira/python-project-skeleton/master?label=TravisCI
    :target: https://travis-ci.org/joaomcteixeira/python-project-skeleton
    :alt: Travis master branch

.. image:: https://ci.appveyor.com/api/projects/status/cqcy2f9s9a7jhh2b/branch/master?svg=true 
    :target: https://ci.appveyor.com/project/joaomcteixeira/python-project-skeleton
    :alt: Appveyor master branch

.. image:: https://codecov.io/gh/joaomcteixeira/python-project-skeleton/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/joaomcteixeira/python-project-skeleton
    :alt: Codecov master branch

.. image:: https://img.shields.io/codacy/grade/ae042ac066554bfab398024b0beea6a5/master?label=Codacy
    :target: https://app.codacy.com/manual/joaomcteixeira/python-project-skeleton/dashboard
    :alt: Codacy master branch

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/stable?label=Read%20the%20Docs
    :target: https://python-project-skeleton.readthedocs.io/en/stable/index.html
    :alt: Read the Docs (stable)


Stable version is hosted at the `master branch`_ and `tagged accordingly`.

Latest Build
============
.. image:: https://img.shields.io/travis/joaomcteixeira/python-project-skeleton/latest?label=TravisCI
    :target: https://travis-ci.org/joaomcteixeira/python-project-skeleton
    :alt: Travis-CI latest branch

.. image:: https://ci.appveyor.com/api/projects/status/cqcy2f9s9a7jhh2b?svg=true
    :target: https://ci.appveyor.com/project/joaomcteixeira/python-project-skeleton
    :alt: Appveyor-CI latest branch

.. image:: https://codecov.io/gh/joaomcteixeira/python-project-skeleton/branch/latest/graph/badge.svg
    :target: https://codecov.io/gh/joaomcteixeira/python-project-skeleton
    :alt: Codecov latest branch

.. image:: https://img.shields.io/coveralls/github/joaomcteixeira/python-project-skeleton/latest?label=COVERALLS&logo=COVERALLS
    :target: https://coveralls.io/github/joaomcteixeira/python-project-skeleton
    :alt: Coveralls

.. image:: https://img.shields.io/codacy/grade/ae042ac066554bfab398024b0beea6a5/latest?label=Codacy
    :target: https://app.codacy.com/manual/joaomcteixeira/python-project-skeleton/dashboard
    :alt: Codacy latest grade

.. image:: https://api.codeclimate.com/v1/badges/d96cc9a1841a819cd4f5/maintainability
   :target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton
   :alt: Code Climate

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/latest?label=Read%20the%20Docs
    :target: https://python-project-skeleton.readthedocs.io/en/latest/index.html
    :alt: Read the Docs (latest)

The latest build is hosted at the `latest branch`_.

Acknowledgments
===============

The whole repository structure and CI layout was strongly based on the discussions provided by `ionel`_ in his `blog post`_ about *Packaging a python library*. I really recommend reading through that post and the other related posts in his blog. `python-nameless`_ and `cookiecutter-pylibrary`_ are two repositories that served as main source of information for this template repositories; other sources of information were also important and those are referenced in context.

Motivation
==========

Understand and implement in my own projects the best practices in software development and deployment for scientific software.

This repository does NOT intent to be a `cookiecutter`_-like repository. Thought there are many and very well documented cookiecutter templates out there, `even for scientific software`_, I felt that directly using a cookiecutter would lead me nowhere because I would miss the whole understanding of what the cookiecutter is automatizing in the first place. Therefore, building a repository from scratch was the only and best approach to achieve a minimum understanding of best practices and protocols.

Repository organization
=======================

Two main branches set the development workflow: the `master branch`_ and the `latest branch`_. The latest branch is thought to evolve according to continuous integration practices, and is referred as the *latest* build or version; while, on the other hand, the *master branch* is considered the *stable* version. Under this configuration the *master* branch receives updates from the *latest* build periodically or when the projects feels an idea under development became solid.

Project Layout
==============

The project layout follow the ``src``, ``tests``, ``docs`` and ``devtools`` folders layout.

The src layout
--------------

As far as my readings went, storing the source library folder under a ``src`` directory instead of directly in the project's root is by far the most controversial point. Here I adopted the ``src``-based layout discussed by `ionel`_ in his `blog post`_. When reading through the discussed arguments, I found this strategy to have many advantages over the common root directory layout and no added disadvantage.

In detail, though encapsulating the source in a ``src`` directory is an uncommon practice in Python projects, adopting this practice avoids unexpected and uncontrolled code imports that could lead to wrong testing operations, as well stated by `ionel`_, see a `src-nosrc example`_. On the same hand, encapsulating the source under a ``src`` directory does not create any problems that would be avoided by the *standard* layout of having the source directly on a folder, usually named the same as the package name, in the root directory of the project.

tests
-----

Tests are nicely encapsulated in a ``tests`` folder. With this encapsulation, outside the library folder, it is easier to control that tests do not import from relative paths and can only access the library code after library installation (whatever the installation mode is). Also, having ``tests`` in a separated folder facilitates the configuration files layout on excluding tests from deployment (``MANIFEST.in`` and code quality (``codacy.yaml``).

docs
----

All documentation related files are stored in a ``docs`` folder. These include files related to the library documentation but also with the development process, such as: ``AUTHORS``, ``CONTRIBUTING``, ``CHANGELOG``, etc.

devtools
--------

Files related to development. Here I used the idea explained by `Chodera Lab`_ in their `structuring your project`_ guidelines, though for other issues I do not follow their guides, as explained in context.

Read the Docs
=============

Activate your project at `Read the Docs platform`_ (RdD), their web interface is easy enough to follow without further explanations. If your documentation is building under the `tox workflow`_ it will build in at Read the Docs.

Build version
-------------

By default, RdD has two main documentation versions (also called builds): the `latest`_ and the `stable`. The *latest* points to the `master branch`_ while the *stable* points to the `latest GitHub tag`_. Therefore, every time changes are pushed to the *master branch* a new build in the latest version of the documentation is created, while the stable version is built only when new tags are created.

However, for many projects it is desirable a different setup where the master branch holds the stable version, that is, the code referent to the latest tag, while another branch (usually named *latest* or *develop*) set to the repositories' default, holds the latest development code that has not yet been merged to the master and considered stable. This is the setup of this template repository. Under this setup, it is desirable that the documentation build referent to the *latest* version points to the `latest branch`, the *stable* doc build will always point to the latest tag. This can be edited in ``Admin`` -> ``Advanced Settings`` and ``Default version`` and ``Default branch``.

Google Analytics
----------------

Read the Docs allows straight forward implementation of Google Analytics tracking in the project documentation, just follow their instructions_.

Continuous Integration
======================

Continuous integration is key in software development projects. Applying these standards guarantees all developers follow the same testing routines and that such routines are also integrated in a online server that runs on each pull request sent to the project.

Uniform testing environment
---------------------------

To assure all developers are forced to the same testing routines, rules and environments, the project itself has to deploy a unified testing configuration; yet this is not straightforward. For Python projects, `Tox`_ comes to the rescue.

With **Tox** the testing setup can be defined in a configuration file, the `tox.ini`, which contains all the operations that are performed during the test phase. Therefore to run the tests developers just need to execute ``tox`` provided ``tox`` is installed in the developing Python environment.

One of the great advantages of using Tox, aside from uniforming the testing routines across developers, is that tests actually take place in isolated environments where the source code has been installed. In order others, tests are performed in an environment simulating post-deployment instead of a development environment. Under this setup, there is no need, in general cases, to deploy test scripts along with the actual source.

Version
=======

v0.0.9

.. _issue: https://github.com/joaomcteixeira/python-project-skeleton/issues
.. _ionel: https://github.com/ionelmc
.. _python-nameless: https://github.com/ionelmc/python-nameless
.. _cookiecutter-pylibrary: https://github.com/ionelmc/cookiecutter-pylibrary
.. _even for scientific software: https://github.com/MolSSI/cookiecutter-cms
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/index.html
.. _chodera lab: https://github.com/choderalab
.. _structuring your project: https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md
.. _src-nosrc example: https://github.com/ionelmc/python-packaging-blunders
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/ 
.. _tox workflow: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _tox ini: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _latest: https://python-project-skeleton.readthedocs.io/en/latest/
.. _stable: https://python-project-skeleton.readthedocs.io/en/stable/
.. _master branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/master
.. _latest branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/latest
.. _latest Github tag: https://github.com/joaomcteixeira/python-project-skeleton/tags
.. _Read the Docs platform: https://readthedocs.org/
.. _instructions: https://docs.readthedocs.io/en/stable/guides/google-analytics.html
