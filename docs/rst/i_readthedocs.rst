Read the Docs
-------------

Activate your project at `Read the Docs platform`_ (RtD), their web interface is easy enough to follow without further explanations. If your documentation is building under the :ref:`tox workflow<Uniformed Tests with tox>` it will build in at Read the Docs.

Docs Requirements
~~~~~~~~~~~~~~~~~

Requirements to build the documentation page are listed in ``devtools/docs_requirements.txt``:

.. literalinclude:: ../../devtools/docs_requirements.txt

Here we use `Sphinx`_ as the documentation builder and the `sphinx-py3doc-enhanced-theme`_ as theme, though you can use many different theme flavors, see `Sphinx Themes`_.

Build version
~~~~~~~~~~~~~

By default, RtD has two main documentation versions (also called builds): the *latest* and the *stable*. The *latest* points to the ``master`` branch while the *stable* points to the `latest GitHub tag`_. However, as we have discussed in :ref:`The Rationale behind the project` section, here we keep only the *latest* version (that of the ``master`` branch) and other versions for the different releases of interest.

Google Analytics
~~~~~~~~~~~~~~~~

Read the Docs allows straight forward implementation of Google Analytics tracking in the project documentation, just follow their instructions_.

Local Build
~~~~~~~~~~~

The ``[testenv:docs]`` in ``tox.ini`` file simulates the RtD execution. If that test passes, RtD should pass.

To build a local version of the documentation, go to the main repository folder and run:

::

    tox -e docs

The documentation is at ``dist/docs/index.html``. The ``tox`` run also reports on inconsistencies and errors. If there are inconsistencies or errors in the documentation build, the PR won't pass the CI tests.

.. _Read the Docs platform: https://readthedocs.org/
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _Sphinx Themes: https://sphinx-themes.org/
.. _sphinx-py3doc-enhanced-theme: https://github.com/ionelmc/sphinx-py3doc-enhanced-theme
.. _latest Github tag: https://github.com/joaomcteixeira/python-project-skeleton/tags
.. _instructions: https://docs.readthedocs.io/en/stable/guides/google-analytics.html
