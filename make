#!/usr/bin/make -f

###
# This Makefile only make sense for developers and CI build bots.
# It provides some shortcuts for common routine operations.
#
# Note that this file should be invoked using `./make' and cannot
# be named as `Makefile' because of some strange debian/rules
# behaviour while building package.
###

VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Just to be safe what empty `make' command won't do anything
# unexpectable.
all:

# Provide only debian-based example here since it be the most popular
install-debian-deps:
	sudo apt-get install python-virtualenv python-all debhelper fakeroot

# Manage python environment
env:
	virtualenv $(VENV)

clean-env:
	rm -rf $(VENV)

re-env: clean-env env

# Install all python dependencies in separate python environment
install-deps: env
	$(PIP) install -e .

# Place your application-related start logic here
run:
	$(PYTHON) python_app_seed/main.py

# Preprocess additional data files
.PHONY: data
data:
	cp python_app_seed.yaml.example \
		data/etc/python_app_seed/python_app_seed.yaml

deb: clean data
	dpkg-buildpackage -b -us -uc
	# XXX: Files shouldn't go to the outside dir
	rm ../python-app-seed_*.changes
	mkdir -p dist/deb/
	mv ../python-app-seed_*.deb dist/deb/

clean:
	rm -rf build dist python_app_seed.egg-info *.egg debian/python-app-seed*
	rm -rf debian/files

mrproper: clean clean-env
