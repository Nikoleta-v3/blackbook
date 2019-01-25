from setuptools import setup, find_packages
import unittest
import doctest
import os

requirements = ["black>=18.9b0"]

# Read in the version number
<<<<<<< 4419fc7fdbd89008a0eb9b57b584a00b873b86df
exec(open("axelrod/version.py", "r").read())
=======
exec(open("src/blackbook/version.py", "r").read())
>>>>>>> Add a version number.

setup(
    name="blackbook",
    version=__version__,
    install_requires=requirements,
    author="Nikoleta Glynatsi, Vince Knight, Henry Wilde",
    author_email=("glynatsine@cardiff.ac.uk"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="",
    license="The MIT License (MIT)",
    description="`Black` for Jupyter notebooks.",
    entry_points={"console_scripts": "blackbook=blackbook.__main__:main"},
)
