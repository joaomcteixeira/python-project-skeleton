#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import os
import re
from glob import glob
from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext

from setuptools import Extension
from setuptools import find_packages
from setuptools import setup
from setuptools.command.build_ext import build_ext

here = abspath(dirname(__file__))


def read(*names, **kwargs):
    with open(join(here, *names), encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()

long_description = '{}\n{}'.format(
    re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
    re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    )

setup(
    name='sampleproject',
    version='0.1.0',
    license='GNU GPLv3 License',
    description='sampleproject small description.',
    long_description=long_description,
    author='Joao Miguel Correia Teixeira',
    author_email='joaomcteixeira@gmail.com',
    url='https://github.com/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    project_urls={
       'webpage': 'https://taurenmd.github.io', 
        #'Documentation': 'https://python-nameless.readthedocs.io/',
        #'Changelog': 'https://python-nameless.readthedocs.io/en/latest/changelog.html',
        #'Issue Tracker': 'https://github.com/ionelmc/python-nameless/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='==3.7.*',
    install_requires=[
        'matplotlib>=3',
    #    'click',
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
     #   'pytest-runner',
     #   'setuptools_scm>=3.3.1',
    ],
    entry_points={
       # 'console_scripts': [
       #     'nameless = nameless.cli:main',
        #]
    },
    #cmdclass={'build_ext': optional_build_ext},
    #ext_modules=[
    #    Extension(
    #        splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
    #        sources=[path],
    #        include_dirs=[dirname(path)]
    #    )
    #    for root, _, _ in os.walk('src')
    #    for path in glob(join(root, '*.c'))
    #],
)
