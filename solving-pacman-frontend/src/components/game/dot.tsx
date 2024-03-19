import React from "react";
import "../../styles/components/game/dot.scss";

/**
 * Props for the Dot.
*/
type DotProps = {
  /**
   * The height of the dot.
  */
 height: number;
 /**
  * The width of the dot.
 */
 width: number;
 /**
  * The left-positioning of the dot.
 */
 xPos: number;
 /**
  * The top-positioning of the dot.
 */
  yPos: number;
}

/**
 * Component to render a Pac-Dot on the game board.
 */
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
