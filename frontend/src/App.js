import React, { useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import MapContainer from './components/MapContainer';
import './styles/map.css';

const App = () => {
  useEffect(() => {
    // Function to dynamically set CSS variables for header and footer heights
    const setDynamicHeights = () => {
      const headerHeight = document.querySelector('header').offsetHeight;
      const footerHeight = document.querySelector('footer').offsetHeight;

      document.documentElement.style.setProperty('--header-height', `${headerHeight}px`);
      document.documentElement.style.setProperty('--footer-height', `${footerHeight}px`);
    };

    setDynamicHeights();
    window.addEventListener('resize', setDynamicHeights);

    return () => window.removeEventListener('resize', setDynamicHeights);
  }, []);

  return (
    <div className="container">
      <Header />
      <MapContainer />
      <Footer />
    </div>
  );
};

export default App;
