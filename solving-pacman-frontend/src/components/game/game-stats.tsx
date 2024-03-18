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
  energised: boolean
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
          border: "3px solid white",
          borderRadius:"5px",
          display: "flex",
          flexDirection: "column",
          padding: "20px",
          textAlign: "center",
          width: "20%"
        }}
      >
        <span className="Stat-Text">TIME: {this.props.time}</span>
        <span className="Stat-Text">SCORE: {this.props.score}</span>
        <span className="Stat-Text">ENERGISED: {this.props.energised.toString().toUpperCase()}</span>
      </div>
    );
  }
}
