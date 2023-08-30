import React, { useState } from 'react';

function SellScreen(){
    const [itemToSell, setItemToSell] = useState({})

    return (
        <div> 
            <form>
                <label> Item ID: <input /> </label>
                <br />
                <label> Description: <input /> </label>
                <br />
                <label> Image URL <input /> </label>
            </form>
        </div>
    )
}

export default SellScreen;