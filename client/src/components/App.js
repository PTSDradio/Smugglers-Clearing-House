import React, { useEffect, useState } from "react";
import { Routes, Route, Router } from "react-router-dom";
import BuyScreen from "./BuyScreen";
import NavBar from "./NavBar";
import SellScreen from "./SellScreen";
import LoginForm from "./LoginForm"
import AccountScreen from "./AccountScreen";

function App() {
  return (
    <div> 
      <NavBar /> 
      <LoginForm />
        <Routes>
          <Route exact path='/' element={<BuyScreen />}/>
          <Route exact path='/sell' element={<SellScreen />}/>
          <Route exact path='account' element={<AccountScreen />}/> 
        </Routes>
    </div>
    );
}

export default App;
