import React, { useState } from 'react';
import { NavLink } from "react-router-dom";
import { Formik, useFormik } from "formik";
import * as yup from "yup";

function LoginForm({ isLoggedIn, setIsLoggedIn }){
    // const [userType, setUserType] = useState('');
    // const [username, setUsername] = useState('');
    // const [password, setPassword] = useState('');

    const formSchema = yup.object().shape({
      username: yup.string().required("Must enter a username"),
      password: yup.string().required("Must enter a password"),
      userType: yup.string().required("Must select an user type"),
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
          }
        })
      }
    })

    // const loginAction = () => {
    //   const loginInfo = {
    //     username: username,
    //     password: password,
    //     user_type: userType
    //   }
      
    //   //This fetch link needs to be changed to a new API route that manages logins. This just posts a new user. 
    //   fetch(`http://localhost:5555/login`, {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(loginInfo)})
    //     .then((res) => res.json())
    //     .then(data => {
    //       console.log(data);
    //     })
    //     .catch(error => {
    //       console.error('Error', error);
    //       window.alert(error);
    //     })
    // }

    // const handleLogin = (e) => {
    //   e.preventDefault();
    //   // Login logic is called on here. 
    //   loginAction()
    // };
    
    // const handleSelectChange = (e) => {
    //   // This determines which URL the login POST request is sent to.
    //   setUserType(e.target.value);
    // };

    return (
      <div>
        Login: 
        {!isLoggedIn ? (
          <form onSubmit={formik.handleSubmit}>
            <label>
              Select user type: 
              <select id='user_type' value={formik.values.user_type} onChange={formik.handleChange}> 
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
            <NavLink to='/register'> Need an account? Register here. </NavLink>
          </form>
        ) : (
          <p>You are logged in!</p>
        )}
      </div>
    );
  }
  
export default LoginForm;
  