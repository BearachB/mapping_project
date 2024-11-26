from flask import Flask, jsonify, send_file
import os
from plot_rail_stops import plot_rail_stops, load_geojson

app = Flask(__name__)

# Base directory of the application
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load data paths
DATA_FILES = {
    "luas_green": os.path.join(BASE_DIR, "data", "luas_stops_green.geojson"),
    "luas_red": os.path.join(BASE_DIR, "data", "luas_stops_red.geojson"),
    "dart": os.path.join(BASE_DIR, "data", "dart_stations.geojson"),
    "intercity": os.path.join(BASE_DIR, "data", "intercity_rail_stations.geojson"),
    "commuter": os.path.join(BASE_DIR, "data", "dublin_commuter_stations.geojson"),
    "atm": os.path.join(BASE_DIR, "data", "atm_data.geojson"),
}

# API endpoint to fetch GeoJSON data
@app.route('/api/data/<dataset_name>', methods=['GET'])
def get_dataset(dataset_name):
    """Serve the requested dataset as GeoJSON."""
    file_path = DATA_FILES.get(dataset_name)
    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "Dataset not found"}), 404

    with open(file_path, 'r') as file:
        return file.read(), 200, {'Content-Type': 'application/json'}

# API endpoint to fetch the map as an HTML file
@app.route('/api/map', methods=['GET'])
def get_map():
    """Generate and serve the map file."""
    # Load data and generate the map
    green_stops = load_geojson(DATA_FILES["luas_green"])
    red_stops = load_geojson(DATA_FILES["luas_red"])
    dart_stations = load_geojson(DATA_FILES["dart"])
    intercity_stations = load_geojson(DATA_FILES["intercity"])
    commuter_stations = load_geojson(DATA_FILES["commuter"])
    atm_locations = load_geojson(DATA_FILES["atm"])

    # Generate the map and return the file path
    map_file = plot_rail_stops(
        green_stops, red_stops, dart_stations, 
        intercity_stations, commuter_stations, atm_locations
    )

    # Serve the generated map file
    return send_file(map_file)


if __name__ == '__main__':
    app.run(debug=True)
