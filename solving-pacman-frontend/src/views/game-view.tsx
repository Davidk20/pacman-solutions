import React from "react";
import { Header } from "../components/header";
import { useLocation } from "react-router-dom";
import GameWindow from "../components/game-window";
import "../styles/views/game-view.scss";

/**
 * View showing the render of the game window.
 */
export function GameView() {
  const location = useLocation();

  return (
    <div className="Page">
      <Header subtitle={location.state.level}></Header>
      <div className="Game-Container">
        <GameWindow></GameWindow>
      </div>

    </div>
  );
}
