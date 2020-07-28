from setuptools import setup, find_packages

setup(
    name="package_testing",
    version="0.1",
    description="this is for testing pip package",
    url="https://github.com/smrati/package_testing",
    author="smrati",
    author_email="smrati.katiyar@abcd.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=False)