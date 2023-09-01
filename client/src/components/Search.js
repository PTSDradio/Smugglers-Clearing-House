import React, { useState } from "react";

function Search({ handleSearch }){
    const [search, setSearch] = useState("");
    const [category, setCategory] = useState("")
    const handleSubmit = (e) => {
      e.preventDefault();
      setSearch(e.target.value)
      handleSearch(search);
    }

    const handleSelectChange = (e) => {
      e.preventDefault();
      setCategory(e.target.value)

      console.log(e.target.value)

    };
  
    return (
        <form className="searchbar">
            <input
            type="text"
            id="search"
            placeholder="Search by name"
            value={search}
            onChange={(e) => {handleSubmit(e)}}
            />
            <label>
              Filter by Category: 
              <select value={category} onChange={handleSelectChange}>
              <option value=''> None </option>
                <option value='furniture'> furniture </option>
                <option value='art'> art </option>
                <option value='contraband'> contraband </option>
                <option value='clothes'> clothes </option>
              </select>
            </label>

      </form>
    )
}

export default Search