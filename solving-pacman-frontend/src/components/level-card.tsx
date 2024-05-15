import React from "react";
import { Link } from "react-router-dom";
import preview from "../assets/images/level_1.png";

/**
 * Props for the Level Card.
 */
type LevelCardProps = {
  /**
   * The name of the level.
   */
  levelName: string
}

/**
 * Card component to render a level preview within the selection screen.
 */
export class LevelCard extends React.Component<LevelCardProps> {

  override render(): React.ReactNode {
    return (
      <Link to={"/game"} state={{level: this.props.levelName}} style={{textDecoration: "none", display: "inline-block"}}>
        <div className="
          flex flex-col items-center justify-center cursor-pointer gap-4
          bg-black rounded-2xl
          p-4
        ">
          <img className="" src={preview} alt="level preview"/>
          <span className="
            text-white font-pixel text-center
            text-xl
          ">
            {this.props.levelName}
          </span>
        </div>
      </Link>
    );
  }

}
