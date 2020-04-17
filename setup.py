import doctest
import os
import unittest
from pathlib import Path

from setuptools import find_packages, setup

requirements = ["black>=18.9b0", "loguru>=0.2.5"]

this_directory = Path(__file__).parent.resolve()
with open(Path(this_directory).joinpath("README.md"), encoding="utf-8") as readme_md:
    README = readme_md.read()

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
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": "blackbook=blackbook.__main__:main"},
)
