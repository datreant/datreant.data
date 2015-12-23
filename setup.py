#! /usr/bin/python
"""Setuptools-based setup script for datreant.data.

For a basic installation just type the command::

  python setup.py install

"""

from setuptools import setup

setup(name='datreant.data',
      version='0.6.0-dev',
      author='David Dotson',
      author_email='dotsdl@gmail.com',
      packages=[
          'datreant.data',
          'datreant.data.tests'],
      scripts=[],
      license='BSD',
      long_description=open('README.rst').read(),
      dependency_links=[
      'http://github.com/datreant/datreant/tarball/develop#egg=datreant-0.6.0-dev',
      ],
      install_requires=[
          'datreant>=0.6.0-dev',
          'numpy',
          'pandas',
          'tables',
          'h5py',
          ]
      )
