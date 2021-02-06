import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_reqs = [x.strip() for x in all_reqs if 'git+' not in x]
dep_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' in x]

setuptools.setup(
    name="python_project_template",
    version="1.0.31337",
    description="provides the capability to generate features",
    packages=setuptools.find_packages(where='src', exclude=['python', 'tests', 'infrastructure']),
    include_package_data=True,
    install_requires=install_reqs,
    package_dir={'': 'src'},
    dependency_links=dep_links)
