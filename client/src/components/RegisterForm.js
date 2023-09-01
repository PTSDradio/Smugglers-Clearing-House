import React, { useState } from 'react';
import { NavLink, Router, useNavigate   } from "react-router-dom";
import { Formik, useFormik } from "formik";
import * as yup from "yup";

function RegisterForm({ setIsLoggedIn }){
    let navigate = useNavigate();

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
        fetch('http://127.0.0.1:5555/register', {
          method: 'POST', 
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values),
        })
        .then((res) => {
          if (res.status == 200) {
            setIsLoggedIn(true)
            navigate('/login')
          }
        })
      }
   
    })
    // console.log(formik.values)
    return (
        <div className="login-container">
          Register: 
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
  