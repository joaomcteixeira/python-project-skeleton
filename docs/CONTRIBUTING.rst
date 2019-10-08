Contributing
============

Uniformed Tests
---------------

Thanks to `Tox`_ we can have a uniform testing platform where all developers are forced to follow the same rules and, above all, all tests occur in a controlled Python environment.

Before creating a Pull Request from your branch, certify that all the tests pass correctly by running:

::
    tox

These are exactly the same tests that will be performed in the CI platforms.

Also, you can run individual environments if you wish to test only specific functionalities, for example:

::
    tox -e check  # code style and file compatibility
    tox -e spell  # spell checks documentation
    tox -e docs  # only builds the documentation

Branch workflow
---------------

Branch workflow for development and contribution should follow the `Gitflow Workflow`_ guidelines. Please read careful through that guide, here we highlight the general approach with our favorite ``--no-ff`` flag.

New feature
~~~~~~~~~~~

::
    git checkout latest
    git checkout -b feature_branch

Work on the feature ``:-)``.

Push to latest
~~~~~~~~~~~~~~

You should create a Pull Request to the ``latest`` branch.
If you are an official contributor to this repository and are sure the new feature branch passes tests, directly merge to the ``latest`` branch.

::
    git checkout latest
    git merge --no-ff feature_branch
    git push origin latest

The ``--no-ff`` option avoid ``Fastforward`` merging, keeping a record of the branching out/in history.

Release Branches
~~~~~~~~~~~~~~~~

::
    git checkout latest
    git checkout -b release/0.1.0

Fix the final bugs, docs and minor corrections, and finally ``bump`` the version.

::
    bumpversion patch|minor|major

Finally, merge to ``master`` AND to ``latest``.

::
    git checkout master
    git merge --no-ff release/0.1.0
    git push origin master --tags
    git checkout latest
    git merge --no-ff release/0.1.0

Hotfixes from master
~~~~~~~~~~~~~~~~~~~~

Hotfix strategy is applied when a bug is identified in the production version that can be easily fixed.

::
    git checkout master
    git checkout -b hotfix_branch

Work on the fix...

::
    git push origin hotfix_branch  # push yours commits to GitHub beforehand
    bumpversion patch
    git push origin hotfix_branch
    git checkout master
    git merge --no-ff hotfix_branch
    git push origin master --tags
    git checkout latest
    git merge --no-ff hotfix_branch
    git push origin latest


.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Gitflow Workflow: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
