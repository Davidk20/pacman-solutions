import React from "react";
import { expect } from "@jest/globals";
import TestRenderer from "react-test-renderer";
import "@testing-library/jest-dom";
import { HomePageView } from "../../views/home-page-view";
import { HomeMenuButton } from "../../components/home-menu-button";

describe.skip("HomePageView", () => {

  it("Should render components", () => {
    const testRenderer = TestRenderer.create(<HomePageView></HomePageView>);
    const testInstance = testRenderer.root;

    expect(testInstance.findByType(HomeMenuButton).props.foo).toBe("bar");
    expect(testInstance.findByProps({className: "sub"}).children).toEqual(["Sub"]);
  });
});
