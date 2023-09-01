import React, { useState } from 'react';
import { NavLink } from "react-router-dom";

function LoginForm(){
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [userType, setUserType] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const loginAction = () => {
      const loginInfo = {
        username: username,
        password: password,
        user_type: userType
      }
      
      //This fetch link needs to be changed to a new API route that manages logins. This just posts a new user. 
      fetch(`http://localhost:5555/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginInfo)})
        .then((res) => res.json())
        .then(data => {
          console.log(data);
        })
        .catch(error => {
          console.error('Error', error);
          window.alert(error);
        })
    }

    const handleLogin = (e) => {
      e.preventDefault();
      // Login logic is called on here. 
      loginAction()
    };
    
    const handleSelectChange = (e) => {
      // This determines which URL the login POST request is sent to.
      setUserType(e.target.value);
    };

    return (
      <div>
        Login: 
        {!isLoggedIn ? (
          <form onSubmit={handleLogin}>
            <label>
              Select user type: 
              <select value={userType} onChange={handleSelectChange}> 
                <option value='buyer'> Buyer </option>
                <option value='seller'> Seller </option>
              </select>
            </label>
            <label>
              Username:
              <input
                type="text"
                value={username}
                placeholder="Username"
                onChange={(e) => setUsername(e.target.value)}
              />
            </label>
            <br />
            <label>
              Password:
              <input
                type="password"
                value={password}
                placeholder="Password"
                onChange={(e) => setPassword(e.target.value)}
              />
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
  