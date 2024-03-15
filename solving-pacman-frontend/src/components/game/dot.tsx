import React from "react";
import "../../styles/components/game/dot.scss";

/**
 * Props for the Game Window.
 */
type DotProps = {
  /**
   * The level.
   */
  height: number;
  width: number;
  xPos: number;
  yPos: number;
}

export class Dot extends React.Component<DotProps> {
  override render(): React.ReactNode {
    return (
      <div
        className="Dot-Container"
        style={
          {
            height: this.props.height,
            width: this.props.width,
            top: this.props.yPos,
            left: this.props.xPos
          }
        }
      >
        <div className="Dot" style={{height: this.props.height / 4, width: this.props.width / 4}}></div>
      </div>

    );
  }
}
