import React from "react";
import "../styles/components/home-menu-button.css";
import { Header } from "../components/header";

/**
 * View showing the configuration screen.
 */
export class ConfigurationView extends React.Component{

  override render(): React.ReactNode {
    return (
      <div className="Page">
        <Header subtitle="CONFIGURATION"></Header>

      </div>
    );
  }
}
