import React from "react";
import "../styles/components/home-menu-button.scss";
import "../styles/views/home-page-view.scss";
import logo from "../assets/images/pacman_logo.png";
import { HomeMenuButton } from "../components/home-menu-button";
import { Header } from "../components/header";
import { Link } from "react-router-dom";


/**
 * View showing the homepage of the application.
 */
export class HomePageView extends React.Component{

  override render(): React.ReactNode {
    return (
      <div className="Page">
        <Header subtitle=""></Header>
        <div className="Home-Menu">
          <img className="Pacman-Logo" src={logo}/>
          <Link to="/level-select" style={{textDecoration: "none"}}>
            <HomeMenuButton buttonText="SELECT A LEVEL"></HomeMenuButton>
          </Link>
          <Link to="/configuration" style={{textDecoration: "none"}}>
            <HomeMenuButton buttonText="CONFIGURATION"></HomeMenuButton>
          </Link>
          <a href="https://david-kidd.gitbook.io/ai-solutions-to-pac-man/" style={{textDecoration: "none"}}>
            <HomeMenuButton buttonText="DOCUMENTATION"></HomeMenuButton>
          </a>
        </div>
      </div>
    );
  }
}
