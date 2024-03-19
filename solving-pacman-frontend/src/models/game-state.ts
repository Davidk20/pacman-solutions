/**
 * Model representing the game state for a single point in time.
 */
export interface GameState {
  /**
   * The time this state was recorded at.
   */
  time: number,
  /**
   * The state of the board at this time.
   */
  state: Array<Array<number>>
}
