import React, { useState } from "react";

const SearchBox = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  const handleInputChange = (event) => {
    const value = event.target.value;
    setQuery(value);
    onSearch(value); // Pass the query back to the parent component
  };

  return (
    <div style={{ margin: "10px 0" }}>
      <input
        type="text"
        placeholder="Search..."
        value={query}
        onChange={handleInputChange}
        style={{
          padding: "10px",
          fontSize: "1rem",
          width: "100%",
          maxWidth: "400px",
          margin: "0 0 0 25px",
        }}
      />
    </div>
  );
};

export default SearchBox;
