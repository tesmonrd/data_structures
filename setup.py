# -*- coding: utf8 -*-

from setuptools import setup


setup(
    name="data-structures",
    description="explore types of data-structures without python buit-ins",
    version=0.1,
    author="Rick Tesmond and Munir Ibrahim",
    lisence="MIT",
    py_modules=["data-structures"],
    package_dir={"": "doubele-linked-list", "": "stack", "": "linked-list", "": "queue"},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
