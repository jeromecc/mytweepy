#!/usr/bin/env python

import re
from setuptools import find_packages, setup

VERSION_FILE = "mytweepy/__init__.py"
with open(VERSION_FILE) as version_file:
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                      version_file.read(), re.MULTILINE)

if match:
    version = match.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="mytweepy",
    version=version,
    description="Twitter library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Joshua Roesslein",
    author_email="tweepy@googlegroups.com",
    url="https://www.tweepy.org/",
    project_urls={
        "Documentation": "https://tweepy.readthedocs.io",
        "Issue Tracker": "https://github.com/tweepy/tweepy/issues",
        "Source Code": "https://github.com/jeromecc/mytweepy",
    },
    download_url="https://pypi.org/project/tweepy/",
    packages=find_packages(),
    install_requires=[
        "oauthlib>=3.2.0,<4",
        "requests>=2.27.0,<3",
        "requests-oauthlib>=1.2.0,<2",
    ],
    extras_require={
        "async": [
            "aiohttp>=3.7.3,<4",
            "async-lru>=1.0.3,<2"
        ],
        "dev": [
            "coverage>=4.4.2",
            "coveralls>=2.1.0",
            "tox>=3.21.0",
         ],
        "socks": ["requests[socks]>=2.27.0,<3"],
        "test": ["vcrpy>=1.10.3"],
    },
    test_suite="tests",
    keywords="twitter library",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    zip_safe=True,
)
