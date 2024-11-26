# Mapping_project
This project visualizes Luas stops on a map using Python and folium. With plans to expand to expand to other public transport services with the aim of eventually tying it all together with housing locations, allowing you to make more informed decisions when choosing to buy or rent a house/apartment.

## Setup Instructions
1. Clone the repository: `git clone https://github.com/BearachB/mapping_project.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Features
- **Interactive Maps**: Displays Luas, DART, and other rail stations on an interactive map.
- **Layer Control**: Toggle between different transport services (e.g., Luas Green Line, DART, etc.).
- **Search Functionality**: Search for an address and visualize it on the map.
- **Dynamic CSS**: Responsive layout with automatically adjusted heights for header and footer.
- **Custom Markers**: Each stop features customized markers and popups with detailed information.
- **Expandable Design**: Designed to integrate housing data and transport overlays seamlessly.

## Technologies Used
- Frontend: HTML, CSS, JavaScript, Folium
- Backend: Python, Flask
- Data Visualization: GeoPandas, Leaflet.js (via Folium)
- Mapping Data: OpenStreetMap
- Search API: Nominatim Geocoding (via geopy)

## Directory Structure
```
mapping_project/
├───backend                     # Core backend directory for the Flask application and data processing logic.
│   │   app.py                  # Main Flask application file, handles routing and server logic.
│   │   plot_rail_stops.py      # Python script for generating map visualizations using folium.
│   │   
│   ├───data                    # Directory for storing geospatial data files.
│   │   │   dart_stations.geojson              # GeoJSON file with details of DART stations.
│   │   │   dublin_commuter_stations.geojson  # GeoJSON file with data for Dublin commuter rail stations.
│   │   │   intercity_rail_stations.geojson   # GeoJSON file containing intercity rail station data.
│   │   │   luas_stops_green.geojson          # GeoJSON data for stops on the Green Luas line.
│   │   │   luas_stops_red.geojson            # GeoJSON data for stops on the Red Luas line.
│   │   │   Rail_Network___OSi_National_250k_Map_Of_Ireland_-6672425458266791814.geojson  
│   │   │                                    # Comprehensive GeoJSON data for Ireland's rail network.
│   │   │   
│   │   └───reference           # Directory for reference materials such as maps and images.
│   │           dublin-rail-map.pdf          # PDF reference map of Dublin's rail network.
│   │           Dublin_Rail_Map.JPG          # Image reference of Dublin's rail map.
│   │           intercity-map.pdf            # PDF reference map for Ireland's intercity rail network.
│   │           Luas_Map.jpg                 # Image of the Luas tram system map.
│   │           
│   ├───static                  # Directory for static assets such as styles, icons, and pre-rendered maps.
│   │   │   rail_map.html       # Rendered HTML file for the interactive rail map.
│   │   │   
│   │   ├───icons               # Placeholder directory for any map icons or visual elements (currently empty).
│   │   │       
│   │   ├───maps                # Directory for storing rendered map files.
│   │   │       rail_map.html   # Rendered HTML for the interactive rail map.
│   │   │       
│   │   └───styles              # Directory for CSS styles.
│   │           map.css         # CSS file for styling the map visualization and related elements.
│   │           
│   ├───templates               # Directory for HTML templates used by Flask.
│   │       map.html            # HTML template for rendering maps dynamically in the application.
│   │       
│   └───__pycache__             # Auto-generated directory for cached Python bytecode files.
│           plot_rail_stops.cpython-39.pyc  # Cached bytecode for `plot_rail_stops.py`.
│           
├───static                      # Root-level static directory for serving additional map assets (currently minimal).
│   └───maps                    # Placeholder for additional static map files.
└───venv                        # Virtual environment directory for managing Python dependencies.
```
## Roadmap

- [x]  Display Luas Green and Red Line stops with interactive markers.
- [x]  Make layers toggle-able.
- [x]  Add DART, intercity, and commuter stations to the map.
  - [x] Find datasets (https://data.gov.ie, https://overpass-turbo.eu/)
  - [x] Download/integrate datasets from overpass:
  - [x] `[out:json];
node["railway"="station"]["network"~"DART"](51.0,-10.5,55.5,-5.0);
out body;`
- [x]  Add reference data for rail stops.
- [x]  Port over to Flask as backend server.
- [x]  Update project structure (change output map name). 
- [x]  Frontend bits:
  - [x]  Create icon set for application. 
  - [x]  Add icon to header and tab.
  - [x]  Header/footer.
    - [x]  Add header/footer.
    - [x]  Choose colour palette.
    - [x]  Make header/footer fixed + add background colour.
- [ ]  Implement search functionality for address lookups.
  - [ ] Add search box for users.
  - [ ] Take user input and use that to fetch location.
  - [ ] Zoom map to location and place marker. 
- [ ] Implement walking time radius functionality around fetched address.
 Customize map markers with descriptive popups.