REVISION?=0

all:

# Create python environment
env:
	sudo apt-get install python-virtualenv
	virtualenv .venv

# Install basic deps
install-deps: env
	.venv/bin/pip install -r requirements.txt

run:
	echo "Not implemented yet"

deb: clean
	cp python_app_seed.cfg.example deb/etc/python_app_seed/python_app_seed.cfg
	.venv/bin/python setup.py --command-packages=stdeb.command \
		sdist_dsc --debian-version=$(REVISION) bdist_deb

clean:
	rm -rf build dist deb_dist python_app_seed.egg-info
