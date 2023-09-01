import { NavLink } from "react-router-dom";
import logo1 from "./images/logo1.png"

function NavBar({ isLoggedIn, setIsLoggedIn }) {
  const logOut = () => {
    //Code here to send delete request to logout 
    setIsLoggedIn(false)
    


  }

  return (
    <header>      
        <nav className="navbar-styles"> 
          <img className="logo1-img" src={logo1} alt={"logo"}/>
          <div>
          <li> <NavLink to='/'> Buy </NavLink> </li>
          <li> <NavLink to="/sell"> Sell </NavLink> </li>
          <li> <NavLink to='/account'> Account </NavLink> </li>
          {isLoggedIn ? <button> Logout </button> :  <li> <NavLink to='/login'> Register/Login </NavLink></li> }
          </div>
        </nav>
    </header>
  );
}

export default NavBar;
