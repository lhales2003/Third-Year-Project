from shapely.affinity import scale

import sys
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

class CartogramGenerator:
    def __init__(self, geodataframe, dataframe, statistic_column):
        """_summary_

        Args:
            geodataframe (_type_): _description_
            dataframe (_type_): _description_
            statistic_column (_type_): _description_
        """
        self.map_borders = None
        self.map_data = None
        self.statistic_column = None
        self.chosen_cartogram = None
        self.merged_data = None
        
                    
        self.load_data(geodataframe, dataframe, statistic_column)
    
    def load_data(self, geodataframe, dataframe, statistic_column):
        if isinstance(geodataframe, gpd.geodataframe.GeoDataFrame) and isinstance(dataframe, pd.core.frame.DataFrame):
            self.map_borders = geodataframe
            self.map_data = dataframe
            self.statistic_column = statistic_column
        else:
            print("Error loading files, ensure DataFrame(s) are of correct type and try again. Terminating program to avoid further errors")
            sys.exit(0)
        
        self.merge_data()
        
    def merge_data(self):
        # TODO: Ensure that columns do match up with each other before proceeding
        geodataframe_columns = list(self.map_borders.columns.values)
        dataframe_columns = list(self.map_data.columns.values)
        
        merge_column = None
        for column in geodataframe_columns:
            if column in dataframe_columns:
                if pd.Series(column).is_unique:
                    merge_column = column
                    pass
        
        if merge_column is None:
            print("No columns in common, must have one column labelled the same in order to merge DataFrames. Please modify the Pandas file and try again.")
            sys.exit(0)
        
        average_statistic = self.map_data[self.statistic_column].mean()

        temp_data = self.map_data
        geodataframe_merge_column_values = self.map_borders[merge_column].tolist()
        temp_data_merge_column_values = temp_data[merge_column].tolist()

        print(temp_data.info())  
        for value in temp_data_merge_column_values:
            if value not in geodataframe_merge_column_values:
                temp_data = temp_data.drop(temp_data[temp_data[merge_column] == value].index)

        print(temp_data.info())        
        for value in geodataframe_merge_column_values:
            if value not in temp_data_merge_column_values:
                new_row = pd.DataFrame({merge_column: [value], self.statistic_column: [average_statistic]})
                temp_data = pd.concat([temp_data, new_row], ignore_index=True)
        
        print(temp_data.info())  

        self.merged_data = self.map_borders.merge(temp_data, left_on=merge_column, right_on=merge_column)
        
        # self.merged_data = self.map_borders.merge(self.map_data, left_on=merge_column, right_on=merge_column)

        # if self.merged_data[merge_column].count() == 0:
        #     print("No values exist in DataFrame after merge. Please try another column")
        #     sys.exit(0)
        
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
    
    def modify_geodataframe(self, new_geodataframe):
        if isinstance(new_geodataframe, gpd.geodataframe.GeoDataFrame):
            self.map_borders = new_geodataframe
        else:
            print("Error loading file, ensure DataFrame is of correct type and try aagin. Terminating program to avoid further errors.")
            sys.exit(0)
        
        self.merge_data()
           
    def modify_dataframe(self, new_dataframe):
        if isinstance(new_dataframe, pd.core.frame.DataFrame):
            self.map_borders = new_dataframe
        else:
            print("Error loading file, ensure DataFrame is of correct type and try aagin. Terminating program to avoid further errors.")
            sys.exit(0)

        self.merge_data()
        
    def plot_heatmap(self):
        fig, ax = plt.subplots(figsize= (10,10))
        self.map_borders.plot(ax=ax, color="lightgray", edgecolor="black")
        self.merged_data.plot(column=self.statistic_column, ax=ax, cmap="OrRd")
        plt.title("Loaded Map with Merged Data")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")

    def cartogram_type(self, type_chosen):
        types = ["Diffusion-Based", "Dorling", "test"]

        if type_chosen not in types:
            print("Invalid cartogram type. Terminating program to avoid further errors.")
            sys.exit(0)
        else:
            self.chosen_cartogram = type_chosen

    def plot_cartogram(self): 
        # TODO: create function that plots cartogram based upon the chosen cartogram type
        if self.chosen_cartogram == "Diffusion-Based":
            print("Diffusion-Based")
        elif self.chosen_cartogram == "Dorling":
           print("Dorling")
        elif self.chosen_cartogram == "test":
            test_algorithm(self.map_borders, self.merged_data, self.statistic_column)

def test_algorithm(gdf, data, column):
    # TODO: produce a test algorithm that mainpulates borders on a map
    gdf["buffered"] = gdf.geometry.buffer(0.5)
    ax = gdf.plot(color="blue", alpha=0.5)
    gdf["buffered"].plot(ax=ax, color="red", alpha=0.3)
    
    total = gdf[column].sum()

    gdf["modified"] = scale(gdf["geometry"])

def diffusion_based(data):
    # TODO: code Gastner-Newmann Equation
    print("diffusion_based")

