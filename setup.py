# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="cfbs",
    version="0.1.0",
    description="CFEngine argument refactor",
    license="MIT",
    author="Lars Erik Wik",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["cfbs = cfbs.main:main"]},
)
