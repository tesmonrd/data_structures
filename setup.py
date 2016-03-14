# _*_ coding utf-8 _*_
"""Setup for the deque data structure."""
from setuptools import setup

setup(
    name="deque",
    description="Deque data structure.",
    version=0.1,
    author="Munir Ibrahim",
    author_email="mibrah04@gmail.com",
    license="MIT",
    py_modules=["deque"],
    package_dir={'': 'deque'},
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
