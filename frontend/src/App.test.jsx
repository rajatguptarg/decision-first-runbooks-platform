import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "./App";

describe("App", () => {
  it("renders the platform title", () => {
    render(<App />);
    expect(
      screen.getByText("Decision First Runbooks Platform"),
    ).toBeInTheDocument();
  });

  it("renders the welcome message", () => {
    render(<App />);
    expect(screen.getByText("Welcome!")).toBeInTheDocument();
  });

  it("renders the count button", () => {
    render(<App />);
    expect(
      screen.getByRole("button", { name: /count is 0/i }),
    ).toBeInTheDocument();
  });
});
