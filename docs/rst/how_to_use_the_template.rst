How to use this template
========================

`Thanks to the template feature of GitHub <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template>`_, you can use the ``python-project-skeleton`` as a template for your own repositories. *(Yes you can also use a cookiecutter, but this is not a coockiecutter).*

Once you have created a new repository from this template, these are the names you need to change to adapt the template to you and your project:

1. Where it says ``joaomcteixeira``, rename it to your GitHub user name. In ``setup.py`` and in ``AUTHORS.rst`` there is also my full written name, rename it to yours.

2. Where ever it says ``sampleproject`` change it for the name of your project. That is, what you would like your users to import.

.. code::

    import sampleproject

3. In ``setup.py`` rename ``jmct-sampleproject`` for the name your project will have at PyPI. Usually this is the same as the name you decided above.

4. Where it says ``python-project-skeleton`` that is the name of the repository. It might be the same name as the Python package and the PyPI package, that is up to you entirely.

If you are using bash (most likely you are) you can run the following on the main project folder for word finding and replace in several files simultaneously (`kudos <https://stackoverflow.com/questions/6758963>`):

.. code::

    find ./ -type f -exec sed -i -e 's/apple/orange/g' {} \;

You can use a ``grep`` beforehand to identify where the strings are, and change them manually.

.. code::

    grep sampleproject -r

Despite you can do this, I suggest you honestly go through every single file and understand its functionality and which parameters you need to change to fit the template to your project. They are not that many files.

**Important to know**, this template is deployed at ``test.pypi.org``. You need to change the last line of the `Version-bump-and-package.yml <https://github.com/joaomcteixeira/python-project-skeleton/blob/master/.github/workflows/version-bump-and-package.yml>`_ file and remove the ``--repository testpypi`` tag.

Please read the :ref:`Template Configuration` section for all the details on the different workflows implemented.

Enjoy, and if you like this template, please let me know.
