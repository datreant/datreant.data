========================
Installing datreant.data
========================
Since ``datreant.data`` uses HDF5 as the file format of choice for persistence,
you will first need to install the HDF5 libraries either using your package
manager or manually. 

On Ubuntu 14.04 this will be ::

    apt-get install libhdf5-serial-1.8.4 libhdf5-serial-dev

and on Arch Linux ::
   
    pacman -S hdf5

You can then install ``datreant.data`` from `PyPI <https://pypi.python.org/>`_
using pip::

    pip install datreant.data

It is also possible to use ``--user`` to install into your user's site-packages
directory::

    pip install --user datreant.data

Dependencies
============
The dependencies of ``datreant.data`` are:

- `pandas`_: 0.16.1 or higher
- `PyTables`_: 3.2.0 or higher
- `h5py`_: 2.5.0 or higher

.. _`pandas`: http://pandas.pydata.org/
.. _`PyTables`: http://www.pytables.org/
.. _`h5py`: http://www.h5py.org/

These are installed automatically when installing with pip.

Installing from source
======================
To install from source, clone the repository and switch to the master branch ::

    git clone git@github.com:datreant/datreant.data.git
    cd datreant.data
    git checkout master

Installation of the packages is as simple as ::

    pip install .

This installs ``datreant.data`` in the system wide python directory; this may
require administrative privileges.

It is also possible to use ``--user`` to install into your user's site-packages
directory::

    pip install --user .
