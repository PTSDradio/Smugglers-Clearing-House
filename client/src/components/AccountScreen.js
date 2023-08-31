import React, { useState, useEffect } from 'react';
import Search from "./Search";
import ItemDisplay from "./ItemDisplay.js";

function AccountScreen({ searchInput, handleSearch }){
    const [itemList, setItemList] = useState([])
    
    useEffect(() => {
        fetch(`http://localhost:3000/items`)
            .then((res) => res.json())
            .then((data) => {
                setItemList(data)
            })
    }, [])

    const filteredItems = itemList.filter((item) => {
        return item.name
          .toLowerCase()
          .includes(searchInput.toLowerCase());
      });
    const itemsToDisplay = filteredItems.map((item) => {
        return <ItemDisplay id={item.id} item={item} /> 
    })

    return (
        <div> 
            <Search /> 
            <div className="items-list">
                {itemsToDisplay}
            </div>
        </div>
    )
}

export default AccountScreen;