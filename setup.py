import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_reqs = [x.strip() for x in all_reqs if 'git+' not in x]
dep_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' in x]

# read the contents of your README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="minimal_aws_example_project",
    version="1.0.4",
    author='Michel Lacle',
    author_email='michel+pypi@f1kart.com',
    url='https://github.com/michel-lacle/minimal_aws_example_project',
    description="a minimal Python project example with unit testing, command line interface, PyPi publishing capabilities",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(where='src', exclude=['env', 'tests', 'infrastructure']),
    include_package_data=True,
    install_requires=install_reqs,
    package_dir={'': 'src'},
    dependency_links=dep_links)
