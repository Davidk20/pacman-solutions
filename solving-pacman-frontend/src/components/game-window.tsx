import React, { useEffect, useState } from "react";
import { Wall } from "./game/wall";
import { Dot } from "./game/dot";
import { Energiser } from "./game/energiser";
import { Agent } from "./game/agents";
import { GameState } from "@models/game-state";


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
   * The state history of the simulation.
   */
  const [state, setState] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      if (store[state + 1]) {
        setState(state + 1);
      }
    }, 1000);

    return () => clearInterval(interval);
  });

  const gameComponents = [];
  for (let row = 0; row < store[state].state.length; row++) {
    const componentRow = [];
    for (let col = 0; col < store[state].state[row].length; col++) {
      // level[0] can only be read whilst accessing props.
      let component;
      switch (store[state].state[row][col]) {
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
        height: entityHeight * store[state].state.length,
        width: entityWidth * store[state].state[0].length,
        position: "absolute",
        backgroundColor: "black"
      }}
    >
      {gameComponents}
    </div>
  );
}
