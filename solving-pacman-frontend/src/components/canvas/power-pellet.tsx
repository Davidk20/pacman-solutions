/**
 * Renders a single Power Pellet.
 *
 * @param context The reference to the canvas on which the pellet is being drawn on.
 * @param size The size of the canvas. Used for scale.
 * @param x The x coordinate to place the pellet at.
 * @param y The y coordinate to place the pellet at.
 */
export default function PowerPellet(context: CanvasRenderingContext2D, size: number, x: number, y: number) {
  const centerX = x + ((size / 28) / 2);
  const centerY = y + ((size / 31) / 2);
  context.fillStyle = "white";
  context.moveTo(x, y);
  context.arc(centerX, centerY, ((size / 28) / 4), 0, 2 * Math.PI);
  context.fill();
}
