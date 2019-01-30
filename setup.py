import doctest
import os
import unittest

from setuptools import find_packages, setup

requirements = ["black>=18.9b0", "loguru>=0.2.5"]

with open("README.md", "r") as readme:
    README = readme.read()

exec(open("src/blackbook/version.py", "r").read())

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
    long_description=README,
    entry_points={"console_scripts": "blackbook=blackbook.__main__:main"},
)
