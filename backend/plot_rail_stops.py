import geopandas as gpd
import folium
import os
from folium import FeatureGroup
# from folium import Map
# from folium.plugins import MousePosition
# from folium import Element
from geopy.geocoders import Nominatim
# from folium import plugins

# Define the project root and target save directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root of the project
OUTPUT_DIR = os.path.join(PROJECT_DIR, "backend", "static", "maps")

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Load stop data from GeoJSON
def load_geojson(file_path):
    """
    Loads a GeoJSON file and returns a GeoDataFrame.
    """
    try:
        return gpd.read_file(file_path)
    except Exception as e:
        print(f"Error loading GeoJSON file: {e}")
        return None
    
def plot_data_on_map(dataset, map_object, layer_name, color, icon="info-sign"):
    """
    Adds markers to the map for each point in the data GeoDataFrame.
    """
    layer = FeatureGroup(name=layer_name)

    for _, location in dataset.iterrows():
        coords = location.geometry.coords[0]  # Get coordinates (longitude, latitude)
        name = location.get("name", "Unknown Name")  # Access the "name" property safely
        description = location.get("description", "No description")  # Access the "description" property

        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude
            popup=f"<b>{name}</b><br>{description}",
            icon=folium.Icon(color=color, icon=icon)
        )
        marker.add_to(layer)

    layer.add_to(map_object)

def plot_atm_on_map(dataset, map_object, layer_name, color, icon="info-sign"):
    """
    Adds markers to the map for each atm in the data GeoDataFrame.
    """
    layer = FeatureGroup(name=layer_name)

    for _, location in dataset.iterrows():
        coords = location.geometry.coords[0]  # Get coordinates (longitude, latitude)
        name = location.get("brand", "Unknown Brand")  # Access the "name" property safely
        operator = location.get("operator", "Unknown Operator")  # Access the "name" property safely

        marker = folium.Marker(
            location=[coords[1], coords[0]],  # Latitude, Longitude
            popup=f"<b>{name}</b><br>{operator}",
            icon=folium.Icon(color=color, icon=icon)
        )
        marker.add_to(layer)

    layer.add_to(map_object)


def plot_rail_stops(green_stops, red_stops, dart_stations, intercity_stations, commuter_stations, atm_data):
    """
    Plots various rail lines and ATM data on the map.
    """
    # Center the map around Dublin
    map_dublin = folium.Map(location=[53.349805, -6.26031], zoom_start=12)

    # Plot each rail line and ATMs
    plot_data_on_map(green_stops, map_dublin, "Luas Green Line", "green", icon="info-sign")
    plot_data_on_map(red_stops, map_dublin, "Luas Red Line", "red", icon="info-sign")
    plot_data_on_map(dart_stations, map_dublin, "DART Line", "darkgreen", icon="info-sign")
    plot_data_on_map(intercity_stations, map_dublin, "Intercity Lines", "blue", icon="info-sign")
    plot_data_on_map(commuter_stations, map_dublin, "Commuter Rail Lines", "orange", icon="info-sign")
    plot_atm_on_map(atm_data, map_dublin, "ATMs", "darkblue", icon="info-sign")

    # Add layer control to toggle between layers
    folium.LayerControl().add_to(map_dublin)

    # Ensure the 'maps' directory exists
    maps_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maps')
    if not os.path.exists(maps_dir):
        os.makedirs(maps_dir)

    # Save the map to an HTML file in the 'maps' directory
    map_file_path = os.path.join(maps_dir, "rail_and_atm_map.html")
    map_dublin.save(map_file_path)
    print(f"Map with rail stops and ATMs has been saved as '{map_file_path}'.")

    return map_file_path  # Return the full path to the map file


# Create a map and plot the Luas line stops and DART stations
# def plot_rail_stops(green_stops, red_stops, dart_stations, intercity_stations, commuter_stations):
    
#     # Center the map around Dublin
#     map_dublin = folium.Map(location=[53.349805, -6.26031], zoom_start=12)

