#!/bin/sh

set -e

###
# Don't run it by hand, it automatically called by Makefile deb target.
#
# Fix version of the generated debian package using version in setup.py
# and passed BUILD_NUMBER.
# Usage: `fix-version.sh <BUILD_NUMBER>'
###

version="`./setup.py --version`-$1"
sed -i "1 s/(99999)/($version)/" deb_dist/*/debian/changelog
