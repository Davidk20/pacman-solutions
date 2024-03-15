/**
 * Base code for this taken with inspiration from
 * https://codesandbox.io/p/sandbox/canvas-react-typescript-lqq9k?file=%2Fsrc%2FApp.tsx
 */

import React from "react";
import { Wall } from "./game/wall";
import { Dot } from "./game/dot";
import { Energiser } from "./game/energiser";

/**
 * Props for the Game Window.
 */
type GameWindowProps = {
  /**
   * The level.
   */
  level: number[][]
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
    this.windowHeight = this.entityHeight * this.props.level.length;

    const gameComponents = [];
    for (let row = 0; row < this.props.level.length; row++) {
      const componentRow = [];
      for (let col = 0; col < this.props.level[row].length; col++) {
        // level[0] can only be read whilst accessing props.
        this.windowWidth = this.entityWidth * this.props.level[0].length;
        if (this.props.level[row][col] == 99) {
          componentRow.push(
            <Wall
              key={col*row*Math.random()}
              width={this.entityWidth}
              height={this.entityHeight}
              yPos={this.entityHeight*row}
              xPos={this.entityWidth*col}
            />
          );
        }
        if (this.props.level[row][col] == 1) {
          componentRow.push(
            <Dot
              key={col*row*Math.random()}
              width={this.entityWidth}
              height={this.entityHeight}
              yPos={this.entityHeight*row}
              xPos={this.entityWidth*col}
            />
          );
        }
        if (this.props.level[row][col] == 2) {
          componentRow.push(
            <Energiser
              key={col*row*Math.random()}
              width={this.entityWidth}
              height={this.entityHeight}
              yPos={this.entityHeight*row}
              xPos={this.entityWidth*col}
            />
          );
        }
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
