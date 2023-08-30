import React, { useState } from 'react';

function LoginForm(){
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [userType, setUserType] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const loginAction = () => {
      const loginInfo = {
        type: userType,
        username: username,
        password: password,
      }

      fetch(`http://localhost:5555/${userType}`, {
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
        {!isLoggedIn ? (
          <form onSubmit={handleLogin}>
            <label>
              Select user type: 
              <select value={userType} onChange={handleSelectChange}> 
                <option value='buyers'> Buyer </option>
                <option value='sellers'> Seller </option>
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
          </form>
        ) : (
          <p>You are logged in!</p>
        )}
      </div>
    );
  }
  
export default LoginForm;
  