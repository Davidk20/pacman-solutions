import React from "react";
import "../styles/components/home-menu-button.css";
import { Header } from "../components/header";

/**
 * Component to render a button for the homepage menu.
 */
export class LevelSelectionView extends React.Component{

  override render(): React.ReactNode {
    return (
      <div className="Page">
        <Header subtitle="LEVEL SELECTION"></Header>

      </div>
    );
  }
}
