Continuous Integration
----------------------

Here, I overview the implementation strategies for the different continuous integration and quality report platforms. In the previous versions of this skeleton template I used `Travis-CI`_ and `AppVeyor-CI`_ to accommodate testing. In the current version, I have migrated all these servers to GitHub actions, and I am not using Travis or AppVeyor anymore (for now).

**Does this mean you should not use Travis or AppVeyor?** *Of course not.* Simply, the needs of my projects and the time I have available to dedicate to CI configuration do not require a dedicated segregation of strategies into multiple servers and services and I can perfectly accommodate my needs in GitHub actions.

**Are GitHub actions better than Travis or AppVeyor?** I am not qualified to answer that question.

When using this repository, keep in mind that you don't need to use all services adopted here. You can drop or add any other at your will.

The following summaries the platforms adopted:

#. Building and testing
    * GitHub actions
#. Quality Control
    * Codacy
    * Code Climate
#. Test Coverage
    * Codecov
#. Documentation
    * Read the Docs

I acknowledge the existence of many other platforms for the same purposes of those listed. I chose these because they fit the size and scope of my projects and are also the most used within my field of development.

Configuring GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~

You may wish to read about `GitHub actions <https://github.com/features/actions>`_. In this repository there are two configured workflows: one to run the tests, lint, documentation check, and all kinds of integrity; and another to bump the version number and deploy new versions on PyPI.

Unittesting and integrity
`````````````````````````

Every time a new Pull Request is issued, the `ci-testing.yml <https://github.com/joaomcteixeira/python-project-skeleton/blob/master/.github/workflows/ci-testing.yml>`_ workflow is triggered. It is responsible to run the unittests, and repository integrity checks (defined at ``tox.ini``), and allow or disallow PR merge in case tests pass or fail.

This template has two example PRs for demonstration: one which `tests pass <https://github.com/joaomcteixeira/python-project-skeleton/pull/10>`_ and another which `tests fail <https://github.com/joaomcteixeira/python-project-skeleton/pull/11>`_.

This workflow also runs when a PR is approved or a new version released.

Version release
```````````````

Every time a Pull Request is merged to `master` the `deployment workflow <https://github.com/joaomcteixeira/python-project-skeleton/blob/master/.github/workflows/version-bump-and-package.yml>`_ is triggered. This action bumps the new version number according to the requests in the Pull Request, creates a new GitHub tag for that commit, and publishes in PyPI the new software version.

As discussed in another section, here I follow the rules of `Semantic Versioning 2 <https://semver.org/>`_.

The PR rules to trigger a *major*, *minor*, or *patch* update concern mainly the main repository maintainer. If the Pull Request merge commit starts with ``[MAJOR]``, a major version increase takes place (attention to the rules of SV2!!), if a PR merge commit message starts with ``[FEATURE]`` it triggers a *minor* update. Finally, if the commit message as not special tag, a *patch* update is triggered.

This whole workflow can be deactivate if the commit to the ``master`` branch starts with ``[SKIP]``.

In conclusion, every commit to ``master`` without the ``[SKIP]`` tag will be followed by a version upgrade, new tag, new commit to ``master`` and consequent release to PyPI. You have a visual representation of the commit workflow in the `Network plot <https://github.com/joaomcteixeira/python-project-skeleton/network>`_.

**How version numbers are managed?**

There are two main version string handlers in the ecosystem I operate: `bump2version`_ and `versioneer`_.  I chose *bump2version* for this repository template. Why? I have no argument against *versioneer* or others, simply I found ``bumpversion`` to be so simple, effective, and configurable that I could only adopt it. Congratulations to both projects nonetheless.

Code coverage
~~~~~~~~~~~~~

``Codecov`` is used very frequently to report test coverage rates. Activate your repository under ``https://about.codecov.io/``, and follow their instructions.

`Coverage`_ reports are sent to Codecov servers when ``ci-testing`` workflow takes place. This happens for each PR and each commit ``master``.

The `.coveragerc`_ file, mirrored bellow, configures ``Coverage``.

.. literalinclude:: ../../.coveragerc

The :code:`.coveragerc` can be expanded to further restraint coverage analysis, for example adding these lines to the :code:`exclude` tag:

::

    [report]
    exclude_lines =
    if self.debug:
    pragma: no cover
    raise NotImplementedError
    if __name__ == .__main__.:

Code Quality
~~~~~~~~~~~~

Here, we have both ``Codacy`` and ``Code Climate`` as code quality inspectors. There are also others out there, feel free to suggested different ones in the `Discussion tab <https://github.com/joaomcteixeira/python-project-skeleton/discussions>`_.

Codacy
``````

There is not much to configure for `Codacy` as far as this template is concerned. The only setup provided is to exclude the analysis of test scripts, this configuration is provided by the :code:`.codacy.yaml` file at the root director of the repository. If you wish Codacy to perform quality analysis on your test scripts just remove the file or comment the line. Here we mirror the `.codacy.yaml`_ file:

.. literalinclude:: ../../.codacy.yaml
    :language: yaml

Code Climate
````````````

There is not much to configure for `Code Climate`_ as well. The only setup provided is to exclude the analysis of test scripts and other *dev* files Code Climate checks by default, the :code:`.codeclimate.yml` file at the root director of the repository configures this behavior (look at the bottom lines). If you wish Code Climate to perform quality analysis on your test scripts just remove the file or comment the line.

Code Climate provides a **technical debt** percentage that can be retrieved nicely with :ref:`Badges`.


.. _Travis-CI: https://travis-ci.org
.. _.travis.yml: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.travis.yml
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Appveyor-CI: https://www.appveyor.com/
.. _tox.ini: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _.appveyor.yml: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.appveyor.yml
.. _.codacy.yaml: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.codacy.yaml
.. _.codeclimate.yml: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.codeclimate.yml
.. _Codacy: https://app.codacy.com/
.. _Code Climate: https://codeclimate.com/
.. _coverage: https://pypi.org/project/coverage/
.. _.coveragerc: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.coveragerc
.. _bump2version: https://pypi.org/project/bumpversion/
.. _versioneer: https://github.com/warner/python-versioneer
