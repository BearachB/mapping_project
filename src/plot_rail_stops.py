import geopandas as gpd
import folium
import os
from folium import FeatureGroup

# Define the project root and target save directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root of the project
OUTPUT_DIR = os.path.join(PROJECT_DIR, "outputs")

# Load Luas stop data from GeoJSON
def load_rail_stops(file_path):
    try:
        return gpd.read_file(file_path)
    except Exception as e:
        print(f"Error loading GeoJSON file: {e}")
        return None

# Create a map and plot the Luas line stops and DART stations
def plot_rail_stops(green_stops, red_stops, dart_stations, intercity_stations, commuter_stations):
    
    # Center the map around Dublin
    map_dublin = folium.Map(location=[53.349805, -6.26031], zoom_start=12)

    # Create FeatureGroups for different Luas lines
    green_line_layer = FeatureGroup(name="Luas Green Line")
    red_line_layer = FeatureGroup(name="Luas Red Line")
    dart_layer = FeatureGroup(name="DART Line")
    intercity_layer = FeatureGroup(name="Intercity Lines")
    commuter_layer = FeatureGroup(name="Commuter Rail Lines")

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
    
    # Add DART stations to the map
    for _, stop in dart_stations.iterrows():
        # Check the structure of the current stop object
        print(stop)  # To see the columns and structure of the stop

        # Access coordinates from geometry
        coords = stop.geometry.coords[0]  # Get coordinates from the Point geometry
        # Safely access the "properties" field
        properties = stop.get('properties', {})  # Default to an empty dictionary if 'properties' is missing
        name = properties.get("name", "Unknown Name")  # Access the "name" property safely
        description = properties.get("description", 'No description')  # Access the "description" property, with a fallback

        # Print the coordinates and properties for debugging
        print(f"DART Line - Name: {name}, Coordinates: {coords}")

        # Create a marker for each stop with a popup
        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude (ensure correct order)
            popup=f"<b>{name}</b><br>{description}",
            icon=folium.Icon(color="darkgreen", icon="info-sign")
        )
        marker.add_to(dart_layer)  # Add to DART layer

    # Add intercity stations to the map
    for _, stop in intercity_stations.iterrows():
        # Check the structure of the current stop object
        print(stop)  # To see the columns and structure of the stop

        # Access coordinates from geometry
        coords = stop.geometry.coords[0]  # Get coordinates from the Point geometry
        # Safely access the "properties" field
        properties = stop.get('properties', {})  # Default to an empty dictionary if 'properties' is missing
        name = properties.get("name", "Unknown Name")  # Access the "name" property safely
        description = properties.get("description", 'No description')  # Access the "description" property, with a fallback

        # Print the coordinates and properties for debugging
        print(f"Intercity Line - Name: {name}, Coordinates: {coords}")

        # Create a marker for each stop with a popup
        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude (ensure correct order)
            popup=f"<b>{name}</b><br>{description}",
            icon=folium.Icon(color="blue", icon="info-sign")
        )
        marker.add_to(intercity_layer)  # Add to Intercity layer

    # Add commuter stations to the map
    for _, stop in commuter_stations.iterrows():
        # Check the structure of the current stop object
        print(stop)  # To see the columns and structure of the stop

        # Access coordinates from geometry
        coords = stop.geometry.coords[0]  # Get coordinates from the Point geometry
        # Safely access the "properties" field
        properties = stop.get('properties', {})  # Default to an empty dictionary if 'properties' is missing
        name = properties.get("name", "Unknown Name")  # Access the "name" property safely
        description = properties.get("description", 'No description')  # Access the "description" property, with a fallback

        # Print the coordinates and properties for debugging
        print(f"Commuter Line - Name: {name}, Coordinates: {coords}")

        # Create a marker for each stop with a popup
        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude (ensure correct order)
            popup=f"<b>{name}</b><br>{description}",
            icon=folium.Icon(color="orange", icon="info-sign")
        )
        marker.add_to(commuter_layer)  # Add to Commuter layer


    # Add the layers to the map
    green_line_layer.add_to(map_dublin)
    red_line_layer.add_to(map_dublin)
    dart_layer.add_to(map_dublin)
    intercity_layer.add_to(map_dublin)
    commuter_layer.add_to(map_dublin)

    # Add layer control to toggle between layers (Green Line, Red Line)
    folium.LayerControl().add_to(map_dublin)

    # Save the map to an HTML file
    map_dublin.save(os.path.join(OUTPUT_DIR, "rail_map.html"))
    print("Map has been saved as 'rail_map.html'.")

def enable_pin_placement(map_object):
    """
    Add functionality to place a pin on the map by clicking.
    """
    from folium import Marker
    from folium.plugins import MousePosition
    
    # Add Mouse Position for latitude/longitude feedback
    MousePosition().add_to(map_object)

    # Handle click events
    def on_click(e):
        lat, lon = e.latlng  # Get latitude and longitude from the event
        print(f"User clicked at: {lat}, {lon}")
        folium.Marker(location=[lat, lon], icon=folium.Icon(color="blue", icon="map-pin")).add_to(map_object)
    
    # Attach the event to the map (this requires custom JS integration)
    map_object.add_child(folium.ClickForMarker())

def main():
    # Paths to the GeoJSON files for Green and Red lines
    green_file_path = "./data/luas_stops_green.geojson"
    red_file_path = "./data/luas_stops_red.geojson"
    dart_file_path = "./data/dart_stations.geojson"
    intercity_file_path = "./data/intercity_rail_stations.geojson"
    commuter_file_path = "./data/dublin_commuter_stations.geojson"

    # Load the Green and Red line stop data
    green_stops = load_rail_stops(green_file_path)
    red_stops = load_rail_stops(red_file_path)
    dart_stations = load_rail_stops(dart_file_path)
    intercity_stations = load_rail_stops(intercity_file_path)
    commuter_stations = load_rail_stops(commuter_file_path)

    # If all datasets are successfully loaded, plot the stops on the map
    if green_stops is not None and red_stops is not None and dart_stations is not None and intercity_stations is not None and commuter_stations is not None:
        plot_rail_stops(green_stops, red_stops, dart_stations, intercity_stations, commuter_stations)
    else:
        print("One or more datasets failed to load.")

if __name__ == "__main__":
    main()
