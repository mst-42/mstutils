"""
Manage developer assigned UUIDs
"""
from __future__ import (
    print_function, division, unicode_literals, absolute_import,
)

import io
import os
import sys

def get_basedir():
    """
    Current directory of this file
    """
    return os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))

def get_csv_path():
    """
    Return the project.csv path
    """
    return os.path.join(
        get_basedir(), 'projects.csv'
    )

def main():
    """
    Dump the CSV contents
    """
    with io.open(get_csv_path(), 'r', encoding='utf-8') as fobj:
        for line in fobj:
            print(line.rstrip('\r\n'))

if __name__ == '__main__':
    main()
