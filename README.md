# Mapping_project
This project visualizes amenities on a map using Python, Folium and React. With plans to expand to expand to other public services with the aim of eventually tying it all together with housing locations, allowing you to make more informed decisions when choosing to buy or rent a house/apartment.

## Setup Instructions
### Local Setup (without Docker)
1. Clone the repository:
   ```bash
   git clone https://github.com/BearachB/mapping_project.git
2. Docker Setup (Preferred):
   1. Install Docker on your system.
   2. Navigate to the project root directory.
   3. Build and run the containers:
      1. docker compose up --build
   4. Access the application:
      1. Frontend: http://localhost:3000
      2. Backend API: http://localhost:5000
3. Dockerless Setup:
   1. Backend:
      1. Navigate to the backend directory:
         1. `cd mapping_project/backend`
      2. Create and activate a virtual environment:
         1. `python3 -m venv venv source venv/bin/activate  # On Windows use: venv\Scripts\activate`
      3. Install dependencies:
         1. `pip install -r requirements.txt`
      4. Run Flask app:
         1. `pip install -r requirements.txt`
   2. Frontend:
      1. Navigate to the frontend directory:
         1. `cd ../frontend`
      2. Install Node.js dependencies:
         1. `npm install`
      3. Start the React development server:
         1. `npm start`

## Features
- **Interactive Maps**: Displays Luas, DART, and other rail stations on an interactive map.
- **Layer Control**: Toggle between different transport services (e.g., Luas Green Line, DART, etc.).
- **Search Functionality**: Search for an address and visualize it on the map.
- **Dynamic CSS**: Responsive layout with automatically adjusted heights for header and footer.
- **Custom Markers**: Each stop features customized markers and popups with detailed information.
- **Expandable Design**: Designed to integrate housing data and transport overlays seamlessly.

## Technologies Used
- Frontend: React, JavaScript, HTML, CSS
- Backend: Python, Flask
- Mapping: Folium, GeoPandas, Leaflet.js (via Folium)
- Data Sources: OpenStreetMap, Overpass API, GeoJSON files
- Search API: Nominatim Geocoding (via geopy)
- Containerization: Docker, Docker Compose

