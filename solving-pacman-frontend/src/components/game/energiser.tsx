import React from "react";
import "../../styles/components/game/energiser.scss";

/**
 * Props for the Game Window.
 */
type EnergiserProps = {
  /**
   * The height of the wall piece.
  */
  height: number;
  /**
   * The width of the wall piece.
  */
  width: number;
  /**
   * The left-positioning of the wall piece.
  */
  xPos: number;
  /**
   * The top-positioning of the wall piece.
  */
  yPos: number;
}

/**
 * Component to render an energiser on the game board.
 */
export class Energiser extends React.Component<EnergiserProps> {
  override render(): React.ReactNode {
    return (
      <div
        className="Energiser-Container"
        style={
          {
            height: this.props.height,
            width: this.props.width,
            top: this.props.yPos,
            left: this.props.xPos
          }
        }
      >
        <div className="Energiser" style={{height: this.props.height / 2, width: this.props.width / 2}}></div>
      </div>

    );
  }
}
