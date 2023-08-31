import React, { useState } from 'react';
import { NavLink, Router, useNavigate   } from "react-router-dom";
import { Formik, useFormik } from "formik";
import * as yup from "yup";

function RegisterForm(){
  let navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    // const [userType, setUserType] = useState('');
    // const [username, setUsername] = useState('');
    // const [password, setPassword] = useState('');

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
      onSubmit:  async (values) => {
        const usernameExists = null //Code here to check if user exists 
        if (usernameExists) {
        alert("Username already exists");
        } else {
        try {
            const response = await fetch("http://127.0.0.1:5555/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(values, null, 2),
            });
            if (response.status === 200) {

            }} 
            catch (error) {
            console.error("Error Posting Users:", error);
        }
        }
      },
    });

    return (
        <div>
            <form onSubmit={formik.handleSubmit}>
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
                  name='username'
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
                  name='password'
                  type="password"
                  value={formik.values.password}
                  placeholder="Password"
                  onChange={formik.handleChange}
                />
                <p style={{ color: "red" }}> {formik.errors.password}</p>
              </label>
              <br />
              <button type="submit">Submit</button>
              <NavLink to='/login'> Already have an account? Login here. </NavLink>
            </form>
        </div>
      );
  }
  
export default RegisterForm;
  