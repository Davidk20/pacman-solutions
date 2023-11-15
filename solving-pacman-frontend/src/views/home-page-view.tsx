import React from "react";
import "../styles/components/home-menu-button.css";
import logo from "../assets/images/pacman_logo.png";
import { HomeMenuButton } from "../components/home-menu-button";

/**
 * Component to render a button for the homepage menu.
 */
export class HomePageView extends React.Component{

  override render(): React.ReactNode {
    return (
      <div className="Home-Menu">
        <img className="Pacman-Logo" src={logo}/>
        <HomeMenuButton buttonText="SELECT A LEVEL"></HomeMenuButton>
        <HomeMenuButton buttonText="CONFIGURATION"></HomeMenuButton>
      </div>
    );
  }
}
