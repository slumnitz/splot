"""
``splot.test_esda``
===============

Provides static and interactive visualisations for the `esda` subpackage.
`esda` provides tools for exploratory spatial data analysis that consider the role of space in a distribution of attribute values.

Moran Local analytics
---------------------

.. autosummary::
   :toctree: generated/
   
   moran_loc_scatterplot
   lisa_cluster
   plot_local_autocorrelation

"""

from ._viz_integrate_backend import (moran_loc_scatterplot,
                                     lisa_cluster,
                                     plot_local_autocorrelation)