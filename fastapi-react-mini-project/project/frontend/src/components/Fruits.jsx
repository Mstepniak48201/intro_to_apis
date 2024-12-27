import React, {useEffect, useState} from "react";
import AddFruitForm from "./AddFruitForm";
import api from "../api.js";

// Declare functional component FruitList
const FruitList = () => {
  // useState() initilaizes fruits as an empty array.
  const [fruits, setFruits] = useState([]);

  // async keyword signals that the function contains asynchronous code an await statements. 
  const fetchFruits = async () => {
    try {
      // await: pauses the code until promis is resolved.
      // wait for the API request to finish and store the result in the response variable.
      const response = await api.get("/fruits");
      setFruits(response.data.fruits);
    } catch (error) {
      console.error("Error fetching fruits", error);
    }
  };

  const addFruit = async (fruitName) => {
    try {
      // Send post request with new fruit's name, sending the fruit's name to the backend.
      // After the request, the server sends a response confirming the addition.
      await api.post("/fruits", {name: fruitName});
      // Refresh the list after adding a fruit.
      // Every time fetchFruits is called, it overwrites the fruits state with a full, updated list from the server.
      fetchFruits();
    } catch (error) {
      console.error("Error adding fruit", error);
    }
  };

  // When the FruitList component is displayed on the page for the first time, fetchFruits is called.
  // This ensures that the initial list of fruits is fetched from the backend and displayed in the component.
  // The empty array is the dependency array: this ensures that the useEffect will run once when the component initially mounts.
  // Running useEffect on mount is good practice: it ensures that the component synchronizes with the
  // latest data from the server.
  useEffect(() => {
    fetchFruits();
  }, []);

  return (
    <div>
      <h2>Fruits List</h2>
      <ul>
        {fruits.map((fruit, index) => (
          <li key={index}>{fruit.name}</li>
        ))}
      </ul>
      <AddFruitForm addFruit={addFruit} />
    </div>
  );
};

export default FruitList;
