import React from "react";

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
      <div className="
        flex items-center justify-center bg-black cursor-pointer rounded-lg border-4 border-pacman-wall-colour
        h-16 w-96
      ">
        <span className="
        text-white font-pixel text-xl
        ">
          {this.props.buttonText}
        </span>
      </div>
    );
  }
}
