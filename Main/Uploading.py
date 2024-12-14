import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# shapefile = gpd.read_file("Main/PCON_JULY_2024_UK_BSC.shp")
csvfile = pd.read_csv("Main/foi20190080data.csv")

# print(shapefile.info())
print(csvfile.info())

# merged_data = shapefile.merge(csvfile, left_on='PCON24NM', right_on='PCON11NM')

# print(merged_data.info())

# fig, ax = plt.subplots(figsize=(10, 10))

# shapefile.plot(ax=ax, color='lightgrey', edgecolor='black')

# merged_data.plot(column='Mid-2018', ax=ax, cmap='OrRd')

# plt.title('Map with Data from CSV')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.show()

# shapefile.plot()

# crs = ccrs.PlateCarree()


# crs_proj4 = crs.proj4_init
# shapefile_ae = shapefile.to_crs(crs_proj4)

# shapefile_ae.plot()
# plt.show()