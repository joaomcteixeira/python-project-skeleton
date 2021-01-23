Configuration Files
-------------------

MANIFEST.in
~~~~~~~~~~~

The ``MANIFEST.in`` file configures which files in the repository/folder are grabbed or ignored when assembly the distributed package. You can see that I package the ``src``, the ``docs``, other ``*.rst`` files, the ``LICENSE`` and nothing more. All configuration files, tests, and other Python related or IDE related files are excluded.

There is a debate on whether tests should be deployed along with the library source. Should they? Tox and the CI integration guarantees tests are run on *installed* versions of the software. So, I am the kind of person that considers there is no need to deploy tests alongside with the source. Users aren't going to run tests. Developers will.

Let me know if you think differently.

It is actually easy to work with MANIFEST.in file. Feel free to add or remove files as your project needs.

tox.ini
~~~~~~~

Tox configuration file might be the trickiest one to learn and operate with until you are familiar with tox's workflows. `Read all about tox in their documentation pages <https://tox.readthedocs.io/en/latest/>`_. The ``tox.ini`` file contains several comments explaining the implementations I adopted.

bumpversion.cfg
~~~~~~~~~~~~~~~

The ``.bumpversion.cfg`` configuration is heavily related with the GitHub Actions workflows for automated packaging and deployment and the ``CONTRIBUTING.rst`` instructions. Specially, the use of commit and tag messages, and the trick with CHANGELOG.rst.

I have also used bumpversion in other projects to update the version on some badges.
