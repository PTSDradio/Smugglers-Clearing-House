import React, { useEffect, useState } from "react";
import ItemDisplay from "./ItemDisplay";

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
        <div> 
            <h1>{itemMap}</h1>
        </div>
    )
}


export default BuyScreen; 