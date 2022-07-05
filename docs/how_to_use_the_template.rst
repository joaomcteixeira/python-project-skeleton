How to use this template
========================

You can use the ``python-project-skeleton`` as a template for your own
repositories thanks to the `template feature of GitHub
<https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template>`_,
*(Yes, you could use a cookiecutter, but this is not a coockiecutter).*

Changing names
--------------

Once you have created a new repository from this template, these are the names
you need to change in the files to adapt the template to you and your project:


.. note::

    If you are using bash, you can use:
    :code:`grep -rliI "text to search" .`
    to identify which files have the string you want to change.

.. note::

    In bash, use the following to replace a string in multiple files.
    :code:`find ./ -type f -exec sed -i -e 's/apple/orange/g' {} \;`
    Kudos to https://stackoverflow.com/questions/6758963.

1. Where it says ``joaomcteixeira``, rename it to your GitHub user name. In
``setup.py`` and in ``AUTHORS.rst`` there is also my full written name, rename
it to yours.

2. Where ever it says ``sampleproject`` change it for the name of your project.
That is, what you would like your users to import.

.. code::

    import sampleproject

3. In ``setup.py`` rename :code:`jmct-sampleproject` for the name your project will
have at PyPI. Usually this is the same as the name you decided above.

4. Replace ``python-project-skeleton`` to the name of the repository of your
project. It might be the same name as the Python package and the PyPI package,
that is up to you entirely.

5. This template is deployed at ``test.pypi.org``. You need to change the last
line of the `version-bump-and-package.yml
<https://github.com/joaomcteixeira/python-project-skeleton/blob/master/.github/workflows/version-bump-and-package.yml>`_
file and remove the ``--repository testpypi`` tag so that your project is
deployed at the main PyPI repository.

6. Remove and edit some of the unnecessary files in the ``docs`` folder. Mainly those
related explicitly to this template repository and reference herein.

Despite you can use the find/replace commands, I suggest you navigate every file
and understand its functionality and which parameters you need to change to fit
the template to your project. They are not that many files.

Please read the :ref:`Template Configuration` section for all the details on the
different workflows implemented.

Finally, you can remove those files or lines that refer to integrations that you
do not want. For example, if you don't want to have your project tracked by
CodeClimate, remove the files and lines related to it.

Enjoy, and if you like this template, please let me know.
