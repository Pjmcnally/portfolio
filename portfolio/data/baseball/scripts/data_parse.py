#!/usr/bin/env python

"""A module to parse data and save it to a datase

This module is designed to parse the files stored in the data folder.
These files originated on the retrosheets webside and are stored as comma
seperated value .txt files.

Example:
    $ python data_parse.py

To Do:
    This is a work in progress.  Everything needs to be done.

"""

# Lines 4-7 import and establis a Django environment with all local settings
# and variables so that this script can directly interact with models/database.
import os
import sys
proj_path = "/home/pjmcnally/programming/portfolio/portfolio/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
sys.path.append(proj_path)
import django  # noqa
django.setup()


# Lines 12-17 are normal imports. "# noqa" disables the linter for that line.
import re # noqa
from baseball.models import (Player)   # noqa
from django.utils.text import slugify  # noqa

def main():
    data_path = '../../baseball/data'
    data_ext = ['.txt']


if __name__ == '__main__':
    main()
