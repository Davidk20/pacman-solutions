import React from "react";
import "./App.css";
import { Route, HashRouter as Router, Routes } from "react-router-dom";
import { LevelSelectionView } from "./views/level-selection-view";
import { HomePageView } from "./views/home-page-view";
import { ConfigurationView } from "./views/configuration-view";
import "module-alias/register";


class App extends React.Component {
  override render(): React.ReactNode {
    return (
      <Router>
        <div>
          <Routes>
            <Route path="/" Component={HomePageView} />
            <Route path="/level-select" Component={LevelSelectionView} />
            <Route path="/configuration" Component={ConfigurationView} />
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
