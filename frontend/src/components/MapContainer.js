import React from 'react';

const MapContainer = () => {
  return (
    <div id="map-container">
      {/* Embed the map dynamically */}
      <iframe
        src="http://127.0.0.1:5000/api/map" // Adjust this to your backend map API endpoint
        title="Dublin Rail Map"
      ></iframe>
    </div>
  );
};

export default MapContainer;
