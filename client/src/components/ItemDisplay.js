import React, { useEffect, useState } from "react";

function ItemDisplay({ item }){
    const [bidAmount, setBidAmount] = useState();

    async function enterBid(){
        const bid = {
            method: "POST", 
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(bidAmount),
        };
        const res = await fetch("/items")
        if (res.ok){
            //Code here to enter bid into item. 
        } else {
            //Code here to alert error. 
        }
    }
    function handleChange(e) {
        setBidAmount(e.target.value);
      }
    
    function handleSubmit(e) {
        e.preventDefault();
        enterBid()
    }


    //Need to add code to show the current highest bid amount.
    return (
        <div className='item-container'>
            <h3> {item.name} </h3>
            <h3> Description: <h4>{item.description}</h4> </h3>
            <h3> $ {item.price} </h3>
            <img src={item.image_url} />
            <form>
                <input type='text' placeholder='Enter bid amount here' onChange={handleChange}></input>
                <button type='submit' onClick={handleSubmit}> Enter Bid </button>
            </form>
        </div>
    )
}


export default ItemDisplay;