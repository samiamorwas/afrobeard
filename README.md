afrobeard
=========

## Setup

First, install [virtualenv](http://www.virtualenv.org/en/latest/#installation).

Then clone this repo:

`git clone https://github.com/samiamorwas/afrobeard.git`

Then, create a virtual environment called flask:

`cd afrobeard`

`virtualenv flask`

Then install the requirements with:

`flask/bin/pip install -r requirements.txt`

## Since we're currently using sqlite, create the database

`./db_create.py`

Then update the database with:

`./db_upgrade.py`
