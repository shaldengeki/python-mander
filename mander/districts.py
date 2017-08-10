import geopandas as gpd


class district(object):

    def __init__(self, pathToGeojsonOrShapefile, epsg='2163'):
        self.epsg = epsg
        self.gdf = gpd.read_file(pathToGeojsonOrShapefile)
        if not self.gdf.crs:
            self.gdf.crs = {'init': 'epsg:4326'}
        self.gdf = self.gdf.to_crs(epsg=self.epsg)
        self.area = self.gdf.area.values[0]
        self.perimeter = self.gdf.length.values[0]
        self.x, self.y = self.gdf.geometry[0].exterior.coords.xy
        self.coordPairs = zip(self.x, self.y)
