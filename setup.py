# _*_ coding utf-8 _*_
"""Setup."""
from setuptools import setup

setup(
    name="proper_parenthetics",
    description="Proper Parenthetics Quiz",
    version=0.1,
    author="Munir Ibrahim",
    author_email="mibrah04@gmail.com",
    license="MIT",
    py_modules=["proper_parenthetics"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
