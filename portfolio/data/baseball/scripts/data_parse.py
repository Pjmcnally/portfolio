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
from datetime import datetime as dt
proj_path = "/home/pjmcnally/programming/portfolio/portfolio/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
sys.path.append(proj_path)
import django  # noqa
django.setup()


# Lines 12-17 are normal imports. "# noqa" disables the linter for that line.
import re # noqa
from baseball.models import (Player)   # noqa
from django.utils.text import slugify  # noqa


def add_player_code_data():
    file = '../players/playercodes.txt'
    with open(file) as f:
        players = f.readlines()

    for player in players:
        player = player.strip().split(',')

    f_name = player[0]
    l_name = player[1]
    ret_code = player[2]
    date = dt.strptime(player[3], "%d/%m/%Y").strftime('%Y-%m-%d')

    obj, created = Player.objects.get_or_create(
        last_name=f_name,
        first_name=l_name,
        ret_code=ret_code,
        first_appearance=date)

    print(obj)


def main():
    add_player_code_data()


if __name__ == '__main__':
    main()
