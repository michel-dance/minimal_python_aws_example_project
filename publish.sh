#!/bin/bash

rm -fr build
rm -fr dist

python3 -m pip install --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel
# publish to our AWS PyPi repo
#python3 -m twine upload --repository codeartifact dist/*

python3 -m  pip install twine
