#!/usr/bin/env python

from setuptools import setup

from python_app_seed.utils import get_data_files


# Settings for collecting additional data files.
# Normally you should just recreate structure of the directories
# from the root in 'data' dir and everything will work.
#
# Pathes from where data files will be collected.
DIRS = ['data']
# Rewrite rules. In this example all files below 'data' will be placed
# to the root of the resulted package.
REWRITES = [('data', '/')]
# Your could exclude dirs
EXCLUDE_DIRS = []
# or separate files. Wildcard characters are supported.
EXCLUDE_FILES = []


setup(
    # Specify your application related info here.
    # Reference: http://pythonhosted.org/distribute/setuptools.html
    name='python_app_seed',
    version='0.0.1',
    author='Your Name',
    author_email='your+name@example.com',
    url='http://example.com/',
    description='Short project description',
    long_description=(
        'Long project description '
        'which may go on '
        'multiple lines.'),
    packages=['python_app_seed'],

    # Place all package dependencies in this section. There is not need
    # in requirements.txt or whatever hacky solutions. Additional
    # requirements for tests could be placed in 'tests_requirements.txt'.
    install_requires=[
        # For config. Feel free to delete if you don't like it.
        'PyYAML==3.10',
        # This is only for example. Delete it.
        'requests==1.2.3',
        'Flask==0.9',
        'python-github==0.1',
    ],
    # If some of the dependencies doesn't present on PyPi you could
    # specify link to it here.
    dependency_links=[
        # This is only for example. Delete it.
        'git+https://github.com/jmoiron/python-github#egg=python-github-0.1',
    ],

    # This line includes additional data files to the resulting package.
    # You could tune settings at the top of this file.
    data_files=get_data_files(DIRS, REWRITES, EXCLUDE_DIRS, EXCLUDE_FILES),
)
