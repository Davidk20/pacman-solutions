/**
 * Base code for this taken with inspiration from
 * https://codesandbox.io/p/sandbox/canvas-react-typescript-lqq9k?file=%2Fsrc%2FApp.tsx
 */

import React from "react";
import { Wall } from "./game/wall";
import { Dot } from "./game/dot";
import { Energiser } from "./game/energiser";
import { Agent } from "./game/agents";
import { GameState } from "@models/game-state";

/**
 * Props for the Game Window.
 */
type GameWindowProps = {
  stateStore: GameState[];
}

/**
 * Component to return the game window from which the user can see the game..
 */
export default class GameWindow extends React.Component<GameWindowProps> {
  entityHeight = 22;
  /**
   * The height of a single entity within the game.
   */
  entityWidth = 22;
  /**
   * The width of a single entity within the game.
   */
  windowHeight: number = 0;
  /**
   * The height of the game window.
   */
  windowWidth: number = 0;
  /**
   * The width of the game window.
   */


  override render(): React.ReactNode {
    const initialState = this.props.stateStore[0].state;
    this.windowHeight = this.entityHeight * initialState.length;

    const gameComponents = [];
    for (let row = 0; row < initialState.length; row++) {
      const componentRow = [];
      for (let col = 0; col < initialState[row].length; col++) {
        // level[0] can only be read whilst accessing props.
        this.windowWidth = this.entityWidth * initialState[0].length;
        let component;
        switch (initialState[row][col]) {
        case 1:
          component = <Dot
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
          />;
          break;
        case 2:
          component = <Energiser
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
          />;
          break;
        case 21:
          component = <Agent
            agent="blinky"
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
          />;
          break;
        case 22:
          component = <Agent
            agent="pinky"
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
          />;
          break;
        case 23:
          component = <Agent
            agent="inky"
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
          />;
          break;
        case 24:
          component = <Agent
            agent="clyde"
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
          />;
          break;
        case 44:
          component = <Agent
            agent="pacman"
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
          />;
          break;
        case 99:
          component = <Wall
            key={col*row*Math.random()}
            width={this.entityWidth}
            height={this.entityHeight}
            yPos={this.entityHeight*row}
            xPos={this.entityWidth*col}
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
          height: this.windowHeight,
          width: this.windowWidth,
          position: "absolute",
          backgroundColor: "black"
        }}
      >
        {gameComponents}
      </div>
    );
  }
}
