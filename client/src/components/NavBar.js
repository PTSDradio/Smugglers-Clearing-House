import { NavLink } from "react-router-dom";


function NavBar({ isLoggedIn }) {
  const logOut = () => {
    //Code here to send delete request to logout 

  }

  return (
    <header>      
        <nav className="navbar-styles"> 
          <h1>Smuggler's Clearing House</h1>  
          <li> <NavLink to='/'> Buy </NavLink> </li>
          <li> <NavLink to="/sell"> Sell </NavLink> </li>
          <li> <NavLink to='/account'> Account </NavLink> </li>
          {isLoggedIn ? <button> Logout </button> :  <li> <NavLink to='/login'> Register/Login </NavLink></li> }
        </nav>
    </header>
  );
}

export default NavBar;
