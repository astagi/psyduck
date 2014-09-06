#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="psyduck",
      py_modules=['psyduck'],
      version="0.1dev",
      description="Python API for Duckdns",
      license="MIT",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="https://github.com/astagi/psyduck",
      keywords= "dyndns dns duckdns",
      install_requires=[
        "requests",
      ],
      zip_safe = True)