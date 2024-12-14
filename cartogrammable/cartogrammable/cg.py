import sys
import geopandas as gpd
import pandas as pd

class CartogramGenerator:
    def __init__(self, shapefile, csv_file, shapefile_column, csv_file_column):
        self.map_borders = None
        self.map_data = None
        self.cartogram_type = None
                    
        self.load_data(shapefile, csv_file, shapefile_column, csv_file_column)
    
    def load_data(self, shapefile, csv_file, shapefile_column, csv_file_column):
        try:
            self.map_borders = gpd.read_file(shapefile)
            self.map_data = pd.read_csv(csv_file)
        except:
            print("Error loading files, ensure file names and paths are correct and try again. Terminating program to avoid further errors")
            sys.exit(0)
        
        
    def shapefile_info(self):
        try:
            return self.map_borders.info()
        except:
            print("Shapefile not present in CartogramGenerator object. Terminating program to avoid further errors")
            sys.exit(0)
    
    def csv_file_info(self):
        try:
            return self.map_data.info()
        except:
            print("CSV file not present in CartogramGenerator object. Terminating program to avoid further errors")
        
        