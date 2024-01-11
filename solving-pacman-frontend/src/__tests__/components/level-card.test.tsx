import React from "react";
import { expect } from "@jest/globals";
import TestRenderer from "react-test-renderer";
import "@testing-library/jest-dom";
import { LevelCard } from "../../components/level-card";

describe.skip("LevelCard", () => {

  it("Should render components", () => {
    const testRenderer = TestRenderer.create(<LevelCard levelName="LEVEL 1"></LevelCard>);
    const testInstance = testRenderer.root;
    expect(testInstance.findByType(LevelCard).props.levelName).toBe("LEVEL 1");
  });
});
