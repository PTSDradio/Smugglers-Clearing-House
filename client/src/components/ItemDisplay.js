import React, { useEffect, useState } from "react";

function ItemDisplay({ item }){
    const [bidAmount, setBidAmount] = useState();

    async function enterBid(){
        const config = {
            method: "POST", 
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(bidAmount),
        };
        const res = await fetch("/items", config)
        if (res.ok){
            //Code here to enter bid into item. 
        } else {
            //Code here to alert error. 
        }
    }
    function handleChange(e) {
        setBidAmount({
          ...bidAmount,
          [e.target.id]: e.target.value,
        });
      }
    
    function handleSubmit(e) {
        e.preventDefault();
        enterBid()
    }
    
    return (
        <div className='item-container'>
            <h3> {item.name} </h3>
            <h3> Description: <h4>{item.description}</h4> </h3>
            <h3> $ {item.price} </h3>
            <img src='https://m.media-amazon.com/images/M/MV5BMTg2MTkwMDcxNF5BMl5BanBnXkFtZTcwNzk1NzEyNw@@._V1_.jpg' class='image'/>
            <form>
                <input type='text' placeholder='Enter bid amount here' onChange={handleChange}></input>
                <button type='submit' onClick={handleSubmit}> Enter Bid </button>
            </form>
        </div>
    )
}


export default ItemDisplay;