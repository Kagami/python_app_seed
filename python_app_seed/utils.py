import os
import os.path as path
import fnmatch
from itertools import chain

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
