import React from "react";
import "../../styles/components/game/energiser.scss";

/**
 * Props for the Game Window.
 */
type EnergiserProps = {
  /**
   * The level.
   */
  height: number;
  width: number;
  xPos: number;
  yPos: number;
}

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
