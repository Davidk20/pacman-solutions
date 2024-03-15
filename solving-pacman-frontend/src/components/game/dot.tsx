import React from "react";
import "../../styles/components/game/dot.scss";

/**
 * Props for the Dot.
 */
type DotProps = {
  height: number;
  /**
   * The height of the dot.
   */
  width: number;
  /**
   * The width of the dot.
   */
  xPos: number;
    /**
   * The left-positioning of the dot.
   */
  yPos: number;
    /**
   * The top-positioning of the dot.
   */
}

export class Dot extends React.Component<DotProps> {
  /**
   * Component to render a Pac-Dot on the game board.
   */
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
