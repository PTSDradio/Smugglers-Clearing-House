import { NavLink } from "react-router-dom";

function NavBar() {
  return (
    <header>
        <h1 class='text-lg font-bold text-center'>Smuggler's Clearing House</h1>
        <nav class='text-center'> 
          <li> Buy </li>
          <li> Sell </li>
          <li> Account </li>
        </nav>
    </header>
  );
}

export default NavBar;
