import React, { useState } from 'react';

function RegisterForm(){
    const [isRegistered, setIsRegistered] = useState(false);
    const [userType, setUserType] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const registerAccount = () => {
      const loginInfo = {
        type: userType,
        name: username,
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
      registerAccount()
    };
    
    const handleSelectChange = (e) => {
      // This determines which URL the login POST request is sent to.
      setUserType(e.target.value);
    };

    return (
      <div>
        Register for New Account: 
        {!isRegistered ? (
          <form onSubmit={handleLogin}>
            <label>
              Select user type: 
              <select value={userType} onChange={handleSelectChange}> 
                <option value='users'> Buyer </option>
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
            <button type="submit">Register</button>
          </form>
        ) : (
          <p>You have registered your account!</p>
        )}
      </div>
    );
  }
  
export default RegisterForm;
  