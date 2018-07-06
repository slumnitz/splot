"""
Integration of different interactive and static plots with set backend option
"""



def lisa_cluster():
    '''
    joint doc
    '''
    if splot._backend == 'mpl':
        return lisa_cluster(moran_loc,gdf, p=p, ax=ax)
    if splot._backend == 'bk':
        return lisa_cluster(moran_loc, gdf, p=p, tool='')

set_backend('bk')

lisa_cluster(moran_loc, gdf, p, tool)