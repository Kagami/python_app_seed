###
# This Makefile only make sense for developers and CI build bots.
# It provides some shortcuts for common routine operations.
###

VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Build bots could pass this option in environment so generated packages
# will have it in version. Use something like `BUILD_NUMBER=123 make deb'
BUILD_NUMBER?=0

# Just to be sure what empty `make' command won't do anything unexpectable
all:

# Provide only debian-based example here since it be the most popular
install-debian-deps:
	sudo apt-get install python-virtualenv python-all debhelper fakeroot

# Create python environment
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

# Build package
deb: clean data
	./setup.py sdist
	mkdir deb_dist
	tar -C deb_dist -xvf dist/python_app_seed-*.tar.gz
	./fix-version.sh $(BUILD_NUMBER)
	cd deb_dist/python_app_seed-*; dpkg-buildpackage -b -us -uc

clean:
	rm -rf build dist deb_dist python_app_seed.egg-info *.egg

mrproper: clean clean-env
	find -name '*.pyc' -delete
