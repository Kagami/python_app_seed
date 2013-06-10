#!/usr/bin/env python

from distutils.core import setup

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
)
