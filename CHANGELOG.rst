
Changelog
=========

v0.11.1 (2022-07-14)
------------------------------------------------------------

* Add a CI .yml for envs running only on PRs (#31)

v0.11.0 (2022-07-14)
------------------------------------------------------------

* merge all tox envs in a single matrix (#30)

v0.10.1 (2022-07-05)
------------------------------------------------------------

* Correct docs/config reference in ``.readthedocs.yml``

v0.10.0 (2022-07-05)
------------------------------------------------------------

* Update docs content and structure

v0.9.6 (2022-06-30)
------------------------------------------------------------

* Update README

v0.9.5 (2022-06-29)
------------------------------------------------------------

* Update CI YAML files:
* Add python 3.10
* reduce number of installs

v0.9.4 (2022-06-29)
------------------------------------------------------------

* move pull request template to ``.github`` folder.

v0.9.3 (2022-06-29)
------------------------------------------------------------

* Add code of conduct from Contributor Covenant v2.

v0.9.2 (2022-05-26)
------------------------------------------------------------

* Update badges in `readme` and corresponding `master` rename to `main` in services.

v0.9.1 (2022-05-26)
------------------------------------------------------------

* revert to `pr` testenv in `tox`
* Remove the empty line in changelog title

v0.9.0 (2022-05-26)
------------------------------------------------------------

* update tox environments. Tests now run with `test` env.
* update/simplify github actions accordingly
* attempts correct changelog line conflict
* update requirements.txt now depending on `setup.py`
* drop python 3.6

v0.8.1 (2021-11-09)
------------------------------------------------------------

* updates radon commands in `tox.ini`

v0.8.0 (2021-01-26)
------------------------------------------------------------

* renames tox env `chlog` to a more general `prreqs`
* corrects details in `CONTRIBUTING.rst`

v0.7.0 (2021-01-24)
------------------------------------------------------------

* increased granularity of tox environments
* new lint env
* new chlog env
* check renamed to build
* tox environment scopes separated into different actions
* new lint only dedicated action
* new pull request requirements action

v0.6.0 (2021-01-24)
------------------------------------------------------------

* updates package check command, now uses twine
* add scripts to clean up dist files after ``tox -e check``
* Adds checks to CHANGELOG
* Adds new tox env just for lint checks
* lint is kept in ``check`` env nonetheless
* updates documentation accordingly

v0.5.0 (2021-01-24)
------------------------------------------------------------

* Adds documentation for some configuration files

v0.4.0 (2021-01-23)
------------------------------------------------------------

* Updates documentation to the new Github Actions integration
* Updates documentation in general

v0.3.1 (2021-01-22)
------------------------------------------------------------

* Synchronized CHANGELOG with ``.bumpversion``

v0.3.0 (2021-01-22)
------------------------------------------------------------

* simplifies ``setup.py``
* defines rules for ``CHANGELOG.rst``
* adds ``check`` ``tox`` env to py37 machine

v0.2.2 (2021-01-22)
------------------------------------------------------------

* Updates CI framework to GitHub Actions
* adds action to automate version bump and package build to PyPI
* completes CI for Linux, Windows, and MacOS
* reports test coverage to Codecov
* updated/enhanced bump2version configuration
* bump2version also changes CHANGELOG

v0.2.1 (2020-05-31)
-------------------

* updated tox to accepts posargs in `pytest` and `flake8`

v0.2.0 (2020-01-31)
-------------------

* Implemented Travis-CI for Windows, MacOSX and Linux
  * for Python: 3.6, 3.7 and 3.8
  * all previous without using anaconda expect for MacOSX 3.8
  * I have nothing against Anaconda ;-), on the contrary, I use it everyday.
* Improved ``tox.ini`` workflow to my current favorite standards.
* Implemented mock strategy to avoid installing dependencies for documentation generation.
  * TOXENV docs

v0.1.0 (2019-10-03)
-------------------

* First release on PyPI.
