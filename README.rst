================================
Python Package Skeleton Template
================================

This is a **project skeleton template** for a **Python project/library**. The repository intents to implement and explain the latest best practices in team software development, continuous integration and deployment. The repository simulates the implementation of a :code:`sampleproject`.

You will find in the `project's documentation`_ all references that motivated the current configuration as well as detailed explanation on the different configuration files.

I intent to keep this repository up to date to my knowledge and needs. Your feedback and suggestions are highly appreciated, please raise an `issue`_ and share your thoughts.

.. start-badges

.. image:: https://github.com/joaomcteixeira/python-project-skeleton/workflows/CI/badge.svg?branch=master
   :target: https://github.com/joaomcteixeira/python-project-skeleton/actions?workflow=CI
   :alt: CI Status

.. image:: https://codecov.io/gh/joaomcteixeira/python-project-skeleton/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/joaomcteixeira/python-project-skeleton
    :alt: Codecov master branch

.. image:: https://img.shields.io/coveralls/github/joaomcteixeira/python-project-skeleton/master?label=COVERALLS&logo=COVERALLS
    :target: https://coveralls.io/github/joaomcteixeira/python-project-skeleton
    :alt: Coveralls master

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

Motivation
==========

Understand and implement in the best practices in software development and deployment for scientific software; actually I think the strategy reviewed here can be applied at many other development contexts.

This repository does NOT intent to be a `cookiecutter`_-like repository. Thought there are many and very well documented cookiecutter templates out there, `even for scientific software`_, I felt that directly using a cookiecutter would lead me nowhere because I would miss the whole understanding of what the cookiecutter is automatizing in the first place. Therefore, building a repository from scratch was the only and best approach to achieve a minimum understanding of best practices and protocols.

Acknowledgments
===============

The whole repository structure and CI layout has strongly influenced by the discussions provided by `ionel`_ in his `blog post`_ about *Packaging a python library*. I really recommend reading through that post and the other related posts in his blog. Hence, `python-nameless`_ and `cookiecutter-pylibrary`_ are two repositories that served as main source of information for the *python-project-skeleton* repository; other sources of information were also important and those are referenced within context.

Version
=======

v0.2.1

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
