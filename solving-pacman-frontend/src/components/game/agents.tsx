import pacman from "../../assets/images/sprites/pacman.png";
import blinky from "../../assets/images/sprites/blinky.png";
import clyde from "../../assets/images/sprites/clyde.png";
import inky from "../../assets/images/sprites/inky.png";
import pinky from "../../assets/images/sprites/pinky.png";
import "../../styles/components/game/agent.scss";
import { ReactNode } from "react";
import React from "react";


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
}

export class Agent extends React.Component<AgentProps> {
  override render(): ReactNode {
    switch (this.props.agent) {
    case "pacman":
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
          src={pacman}
          alt={"Pac-Man"}
          style={{
            height: this.props.height,
            width: this.props.width,
          }}
        />
      </div>;
    case "blinky":
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
          src={blinky}
          alt={"Blinky"}
          style={{
            height: this.props.height,
            width: this.props.width,
          }}
        />
      </div>;
    case "clyde":
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
          src={pinky}
          alt={"Pinky"}
          style={{
            height: this.props.height,
            width: this.props.width,
          }}
        />
      </div>;
    case "inky":
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
          src={inky}
          alt={"Pac-Man"}
          style={{
            height: this.props.height,
            width: this.props.width,

          }}
        />
      </div>;
    case "pinky":
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
          src={clyde}
          alt={"Pac-Man"}
          style={{
            height: this.props.height,
            width: this.props.width,
          }}
        />
      </div>;
    default:
      throw new Error("Agent not found");
    }
  }
}
