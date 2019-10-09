Contributing
============

Here we explain how to contribute to a project that adopted this template. Actually, you can use this same scheme when contributing to this template.

Fork this repository
--------------------

`Fork this repository before contributing`_. It is a better practice, possibly even enforced, that only Pull Request from forks are accepted. In my opinion this creates a cleaner representation of the whole `contributions to the project`_.

Uniformed Tests
---------------

Thanks to `Tox`_ we can have a uniform testing platform where all developers are forced to follow the same rules and, above all, all tests occur in a controlled Python environment.

With *Tox*, the testing setup can be defined in a configuration file, the `tox.ini`_, which contains all the operations that are performed during the test phase. Therefore, to run the unified test suite, developers just need to execute ``tox``, provided `tox is installed`_ in the Python environment in use.

::

    pip install tox
    # or
    conda install tox -c conda-forge

.. TODO::

    Review and consider integrating using tox to setup development envs -> https://tox.readthedocs.io/en/latest/example/devenv.html


One of the greatest advantages of using Tox together with the :ref:`src layout<The src layout>`, aside from uniforming the testing routines across developers, is that tests scripts actually perform against an installed source (our package) inside an isolated deployment environment. In order words, tests are performed in an environment simulating a post-deployment state instead of a pre-deploy/development environment. Under this setup, there is no need, in general cases, to deploy test scripts along with the actual source, in my honest opinion - see `MANIFEST.in`_.

.. TODO::

    Discuss the need to deploy test scripts.


Before creating a Pull Request from your branch, certify that all the tests pass correctly by running:

::
    
    tox

These are exactly the same tests that will be performed in the :ref:`CI platforms`.

Also, you can run individual environments if you wish to test only specific functionalities, for example:

::
    
    tox -e check  # code style and file compatibility
    tox -e spell  # spell checks documentation
    tox -e docs  # only builds the documentation

Branch workflow
---------------

Branch workflow for development and contribution should follow the `Gitflow Workflow`_ guidelines. Please read careful through that guide. Here we highlight the general approach with our favorite ``--no-ff`` flag.

Clone your fork
~~~~~~~~~~~~~~~

Indeed the first thing to do is to clone your fork, and keep it `up to date with the upstream`_:

::

    git clone https://github.com/YOUR-USERNAME/python-project-skeleton.git
    cd into/cloned/fork-repo
    git remote add upstream git://github.com/joaomcteixeira/python-project-skeleton.git
    git fetch upstream
    git pull upstream latest

New feature
~~~~~~~~~~~

::
    
    git checkout latest
    git checkout -b feature_branch

Work on the feature ``:-)``, keep regular commit/pushes to your fork.

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

Create a short lived branch to prepare for the release candidate.

::
    
    git checkout latest
    git checkout -b release/0.1.0

Fix the final bugs, docs and minor corrections, and finally :ref:`bump the version<Bumpversion>`.

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

The hotfix strategy is applied when a bug is identified in the production version that can be easily fixed.

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


Bumpversion
-----------

I found two main version string handlers around: `bumpversion`_ and `versioneer`_.
I chose *bumpversion* for this repository template. Why? I have no argument against *versioneer*, simply I found `bumpversion`_ to be so simple, effective and configurable that I could only adopt it. Congratulations to both projects nonetheless.


.. _tox.ini: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _tox is installed: https://tox.readthedocs.io/en/latest/install.html
.. _MANIFEST.in: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/MANIFEST.in
.. _Fork this repository before contributing: https://github.com/joaomcteixeira/python-project-skeleton/network/members
.. _up to date with the upstream: https://gist.github.com/CristinaSolana/1885435
.. _contributions to the project: https://github.com/joaomcteixeira/python-project-skeleton/network
.. _Gitflow Workflow: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
.. _bumpversion: https://pypi.org/project/bumpversion/
.. _versioneer: https://github.com/warner/python-versioneer
