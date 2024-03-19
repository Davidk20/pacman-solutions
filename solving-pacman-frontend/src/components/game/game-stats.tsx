import React from "react";
import "../../styles/components/game/game-stats.scss";

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
 toggleRestart: () => void
}

/**
 * Card showing the stats of the current state of the simulation
 */
export class GameStats extends React.Component<GameStatsProps>{
  override render(): React.ReactNode {
    return(
      <div
        className="Game-Stats-Container"
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: "20px",
          textAlign: "center",
          width: "20%",
          border: "3px solid white",
          borderRadius:"5px",
          boxShadow: "5px 5px 15px 5px #000000"
        }}
      >
        {!this.props.gameOver ?
          <div className="Button" onClick={this.props.toggleGame}>
            <span>{!this.props.running ? "START" : "PAUSE"}</span>
          </div>
          :
          <div>
            <span className="Stat-Text">GAME OVER</span>
            <div className="Button" onClick={this.props.toggleRestart}>
              <span>RESTART</span>
            </div>
          </div>
        }
        <span className="Stat-Text">TIME: {this.props.time}</span>
        <span className="Stat-Text">SCORE: {this.props.score}</span>
        <span className="Stat-Text">ENERGISED: {this.props.energised.toString().toUpperCase()}</span>
      </div>
    );
  }
}
