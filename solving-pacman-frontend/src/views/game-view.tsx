import React, { useEffect, useState } from "react";
import { Header } from "../components/header";
import { useLocation } from "react-router-dom";
import GameWindow from "../components/game-window";
import "../styles/views/game-view.scss";
import { fetchLevel } from "../services/api-service";

/**
 * View showing the render of the game window.
 */
export function GameView() {
  const location = useLocation();
  const level_num = location.state.level;
  const [level, setLevel] = useState<number[][]>([]);

  useEffect(() => {
    const fetchData = async () => {
      setLevel(await fetchLevel(level_num.charAt(level_num.length-1)));
      console.log("Level Loaded");
    };
    fetchData()
      .catch(console.error);
  }, []);
  return (
    <div className="Page">
      <Header subtitle={level_num}></Header>
      <div className="Game-Container">
        <GameWindow level={level} ></GameWindow>
      </div>

    </div>
  );
}
