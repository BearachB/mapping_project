import osmnx as ox
import os
import geopandas as gpd

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root of the project
OUTPUT_DIR = os.path.join(PROJECT_DIR, "..", "outputs") 

# Define a place (Dublin in this case)
place_name = "Dublin, Ireland"

# Get the stations data from OSM using the query
graph = ox.graph_from_place(place_name, network_type="all")

# Get the nodes as a GeoDataFrame
nodes, edges = ox.graph_to_gdfs(graph)

# Print the columns to see what we have
print("Columns in the nodes DataFrame:", nodes.columns)
# Print the first few rows of the nodes DataFrame to understand the structure
print(nodes.head())

# Filter nodes that are tagged as stations (e.g., 'station' or 'railway=station')
# Here we will print the tags that are present in the nodes to find the relevant tag
station_nodes = nodes[nodes['amenity'] == 'station']  # If amenity=station is used

# Check the first few rows of filtered station nodes
print(station_nodes.head())

# If stations are found, we can save them as a GeoJSON file
if not station_nodes.empty:
    station_nodes.to_file('./outputs/dart_stations_filtered.geojson', driver="GeoJSON")
else:
    print("No station nodes found.")

# # Filter nodes that are tagged as stations in OSM (railway=station)
# stations = nodes[nodes['railway'] == 'station']

# # Select the relevant columns: x and y coordinates, and the name of the station
# stations = stations[['name', 'geometry']]

# # Check the first few rows to ensure it's correct
# print(stations.head())

# # Convert the stations into a GeoDataFrame
# stations_gdf = gpd.GeoDataFrame(stations, geometry=gpd.points_from_xy(stations.x, stations.y))

# # Save the GeoDataFrame as a GeoJSON file
# stations_gdf.to_file(os.path.join(OUTPUT_DIR,"dart_stations.geojson"))