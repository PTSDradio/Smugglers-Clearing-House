import React, { useState } from 'react';
import { NavLink } from "react-router-dom";
import { useFormik } from "formik";
import * as yup from "yup";

function LoginForm({ isLoggedIn, setIsLoggedIn }){

    const formSchema = yup.object().shape({
      username: yup.string().required("Must enter a username"),
      password: yup.string().required("Must enter a password"),
      user_type: yup.string().required("Must select an user type"),
    })
    
    const formik = useFormik({
      initialValues: {
        username: "",
        password: "", 
        user_type: "",
      },
      validationSchema: formSchema, 
      onSubmit: (values) => {
        fetch('http://127.0.0.1:5555/login', {
          method: 'POST', 
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values, null, 2),
        })
        .then((res) => {
          if (res.status == 200) {
            setIsLoggedIn(true)
            console.log(res)
          }
        })
        //Back end - Write a function that Users/Sellers.query.filter(values.username)
        //Back end - GET request by user/seller ID.
        //Front end - Assign useState variable with user/seller items. 
      }
    })

  
    return (
      <div className="login-container">
        Login: 
        {isLoggedIn ? (
          <p>You are logged in!</p>
        ) : (
          <form onSubmit={formik.handleSubmit} className="login-form">
            <label>
              Select user type: 
              <select id='user_type' name='user_type' value={formik.values.user_type} onChange={formik.handleChange}> 
                <option > select type </option>
                  <option value='buyer'> Buyer </option>
                  <option value='seller'> Seller </option>
                </select>
              <p style={{ color: "red" }}> {formik.errors.user_type}</p>
            </label>
            <label>
              Username: 
              <input
                id='username'
                type="text"
                value={formik.values.username}
                placeholder="Username"
                onChange={formik.handleChange}
              />
              <p style={{ color: "red" }}> {formik.errors.username}</p>
            </label>
            <br />
            <label>
              Password:
              <input
                id='password'
                type="password"
                value={formik.values.password}
                placeholder="Password"
                onChange={formik.handleChange}
              />
              <p style={{ color: "red" }}> {formik.errors.password}</p>
            </label>
            <br />
            <button type="submit">Login</button>
            <br />
            <br />
            <br /> 
            <NavLink className="register-link" to='/register'> Need an account? Register here. </NavLink>
          </form>
        )}
      </div>
    );
  }
  
export default LoginForm;
  