import React from "react";
import "../styles/components/home-menu-button.css";

/**
 * Props for HomeMenuButton.
 */
type HomeMenuButtonProps = {
  buttonText: string
}

/**
 * Component to render a button for the homepage menu.
 */
export class HomeMenuButton extends React.Component<HomeMenuButtonProps>{

  override render(): React.ReactNode {
    return (
      <div className="Button-Container">
        <span>{this.props.buttonText}</span>
      </div>
    );
  }
}
