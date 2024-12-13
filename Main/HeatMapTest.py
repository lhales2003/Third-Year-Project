import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from shapely.geometry import Point

points = gpd.GeoDataFrame({'geometry': [Point(-10, -10), Point(60, 60)]}, crs="EPSG:4326")

ax = plt.axes(projection=ccrs.PlateCarree())

ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)

ax.set_global()

points.plot(ax=ax, marker='o', color='red', markersize=20)

plt.show()
