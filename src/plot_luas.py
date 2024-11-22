import geopandas as gpd
import folium
import os
from folium import FeatureGroup

# Define the project root and target save directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root of the project
OUTPUT_DIR = os.path.join(PROJECT_DIR, "outputs")

# Load Luas stop data from GeoJSON
def load_luas_stops(file_path):
    try:
        return gpd.read_file(file_path)
    except Exception as e:
        print(f"Error loading GeoJSON file: {e}")
        return None

# Create a map and plot the Luas stops
def plot_luas_stops(green_stops, red_stops):
    # Center the map around Dublin
    map_dublin = folium.Map(location=[53.349805, -6.26031], zoom_start=12)

    # Create FeatureGroups for different Luas lines
    green_line_layer = FeatureGroup(name="Luas Green Line")
    red_line_layer = FeatureGroup(name="Luas Red Line")

    # Add Green Line Stops to the map
    for _, stop in green_stops.iterrows():
        coords = stop.geometry.coords[0]  # Get coordinates (longitude, latitude)
        name = stop["Name"]  # Access the "Name" property
        description = stop["Description"]  # Access the "Description" property

        # Print the coordinates and properties for debugging
        print(f"Green Line - Name: {name}, Coordinates: {coords}")

        # Create a marker for each stop with a popup
        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude
            popup=f"<b>{name}</b><br>{description if description else 'No description'}",
            icon=folium.Icon(color="green", icon="info-sign")
        )
        marker.add_to(green_line_layer)  # Add to Green Line layer

    # Add Red Line Stops to the map
    for _, stop in red_stops.iterrows():
        coords = stop.geometry.coords[0]  # Get coordinates (longitude, latitude)
        name = stop["Name"]  # Access the "Name" property
        description = stop["Description"]  # Access the "Description" property

        # Print the coordinates and properties for debugging
        print(f"Red Line - Name: {name}, Coordinates: {coords}")

        # Create a marker for each stop with a popup
        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude
            popup=f"<b>{name}</b><br>{description if description else 'No description'}",
            icon=folium.Icon(color="red", icon="info-sign")
        )
        marker.add_to(red_line_layer)  # Add to Red Line layer

    # Add the layers to the map
    green_line_layer.add_to(map_dublin)
    red_line_layer.add_to(map_dublin)

    # Add layer control to toggle between layers (Green Line, Red Line)
    folium.LayerControl().add_to(map_dublin)

    # Save the map to an HTML file
    map_dublin.save(os.path.join(OUTPUT_DIR, "luas_map.html"))
    print("Map has been saved as 'luas_map.html'.")

def main():
    # Paths to the GeoJSON files for Green and Red lines
    green_file_path = "./data/luas_stops_green.geojson"
    red_file_path = "./data/luas_stops_red.geojson"

    # Load the Green and Red line stop data
    green_stops = load_luas_stops(green_file_path)
    red_stops = load_luas_stops(red_file_path)

    # If both datasets are successfully loaded, plot the stops on the map
    if green_stops is not None and red_stops is not None:
        plot_luas_stops(green_stops, red_stops)

if __name__ == "__main__":
    main()
