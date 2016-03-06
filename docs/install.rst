========================
Installing datreant.data
========================
There are no official releases of datreant.data yet, but the master branch on
GitHub gives the most current state of the package. 

First install the dependencies. Since datreant.data uses HDF5 as the file
format of choice for persistence, you will need to install the libraries either
using your package manager or manually. 

On Ubuntu 14.04 this will be ::

    apt-get install libhdf5-serial-1.8.4 libhdf5-serial-dev

and on Arch Linux ::
   
    pacman -S hdf5
    
PyTables can be particularly picky, and it often fails to obtain its own
dependencies. It is best to first install PyTables' dependencies explicitly ::

    pip install numpy numexpr Cython

Then install PyTables and everything else ::
    
    pip install tables 
    pip install pandas h5py scandir

Then clone the repository and switch to the master branch ::

    git clone git@github.com:datreant/datreant.data.git
    cd datreant.data
    git checkout master

Installation of the packages is as simple as ::

    pip install .

This installs datreant in the system wide python directory; this may
require administrative privileges.

It is also possible to use ``--prefix`` or ``--user`` options for
pip to install in a different (probably your private) python directory
hierarchy. ``python setup.py install --help`` should show you your options.
