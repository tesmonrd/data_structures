"""Setup for the SimpleGraph data structure."""
from setuptools import setup

setup(
    name="shortest distance",
    description="Find the shortest distance b/t nodes.",
    version=0.1,
    author="Munir Ibrahim and Rick Tesmond",
    author_email="mibrah04@gmail.com",
    license="MIT",
    py_modules=["shortest"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
