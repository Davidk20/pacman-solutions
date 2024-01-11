/**
 * Renders a single Pac-Dot.
 *
 * @param context The reference to the canvas on which the dot is being drawn on.
 * @param size The size of the canvas. Used for scale.
 * @param x The x coordinate to place the dot at.
 * @param y The y coordinate to place the dot at.
 */
export default function Dot(context: CanvasRenderingContext2D, size: number, x: number, y: number) {
  const centerX = x + ((size / 28) / 2);
  const centerY = y + ((size / 31) / 2);
  context.fillStyle = "white";
  context.moveTo(x, y);
  context.arc(centerX, centerY, ((size / 28) / 8), 0, 2 * Math.PI);
  context.fill();
}
