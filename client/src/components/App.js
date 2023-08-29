import React, { useEffect, useState } from "react";
import { Routes, Route, Router } from "react-router-dom";
import BuyScreen from "./BuyScreen";
import NavBar from "./NavBar";
import SellScreen from "./SellScreen";
import LoginForm from "./LoginForm"
import AccountScreen from "./AccountScreen";
import Search from "./Search";

function App() {
  const [searchInput, setSearchInput] = useState("");

  const handleSearch = (input) => {
    setSearchInput(input);
  }; 

  return (
    <div> 
      <NavBar /> 
      <Search handleSearch={handleSearch} />
      <LoginForm />
        <Routes>
          <Route exact path='/' element={<BuyScreen searchInput={searchInput}/>}/>
          <Route exact path='/sell' element={<SellScreen />}/>
          <Route exact path='account' element={<AccountScreen searchInput={searchInput}/>}/> 
        </Routes>
    </div>
    );
}

export default App;
