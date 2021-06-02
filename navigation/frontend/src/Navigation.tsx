import {
  ComponentProps,
  StreamlitComponentBase,
  withStreamlitConnection,
  Streamlit,
} from "streamlit-component-lib";
import React, { ReactNode } from "react";

import "rsuite/dist/styles/rsuite-default.css";
import { Nav } from "rsuite";

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class Navigation extends StreamlitComponentBase {
  public constructor(props: ComponentProps) {
    super(props)

    // Default active page
    const defaultPage = this.props.args["default"] as string;

    // Store default page as the active page at first
    this.state = { active: defaultPage }
  }

  private handleSelect = (eventKey: string) => {
    this.state = { active: eventKey }
    Streamlit.setComponentValue(eventKey)
  }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`
    const pages = this.props.args["pages"] as string[]

    return (
      <Nav
        appearance="tabs"
        activeKey={this.state}
        onSelect={this.handleSelect}
        vertical
      >
        {pages.map((page: string) => (
          <Nav.Item eventKey={page}>
            {page}
          </Nav.Item>
        ))}
      </Nav>
    )
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(Navigation)
