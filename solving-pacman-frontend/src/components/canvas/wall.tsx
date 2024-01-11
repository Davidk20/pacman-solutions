/**
 * Renders a single wall block.
 *
 * The size for a wall block is calculated by taking the size of the canvas and
 * dividing it by the size of the traditional grid.
 *
 * @param context The reference to the canvas on which the wall is being drawn on.
 * @param x The x coordinate to place the wall at.
 * @param y The y coordinate to place the wall at.
 */
export default function Wall(context: CanvasRenderingContext2D, size: number, x: number, y: number) {
  const height = size / 31;
  const width = size / 28;
  context.strokeStyle = "#2120D2";
  context.lineWidth = 4;
  context.strokeRect(x, y, width, height);
}
