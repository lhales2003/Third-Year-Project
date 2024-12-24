import sys
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

class CartogramGenerator:
    def __init__(self, shapefile, csv_file, statistic_column):
        self.map_borders = None
        self.map_data = None
        self.statistic_column = None
        self.cartogram_type = None
        self.merged_data = None
                    
        self.load_data(shapefile, csv_file, statistic_column)
    
    def load_data(self, shapefile, csv_file, statistic_column):
        if isinstance(shapefile, gpd.geodataframe.GeoDataFrame) and isinstance(csv_file, pd.core.frame.DataFrame):
            self.map_borders = shapefile
            self.map_data = csv_file
            self.statistic_column = statistic_column
        else:
            print("Error loading files, ensure DataFrame(s) are of correct type and try again. Terminating program to avoid further errors")
            sys.exit(0)
        
        self.merge_data()
        
    def merge_data(self):
        shapefile_columns = list(self.map_borders.columns.values)
        csv_file_columns = list(self.map_data.columns.values)
        
        merge_column = None
        for column in shapefile_columns:
            if column in csv_file_columns:
                merge_column = column
                pass
        
        if merge_column is None:
            print("No columns in common, must have one column labelled the same in order to merge DataFrames. Please modify the Pandas file and try again.")
            sys.exit(0)
        
        average_statistic = self.map_data[self.statistic_column].mean()
        
        
        self.merged_data = self.map_borders.merge(self.map_data, left_on=merge_column, right_on=merge_column)

        if self.merged_data[merge_column].count() == 0:
            print("No values exist in DataFrame after merge. Please try another column")
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
    
    def modify_shapefile(self, new_shapefile):
        if isinstance(new_shapefile, gpd.geodataframe.GeoDataFrame):
            self.map_borders = new_shapefile
        else:
            print("Error loading file, ensure DataFrame is of correct type and try aagin. Terminating program to avoid further errors.")
        
        self.merge_data()
           
    def modify_csv_file(self, new_csv_file):
        if isinstance(new_csv_file, pd.core.frame.DataFrame):
            self.map_borders = new_csv_file
        else:
            print("Error loading file, ensure DataFrame is of correct type and try aagin. Terminating program to avoid further errors.")
        
        self.merge_data()
        
    def plot_heatmap(self):
        fig, ax = plt.subplots(figsize= (10,10))
        self.map_borders.plot(ax=ax, color="lightgray", edgecolor="black")
        self.merged_data.plot(column=self.statistic_column, ax=ax, cmap="OrRd")
        plt.title("Loaded Map with Merged Data")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        