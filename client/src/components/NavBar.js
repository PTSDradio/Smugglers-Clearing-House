import { NavLink } from "react-router-dom";


function NavBar() {
 
  return (
    <header>      
        <nav className="navbar-styles"> 
          <h1>Smuggler's Clearing House</h1>  
          <li> <NavLink to='/'> Buy </NavLink> </li>
          <li> <NavLink to="/sell"> Sell </NavLink> </li>
          <li> <NavLink to='/account'> Account </NavLink> </li>
        </nav>
    </header>
  );
}

export default NavBar;
