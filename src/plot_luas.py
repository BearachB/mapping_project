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
def plot_luas_stops(luas_stops):
    # Center the map around Dublin
    map_dublin = folium.Map(location=[53.349805, -6.26031], zoom_start=12)

    # Create FeatureGroups for different Luas lines and all stops
    all_stops_layer = FeatureGroup(name="All Luas Stops", show=True)  # All stops visible by default
    red_line_layer = FeatureGroup(name="Red Line Stops", show=True)  # Red line initially hidden
    green_line_layer = FeatureGroup(name="Green Line Stops", show=True)  # Green line initially hidden

    # Loop through the rows of the stops and add them to the appropriate layer
    for _, stop in luas_stops.iterrows():
        coords = stop.geometry.coords[0]  # Get coordinates (longitude, latitude)
        name = stop["Name"]  # Access the "Name" property
        line = stop["Line"]  # Access the "Line" property (Red or Green)
        description = stop["Description"]  # Access the "Description" property

        # Print the coordinates and properties for debugging
        print(f"Name: {name}, Line: {line}, Coordinates: {coords}")

        # Determine the icon color based on the line
        icon_color = "red" if line == "Red" else "green"

        # Create a marker for each stop with a popup
        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude
            popup=f"<b>{name}</b><br>{description if description else 'No description'}",
            icon=folium.Icon(color=icon_color, icon="info-sign")
        )

        # Add marker to the appropriate layers
        marker.add_to(all_stops_layer)  # All stops will go in this layer

        # if line == "Red":
        #     marker.add_to(red_line_layer)  # Red line stops go to this layer
        # elif line == "Green":
        #     marker.add_to(green_line_layer)  # Green line stops go to this layer

    # Add the layers to the map
    all_stops_layer.add_to(map_dublin)
    # red_line_layer.add_to(map_dublin)
    # green_line_layer.add_to(map_dublin)

    # Add layer control to toggle between layers (All stops, Red, Green)
    folium.LayerControl().add_to(map_dublin)

    # Save the map to an HTML file
    map_dublin.save(os.path.join(OUTPUT_DIR, "luas_map.html"))
    print("Map has been saved as'luas_map.html'.")

def main():
    # Path to the GeoJSON file
    file_path = "./data/luas_stops.geojson"

    # Load the data
    luas_stops = load_luas_stops(file_path)
    if luas_stops is not None:
        plot_luas_stops(luas_stops)

if __name__ == "__main__":
    main()
