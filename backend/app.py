from flask import Flask, render_template
import os
from plot_rail_stops import plot_rail_stops, load_rail_stops

app = Flask(__name__)

# Serve the map
@app.route('/')
def index():
    # Paths to the GeoJSON files for rail stops
    green_file_path = "./data/luas_stops_green.geojson"
    red_file_path = "./data/luas_stops_red.geojson"
    dart_file_path = "./data/dart_stations.geojson"
    intercity_file_path = "./data/intercity_rail_stations.geojson"
    commuter_file_path = "./data/dublin_commuter_stations.geojson"

    # Load the rail stops data
    green_stops = load_rail_stops(green_file_path)
    red_stops = load_rail_stops(red_file_path)
    dart_stations = load_rail_stops(dart_file_path)
    intercity_stations = load_rail_stops(intercity_file_path)
    commuter_stations = load_rail_stops(commuter_file_path)

    # Generate the map and return the file path
    map_file = plot_rail_stops(green_stops, red_stops, dart_stations, intercity_stations, commuter_stations)

    return render_template('map.html', map_file=map_file)

if __name__ == '__main__':
    app.run(debug=True)
