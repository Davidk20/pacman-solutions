import React from "react";
import "../../styles/components/game/wall.scss";

/**
 * Props for the Wall.
 */
type WallProps = {
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
 * Component to render a singular piece of the game wall.
 */
export class Wall extends React.Component<WallProps> {
  override render(): React.ReactNode {
    return (
      <div
        className="Wall"
        style={{
          height: this.props.height,
          width: this.props.width,
          top: this.props.yPos,
          left: this.props.xPos
        }}
      >

      </div>
    );
  }
}
