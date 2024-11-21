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

    # Create a FeatureGroup for Luas stops
    luas_layer = FeatureGroup(name="Luas Stops", show=True)

    # Add each stop as a marker to the layer
    for _, stop in luas_stops.iterrows():
        # Extract coordinates and properties
        coords = stop.geometry.coords[0]  # Get (longitude, latitude) tuple
        name = stop["Name"]  # Access the "Name" property
        description = stop["Description"]  # Access the "Description" property (optional)

        # Add a marker for each stop
        folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude
            popup=f"<b>{name}</b><br>{description if description else 'No description'}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(luas_layer)

    # Add the layer to the map
    luas_layer.add_to(map_dublin)

    # Add layer control to toggle the dataset
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
