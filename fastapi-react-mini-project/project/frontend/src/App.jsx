import React from "react";
import "./App.css";
import FruitList from "./components/Fruits";

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Fruit Management App</h1>
        <main>
          <FruitList />
        </main>
      </header>
    </div>
  );
};

export default App;
