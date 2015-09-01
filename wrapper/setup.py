from setuptools import setup, find_packages

setup(
    name="cxxnet_lib",
    version="0.1.0",
    packages=find_packages(exclude=["*.tests"]),
    scripts=[],

    # python dependency
    install_requires=['numpy==1.9.2'],

    # Additional files
    package_data={
        # C++ Lib (FIXME: support for Linux only)
        '': ['libcxxnetwrapper.so'],
    },

    # metadata for upload to PyPI
    author="",
    author_email="",
    description="CXXNET Lib wrapper for python.",
    license="",
    keywords="cxxnet, deep learning",
)
