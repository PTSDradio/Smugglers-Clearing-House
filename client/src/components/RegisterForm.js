import React, { useState } from 'react';
import { NavLink } from "react-router-dom";
import { Formik, useFormik } from "formik";
import * as yup from "yup";

function RegisterForm(){
    const [isLoggedIn, setIsLoggedIn] = useState(false);
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
          body: JSON.stringify(values),
        })
        .then((res) => {
          if (res.status == 200) {
            setIsLoggedIn(true)
          }
        })
      }
    })

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
              <NavLink to='/login'> Already have an account? Login here. </NavLink>
            </form>
          ) : (
            <p>You have registered your account! <link href='http://localhost:3000/login'> Sign in here </link> </p>
          )}
        </div>
      );
  }
  
export default RegisterForm;
  