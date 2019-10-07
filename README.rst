================================
Python Package Skeleton Template
================================

This is a skeleton template for a Python project aimed at distribution and continuous integration.

Stable version
==============

Stable version is hosted at the `master branch`_ and `tagged accordingly`.

.. image:: https://api.travis-ci.org/joaomcteixeira/python-project-skeleton.svg?branch=latest
    :target: https://travis-ci.org/joaomcteixeira/python-project-skeleton
    :alt: Travis-CI

.. image:: https://readthedocs.org/projects/python-project-skeleton/badge/?version=latest
    :target: https://python-project-skeleton.readthedocs.io/en/latest/index.html
    :alt: Documentation Status

Latest Build
============

The latest build is hosted at the `latest branch`_.


.. image:: https://api.travis-ci.org/joaomcteixeira/python-project-skeleton.svg?branch=master
    :target: https://travis-ci.org/joaomcteixeira/python-project-skeleton
    :alt: Travis-CI

.. image:: https://readthedocs.org/projects/python-project-skeleton/badge/?version=stable
    :target: https://python-project-skeleton.readthedocs.io/en/stable/index.html
    :alt: Documentation Status

.. image:: https://api.codeclimate.com/v1/badges/d96cc9a1841a819cd4f5/maintainability
   :target: https://codeclimate.com/github/joaomcteixeira/python-project-skeleton
   :alt: Maintainability

.. image:: https://api.codacy.com/project/badge/Grade/ae042ac066554bfab398024b0beea6a5?isInternal=true
   :target: https://app.codacy.com/manual/joaomcteixeira/python-project-skeleton/dashboard?bid=14602881
   :alt: Codacy Latest

Documentation
=============

Read the Docs
-------------

Activate your project at `Read the Docs platform`_ (RdD), their web interface is easy enough to follow without further explanations. If your documentation is building under the `tox workflow`_ it will build in at Read the Docs.

Build version
~~~~~~~~~~~~~

By default, RdD has two main documentation versions (also called builds): the `latest`_ and the `stable`. The *latest* points to the `master branch`_ while the *stable* points to the `latest GitHub tag`_. Therefore, every time changes are pushed to the *master branch* a new build in the latest version of the documentation is created, while the stable version is built only when new tags are created.

However, for many projects it is desirable a different setup where the master branch holds the stable version, that is, the code referent to the latest tag, while another branch (usually named *latest* or *develop*) set to the repositories' default, holds the latest development code that has not yet been merged to the master and considered stable. This is the setup of this template repository. Under this setup, it is desirable that the documentation build referent to the *latest* version points to the `latest branch`, the *stable* doc build will always point to the latest tag. This can be edited in ``Admin`` -> ``Advanced Settings`` and ``Default version`` and ``Default branch``.

Google Analytics
~~~~~~~~~~~~~~~~

Read the Docs allows straight forward implementation of Google Analytics tracking in the project documentation, just follow their instructions_.

Version
=======

v0.0.7

.. _tox workflow: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _latest: https://python-project-skeleton.readthedocs.io/en/latest/
.. _stable: https://python-project-skeleton.readthedocs.io/en/stable/
.. _master branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/master
.. _latest branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/latest
.. _latest Github tag: https://github.com/joaomcteixeira/python-project-skeleton/tags
.. _Read the Docs platform: https://readthedocs.org/
.. _instructions: https://docs.readthedocs.io/en/stable/guides/google-analytics.html
