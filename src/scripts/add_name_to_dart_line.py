import json
import geojson

# Path to the input GeoJSON file (existing DART stations data)
input_file = 'data\dart_stations.geojson'

# Path to the output GeoJSON file (where modified data will be saved)
output_file = 'data\dart_stations_modified.geojson'  # The modified file path

# Read the original GeoJSON data from the input file
with open(input_file, 'r') as f:
    dart_stations_data = geojson.load(f)

# Add the "Name", "Line", and "Description" fields to each feature
for idx, feature in enumerate(dart_stations_data['features']):
    # Create a placeholder name: "Station 1", "Station 2", ...
    name = f"Station {idx + 1}"
    # Assign the new properties
    feature['properties']['Name'] = name
    feature['properties']['Line'] = "DART"  # Default to "Green", modify as needed
    feature['properties']['Description'] = ""  # Empty description for now

# Save the modified data as a new GeoJSON file
with open(output_file, 'w') as f:
    geojson.dump(dart_stations_data, f, indent=4)

print(f"Modified dataset saved as '{output_file}'")
