import { NavLink } from "react-router-dom";
import logo2 from "./images/logo2.png"

function NavBar() {
  
  return (
    <header>      
        <nav className="navbar-styles"> 
          <img className="logo2-img" src={logo2} alt={"logo"}/>
          <li> <NavLink to='/'> Buy </NavLink> </li>
          <li> <NavLink to="/sell"> Sell </NavLink> </li>
          <li> <NavLink to='/account'> Account </NavLink> </li>
        </nav>
    </header>
  );
}

export default NavBar;
