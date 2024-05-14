import React from "react";

/**
 * Props for the GameStats Component.
 */
export interface GameStatsProps {
  /**
   * The time at the current state.
   */
  time: number,
  /**
   * The score at the current state.
   */
  score: number,
  /**
   * `true` if Pac-Man is energised in the current state
   */
  energised: boolean,
  /**
   * `true` if the game is currently running
   */
  running: boolean,
  /**
   * Callback function to parent component allowing the game to be paused.
   */
  toggleGame: () => void,
  /**
   * `true` if the game simulation has finished.
   */
  gameOver: boolean,
  /**
   * Function to restart the game simulation.
   */
  toggleRestart: () => void,
}

/**
 * Card showing the stats of the current state of the simulation
 */
export class GameStats extends React.Component<GameStatsProps>{
  override render(): React.ReactNode {
    return(
      <div
        className="
          flex flex-col items-center justify-center p-5 gap-2 
          border-2 border-pacman-wall-colour rounded-md
          text-white font-pixel text-center
        "
      >
        {!this.props.gameOver ?
          <div 
            className="
              flex items-center justify-center bg-black cursor-pointer 
              rounded-lg border-2 border-pacman-wall-colour
              px-6 py-2
            " 
            onClick={this.props.toggleGame}
          >
            <span>{!this.props.running ? "START" : "PAUSE"}</span>
          </div>
          :
          <div>
            <span>GAME OVER</span>
            <div 
              className="
                flex items-center justify-center bg-black cursor-pointer 
                rounded-lg border-2 border-pacman-wall-colour
                px-6 py-2
              " 
              onClick={this.props.toggleRestart}
            >
              <span>RESTART</span>
            </div>
          </div>
        }
        <span>TIME: {this.props.time}</span>
        <span>SCORE: {this.props.score}</span>
        <span>ENERGISED: {this.props.energised.toString().toUpperCase()}</span>
      </div>
    );
  }
}
