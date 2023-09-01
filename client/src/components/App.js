import React, { useEffect, useState } from "react";
import { Routes, Route, Router } from "react-router-dom";
import BuyScreen from "./BuyScreen";
import NavBar from "./NavBar";
import SellScreen from "./SellScreen";
import LoginForm from "./LoginForm"
import AccountScreen from "./AccountScreen";
import RegisterForm from "./RegisterForm";

function App() {
  const [searchInput, setSearchInput] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState(false)

  const handleSearch = (input) => {
    setSearchInput(input);
  }; 

  return (
    <div> 
      <NavBar isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn}/> 
        <Routes>
          <Route exact path='/' element={<BuyScreen searchInput={searchInput} handleSearch={handleSearch}/>}/>
          <Route exact path='/sell' element={<SellScreen />}/>
          <Route exact path='account' element={<AccountScreen searchInput={searchInput} handleSearch={handleSearch}/>}/> 
          <Route exact path='/login' element={<LoginForm isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn}/>}/>
          <Route exact path='/register' element={<RegisterForm setIsLoggedIn={setIsLoggedIn}/>}/> 
        </Routes>
    </div>
    );
}

export default App;
