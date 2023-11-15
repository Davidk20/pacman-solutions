import React from "react";
import "./App.css";
import logo from "./assets/images/pacman_logo.png";

function App() {
  return (
    <div className="App">
      <header className="App-Header">
        <h1 className="Page-Title">PACMAN SOLUTIONS</h1>
      </header>
      <div className="Home-Menu">
        <img className="Pacman-Logo" src={logo}/>
      </div>
    </div>
  );
}

export default App;
