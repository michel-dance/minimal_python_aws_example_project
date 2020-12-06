import setuptools

setuptools.setup(
    name="merkle_example",
    version="1.0.0",
    description="a simple merkle tree demonstration",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'})
