from shapely.affinity import scale
from shapely.geometry import Polygon, MultiPolygon
import numpy as np
import sys
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

class CartogramGenerator:
    """The class of the object the user will interact with in order to create Cartograms
    """
    def __init__(self, geodataframe, dataframe, statistic_column):
        """Initialises Cartogram object, using GeoDataFrame and DataFrame provided.

        Args:
            geodataframe (gpd.geodataframe.GeoDataFrame): The GeoDataFrame which will provide the data of the map to be manipulated based on the DataFrame
            dataframe (pd.core.frame.DataFrame): The DataFrame which holds all of the data relating to the map provided
            statistic_column (str): The name of the column in dataframe which will be displayed and used to manipulate the map
        """
        
        self.map_borders = None
        self.map_data = None
        self.statistic_column = None
        self.chosen_cartogram = None
        self.merged_data = None
        
        self.load_data(geodataframe, dataframe, statistic_column)
    
    def load_data(self, geodataframe, dataframe, statistic_column):
        """Stores the parameters in the object if they are of the correct types required

        Args:
            geodataframe (gpd.geodataframe.GeoDataFrame): The GeoDataFrame which will provide the data of the map to be manipulated based on the DataFrame
            dataframe (pd.core.frame.DataFrame): The DataFrame which holds all of the data relating to the map provided
            statistic_column (str): The name of the column in dataframe which will be displayed and used to manipulate the map
        """
        if isinstance(geodataframe, gpd.geodataframe.GeoDataFrame) and isinstance(dataframe, pd.core.frame.DataFrame):
            self.map_borders = geodataframe
            self.map_data = dataframe
            self.statistic_column = statistic_column
        else:
            print("Error loading files, ensure DataFrame(s) are of correct type and try again. Terminating program to avoid further errors")
            sys.exit(0)
        
        self.merge_data()
        
    def merge_data(self):
        """Merges the data into one DataFrame
        """
        geodataframe_columns = list(self.map_borders.columns.values)
        dataframe_columns = list(self.map_data.columns.values)
        
        merge_columns = []
        for column in geodataframe_columns:
            if column in dataframe_columns:
                if pd.Series(column).is_unique:
                    merge_columns.append(column)
                    pass
        
        if not merge_columns:
            print("No columns in common, must have one column labelled the same in order to merge DataFrames. Please modify the Pandas file and try again.")
            sys.exit(0)
        
        merge_column = None
        
        for column in merge_columns:
        
            average_statistic = self.map_data[self.statistic_column].mean()
        
            temp_data = self.map_data
            geodataframe_merge_column_values = self.map_borders[column].tolist()
            temp_data_merge_column_values = temp_data[column].tolist()

            print(temp_data.info())  
            for value in temp_data_merge_column_values:
                if value not in geodataframe_merge_column_values:
                    temp_data = temp_data.drop(temp_data[temp_data[column] == value].index)

            if temp_data[column].tolist():
                merge_column = column
                pass
            
        if merge_column is None:
            print("No columns in common, must have one column labelled the same in order to merge DataFrames. Please modify the Pandas file and try again.")
            sys.exit(0)
                
            
        print(temp_data.info())        
        for value in geodataframe_merge_column_values:
            if value not in temp_data_merge_column_values:
                new_row = pd.DataFrame({merge_column: [value], self.statistic_column: [average_statistic]})
                temp_data = pd.concat([temp_data, new_row], ignore_index=True)
        
        print(temp_data.info())  

        self.merged_data = self.map_borders.merge(temp_data, left_on=merge_column, right_on=merge_column)

        
    def geodataframe_info(self):
        """Returns the information of the GeoDataFrame provided, if applicable

        Returns:
            NoneType: The information of the GeoDataFrame 
        """
        try:
            return self.map_borders.info()
        except:
            print("Shapefile not present in CartogramGenerator object. Terminating program to avoid further errors")
            sys.exit(0)
    
    def dataframe_info(self):
        """Returns the information of the DataFrame provided, if applicable

        Returns:
            NoneType: The information of the DataFrame 
        """
        try:
            return self.map_data.info()
        except:
            print("CSV file not present in CartogramGenerator object. Terminating program to avoid further errors")
    
    def modify_geodataframe(self, new_geodataframe):
        """Replaces the current GeoDataFrame with the new GeoDataFrame provided

        Args:
            new_geodataframe (gpd.geodataframe.GeoDataFrame): The new GeoDataFrame to be set in the object
        """
        if isinstance(new_geodataframe, gpd.geodataframe.GeoDataFrame):
            self.map_borders = new_geodataframe
        else:
            print("Error loading file, ensure DataFrame is of correct type and try aagin. Terminating program to avoid further errors.")
            sys.exit(0)
        
        self.merge_data()
           
    def modify_dataframe(self, new_dataframe):
        """Replaces the current DataFrame to the new DataFrame provided

        Args:
            new_dataframe (pandas.core.frame.DataFrame): The new DataFrame to be set in the object
        """
        if isinstance(new_dataframe, pd.core.frame.DataFrame):
            self.map_borders = new_dataframe
        else:
            print("Error loading file, ensure DataFrame is of correct type and try aagin. Terminating program to avoid further errors.")
            sys.exit(0)

        self.merge_data()
        
    def plot_heatmap(self):
        """Plots a heatmap of the data provided
        """
        fig, ax = plt.subplots(figsize= (10,10))
        self.map_borders.plot(ax=ax, color="lightgray", edgecolor="black")
        self.merged_data.plot(column=self.statistic_column, ax=ax, cmap="OrRd")
        plt.title("Loaded Map with Merged Data")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")

    def cartogram_type(self, type_chosen):
        """Define the Cartogram type to be used

        Args:
            type_chosen (str): The name of the Cartogram type to be used
        """
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
    def distort_shape(polygon):
        coords = np.array(polygon.exterior.coords)
        distorted_coords = coords + np.random.uniform(-5000, 5000, coords.shape)
        distorted_polygon = Polygon(distorted_coords)
        return Polygon(distorted_polygon.exterior)
    
    def distort_geometry(geometry):
        if geometry.geom_type == "Polygon":
            return distort_shape(geometry) 
        elif geometry.geom_type == "MultiPolygon":
            distorted_shapes = [distort_shape(shape) for shape in geometry.geoms]
            return MultiPolygon(distorted_shapes)
    
    gdf["geometry"] = gdf["geometry"].apply(lambda geom: distort_geometry(geom))
    gdf.plot(edgecolor="black", facecolor="lightblue", figsize=(10, 10))

def diffusion_based(data):
    # TODO: code Gastner-Newmann Equation
    print("diffusion_based")

