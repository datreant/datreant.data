#! /usr/bin/python
"""Setuptools-based setup script for datreant.data.

For a basic installation just type the command::

  python setup.py install

"""

from setuptools import setup, find_packages

setup(name='datreant.data',
      version='0.6.0-dev',
      author='David Dotson',
      author_email='dotsdl@gmail.com',
      packages=find_packages('src'),
      namespace_packages=['datreant'],
      package_dir={'': 'src'},
      scripts=[],
      license='BSD',
      long_description=open('README.rst').read(),
      dependency_links=[
      'http://github.com/datreant/datreant.core/tarball/develop#egg=datreant.core-0.6.0-dev',
      ],
      install_requires=[
          'datreant.core',
          'numpy',
          'pandas',
          'tables',
          'h5py',
          ]
      )
