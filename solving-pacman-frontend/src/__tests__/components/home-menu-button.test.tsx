import React from "react";
import { expect } from "@jest/globals";
import TestRenderer from "react-test-renderer";
import "@testing-library/jest-dom";
import { HomeMenuButton } from "../../components/home-menu-button";

describe("HomeMenuButton", () => {

  it("Should render components", () => {
    const testRenderer = TestRenderer.create(<HomeMenuButton buttonText="test"></HomeMenuButton>);
    const testInstance = testRenderer.root;
    expect(testInstance.findByType(HomeMenuButton).props.buttonText).toBe("test");
  });
});
