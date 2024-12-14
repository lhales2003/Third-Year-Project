import geopandas as gpd
import pandas as pd

from cartogrammable.cg import CartogramGenerator

test_shapefile = gpd.read_file("tests/PCON_JULY_2024_UK_BUC.shp")
test_csv_file = pd.read_csv("tests/foi20190080data.csv")

def test_load_data():
    generator = CartogramGenerator()
    generator.load_data("tests/PCON_JULY_2024_UK_BUC.shp", "tests/foi20190080data.csv")
    assert generator.map_borders.info() == test_shapefile.info()
    assert generator.map_data.info() == test_csv_file.info()