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
  /**
   * `true` if Pac-Man is energised in this current state.
   */
  energised: boolean
  /**
   * Pac-Man's score at the current state.
   */
  score: number
}

/**
 * Model representing the response from the server.
 */
export interface GameResponse {
  /**
   * A list of the game states.
   */
  states: GameState[]
}
