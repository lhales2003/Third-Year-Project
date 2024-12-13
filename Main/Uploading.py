import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the shapefile
shapefile = gpd.read_file("Main/NUTS_Level_1_January_2018_FEB_in_the_United_Kingdom.shp")

shapefile.plot()

crs = ccrs.PlateCarree()


crs_proj4 = crs.proj4_init
shapefile_ae = shapefile.to_crs(crs_proj4)

shapefile_ae.plot()
plt.show()