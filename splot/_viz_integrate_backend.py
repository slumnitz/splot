"""
Integration of different interactive and static plots with set backend option
"""

def lisa_cluster(moran_loc, gdf, p=0.05,
                 ax=None, legend=True, legend_kwds=None, **kwargs,
                 title=None, plot_width=500, plot_height=500,
                 region_column='', tools=''):
    """
    Create a LISA Cluster map

    Global Parameters
    -----------------
    moran_loc : esda.moran.Moran_Local or Moran_Local_BV instance
        Values of Moran's Local Autocorrelation Statistic
    gdf : geopandas dataframe instance
        The Dataframe containing information to plot. Note that `gdf` will be
        modified, so calling functions should use a copy of the user
        provided `gdf`. (either using gdf.assign() or gdf.copy())
    p : float, optional
        The p-value threshold for significance. Points will
        be colored by significance.
    
    Matplotlib specific Parameters
    ------------------------------
    ax : matplotlib Axes instance, optional
        Axes in which to plot the figure in multiple Axes layout.
        Default = None
    legend : boolean, optional
        If True, legend for maps will be depicted. Default = True
    legend_kwds : dict, optional
        Dictionary to control legend formatting options. Example:
        ``legend_kwds={'loc': 'upper left', 'bbox_to_anchor': (0.92, 1.05)}``
        Default = None
    **kwargs : keyword arguments, optional
        Keywords used for creating and designing the plot.
        TODO geodataframe.plot
    
    Bokeh specific Parameters
    -------------------------
    title : str, optional
        Title of map. Default title=None
    plot_width : int, optional
        Width dimension of the figure in screen units/ pixels.
        Default = 500
    plot_height : int, optional
        Height dimension of the figure in screen units/ pixels.
        Default = 500
    region_column : str, optional
        Columname in geodataframe containing information that will be displayed
        through Bokeh hover, e.g. columnname containing region names.
        Default = ''.
    tools : str, optional
        Specific Bokeh tooltips, eg. 'hover'. Default =''


    Matplotlib specific Returns
    ---------------------------
    fig : matplotlip Figure instance
        Figure of LISA cluster map
    ax : matplotlib Axes instance
        Axes in which the figure is plotted
    
    Bokeh specific Returns
    ----------------------
    fig : Bokeh figure instance
        Figure of LISA cluster map, colored by local spatial autocorrelation
    

    Matplotlib Examples
    -------------------
    >>> import matplotlib.pyplot as plt
    >>> import libpysal.api as lp
    >>> from libpysal import examples
    >>> import geopandas as gpd
    >>> from esda.moran import Moran_Local
    >>> from splot.esda import lisa_cluster

    >>> link = examples.get_path('columbus.shp')
    >>> gdf = gpd.read_file(link)
    >>> y = gdf['HOVAL'].values
    >>> w = lp.Queen.from_dataframe(gdf)
    >>> w.transform = 'r'
    >>> moran_loc = Moran_Local(y, w)

    >>> fig = lisa_cluster(moran_loc, gdf)
    >>> plt.show()
    
    Bokeh Examples
    --------------
    >>> import libpysal.api as lp
    >>> from libpysal import examples
    >>> import geopandas as gpd
    >>> from esda.moran import Moran_Local
    >>> from splot.bk import lisa_cluster
    >>> from bokeh.io import show

    >>> link = examples.get_path('columbus.shp')
    >>> df = gpd.read_file(link)
    >>> y = df['HOVAL'].values
    >>> w = lp.Queen.from_dataframe(df)
    >>> w.transform = 'r'
    >>> moran_loc = Moran_Local(y, w)

    >>> TOOLS = "tap,reset,help"
    >>> fig = lisa_cluster(moran_loc, df, p=0.05, tools=TOOLS)
    >>> show(fig)
    """
    if splot._backend == 'mpl':
        return lisa_cluster(moran_loc, gdf, p=p, ax=ax,
                            legend=True, legend_kwds=None, **kwargs)
    if splot._backend == 'bk':
        return lisa_cluster(moran_loc, gdf, p=p, title=title,
                            plot_width=plot_width, plot_height=plot_height,
                            region_column=region_column, tools=tools)

