import { NavLink } from "react-router-dom";
import Button from 'react-bootstrap/Button';

function NavBar() {
  return (
    <header>      
        <nav className="navbar-styles"> 
          <h1>Smuggler's Clearing House</h1>  
          <li> Buy </li>
          <li> Sell </li>
          <li> Account </li>
        </nav>
    </header>
  );
}

export default NavBar;
