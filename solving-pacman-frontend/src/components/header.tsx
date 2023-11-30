import React from "react";
import "../styles/components/header.scss";
import { Link } from "react-router-dom";

/**
 * Props for Header.
 */
type HeaderProps = {
  subtitle: string
}

/**
 * Component to render the site header.
 */
export class Header extends React.Component<HeaderProps>{

  override render(): React.ReactNode {
    return (
      <header className="App-Header">
        <Link to="/" style={{textDecoration: "none"}}>
          <h1 className="Page-Title">PACMAN SOLUTIONS</h1>
        </Link>
        <h2 className="Page-Subtitle">{this.props.subtitle.toUpperCase()}</h2>
      </header>
    );
  }
}
