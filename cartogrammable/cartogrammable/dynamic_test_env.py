import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from cg import CartogramGenerator

test_shapefile = gpd.read_file("cartogrammable/cartogrammable/PCON_JULY_2024_UK_BUC.shp")
test_csv_file = pd.read_csv("cartogrammable/cartogrammable/foi20190080data.csv")

print(test_shapefile.head())
print(test_shapefile.info())
print(test_csv_file.head())
print(test_csv_file.info())

print(test_shapefile["geometry"][0])

print(type(test_shapefile)) 
print(type(test_csv_file))
print(isinstance(test_shapefile, gpd.geodataframe.GeoDataFrame))
print(isinstance(test_csv_file, pd.core.frame.DataFrame))

print(list(test_shapefile.columns.values))
print(list(test_csv_file.columns.values))

test_csv_file["PCON24NM"] = test_csv_file["PCON11NM"]
test_csv_file["Mid-2018"] = test_csv_file["Mid-2018"].str.replace(",", "").astype("int64")
cg = CartogramGenerator(test_shapefile, test_csv_file, "Mid-2018")

# cg.plot_heatmap()
cg.cartogram_type("test")
cg.plot_cartogram()
plt.show()