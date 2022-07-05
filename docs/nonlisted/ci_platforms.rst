Continuous Integration
----------------------

Here, I overview the implementation strategies for the different continuous
integration and quality report platforms. In the previous versions of this
skeleton template, I used `Travis-CI`_ and `AppVeyor-CI`_ to run the testing
workflows. In the current version, I have migrated all these operations to GitHub
Actions.

**Does this mean you should not use Travis or AppVeyor?** *Of course not.*
Simply, the needs of my projects and the time I have available to dedicate to
CI configuration do not require a dedicated segregation of strategies into
multiple servers and services and I can perfectly accommodate my needs in
GitHub actions.

**Are GitHub actions better than Travis or AppVeyor?** I am not qualified to
answer that question.

When using this repository, keep in mind that you don't need to use all
services adopted here. You can drop or add any other at your will by removing
the files or lines related to them or adding new ones following the patterns
presented here.

The following list summarizes the platforms adopted:

#. Building and testing
    * GitHub actions
#. Quality Control
    * Codacy
    * Code Climate
#. Test Coverage
    * Codecov
#. Documentation
    * Read the Docs

I acknowledge the existence of many other platforms for the same purposes of
those listed. I chose these because they fit the size and scope of my projects
and are also the most used within my field of work.

Configuring GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~

You may wish to read about `GitHub actions
<https://github.com/features/actions>`_. Here, I have one Action workflow per
environment defined in ``tox``. Each of these workflows runs on each of the
python supported versions and OSes. These tests regard unit tests,
documentation build, lint, integrity checks, and, finally, version bump and
package deploying on PyPI.

The CI workflows trigger every time a new pull request is created and at each
commit to that PR. However, the ``lint`` tests do not trigger when the PR is
merged to the ``main`` branch. On the other hand, the ``version bump`` workflow
triggers only when the PR is accepted.

In this repository you can find two PRs demonstrating: one where `tests pass
<https://github.com/joaomcteixeira/python-project-skeleton/pull/10>`_ and
another where `tests fail
<https://github.com/joaomcteixeira/python-project-skeleton/pull/11>`_.

Version release
```````````````

Every time a Pull Request is merged to `main` branch, the `deployment workflow
<https://github.com/joaomcteixeira/python-project-skeleton/blob/master/.github/workflows/version-bump-and-package.yml>`_
triggers. This action bumps the new version number according to the
merge commit message, creates a new GitHub tag for that commit, and
publishes in PyPI the new software version.

As discussed in another section, here I follow the rules of `Semantic
Versioning 2 <https://semver.org/>`_.

If the Pull Request merge commit starts with ``[MAJOR]``, a major version
increase takes place (attention to the rules of SV2!), if a PR merge commit
message starts with ``[FEATURE]`` it triggers a *minor* update. Finally, if the
commit message as not special tag, a *patch* update is triggered. Whether to
trigger a *major*, *minor*, or *patch* update concern mainly the main
repository maintainer.

This whole workflow can be deactivate if the commit to the ``main`` branch
starts with ``[SKIP]``.

In conclusion, every commit to ``main`` without the ``[SKIP]`` tag will be
followed by a version upgrade, new tag, new commit to ``main`` and consequent
release to PyPI. You have a visual representation of the commit workflow in the
`Network plot
<https://github.com/joaomcteixeira/python-project-skeleton/network>`_.

**How version numbers are managed?**

There are two main version string handlers out there:
`bump2version`_ and `versioneer`_.  I chose *bump2version* for this repository
template. Why? I have no argument against *versioneer* or others, simply I
found ``bumpversion`` to be so simple, effective, and configurable that I could
only adopt it. Congratulations to both projects nonetheless.

Code coverage
~~~~~~~~~~~~~

``Codecov`` is used very frequently to report test coverage rates. Activate
your repository under ``https://about.codecov.io/``, and follow their
instructions.

`Coverage`_ reports are sent to Codecov servers when the ``test.yml`` workflow
takes place. This happens for each PR and each merge commit to ``maint``.

The `.coveragerc`_ file, mirrored below, configures ``Coverage`` reports.

.. literalinclude:: ../.coveragerc

The :code:`.coveragerc` can be expanded to further restraint coverage analysis,
for example adding these lines to the :code:`exclude` tag:

::

    [report]
    exclude_lines =
    if self.debug:
    pragma: no cover
    raise NotImplementedError
    if __name__ == .__main__.:

Remember that if you don't want to use these services, you can simply remove
the respective files from your project.

Code Quality
~~~~~~~~~~~~

Here, we have both ``Codacy`` and ``Code Climate`` as code quality inspectors.
There are also others out there, feel free to suggested different ones in the
`Discussion tab
<https://github.com/joaomcteixeira/python-project-skeleton/discussions>`_.

Codacy
``````

There is not much to configure for `Codacy` as far as this template is
concerned. The only setup provided is to exclude the analysis of test scripts,
this configuration is provided by the :code:`.codacy.yaml` file at the root
director of the repository. If you wish Codacy to perform quality analysis on
your test scripts just remove the file or comment the line. Here we mirror the
`.codacy.yaml`_ file:

.. literalinclude:: ../.codacy.yaml
    :language: yaml

Code Climate
````````````

There is not much to configure for `Code Climate`_, as well. The only setup
provided here is to exclude the analysis of test scripts and other *dev* files
Code Climate checks by default, the :code:`.codeclimate.yml` file at the root
directory of the repository configures this behavior (look at the bottom
lines).  If you wish Code Climate to perform quality analysis on your test
scripts just remove the file or comment the line.

Code Climate provides a **technical debt** percentage that can be retrieved
nicely with :ref:`Badges`.


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
