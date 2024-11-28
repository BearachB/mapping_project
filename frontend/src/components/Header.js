import React from 'react';
import SearchBox from './SearchBox';

const Header = () => {
  return (
    <header style={{ display: 'flex', alignItems: 'center' }}>
      <img
        src={`${process.env.PUBLIC_URL}/favicon.ico`}
        alt="Icon"
        style={{ width: '32px', height: '32px', verticalAlign: 'bottom' }}
      />
      <h3 style={{ marginLeft: '10px' }}>Dublin Rail Map</h3>
      <br></br>
      <br></br>
      <SearchBox></SearchBox>
    </header>
  );
};

export default Header;
