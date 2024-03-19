import React, { ReactElement } from "react";
import "../styles/views/level-selection-view.scss";
import { Header } from "../components/header";
import { fetchOverview } from "../services/api-service";
import { LevelCard } from "../components/level-card";

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
      levelElements.push(<LevelCard levelName={level.toUpperCase()} key={level}></LevelCard>);
    }
    this.setState({formattedLevels: levelElements});
  }

  override render(): React.ReactNode {
    return (
      <div className="Page">
        <Header subtitle="LEVEL SELECTION"></Header>
        <div className="Levels-Container">
          {this.state.formattedLevels}
        </div>
      </div>
    );
  }
}
