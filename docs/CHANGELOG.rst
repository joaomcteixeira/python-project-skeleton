Changelog
=========

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
