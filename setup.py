from setuptools import setup
from setuptools import find_packages

__version__ = "0.0.1"

setup(
    name="mypackage",
    version=__version__,
    description="test package",
    long_description="""
    This is test package.
    """,
    author="Yuka Miyake",
    url="https://github.com/piz3in/python_package_development",
    license="MIT",
    package_dir={"": "src", "resource": "resource"},
    packages=find_packages(where="src", exclude=("tests")),
)
