# Minimal Example Project

This repo provides a complete example for a PRO Python
project that you and your fellow developers will be proud of.

**It provides:**
 
* a pip installable project.
* module entry point examples, so you can run your modules from the command line.
* a pytest based testing framework.
* example commands for various workflows.
* scripts to publish project to AWS CodeArtifact PyPi repo & AWS ECR Docker Registry.

## Developer Workflows ##

### Initialize the python project ###

This you only do once after you clone this repo.
````
# setup your environment to put all python dependencies in the env folder
python3 -m venv env

# set python path to use our isolated python environment
. env/bin/activate

# install the package in editable mode so you can
# develop & test without having to reinstall the package
python3 -m pip install -e ./
````

### Development & Testing ###

This you do every time open a new shell to develop, run, and test your code.
````
# set python path to use our isolated python environment
. env/bin/activate

# install project dependencies
python3 -m pip install -r requirements.txt

# add a project dependency
python3 -m pip install <new dependency>

# then you need to save the dependency
python3 -m pip freeze > requirements.txt

# run all tests
python3 -m pytest

# install the package in non editable mode
python3 -m pip install ./

# uninstall the package
python3 -m pip uninstall minimal_example_project

# run the package main
python3 -m example
````





