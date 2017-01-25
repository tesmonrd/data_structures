from setuptools import setup

setup(
    name="graphtrav",
    description="Graph Traversal data structure.",
    version=0.1,
    author="Munir Ibrahim and Rick Tesmond",
    author_email="mibrah04@gmail.com",
    license="MIT",
    py_modules=["graphtrav"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
