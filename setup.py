from setuptools import setup, find_packages

VERSION = '0.0.2'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='piptests',
    version=VERSION,
    description='Pop Tests',
    author="Rogerio Riffel",
    author_email="riffel.rogerio@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "astropy",
        "matplotlib",
        "scipy"
    ]
)