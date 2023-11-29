import React, { ReactElement } from "react";
import "../styles/components/home-menu-button.css";
import { Header } from "../components/header";
import { fetchOverview } from "../services/api-service";

/**
 * View showing the level selection screen.
 */
export class LevelSelectionView extends React.Component{

  override state = {
    formattedLevels: []
  };


  override async componentDidMount(): Promise<void> {
    const levels = await fetchOverview();
    const levelElements: Array<ReactElement> = [];
    for (const level of levels){
      levelElements.push(<span>{level}</span>);
    }
    this.setState({formattedLevels: levelElements});
  }

  override render(): React.ReactNode {
    return (
      <div className="Page">
        <Header subtitle="LEVEL SELECTION"></Header>
        {this.state.formattedLevels}
      </div>
    );
  }
}
