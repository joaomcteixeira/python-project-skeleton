The rationale behind the project
================================

In the following sections I explain the rationale I used to configure this template repository. Also, these are the same strategies I adopt in my current projects. In summary, the following sections represent my view on software development practices, either it is open or closed source, done in teams or by single individuals. Yes, I also follow these *rules* when I am the sole developer.

Branch organization
-------------------

This repository complies with the ideas of agile development. Why? Because I found the agile strategy to fit best the kind of projects I develop. Is this the best strategy for your project? Well, you have to evaluate that.

In the "python-project-skeleton" layout, there is only one production branch, the `master` branch, where both the latest and the, so called, stable versions converge. This layout contrasts with the opposite strategy where the `stable` and the `latest` branches are kept separate. For the kind of projects I develop, keeping the `stable` and the `latest` separated is just troublesome. Honestly, I believe such separation defeats the purpose of agile development with Semantic Versioning 2, which is the versioning scheme I adopted.

Versioning
----------

The versioning scheme adopted here is the `Semantic Versioning 2`_.

The development process
-----------------------

Any code addition must come in the form of Pull Requests from forked repositories. Any merged pull request is followed the by respective increment in the software version and consecutive deployment of the new version in PyPI. If there are 5 pull request merges in one day, there will be 5 new versions releases that same day. Each new version should be tagged accordingly in git.

Additions to the documentation *also* count to the version number.

Additions to the CI platform *may* be pushed directly to the master by the main maintainer and should skip an increase in version number.

.. _Semantic Versioning 2: https://semver.org/#semantic-versioning-200