#     # Create FeatureGroups for different Luas lines
#     green_line_layer = FeatureGroup(name="Luas Green Line")
#     red_line_layer = FeatureGroup(name="Luas Red Line")
#     dart_layer = FeatureGroup(name="DART Line")
#     intercity_layer = FeatureGroup(name="Intercity Lines")
#     commuter_layer = FeatureGroup(name="Commuter Rail Lines")

#     # Add Green Line Stops to the map
#     for _, stop in green_stops.iterrows():
#         coords = stop.geometry.coords[0]  # Get coordinates (longitude, latitude)
#         name = stop["Name"]  # Access the "Name" property
#         description = stop["Description"]  # Access the "Description" property

#         # Print the coordinates and properties for debugging
#         # print(f"Green Line - Name: {name}, Coordinates: {coords}")

#         # Create a marker for each stop with a popup
#         marker = folium.Marker(
#             location=[coords[1], coords[0]],  # Latitude, Longitude
#             popup=f"<b>{name}</b><br>{description if description else 'No description'}",
#             icon=folium.Icon(color="green", icon="info-sign")
#         )
#         marker.add_to(green_line_layer)  # Add to Green Line layer

#     # Add Red Line Stops to the map
#     for _, stop in red_stops.iterrows():
#         coords = stop.geometry.coords[0]  # Get coordinates (longitude, latitude)
#         name = stop["Name"]  # Access the "Name" property
#         description = stop["Description"]  # Access the "Description" property

#         # Print the coordinates and properties for debugging
#         # print(f"Red Line - Name: {name}, Coordinates: {coords}")

#         # Create a marker for each stop with a popup
#         marker = folium.Marker(
#             location=[coords[1], coords[0]],  # Latitude, Longitude
#             popup=f"<b>{name}</b><br>{description if description else 'No description'}",
#             icon=folium.Icon(color="red", icon="info-sign")
#         )
#         marker.add_to(red_line_layer)  # Add to Red Line layer
    
#     # Add DART stations to the map
#     for _, stop in dart_stations.iterrows():
#         # Check the structure of the current stop object
#         print(stop)  # To see the columns and structure of the stop

#         # Access coordinates from geometry
#         coords = stop.geometry.coords[0]  # Get coordinates from the Point geometry
#         # Safely access the "properties" field
#         properties = stop.get('properties', {})  # Default to an empty dictionary if 'properties' is missing
#         name = stop.get("name", "Unknown Name")  # Access the "name" property safely
#         description = stop.get("description", 'No description')  # Access the "description" property, with a fallback

#         # Print the coordinates and properties for debugging
#         print(f"DART Line - Name: {name}, Coordinates: {coords}")

#         # Create a marker for each stop with a popup
#         marker = folium.Marker(
#             location=[coords[1], coords[0]],  # Latitude, Longitude (ensure correct order)
#             popup=f"<b>{name}</b><br>{description}",
#             icon=folium.Icon(color="darkgreen", icon="info-sign")
#         )
#         marker.add_to(dart_layer)  # Add to DART layer

#     # Add intercity stations to the map
#     for _, stop in intercity_stations.iterrows():
#         # Check the structure of the current stop object
#         # print(stop)  # To see the columns and structure of the stop

#         # Access coordinates from geometry
#         coords = stop.geometry.coords[0]  # Get coordinates from the Point geometry
#         # Safely access the "properties" field
#         properties = stop.get('properties', {})  # Default to an empty dictionary if 'properties' is missing
#         name = stop.get("name", "Unknown Name")  # Access the "name" property safely
#         description = properties.get("description", 'No description')  # Access the "description" property, with a fallback

#         # Print the coordinates and properties for debugging
#         # print(f"Intercity Line - Name: {name}, Coordinates: {coords}")

#         # Create a marker for each stop with a popup
#         marker = folium.Marker(
#             location=[coords[1], coords[0]],  # Latitude, Longitude (ensure correct order)
#             popup=f"<b>{name}</b><br>{description}",
#             icon=folium.Icon(color="blue", icon="info-sign")
#         )
#         marker.add_to(intercity_layer)  # Add to Intercity layer

#     # Add commuter stations to the map
#     for _, stop in commuter_stations.iterrows():
#         # Check the structure of the current stop object
#         # print(stop)  # To see the columns and structure of the stop

