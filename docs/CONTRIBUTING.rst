Contributing
============

How to contribute to this project.

Fork this repository
--------------------

`Fork this repository before contributing`_. It is a better practice, possibly even enforced, that only Pull Request from forks are accepted - consider a case where there are several main maintainers. In my opinion enforcing forks creates a cleaner representation of the `contributions to the project`_.

Clone your fork
~~~~~~~~~~~~~~~

Next, clone your fork to your local machine, keep it `up to date with the upstream`_, and update the online fork with those updates.

::

    git clone https://github.com/YOUR-USERNAME/python-project-skeleton.git
    cd python-project-skeleton
    git remote add upstream git://github.com/joaomcteixeira/python-project-skeleton.git
    git fetch upstream
    git merge upstream/master
    git pull origin master

Install for developers
----------------------

Create a dedicated Python environment where to develop the project.

If you are using :code:`pip` follow the official instructions on `Installing packages using pip and virtual environments`_, most likely what you want is:

::

    python3 -m venv pyprojskel
    source pyprojskel/bin/activate

If you are using `Anaconda`_ go for:

::

    conda create --name pyprojskel python=3.7
    conda activate pyprojskel

Where :code:`pyprojskel` is the name you wish to give to the environment dedicated to this project.

Either under *pip* or *conda*, install the package in :code:`develop` mode, and also :ref:`tox<Uniformed Tests with tox>`. **Note**, here I assume our project has **no** dependencies.

::

    python setup.py develop
    pip install tox

This configuration, together with the use of the ``src`` folder layer, guarantee that you will always run the code after installation. Also, thanks to the ``develop`` flag, any changes in the code will be automatically reflected in the installed version.

Make a new branch
-----------------

From the ``master`` branch create a new branch where to develop the new code.

::

    git checkout master
    git checkout -b new_branch


Develop the feature and keep regular pushes to your fork with comprehensible commit messages.

::

    git status
    git add (the files you want)
    git commit (add a nice commit message)
    git push origin new_branch

While you are developing, you can execute ``tox`` as needed to run your unittests or inspect lint, etc. See the last section of this page.

Update CHANGELOG
~~~~~~~~~~~~~~~~

Update the changelog file under :code:`docs/CHANGELOG.rst` with an explanatory bullet list of your contribution. Add that list right after the main title and before the last version subtitle::

    Changelog
    =========

    * here goes my new additions
    * explain them shortly and well

    vX.X.X (1900-01-01)
    -------------------

Also add your name to the authors list at :code:`docs/AUTHORS.rst`.

Pull Request
~~~~~~~~~~~~

Once you are finished, you can Pull Request you additions to the main repository, and engage with the community. Please read the ``PULLREQUEST.rst`` guidelines first, you will see them when you open a PR.

**Before submitting a Pull Request, verify your development branch passes all tests as** :ref:`described bellow<Uniformed Tests with tox>` **. If you are developing new code you should also implement new test cases.**


Uniformed Tests with tox
------------------------

Thanks to `Tox`_ we can have a unified testing platform where all developers are forced to follow the same rules and, above all, all tests occur in a controlled Python environment.

With *Tox*, the testing setup can be defined in a configuration file, the `tox.ini`_, which contains all the operations that are performed during the test phase. Therefore, to run the unified test suite, developers just need to execute ``tox``, provided `tox is installed`_ in the Python environment in use.

::

    pip install tox
    # or
    conda install tox -c conda-forge


One of the greatest advantages of using Tox together with the :ref:`src layout<The src layout>` is that unittest actually perform on the installed source (our package) inside an isolated deployment environment. In order words, tests are performed in an environment simulating a post-installation state instead of a pre-deploy/development environment. Under this setup, there is no need, in general cases, to distribute test scripts along with the actual source, in my honest opinion - see `MANIFEST.in`_.

Before creating a Pull Request from your branch, certify that all the tests pass correctly by running:

::

    tox

These are exactly the same tests that will be performed online in the Github Actions.

Also, you can run individual environments if you wish to test only specific functionalities, for example:

::

    tox -e lint  # code style
    tox -e build  # packaging
    tox -e docs  # only builds the documentation
    tox -e prreqs  # special requirements before Pull Request
    tox -e py37


.. _tox.ini: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _tox is installed: https://tox.readthedocs.io/en/latest/install.html
.. _MANIFEST.in: https://github.com/joaomcteixeira/python-project-skeleton/blob/master/MANIFEST.in
.. _Fork this repository before contributing: https://github.com/joaomcteixeira/python-project-skeleton/network/members
.. _up to date with the upstream: https://gist.github.com/CristinaSolana/1885435
.. _contributions to the project: https://github.com/joaomcteixeira/python-project-skeleton/network
.. _Gitflow Workflow: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
.. _Pull Request: https://github.com/joaomcteixeira/python-project-skeleton/pulls
.. _PULLREQUEST.rst: https://github.com/joaomcteixeira/python-project-skeleton/blob/master/docs/PULLREQUEST.rst
.. _1: https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-ff
.. _2: https://stackoverflow.com/questions/9069061/what-is-the-difference-between-git-merge-and-git-merge-no-ff
.. _Installing packages using pip and virtual environments: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
.. _Anaconda: https://www.anaconda.com/
