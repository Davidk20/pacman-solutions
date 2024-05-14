import React from "react";
import logo from "../assets/images/solutions-logo.png";
import { HomeMenuButton } from "../components/home-menu-button";
import { Link } from "react-router-dom";


/**
 * View showing the homepage of the application.
 */
export class HomePageView extends React.Component{

  override render(): React.ReactNode {
    return (
      <div className="
        flex flex-col items-center justify-center h-dvh w-dvw bg-background-colour
        gap-10
      ">
        <img className="h-1/4" src={logo} alt="Solutions Logo"/>
        <span className="
          text-pacman-yellow font-pixel
          text-6xl
        ">
          PAC-MAN SOLUTIONS
        </span>
        <Link to="/level-select" style={{textDecoration: "none"}}>
          <HomeMenuButton buttonText="SELECT A LEVEL"></HomeMenuButton>
        </Link>
        <a href="https://david-kidd.gitbook.io/ai-solutions-to-pac-man/" style={{textDecoration: "none"}}>
          <HomeMenuButton buttonText="DOCUMENTATION"></HomeMenuButton>
        </a>
      </div>
    );
  }
}
