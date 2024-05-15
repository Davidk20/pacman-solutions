import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { GameWindow } from "../components/game-window";
import { fetchGame } from "../services/api-service";
import { GameState } from "@models/game-state";
import { tailChase } from "ldrs";

/**
 * View showing the render of the game window.
 */
export function GameView() {
  const location = useLocation();
  const level_num = location.state.level;
  const [game, setGame] = useState<GameState[]>();

  tailChase.register();

  /**
   * Fetches the game data from the API service.
   * @returns A `list` of `GameStates`
   */
  const fetchData = async (): Promise<GameState[]> => {
    return (await fetchGame(level_num.charAt(level_num.length-1))).states;
  };

  useEffect(() => {
    fetchData()
      .then(response => {
        setGame(response);
      })
      .catch(console.error);
  }, []);

  return (
    <div className="
      flex flex-col items-center justify-center h-dvh w-dvw bg-background-colour
      gap-10
    ">
      {game ? <GameWindow {...game} ></GameWindow> : <l-tail-chase size="150" speed="2.5" color="#F4D147"></l-tail-chase>}
    </div>
  );
}
