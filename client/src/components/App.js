import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar"
import BuyScreen from "./BuyScreen";

function App() {
  return (
    <div> 
      <NavBar />
      <BuyScreen /> 
    </div>
    );
}

export default App;
