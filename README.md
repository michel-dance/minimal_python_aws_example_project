# python_project_template #

This repo provides a complete example for a PRO ptyhon
package that you and your fellow developer will be proud of.

**It provides:**
 
* a pip installable package.
* a main entry point, so you can run as a pip module
* a pytest based testing framework
* example commands for various workflows.

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
python3 -m pip uninstall merkle_example

# run the package main
python3 -m merkle_example
````





