================================
Python Package Skeleton Template
================================

This is a **project skeleton template** for a **Python project/library**. The repository intents to implement the latest best practices in team software development, continuous integration and deployment.

You will find in the `project's documentation`_ all references that motivated the current configuration as well as detailed explanation on the different configuration files.

I intent to keep this repository up to date to my knowledge and needs. Your feedback and suggestions are highly appreciated, please raise an `issue`_ and share your thoughts.

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

.. image:: https://img.shields.io/coveralls/github/joaomcteixeira/python-project-skeleton/master?label=COVERALLS&logo=COVERALLS
    :target: https://coveralls.io/github/joaomcteixeira/python-project-skeleton
    :alt: Coveralls master

.. image:: https://img.shields.io/codacy/grade/ae042ac066554bfab398024b0beea6a5/master?label=Codacy
    :target: https://app.codacy.com/manual/joaomcteixeira/python-project-skeleton/dashboard
    :alt: Codacy master branch

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/stable?label=Read%20the%20Docs
    :target: https://python-project-skeleton.readthedocs.io/en/stable/index.html
    :alt: Read the Docs (stable)


The stable version is hosted at the `master branch`_.

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
    :alt: Coveralls latest

.. image:: https://img.shields.io/codacy/grade/ae042ac066554bfab398024b0beea6a5/latest?label=Codacy
    :target: https://app.codacy.com/manual/joaomcteixeira/python-project-skeleton/dashboard
    :alt: Codacy latest grade

.. image:: https://api.codeclimate.com/v1/badges/d96cc9a1841a819cd4f5/maintainability
   :target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton
   :alt: Code Climate

.. image:: https://img.shields.io/codeclimate/tech-debt/joaomcteixeira/python-project-skeleton?label=Code%20Climate%20tech%20dept
    :target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton
    :alt: Code Climate technical debt

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/latest?label=Read%20the%20Docs
    :target: https://python-project-skeleton.readthedocs.io/en/latest/index.html
    :alt: Read the Docs (latest)

The latest build is hosted at the `latest branch`_.

Motivation
==========

Understand and implement in the best practices in software development and deployment for scientific software; actually I think the strategy reviewed here can be applied at many other development contexts.

This repository does NOT intent to be a `cookiecutter`_-like repository. Thought there are many and very well documented cookiecutter templates out there, `even for scientific software`_, I felt that directly using a cookiecutter would lead me nowhere because I would miss the whole understanding of what the cookiecutter is automatizing in the first place. Therefore, building a repository from scratch was the only and best approach to achieve a minimum understanding of best practices and protocols.

Acknowledgments
===============

The whole repository structure and CI layout has strongly influenced by the discussions provided by `ionel`_ in his `blog post`_ about *Packaging a python library*. I really recommend reading through that post and the other related posts in his blog. Hence, `python-nameless`_ and `cookiecutter-pylibrary`_ are two repositories that served as main source of information for the *python-project-skeleton* repository; other sources of information were also important and those are referenced within context.

Version
=======

v0.0.14

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
