import React from "react";
import "../../styles/components/game/wall.scss";

/**
 * Props for the Game Window.
 */
type WallProps = {
  /**
   * The level.
   */
  height: number;
  width: number;
  xPos: number;
  yPos: number;
}

export class Wall extends React.Component<WallProps> {
  override render(): React.ReactNode {
    return (
      <div className="Wall" style={{ height: this.props.height, width: this.props.width, top: this.props.yPos, left: this.props.xPos}}>

      </div>
    );
  }
}