#         # Access coordinates from geometry
#         coords = stop.geometry.coords[0]  # Get coordinates from the Point geometry
#         # Safely access the "properties" field
#         properties = stop.get('properties', {})  # Default to an empty dictionary if 'properties' is missing
#         name = stop.get("name", "Unknown Name")  # Access the "name" property safely
#         description = properties.get("description", 'No description')  # Access the "description" property, with a fallback

#         # Print the coordinates and properties for debugging
#         # print(f"Commuter Line - Name: {name}, Coordinates: {coords}")

#         # Create a marker for each stop with a popup
#         marker = folium.Marker(
#             location=[coords[1], coords[0]],  # Latitude, Longitude (ensure correct order)
#             popup=f"<b>{name}</b><br>{description}",
#             icon=folium.Icon(color="orange", icon="info-sign")
#         )
#         marker.add_to(commuter_layer)  # Add to Commuter layer


#     # Add the layers to the map
#     green_line_layer.add_to(map_dublin)
#     red_line_layer.add_to(map_dublin)
#     dart_layer.add_to(map_dublin)
#     intercity_layer.add_to(map_dublin)
#     commuter_layer.add_to(map_dublin)

#     # Add layer control to toggle between layers (Green Line, Red Line)
#     folium.LayerControl().add_to(map_dublin)

#     # Add search functionality to the map
#     add_search_functionality(map_dublin)

#     # Save the map to an HTML file
#     map_dublin.save(os.path.join(OUTPUT_DIR, "rail_map.html"))
#     print("Map has been saved as 'rail_map.html'.")

#     return "maps/rail_map.html"

def add_search_functionality(map_object):
    """
    Adds a search function to the Folium map to zoom to an entered address and add a marker.
    """
    search_bar = """
    <div style="position: fixed; top: 10px; left: 5%; z-index: 1000; background-color: white; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
        <input id="addressInput" type="text" placeholder="Enter an address" style="width: 200px; padding: 5px;">
        <button onclick="geocodeAndZoom()" style="padding: 5px;">Search</button>
    </div>
    <script>
    let userMarker;

    async function geocodeAndZoom() {
        const address = document.getElementById("addressInput").value;
        if (!address) {
            alert("Please enter an address!");
            return;
        }

        const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(address)}`);
        const results = await response.json();
        
        if (results.length > 0) {
            const lat = parseFloat(results[0].lat);
            const lon = parseFloat(results[0].lon);
            const displayName = results[0].display_name;

            // Zoom the map to the new location
            map.setView([lat, lon], 15);

            // Remove any existing marker
            if (userMarker) {
                map.removeLayer(userMarker);
            }

            // Add a marker at the location with a popup
            userMarker = L.marker([lat, lon]).addTo(map);
            userMarker.bindPopup(`<b>Address:</b> ${displayName}`).openPopup();
        } else {
            alert("Address not found!");
        }
    }
    </script>
    """

    # Add the HTML/JS to the map as a child element
    map_object.get_root().html.add_child(folium.Element(search_bar))


def main():
    # Paths to the GeoJSON files for Green and Red lines
    green_file_path = "./data/luas_stops_green.geojson"
    red_file_path = "./data/luas_stops_red.geojson"
    dart_file_path = "./data/dart_stations.geojson"
    intercity_file_path = "./data/intercity_rail_stations.geojson"
    commuter_file_path = "./data/dublin_commuter_stations.geojson"
    atm_file_path = "./data/atm_data.geojson"

    # Load the Green and Red line stop data
    green_stops = load_geojson(green_file_path)
    red_stops = load_geojson(red_file_path)
    dart_stations = load_geojson(dart_file_path)
    intercity_stations = load_geojson(intercity_file_path)
    commuter_stations = load_geojson(commuter_file_path)
    atm_data = load_geojson(atm_file_path)

    # If all datasets are successfully loaded, plot the stops on the map
    if green_stops is not None and red_stops is not None and dart_stations is not None and intercity_stations is not None and commuter_stations is not None and atm_data is not None:
        plot_rail_stops(green_stops, red_stops, dart_stations, intercity_stations, commuter_stations)
    else:
        print("One or more datasets failed to load.")

if __name__ == "__main__":
    main()
