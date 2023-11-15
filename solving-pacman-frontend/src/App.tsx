import React from "react";
import "./App.css";
import { Route, HashRouter as Router, Routes } from "react-router-dom";
import { LevelSelectionView } from "./views/level-selction-view";
import { HomePageView } from "./views/home-page-view";

class App extends React.Component {
  override render(): React.ReactNode {
    return (
      <Router>
        <div>
          <Routes>
            <Route path="/" Component={HomePageView} />
            <Route path="/level-select" Component={LevelSelectionView} />
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
