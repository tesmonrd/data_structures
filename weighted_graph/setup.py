"""Setup for the SimpleGraph data structure."""
from setuptools import setup

setup(
    name="weighted_graph",
    description="Weighted edge data structure.",
    version=0.1,
    author="Munir Ibrahim and Rick Tesmond",
    author_email="mibrah04@gmail.com",
    license="MIT",
    py_modules=["weighted"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
