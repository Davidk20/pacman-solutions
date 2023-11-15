import React from "react";
import "../styles/components/home-menu-button.css";
import logo from "../assets/images/pacman_logo.png";
import { HomeMenuButton } from "../components/home-menu-button";
import { Header } from "../components/header";
import { Link } from "react-router-dom";


/**
 * Component to render a button for the homepage menu.
 */
export class HomePageView extends React.Component{

  override render(): React.ReactNode {
    return (
      <div className="Page">
        <Header subtitle=""></Header>
        <div className="Home-Menu">
          <img className="Pacman-Logo" src={logo}/>
          <Link to="/level-select">
            <HomeMenuButton buttonText="SELECT A LEVEL"></HomeMenuButton>
          </Link>
          <HomeMenuButton buttonText="CONFIGURATION"></HomeMenuButton>
        </div>
      </div>
    );
  }
}
