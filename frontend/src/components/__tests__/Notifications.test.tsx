import { render, screen } from "@testing-library/react";
import Notifications from "../Notifications";

test("renders notifications component", () => {
    render(<Notifications />);
    expect(screen.getByText("Notifications")).toBeInTheDocument();
});