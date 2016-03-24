================================================================
datreant.data: convenient data storage and retrieval for Treants
================================================================

|docs| |build| |cov|

This `datreant`_ submodule adds a convenience interface for `numpy`_ and
`pandas`_ data storage and retrieval using `HDF5`_ within a Treant's directory
structure. It provides the ``data`` limb for Treants, Trees, Bundles, and Views
from `datreant.core`_.

See the ``datreant.data`` `documentation`_ for information on how to use this
submodule.

For more information on what **datreant** is and what it does, check out the
`official documentation`_.

.. _`documentation`: http://datreantdata.readthedocs.org/
.. _`official documentation`: http://datreant.readthedocs.org/

.. _`datreant`: http://datreant.org/
.. _`numpy`: http://www.numpy.org/
.. _`pandas`: http://pandas.pydata.org/
.. _`HDF5`: https://www.hdfgroup.org/HDF5/whatishdf5.html

.. _`datreant.core`: https://github.com/datreant/datreant.core

Getting datreant.data
=====================
See the `installation instructions`_ for installation details.

If you want to work on the code, either for yourself or to contribute back to
the project, clone the repository to your local machine with::

    git clone https://github.com/datreant/datreant.data.git

.. _`installation instructions`: http://datreantdata.readthedocs.org/en/develop/install.html

Contributing
============
This project is still under heavy development, and there are certainly rough
edges and bugs. Issues and pull requests welcome! 

Check out our `contributor's guide`_ to learn how to get started with
contributing back.

.. _`contributor's guide`: http://datreant.readthedocs.org/en/develop/contributing.html

.. |docs| image:: http://readthedocs.org/projects/datreantdata/badge/?version=develop
    :target: http://datreantdata.readthedocs.org/en/develop/?badge=develop
    :alt: Documentation Status

.. |build| image:: https://travis-ci.org/datreant/datreant.data.svg?branch=develop
    :target: https://travis-ci.org/datreant/datreant.data

.. |cov| image:: https://codecov.io/github/datreant/datreant.data/coverage.svg?branch=develop
    :target: https://codecov.io/github/datreant/datreant.data?branch=develop
