import satsearch

SentinelSTAC = satsearch.Search.search( url = "https://earth-search.aws.element84.com/v0" )
print("Found ",SentinelSTAC.found(),"items")

from json import load
import os
import geopandas as gpd


shapefile = gpd.read_file("/Users/sofiasinoti/Downloads/zonas_vinhas/zona1.shp")
shapefile.to_file("zona1.geojson")
file_path = "zona1.geojson"
file_content = load(open(file_path))
geometry = file_content["features"][0]["geometry"]
print(geometry)

import satsearch
timeRange = '2022-05-01/2022-06-01'

SentinelSearch = satsearch.Search.search(
    url = "https://earth-search.aws.element84.com/v0",
    intersects = geometry,
    datetime = timeRange,
    collections = ['sentinel-s2-l2a'])

Sentinel_items = SentinelSearch.items()

for item in Sentinel_items:
    red_s3 = Sentinel_items[0].assets['B04']['href']
    print(red_s3)
