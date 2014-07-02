"""
    python_app_seed.config
    ~~~~~~~~~~~~~~~~~~~~~~

    This module provides wrapper around PyYAML and initialization
    facilities. The main point is that you don't need to keep
    reference to config dict after initialization and pass it all
    the time. Instead you just import mutable reference and it will
    contain all data when you need it.

    Usage example:

    >>> # Start point of your application
    >>>
    >>> from python_app_seed.config import init_config
    >>>
    >>> def main():
    >>>     init_config('/path/to/config.yaml')
    >>>
    >>> if __name__ == '__main__':
    >>>     main()

    >>> # Inside some module of your app
    >>>
    >>> import requests
    >>> from python_app_seed.config import config
    >>>
    >>> def get_page():
    >>>     page = requests.get('http://' + config.host + ':' + config.port)
    >>>     return page

    You could simple delete this module (and also dependency in
    setup.py) if you don't like it and want to use something like
    ConfigParser.

    Note that your config toplevel structure should be a dict
    otherwise this module doesn't make much sense. You still could
    use config.items though.
"""

import yaml


class _ConfigDict(object):
    """
    Proxy around dict. It allows you do some of the dict things:

    >>> config['item'] = 1
    >>> config.get('item', 1)

    and also nice syntactic sugar like this:

    >>> config.item
    >>> config.item = 1
    """

    def __init__(self):
        self.set_items({})

    def clear(self):
        """Remove all items from config dict."""
        self.set_items({})

    @property
    def items(self):
        """All items in the config dict."""
        return self._items

    def set_items(self, items):
        """Set config dict. Useful for initialization."""
        object.__setattr__(self, '_items', items)

    def __getattr__(self, name):
        if name not in self._items:
            raise AttributeError('No "{0}" config option.'.format(name))
        else:
            return self._items[name]

    def __getitem__(self, key):
        if key not in self._items:
            raise KeyError('No "{0}" config option.'.format(key))
        else:
            return self._items[key]

    def get(self, name, default=None):
        """
        Similar to dict.get return element from config or just
        default value.
        """
        return self._items.get(name, default)
        
    def __iter__(self):
        return self._items.__iter__()

    def next(self):
        return self._items.next()

    def __setattr__(self, name, value):
        self._items[name] = value

    def __setitem__(self, key, value):
        self._items[key] = value


config = _ConfigDict()


def init_config(path):
    """
    Load YAML config from the specified path and init proxy wrapper.
    """
    items = yaml.load(open(path))
    config.set_items(items)
