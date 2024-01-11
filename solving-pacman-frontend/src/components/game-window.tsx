/**
 * Base code for this taken with inspiration from
 * https://codesandbox.io/p/sandbox/canvas-react-typescript-lqq9k?file=%2Fsrc%2FApp.tsx
 */

import React, { useEffect, useRef } from "react";
import Wall from "./canvas/wall";
import Dot from "./canvas/dot";
import PowerPellet from "./canvas/power-pellet";
import Agent from "./canvas/agent";

/**
 * Function to return a game window.
 *
 * @param level The level as a 2-D array.
 */
export default function GameWindow( {level}: Readonly<{level: number[][]}> ) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frameRef = useRef<number>(0);
  const height = 800;
  const width = 800;
  let xPos = 0;
  let yPos = 0;

  function draw(context: CanvasRenderingContext2D) {
    if (context) {
      // Draw base game window
      context.fillStyle = "black";
      context.fillRect(0, 0, height, width);
      // Draw game
      for (const row of level) {
        for (const pos of row) {
          switch (pos) {
          case 1:
            Dot(context, height, xPos, yPos);
            break;
          case 2:
            PowerPellet(context, height, xPos, yPos);
            break;
          case 21:
            Agent(context, "blinky", height, xPos, yPos);
            break;
          case 22:
            Agent(context, "clyde", height, xPos, yPos);
            break;
          case 23:
            Agent(context, "inky", height, xPos, yPos);
            break;
          case 24:
            Agent(context, "pinky", height, xPos, yPos);
            break;
          case 44:
            Agent(context, "pacman", height, xPos, yPos);
            break;
          case 99:
            Wall(context, height, xPos, yPos);
            break;
          default:
            break;
          }
          xPos = xPos + (width / 28);
        }
        xPos = 0;
        yPos = yPos + (height / 31);
      }
    }
  }

  useEffect(() => {
    if (canvasRef.current) {
      const context = canvasRef.current.getContext("2d");

      if (context) {
        context.canvas.height = height;
        context.canvas.width = width;

        frameRef.current = requestAnimationFrame(() => draw(context));
      }
    }
    return () => cancelAnimationFrame(frameRef.current);
  }, [height, width]);

  return <canvas ref={canvasRef} />;
}
