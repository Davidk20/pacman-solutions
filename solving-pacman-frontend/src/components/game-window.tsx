/**
 * Base code for this taken with inspiration from
 * https://codesandbox.io/p/sandbox/canvas-react-typescript-lqq9k?file=%2Fsrc%2FApp.tsx
 */

import React from "react";
import { useEffect, useRef } from "react";

/**
 * Function to return a game window.
 */
export default function GameWindow() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frameRef = useRef<number>(0);
  const height = 800;
  const width = 800;

  useEffect(() => {
    function draw(context: CanvasRenderingContext2D) {
      if (context) {
        context.fillStyle = "black";
        context.fillRect(0, 0, height, width);

        frameRef.current = requestAnimationFrame(() => draw(context));
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
