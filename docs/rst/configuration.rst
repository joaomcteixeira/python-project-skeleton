Configuration
=============

Badges
------

Badges point to the current status of different Continuous Integration tools, for example, Travis-CI or Appveyor, but also documentation and code quality reports.

This project has two badge groups, one for the master (stable) branch and other for the latest (develop) branch. By showing information for these two groups the development team can keep track on the improvements (or losses) on code quality or the success of the different building processes. Though, in the case of building (Travis and Appveyor) they should always pass because no Pull Request should be allowed to merged without building success.

Each platform provide their own badges, yet you can further tune the badges style by creating your own personalized badge with `Shields.io`_.

You will notice that the badges for Coveralls and Code Climate are missing in the master branch. I could not find yet a straightforward and easy implementation for several branches in these platforms, so, they report on the main branch set for the repository, in this case the *latest* branch. Also at `Shields.io` there is no shortcut to *branch* for these platforms as there is for others.

.. _Shields.io: ttps://shields.io/
