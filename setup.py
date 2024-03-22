# -*- coding: utf-8 -*-
 
"""setup.py: setuptools control."""
 
import re
from setuptools import setup
 
version = re.search(
        '^__version__\s*=\s*"(.*)"',
        open('enigme/__init__.py').read(),
        re.M
    ).group(1)
 
with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
      license="MIT",
      name = "enigme",
      packages = ["enigme"],
      install_requires=[
        'pandas','numpy'
      ],
      include_package_data=True,
      entry_points = {
        "console_scripts": ['enigme = enigme.cli:main']
      },
      version = version,
      description = "Python command line application for generating reasoning puzzles.",
      long_description = long_descr,
      long_description_content_type='text/markdown',
      author = "John Hawkins",
      author_email = "johnc@getting-data-science-done.com",
      url = "http://getting-data-science-done.com",
      project_urls = {
          'Documentation': "http://enigme.readthedocs.io",
          'Source': 'https://github.com/john-hawkins/enigme',
          'Tracker': 'https://github.com/john-hawkins/enigme/issues',
      },
    )


