Read the Docs
-------------

Activate your project at `Read the Docs platform`_ (RdD), their web interface is easy enough to follow without further explanations. If your documentation is building under the :ref:`tox workflow<Uniformed Tests>` it will build in at Read the Docs.

Docs Requirements
~~~~~~~~~~~~~~~~~

Requirements to build the documentation page are listed in ``docs/requirements.txt``:

.. literalinclude:: ../requirements.txt

In this repository we are using `Sphinx`_ as documentation builder and the `sphinx-py3doc-enhanced-theme`_ as theme, though you can use many different theme flavors, see `Sphinx Themes`_.

Build version
~~~~~~~~~~~~~

By default, RdD has two main documentation versions (also called builds): the `latest`_ and the `stable`_. The *latest* points to the `master branch`_ while the *stable* points to the `latest GitHub tag`_. Therefore, every time changes are pushed to the *master branch* a new build in the latest version of the documentation is created, while the stable version is built only when new tags are created.

However, for many projects it is desirable a different setup where the master branch holds the stable version, that is, the code referent to the latest tag, while another branch (usually named *latest* or *develop*) set to the repositories' default, holds the latest development code that has not yet been merged to the master and considered stable. This is the setup of this template repository. Under this setup, it is desirable that the documentation build referent to the *latest* version points to the `latest branch`_, the *stable* doc build will always point to the latest tag. This can be edited in ``Admin`` -> ``Advanced Settings`` and ``Default version`` and ``Default branch``.

Google Analytics
~~~~~~~~~~~~~~~~

Read the Docs allows straight forward implementation of Google Analytics tracking in the project documentation, just follow their instructions_.

.. _Read the Docs platform: https://readthedocs.org/
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _Sphinx Themes: https://sphinx-themes.org/
.. _sphinx-py3doc-enhanced-theme: https://github.com/ionelmc/sphinx-py3doc-enhanced-theme
.. _latest Github tag: https://github.com/joaomcteixeira/python-project-skeleton/tags
.. _instructions: https://docs.readthedocs.io/en/stable/guides/google-analytics.html
.. _latest branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/latest
.. _master branch: https://github.com/joaomcteixeira/python-project-skeleton/tree/master
.. _latest: https://python-project-skeleton.readthedocs.io/en/latest/
.. _stable: https://python-project-skeleton.readthedocs.io/en/stable/
