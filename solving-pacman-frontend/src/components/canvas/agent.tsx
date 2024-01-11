import pacman from "../../assets/images/sprites/pacman.png";
import blinky from "../../assets/images/sprites/blinky.png";
import clyde from "../../assets/images/sprites/clyde.png";
import inky from "../../assets/images/sprites/inky.png";
import pinky from "../../assets/images/sprites/pinky.png";

/**
 * Renders the Pac-Man agent.
 *
 * @param context The reference to the canvas on which the dot is being drawn on.
 * @param agent The agent to be rendered.
 * @param size The size of the canvas. Used for scale.
 * @param x The x coordinate to place the dot at.
 * @param y The y coordinate to place the dot at.
 */
export default function Agent(context: CanvasRenderingContext2D, agent: string, size: number, x: number, y: number) {
  const offset = (size / 31) * 0.15;
  const image = new Image();
  switch (agent) {
  case "pacman":
    image.src = pacman;
    break;
  case "blinky":
    image.src = blinky;
    break;
  case "clyde":
    image.src = clyde;
    break;
  case "inky":
    image.src = inky;
    break;
  case "pinky":
    image.src = pinky;
    break;
  default:
    throw new Error("Agent not found");
  }
  image.onload = () => {
    context.drawImage(image, x + offset, y + offset, (size / 31) * 0.7, (size / 28) * 0.7);
  };
}
