import React from "react";

function ItemDisplay({ item }){

    return (
        <div>
            <h1> {item.name} </h1>
            <h1> {item.price} </h1>
            <h1> {item.description} </h1>
        </div>
    )
}

export default ItemDisplay