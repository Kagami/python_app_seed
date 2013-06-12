###
# This Makefile only make sense for developers and CI build bots.
# It just provides some shortcuts for common routine operations.
###

VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Build bots could pass this option in environment so generated packages
# will have it in version.
BUILD_NUMBER?=0

# Just to be safe what empty `make' command won't do anything
# unexpectable.
all:

# Provide only debian-based example here since it be the most popular
install-debian-deps:
	sudo apt-get install python-virtualenv

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

deb: clean
	cp python_app_seed.cfg.example deb/etc/python_app_seed/python_app_seed.cfg
	$(PYTHON) setup.py --command-packages=stdeb.command \
		sdist_dsc --debian-version=$(BUILD_NUMBER) bdist_deb

clean:
	rm -rf build dist deb_dist python_app_seed.egg-info *.egg

mrproper: clean clean-env
