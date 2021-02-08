#!/bin/bash

set -e

rm -fr build
rm -fr dist

aws codeartifact login --tool pip --repository private --domain f1kart --domain-owner ${AWS_ACCOUNT} --profile ${AWS_PROFILE}
python3 -m pip install --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m  pip install twine

aws codeartifact login --tool twine --repository private --domain f1kart --domain-owner ${AWS_ACCOUNT} --profile ${AWS_PROFILE}

twine check dist/*
twine upload --repository codeartifact dist/*
