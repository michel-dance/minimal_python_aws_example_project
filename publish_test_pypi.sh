#!/bin/bash

set -e

rm -fr build
rm -fr dist

python3 -m pip install --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel

python3 -m  pip install twine

twine check dist/*

twine upload --repository-url https://test.pypi.org/legacy/ dist/*
