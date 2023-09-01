import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function ItemDisplay({ item }){
    const formSchema = yup.object().shape({
        bid_amount: yup.number().required("Must enter a bid amount higher than the current bid amount.")
        })
        
        const formik = useFormik({
        initialValues: {
            user_id: "user_id", //Code here to input user_id from session cookie. 
            bid_amount: "",
        },
        validationSchema: formSchema, 
        onSubmit: (values) => {
            fetch(`http://127.0.0.1:5555/auctions/${item.id}`, {
            method: 'POST', 
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(values, null, 2),
            })
            .then((res) => {
            if (res.status == 200) {
                
                console.log(res)
            }
            })
            //Back end - Write a function that Users/Sellers.query.filter(values.username)
            //Back end - GET request by user/seller ID.
            //Front end - Assign useState variable with user/seller items. 
        }
        })


    //Need to add code to show the current highest bid amount.
    //Need to add code to show the list of categories.
    return (
        <div className='item-container'>
            <h3> {item.name} </h3>
            <h3> Description: <h4>{item.description}</h4> </h3>
            <h3> $ {item.price} </h3>
            <img src={item.image_url} />
            <form> onSubmit={formik.handleSubmit}
                <input type='text' placeholder='Enter bid amount here' value={formik.values.bid_amount} onChange={formik.handleChange}></input>
                <button type='submit'> Enter Bid </button>
            </form>
        </div>
    )
}


export default ItemDisplay;