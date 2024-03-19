import React, { useEffect, useState } from "react";
import { Wall } from "./game/wall";
import { Dot } from "./game/dot";
import { Energiser } from "./game/energiser";
import { Agent } from "./game/agents";
import { GameState } from "@models/game-state";
import { GameStats } from "./game/game-stats";


export function GameWindow(stateStore: GameState[]) {
  const entityHeight = 22;
  /**
   * The height of a single entity within the game.
   */
  const entityWidth = 22;
  /**
   * The width of a single entity within the game.
   */

  const store = stateStore;
  /**
   * The tick history of the simulation.
   */
  const [tick, setTick] = useState(0);
  /**
   * `true` if the game is currently running.
   */
  const [running, setRunning] = useState<boolean>(false);
  /**
   * `true` if the game is completed.
   */
  const [gameOver, setGameOver] = useState<boolean>(false);

  /**
   * Starts the game simulation.
   */
  function toggleGame(): void {
    setRunning(!running);
  }

  /**
   * Restart the game once the simulation has finished.
   */
  function startGame(): void {
    setTick(0);
    setGameOver(false);
    setRunning(true);
  }

  useEffect(() => {
    const interval = setInterval(() => {
      if (running && store[tick + 1]) {
        setTick(tick + 1);
      } else if (!store[tick + 1]) {
        // Stops the game when the simulation is finished.
        setGameOver(true);
        setRunning(false);
      }
    }, 250);

    return () => clearInterval(interval);
  });

  const gameComponents = [];
  for (let row = 0; row < store[tick].state.length; row++) {
    const componentRow = [];
    for (let col = 0; col < store[tick].state[row].length; col++) {
      // level[0] can only be read whilst accessing props.
      let component;
      switch (store[tick].state[row][col]) {
      case 1:
        component = <Dot
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      case 2:
        component = <Energiser
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      case 21:
        component = <Agent
          agent="blinky"
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      case 22:
        component = <Agent
          agent="pinky"
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      case 23:
        component = <Agent
          agent="inky"
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      case 24:
        component = <Agent
          agent="clyde"
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      case 44:
        component = <Agent
          agent="pacman"
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      case 99:
        component = <Wall
          key={col*row*Math.random()}
          width={entityWidth}
          height={entityHeight}
          yPos={entityHeight*row}
          xPos={entityWidth*col}
        />;
        break;
      }
      componentRow.push(component);
    }
    gameComponents.push(componentRow);
  }

  return (
    <div
      style={{
        position: "relative",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        width:"100vw",
        height:"90vh"
      }}
    >
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          width: "40%",
          height: "100%"
        }}
      >
        <div
          style={{
            height: entityHeight * store[tick].state.length,
            width: entityWidth * store[tick].state[0].length,
            position: "absolute",
            backgroundColor: "black"
          }}
        >
          {gameComponents}
        </div>
      </div>
      <GameStats
        time={store[tick].time}
        score={0}
        energised={false}
        running={running}
        toggleGame={toggleGame}
        gameOver={gameOver}
        toggleRestart={startGame}
      >
      </GameStats>
    </div>
  );
}
