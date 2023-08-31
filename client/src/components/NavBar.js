import { NavLink } from "react-router-dom";
import logo1 from "./images/logo1.png"

function NavBar() {
  
  return (
    <header>      
        <nav className="navbar-styles"> 
          <img className="logo1-img" src={logo1} alt={"logo"}/>
          <div>
            <li> <NavLink to='/'> Buy </NavLink> </li>
            <li> <NavLink to="/sell"> Sell </NavLink> </li>
            <li> <NavLink to='/account'> Account </NavLink> </li>
          </div>
        </nav>
    </header>
  );
}

export default NavBar;
