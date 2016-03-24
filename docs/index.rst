.. datreant documentation master file

================================================================
datreant.data: convenient data storage and retrieval for Treants
================================================================
This `datreant`_ submodule adds a convenience interface for `numpy`_ and
`pandas`_ data storage and retrieval using `HDF5`_ within a Treant's directory
structure. It provides the ``data`` limb for Treants, Trees, Bundles, and Views
from `datreant.core`_.

.. _`datreant`: http://datreant.org/
.. _`numpy`: http://www.numpy.org/
.. _`pandas`: http://pandas.pydata.org/
.. _`HDF5`: https://www.hdfgroup.org/HDF5/whatishdf5.html

.. _`datreant.core`: http://datreant.readthedocs.org/en/latest/

Getting datreant.data
=====================
See the :doc:`installation instructions <install>` for installation details.
The package itself is pure Python, but it is dependent on `HDF5`_ libraries
and the Python interfaces to these.

If you want to work on the code, either for yourself or to contribute back to
the project, clone the repository to your local machine with::

    git clone https://github.com/datreant/datreant.git

.. _`HDF5`: https://www.hdfgroup.org/HDF5/whatishdf5.html

Contributing
============
This project is still under heavy development, and there are certainly rough
edges and bugs. Issues and pull requests welcome! Check out our `contributor's guide`_
to learn how to get started with contributing back.

.. _`contributor's guide`: http://datreant.readthedocs.org/en/latest/contributing.html

--------------------------------------------------------------------------------

.. toctree::
    :caption: User Documentation
    :maxdepth: 1

    install
    treants
    trees
    view_bundles
    api 

.. toctree::
    :maxdepth: 1
    :caption: For Developers

    contributing
