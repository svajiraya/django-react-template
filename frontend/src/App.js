import React, { Component } from "react";

import axios from "axios";

import logo from "./logo.svg";
import "./App.css";

class App extends Component {
  state = { loading: true };

  componentDidMount() {
    axios.defaults.baseURL = process.env.REACT_APP_BACKEND_URL;

    axios.get(`example/`).then(res => {
      console.log(res.data);

      this.setState({
        loading: false
      });
    });
  }

  render() {
    const { loading } = this.state;
    
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />

          {loading ? (
            <div>Performing example API call... </div>
          ) : (
            <div>Example API call completed. </div>
          )}
        </header>
      </div>
    );
  }
}

export default App;
