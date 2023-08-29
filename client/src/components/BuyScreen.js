import React, { useEffect, useState } from "react";
import ItemDisplay from "./ItemDisplay.js";

function BuyScreen(){
    const [items, setItems] = useState([])

    useEffect(() => {
        fetch("http://localhost:3000/items")
            .then((res) => res.json())
            .then((data) => {
                setItems(data)
            })
    }, [])

    const itemMap = items.map((item) => {
        return <ItemDisplay id={item.id} item={item} /> 
    })

    return (
        <div className="items-list"> 
            {itemMap}
        </div>
    )
}


export default BuyScreen; 