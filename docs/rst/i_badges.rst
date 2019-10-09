Badges
------

Badges point to the current status of the different Continuous Integration tools, for example, Travis-CI or Appveyor, but also documentation and code quality reports.

This project has two badge groups, one for the master (stable) branch and other for the latest (develop) branch. By showing information for these two groups the development team can keep track on the improvements (or losses) on code quality or the success of the different building processes.

Each platform provide their own badges, yet you can further tune the badges style by creating your own personalized badge with `Shields.io`_.

You will notice that the badge for Code Climate is missing in the master branch. I could not find yet a straightforward and easy implementation for several branches at Code Climate, so, the badge reports on the main branch set for the repository, in this case the *latest* branch. Also at `Shields.io` there is no shortcut to *branch* for this platform as there is for others.

I observed this same issue for COVERALLS, but then I realize that after the first commit to the master, COVERALLS actually displays nicely the information for both branches.

.. _Shields.io: https://shields.io/
