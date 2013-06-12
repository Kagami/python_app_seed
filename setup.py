#!/usr/bin/env python

from setuptools import setup

from python_app_seed.utils import get_data_files


DIRS = ['deb']
REWRITES = [('deb', '/')]
EXCLUDE_DIRS = []
EXCLUDE_FILES = ['.*.swp']


setup(
    name='python_app_seed',
    version='0.0.1',
    author='Your Name',
    author_email='your+name@example.com',
    url='http://example.com/',
    description='Very cool app',
    long_description=(
        'Long long long long long '
        'description.'),
    packages=['python_app_seed'],
    data_files=get_data_files(DIRS, REWRITES, EXCLUDE_DIRS, EXCLUDE_FILES),

    # Place all package dependencies in this section. There is not need
    # in requirements.txt or whatever hacky solutions.
    install_requires=[
        'requests==1.2.3',
        'Flask==0.9',
        'python-github==0.1',
    ],
    # If some of the dependencies doesn't present on PyPi you could
    # specify link to it here. See
    # http://pythonhosted.org/distribute/setuptools.html for the
    # details.
    dependency_links=[
        'git+https://github.com/jmoiron/python-github#egg=python-github-0.1',
    ],
    # Dependencies only for tests.
    tests_require=[
        'pytest==2.3.5',
        'coverage==3.6',
    ],
)
