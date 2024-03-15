import React from "react";
import "../../styles/components/game/wall.scss";

/**
 * Props for the Wall.
 */
type WallProps = {
  height: number;
  /**
   * The height of the wall piece.
   */
  width: number;
  /**
   * The width of the wall piece.
   */
  xPos: number;
    /**
   * The left-positioning of the wall piece.
   */
  yPos: number;
    /**
   * The top-positioning of the wall piece.
   */
}

export class Wall extends React.Component<WallProps> {
  /**
   * Component to render a singular piece of the game wall.
   */
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
