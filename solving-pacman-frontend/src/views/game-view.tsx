import React, { useEffect, useState } from "react";
import { Header } from "../components/header";
import { useLocation } from "react-router-dom";
import GameWindow from "../components/game-window";
import "../styles/views/game-view.scss";
import { fetchGame } from "../services/api-service";
import { GameState } from "@models/game-state";

/**
 * View showing the render of the game window.
 */
export function GameView() {
  const location = useLocation();
  const level_num = location.state.level;
  const [game, setGame] = useState<GameState[]>();

  /**
   * Fetches the game data from the API service.
   * @returns A `list` of `GameStates`
   */
  const fetchData = async (): Promise<GameState[]> => {
    return await fetchGame(level_num.charAt(level_num.length-1));
  };

  useEffect(() => {
    fetchData()
      .then(response => {
        setGame(response);
      })
      .catch(console.error);
  }, []);

  if (game) {
    console.log(game);
    return (
      <div className="Page">
        <Header subtitle={level_num}></Header>
        <div className="Game-Container">
          <GameWindow level={game[0].state} ></GameWindow>
        </div>

      </div>
    );
  }
  else {
    return (
      <div className="Page">
        <Header subtitle={level_num}></Header>
        <div className="Game-Container">
          <p>loading...</p>
        </div>
      </div>
    );
  }
}
