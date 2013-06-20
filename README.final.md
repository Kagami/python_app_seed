# python_app_seed

Project description.

### Dependencies

Install dependencies via:

    $ make install-debian-deps  # Binary deps
    $ make install-deps  # Python deps

(First command assume what you have Debian-based distro.)

### Config

Copy example stub:

    $ cp python_app_seed.yaml.example python_app_seed.yaml

And edit it inside your favourite text editor.

### Run

    $ make run

### Create deb package

Bump version in setup.py (recommended) and run:

    $ make deb

You could pass BUILD\_NUMBER environment variable to set
debian\_revision number (useful when build on CI bot):

    $ BUILD_NUMBER=123 make deb

### Manage virtual environment

    $ make env
    $ make clean-env
    $ make re-env

### Other

Don't fear to look at Makefile to find some delicious shortcut.
Or maybe add your own.
