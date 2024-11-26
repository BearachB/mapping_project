from flask import Flask, render_template
import os
from plot_rail_stops import plot_rail_stops, load_geojson

app = Flask(__name__)

# Base directory of the application
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Serve the map
@app.route('/')
def index():
    # Paths to the GeoJSON files for rail stops
    green_file_path = os.path.join(BASE_DIR, "data", "luas_stops_green.geojson")
    red_file_path = os.path.join(BASE_DIR, "data", "luas_stops_red.geojson")
    dart_file_path = os.path.join(BASE_DIR, "data", "dart_stations.geojson")
    intercity_file_path = os.path.join(BASE_DIR, "data", "intercity_rail_stations.geojson")
    commuter_file_path = os.path.join(BASE_DIR, "data", "dublin_commuter_stations.geojson")
    atm_file_path = os.path.join(BASE_DIR, "data", "atm_data.geojson")


    # Load the rail stops data
    green_stops = load_geojson(green_file_path)
    red_stops = load_geojson(red_file_path)
    dart_stations = load_geojson(dart_file_path)
    intercity_stations = load_geojson(intercity_file_path)
    commuter_stations = load_geojson(commuter_file_path)
    atm_locations = load_geojson(atm_file_path)

    # Generate the map and return the file path
    map_file = plot_rail_stops(green_stops, red_stops, dart_stations, intercity_stations, commuter_stations, atm_locations)

    return render_template('map.html', map_file=map_file)

if __name__ == '__main__':
    app.run(debug=True)
