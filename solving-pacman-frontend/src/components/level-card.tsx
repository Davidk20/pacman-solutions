import React from "react";
import { Link } from "react-router-dom";
import "../styles/components/level-card.scss";
import placeholder from "../assets/images/level_1.png";

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
      <Link to={"/game"} state={{level: this.props.levelName}} style={{textDecoration: "none"}}>
        <div className="Level-Card-Container">
          <img className="Level-Card-Preview" src={placeholder}/>
          <h1 className="Level-Card-Title">{this.props.levelName}</h1>
        </div>
      </Link>
    );
  }

}
