from setuptools import setup, find_packages
import unittest
import doctest
import os

requirements = ["black>=18.9b0", "loguru>=0.2.5"]

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
    entry_points={"console_scripts": "blackbook=blackbook.__main__:main"},
)
