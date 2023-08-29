import { NavLink } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import LoginForm from "./LoginForm"

function NavBar() {
  

  return (
    <header>      
        <nav className="navbar-styles"> 
          <h1>Smuggler's Clearing House</h1>  
          <li> Buy </li>
          <li> Sell </li>
          <li> Account </li>
        </nav>
        <LoginForm />
    </header>
  );
}

export default NavBar;
