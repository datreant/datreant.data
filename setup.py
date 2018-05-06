#! /usr/bin/python
"""Setuptools-based setup script for datreant.data.

For a basic installation just type the command::

  python setup.py install

"""

from setuptools import setup, find_packages

setup(name='datreant.data',
      version='0.7.1',
      description='convenient data storage and retrieval in HDF5 for Treants',
      author='David Dotson',
      author_email='dotsdl@gmail.com',
      url = 'http://datreant.org/',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      packages=find_packages('src'),
      namespace_packages=['datreant'],
      package_dir={'': 'src'},
      scripts=[],
      license='BSD',
      long_description=open('README.rst').read(),
      install_requires=[
          'datreant.core==0.7.1',
          'six',
          'numpy',
          'pandas',
          'tables',
          'h5py',
          ]
      )
