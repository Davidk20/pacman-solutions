import React from "react";
import { expect } from "@jest/globals";
import TestRenderer from "react-test-renderer";
import "@testing-library/jest-dom";
import { Header } from "../../components/header";

describe.skip("HomeMenuButton", () => {

  it("Should render components", () => {
    const testRenderer = TestRenderer.create(<Header subtitle=""></Header>);
    const testInstance = testRenderer.root;
    expect(testInstance.findByType(Header).props.buttonText).toBe("test");
    expect(testInstance.findByProps({className: "h1"}).children).toEqual(["Sub"]);
  });
});
