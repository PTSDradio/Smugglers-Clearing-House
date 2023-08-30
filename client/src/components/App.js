import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import BuyScreen from "./BuyScreen";
import NavBar from "./NavBar";

function App() {
  return (
    <div> 
      <NavBar /> 
      <BuyScreen /> 
    </div>
    );
}

export default App;
