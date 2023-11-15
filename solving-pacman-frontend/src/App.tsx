import React from "react";
import "./App.css";
import { HomePageView } from "./views/home-page-view";

function App() {
  return (
    <div className="App">
      <header className="App-Header">
        <h1 className="Page-Title">PACMAN SOLUTIONS</h1>
      </header>
      <HomePageView></HomePageView>
    </div>
  );
}

export default App;
