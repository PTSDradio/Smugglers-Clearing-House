import React, { useState } from "react";

function Search({ handleSearch }){
    const [search, setSearch] = useState("");

    const handleSubmit = (e) => {
      e.preventDefault();
      setSearch(e.target.value)
      handleSearch(search);
    }

  
    return (
        <form className="searchbar">
            <input
            type="text"
            id="search"
            placeholder="Search by name"
            value={search}
            onChange={(e) => {handleSubmit(e)}}
            />
      </form>
    )
}

export default Search