## Directory Structure
```
mapping_project/    # Project root.
│   .gitattributes        # Git attributes file, used to define repository-specific attributes.
│   .gitignore            # Specifies files and directories that should be ignored by Git.
│   dirtree.txt           # Output file from your directory tree, showing the folder structure.
│   docker-compose.yml    # Defines services, networks, and volumes for Docker containers.
│   README.md             # The README file containing documentation about the project.
│   requirements.txt      # Lists Python dependencies required for the project.
│   
├───backend               # Backend directory, contains server-side code and assets.
│   │   .dockerignore      # Specifies files to ignore when building Docker images for the backend.
│   │   app.py             # Main application script for the backend (likely Flask or another framework).
│   │   Dockerfile         # Instructions for building a Docker image for the backend.
│   │   plot_rail_stops.py # Python script for plotting rail station locations on a map.
│   │   requirements.txt   # Python dependencies for the backend.
│   │   
│   ├───data              # Directory containing data files used in the backend.
│   │   │   atm_data.geojson                 # GeoJSON file containing ATM locations.
│   │   │   dart_stations.geojson            # GeoJSON file containing Dart station locations.
│   │   │   dublin_commuter_stations.geojson # GeoJSON file for Dublin commuter station data.
│   │   │   dunnes_stores.geojson            # GeoJSON file with locations of Dunnes Stores.
│   │   │   intercity_rail_stations.geojson  # GeoJSON file with intercity rail station data.
│   │   │   luas_stops_green.geojson         # GeoJSON file with green line Luas station data.
│   │   │   luas_stops_red.geojson           # GeoJSON file with red line Luas station data.
│   │   │   Rail_Network___OSi_National_250k_Map_Of_Ireland.geojson  # GeoJSON map of Ireland’s rail network.
│   │   │   
│   │   └───reference       # Reference materials related to the rail network.
│   │           dublin-rail-map.pdf        # PDF of Dublin rail map.
│   │           Dublin_Rail_Map.JPG        # JPEG version of the Dublin rail map.
│   │           intercity-map.pdf          # PDF of intercity rail map.
│   │           Luas_Map.jpg               # JPEG of the Luas map.
│   ├───maps                # Maps directory, likely contains HTML files for visualizing maps.
│   │       rail_and_atm_map.html   # HTML map showing both rail stations and ATM locations.
│   │       
│   ├───static              # Static files like HTML, images, CSS, etc., used in the backend.
│   │   │   rail_map.html    # HTML file showing the rail map.
│   │   │   
│   │   ├───icons           # Icons for the web application.
│   │   │       android-chrome-192x192.png   # Android icon (192x192px).
│   │   │       android-chrome-512x512.png   # Android icon (512x512px).
│   │   │       apple-touch-icon.png         # Apple touch icon.
│   │   │       favicon-16x16.png            # 16x16 favicon for the website.
│   │   │       favicon-32x32.png            # 32x32 favicon for the website.
│   │   │       favicon.ico                 # Default favicon for the site.
│   │   │       site.webmanifest            # Web app manifest, used for Progressive Web Apps.
│   │   │       
│   │   ├───maps            # Additional map-related HTML files.
│   │   │       rail_and_atm_map.html   # HTML map showing rail and ATM locations.
│   │   │       rail_map.html          # HTML rail map for the backend.
│   │   │       
│   │   └───styles          # Styles directory, for CSS files used by the static content.
│   │           map.css      # CSS file defining styles for maps.
│   ├───templates           # Template files used by the backend, often for rendering dynamic HTML.
│   │       map.html         # Template file for rendering a map on the frontend.
│   └───__pycache__         # Python bytecode files, generated automatically.
│           app.cpython-310.pyc    # Compiled bytecode for app.py (Python 3.10).
│           app.cpython-39.pyc     # Compiled bytecode for app.py (Python 3.9).
│           plot_rail_stops.cpython-310.pyc   # Compiled bytecode for plot_rail_stops.py (Python 3.10).
│           plot_rail_stops.cpython-39.pyc    # Compiled bytecode for plot_rail_stops.py (Python 3.9).
│           
├───frontend                # Frontend directory, contains the client-side code.
│   │   .dockerignore        # Specifies files to ignore when building Docker images for the frontend.
│   │   .gitignore           # Specifies frontend-related files to ignore in Git.
│   │   Dockerfile           # Instructions for building a Docker image for the frontend.
│   │   package-lock.json    # Lock file for the npm dependencies.
│   │   package.json         # Lists npm dependencies and scripts for the frontend.
│   │   README.md            # Documentation specific to the frontend.
│   │   
│   ├───build               # Contains the build output files, generated after running a build command (e.g., `npm run build`).
│   │   │   android-chrome-192x192.png   # Icon for Android devices (192x192px).
│   │   │   android-chrome-512x512.png   # Icon for Android devices (512x512px).
│   │   │   apple-touch-icon.png         # Apple touch icon.
│   │   │   asset-manifest.json          # JSON file with asset information (for cache management).
│   │   │   favicon-16x16.png            # 16x16 favicon.
│   │   │   favicon-32x32.png            # 32x32 favicon.
│   │   │   favicon.ico                 # Default favicon.
│   │   │   index.html                  # The main HTML file for the frontend.
│   │   │   logo192.png                 # Logo for the app (192x192px).
│   │   │   logo512.png                 # Logo for the app (512x512px).
│   │   │   manifest.json               # Web app manifest file, used for PWA.
│   │   │   robots.txt                  # Specifies the search engine crawling behavior.
│   │   │   site.webmanifest            # Web app manifest file.
│   │   └───static                    # Static assets like images and CSS for the build.
│   │       ├───css
│   │       │       main.46c5cb7a.css     # CSS file for the main app.
│   │       │       main.46c5cb7a.css.map # Source map for the main CSS file.
│   │       └───js
│   │               453.8ab44547.chunk.js          # JavaScript chunk file.
│   │               453.8ab44547.chunk.js.map      # Source map for the JavaScript chunk.
│   │               main.7d8396d8.js               # Main JavaScript file for the app.
│   │               main.7d8396d8.js.LICENSE.txt    # License file for the main JS.
│   │               main.7d8396d8.js.map           # Source map for the main JavaScript.
│   ├───public              # Public assets, generally static files served by the frontend.
│   │       android-chrome-192x192.png   # Android icon (192x192px).
│   │       android-chrome-512x512.png   # Android icon (512x512px).
│   │       apple-touch-icon.png         # Apple touch icon.
│   │       favicon-16x16.png            # Favicon.
│   │       favicon-32x32.png            # Favicon.
│   │       favicon.ico                 # Default favicon.
│   │       index.html                  # Main HTML file for the frontend.
│   │       logo192.png                 # App logo.
│   │       logo512.png                 # App logo.
│   │       manifest.json               # Web app manifest.
│   │       robots.txt                  # Specifies robots crawling behavior.
│   │       site.webmanifest            # Web app manifest.
│   └───src                  # Source code for the frontend.
│       │   App.css            # CSS file for the app component.
│       │   App.js             # Main JavaScript file for the app component.
│       │   App.test.js        # Test file for the app component.
│       │   index.css          # Global CSS for the frontend.
│       │   index.js           # Entry point for the frontend JavaScript.
│       │   logo.svg           # SVG logo for the frontend.
│       │   MapComponent.js    # React component for the map visualization.
│       │   reportWebVitals.js # Web vitals report (performance tracking).
│       │   setupTests.js      # Configuration for tests (likely using Jest).
│       ├───components         # React components used in the frontend.
│       │       Footer.js       # Footer component.
│       │       Header.js       # Header component.
│       │       MapContainer.js # Container for map components.
│       │       SearchBox.js    # Search box component.
│       └───styles             # Styles used in the frontend.
│               map.css        # CSS styles for the map component.
│               
├───static                   # Public static files that are not part of the frontend or backend.
    └───maps                  # Additional map-related assets.

```
## Roadmap

- [x]  Display Luas Green and Red Line stops with interactive markers.
- [x]  Make layers toggle-able.
- [ ]  Add other datasets to the map.
  - [x] DART, intercity, and commuter stations
  - [x] Find datasets (https://data.gov.ie, https://overpass-turbo.eu/)
  - [x] Download/integrate datasets from overpass:
    - [x] `[out:json];
node["railway"="station"]["network"~"DART"](51.0,-10.5,55.5,-5.0);
out body;`
  - [x] ATM location data.
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
- [x] Integrate Docker into backend and frontend.
  - [x] Install Docker.
  - [x] Backend & Frontend:
    - [x] Create Dockerfile.
    - [x] Create Dockerignore.
 Customize map markers with descriptive popups.