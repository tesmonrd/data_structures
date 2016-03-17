# _*_ coding utf-8 _*_
"""Setup."""
from setuptools import setup

setup(
    name="queue",
    description="Priortiy Queue Data Structure",
    version=0.1,
    author="Munir Ibrahim",
    author_email="mibrah04@gmail.com",
    license="MIT",
    py_modules=["priorityq"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)