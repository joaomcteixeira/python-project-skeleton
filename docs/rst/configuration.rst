Configuration
=============

Badges
------

Badges point to the current status of different Continuous Integration tools, for example, Travis-CI or Appveyor, but also documentation and code quality reports.

This project has two badge groups, one for the master (stable) branch and other for the latest (develop) branch. By showing information for these two groups the development team can keep track on the improvements (or losses) on code quality or the success of the different building processes. Though, in the case of building (Travis and Appveyor) they should always pass because no Pull Request should be allowed to merged without building success.

Each platform provide their own badges, yet you can further tune the badges style by creating your own personalized badge with `Shields.io`_.

You will notice that the badge Code Climate is missing in the master branch. I could not find yet a straightforward and easy implementation for several branches in CC, so, it reports on the main branch set for the repository, in this case the *latest* branch. Also at `Shields.io` there is no shortcut to *branch* for these platforms as there is for others.

I observed the same issue detailed in the above paragraph for COVERALLS, but then I realize that after the first commit to the master, COVERALLS actually displays nicely the information for both branches.

.. _Shields.io: ttps://shields.io/
