/**
 * Base code for this taken with inspiration from
 * https://codesandbox.io/p/sandbox/canvas-react-typescript-lqq9k?file=%2Fsrc%2FApp.tsx
 */

import React, { useEffect, useRef } from "react";
import Wall from "./canvas/wall";

/**
 * Function to return a game window.
 *
 * @param level The level as a 2-D array.
 */
export default function GameWindow( {level}: {level: number[][]} ) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frameRef = useRef<number>(0);
  const height = 800;
  const width = 800;
  let xPos = 0;
  let yPos = 0;

  useEffect(() => {
    function draw(context: CanvasRenderingContext2D) {
      if (context) {
        // Draw base game window
        context.fillStyle = "black";
        context.fillRect(0, 0, height, width);
        // Draw game
        for (const row of level) {
          for (const pos of row) {
            if (pos == 99) {
              Wall(context, height, xPos, yPos);
            }
            xPos = xPos + (width / 28);
          }
          xPos = 0;
          yPos = yPos + (height / 31);
        }
      }
    }
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
