import React, { useState } from 'react';

function SellScreen(){
    const [itemToSell, setItemToSell] = useState({})
    const [itemName, setItemName] = useState('')
    const [itemDesc, setItemDesc] = useState('')
    const [itemPrice, setItemPrice] = useState('')
    const [itemImageUrl, setItemImageUrl] = useState('')

    const itemListing = {
        name: itemName,
        description: itemDesc,
        price: itemPrice,
        image_url: itemImageUrl,
        seller_id: null,
    }

    const listItem = () => {
        fetch("http://localhost:3000/items", {
            method: "POST", 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(itemListing)})
            .then((res) => res.json())
            .then(data => {console.log(data)})
            .catch(error => {
                console.error('Error', error);
                window.alert(error);
              })
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        listItem() 
    }

    return (
        <div> 
            <form>
                <label> Item Name: <input type='text' onChange={(e) => setItemName(e.target.value)}/> </label>
                <br />
                <label> Description: <input type='text' onChange={(e) => setItemDesc(e.target.value)}/> </label>
                <br />
                <label> Item Price: <input type='number' onChange={(e) => setItemPrice(e.target.value)}/> </label>
                <br /> 
                <label> Image URL <input type='text'onChange={(e) => setItemImageUrl(e.target.value)}/> </label>
                <br /> 
                <button onClick={handleSubmit}> Submit Item Listing </button>
            </form>
        </div>
    )
}

export default SellScreen;