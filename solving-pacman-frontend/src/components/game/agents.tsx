import pacman from "../../assets/images/sprites/pacman.png";
import blinky from "../../assets/images/sprites/blinky.png";
import clyde from "../../assets/images/sprites/clyde.png";
import inky from "../../assets/images/sprites/inky.png";
import pinky from "../../assets/images/sprites/pinky.png";
import frightened from "../../assets/images/sprites/frightened.png";
import "../../styles/components/game/agent.scss";
import React, { ReactNode } from "react";


type AgentProps = {
  /**
   * The agent to be rendered.
   */
  agent: string;
  /**
   * The height to render the agent.
   */
  height: number;
  /**
   * The width to render the agent.
   */
  width: number;
  /**
   * The x coordinate to place the agent at.
   */
  xPos: number;
  /**
   * The y coordinate to place the agent at.
   */
  yPos: number;
  /**
   * `true` if Pac-Man is energised.
   */
  energised: boolean;
}

export class Agent extends React.Component<AgentProps> {
  agentPath: string = "";

  override render(): ReactNode {
    if (this.props.energised && this.props.agent != "pacman") {
      this.agentPath = frightened;
    } else {
      switch (this.props.agent) {
      case "pacman":
        this.agentPath = pacman;
        break;
      case "blinky":
        this.agentPath = blinky;
        break;
      case "clyde":
        this.agentPath = clyde;
        break;
      case "inky":
        this.agentPath = inky;
        break;
      case "pinky":
        this.agentPath = pinky;
        break;
      default:
        throw new Error("Agent not found");
      }
    }
    return <div
      className="Agent-Container"
      style={{
        height: this.props.height,
        width: this.props.width,
        top: this.props.yPos,
        left: this.props.xPos
      }}
    >
      <img
        className="Agent"
        src={this.agentPath}
        alt={this.props.agent}
        style={{
          height: this.props.height,
          width: this.props.width,
        }}
      />
    </div>;
  }
}
