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
        image_url: itemImageUrl
    }
    
    const listItem = () => {
        window.alert("gotcha!")
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
                <label> Item Price: <input type='text' onChange={(e) => setItemPrice(e.target.value)}/> </label>
                <br /> 
                <label> Image URL <input type='text'onChange={(e) => setItemImageUrl(e.target.value)}/> </label>
                <br /> 
                <button onClick={handleSubmit}> Submit Item Listing </button>
            </form>
        </div>
    )
}

export default SellScreen;