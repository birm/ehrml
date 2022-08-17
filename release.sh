#! /usr/bin/env bash

# Make sure to update the setup.py version number first.
pip install -r requirements.txt
pytest

python3 -m build

python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
