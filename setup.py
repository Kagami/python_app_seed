#!/usr/bin/env python

import os
import os.path as path
import fnmatch
from itertools import chain
from setuptools import setup, find_packages


def get_data_files(dirs, rewrites, exclude_dirs, exclude_files):
    """
    Collect data from the specified dirs and provide them in
    distutils-friendly format.
    """
    def _get_data_files(topdir):
        data_files = []
        for dirname, dirnames, filenames in os.walk(topdir):
            if dirname in exclude_dirs:
                continue
            files = []
            for filename in filenames:
                for pattern in exclude_files:
                    if fnmatch.fnmatch(filename, pattern):
                        break
                else:
                    files.append(path.join(dirname, filename))
            if not files:
                continue
            location = None
            for from_d, to_d in rewrites:
                if dirname.startswith(from_d):
                    location = path.join(to_d, path.relpath(dirname, from_d))
                    location = path.normpath(location)
            if location is None:
                location = dirname
            data_files.append((location, files))
        return data_files

    files = map(_get_data_files, dirs)
    # Flatten list
    return list(chain.from_iterable(files))


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
    packages=find_packages(exclude=['tests']),

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
    # You could tune settings with the variables above.
    data_files=get_data_files(DIRS, REWRITES, EXCLUDE_DIRS, EXCLUDE_FILES),
)
