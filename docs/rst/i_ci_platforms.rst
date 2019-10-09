CI Platforms
------------

Here we provide an overview of the implementation strategies for the different continuous integration and quality report platforms. We have adopted a total of seven platforms, two for building and testing, two for code quality control, two for test coverage and one for documentation deployment:

#. Building and testing
    * Travis-CI (Linux and OSX)
    * Appveyor (Windows)
#. Quality Control
    * Codacy
    * Code Climate
#. Test Coverage
    * Codecov
    * Coveralls
#. Documentation
    * Read the Docs

We acknowledge the existence of many other platforms for the same purposes. Though, we have chosen these because they fit the size and scope of the projects to which this template aims at and are those platforms most used within our field of development.

Choosing the CIs
~~~~~~~~~~~~~~~~

Please note that you do not need to use all these platforms when adapting this template for your project, we do suggest you use at least one for each topic. For example, you do not need to activate Appveyor if you do not intent to deploy/distribute your code for Windows machines. Also, for quality control and test coverage one of the two provided options may suffice, however, having both is free and you can benefit from the different analysis reports the platforms provide.

.. note::

   To **NOT** use a specific CI platform simply do not activate it in their website, remove the configuration file from the root directory of the project, and remove the badge image link from the :code:`README.rst` file. Continue reading to understand better these concepts.

Activate CI
~~~~~~~~~~~

To activate the different CI platforms for you repository just navigate to their website, login with your GitHub account and activate the repository. The configurations provided in this template should to the rest automatically :code:`:-)`, just start pushing your commits to the server.

Travis-CI
~~~~~~~~~

The configuration for `Travis-CI`_ is defined in the :code:`.travis.yml` file.

Overall, the Travis configuration defines how to execute the different :ref:`tox environments<Uniformed Tests>` defined in the :code:`tox.ini` file.

Find in the `.travis.yml`_ file the complete explanation for the implementation proposed, here we mirror the file:

.. TODO::

   Configure Travis to run OSX tests.

.. literalinclude:: ../../.travis.yml
   :language: yaml

Appveyor
~~~~~~~~

The configuration for `AppVeyor-CI`_ is defined in the :code:`.appveyor.yml` file.

Contrary to our configuration for :ref:`Travis-CI`, with Appveyor, the configuration file simply attempts to build the package and run the unittests battery in the different Python versions.

Find in the `.appveyor.yml_` file the complete explanation for the implementation proposed, here we mirror the file:

.. literalinclude:: ../../.appveyor.yml
   :language: yaml

Codacy
~~~~~~

There is not much to configure for `Codacy` in the version we propose in this template. The only setup provided is to exclude the analysis of test scripts, this configuration is provided by the :code:`.codacy.yaml` file at the root director of the repository. If you wish Codacy to perform quality analysis on your test scripts just remove the file or comment the line. Here we mirror the `.codacy.yaml`_ file:

.. literalinclude:: ../../.codacy.yaml
    :language: yaml

Code Climate
~~~~~~~~~~~~

There is not much to configure for `Code Climate`_ in the version we propose in this template. The only setup provided is to exclude the analysis of test scripts and other *dev* files Code Climate by default analysis, this configuration is provided by the :code:`.codeclimate.yml` file at the root director of the repository. If you wish Code Climate to perform quality analysis on your test scripts just remove the file or comment the line.

Code Climate provides a **technical debt** percentage that can be retrieved nicely with a `badge<Badges>`

Here we mirror the `.codeclimate.yml`_ file:

.. literalinclude:: ../../.codeclimate.yml
    :language: yaml

Badges
------

Badges point to the current status of the different Continuous Integration tools, for example, Travis-CI or Appveyor, but also documentation and code quality reports.

This project has two badge groups, one for the master (stable) branch and other for the latest (develop) branch. By showing information for these two groups the development team can keep track on the improvements (or losses) on code quality or the success of the different building processes.

Each platform provide their own badges, yet you can further tune the badges style by creating your own personalized badge with `Shields.io`_.

You will notice that the badge for Code Climate is missing in the master branch. I could not find yet a straightforward and easy implementation for several branches at Code Climate, so, the badge reports on the main branch set for the repository, in this case the *latest* branch. Also at `Shields.io` there is no shortcut to *branch* for this platform as there is for others.

I observed this same issue for COVERALLS, but then I realize that after the first commit to the master, COVERALLS actually displays nicely the information for both branches.

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
.. _Shields.io: https://shields.io/

