import React, { useEffect, useState } from "react";
import ItemDisplay from "./ItemDisplay.js";

function BuyScreen({ searchInput }){
    const [itemList, setItemList] = useState([])

    useEffect(() => {
        fetch("http://localhost:3000/items")
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
    //Where can we code so if item.is_purchased is true, 
    //the item does not show up in the list.  
    
    return (
        <div className="items-list"> 
            {itemsToDisplay}
        </div>
    )
}


export default BuyScreen; 