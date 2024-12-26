import React, {useState} from "react";

// Create functional component AddFruitForm that takes the function addFruit() as a prop.
const AddFruitForm = ({addFruit}) => {
  
  // Declare State.
  // In this state hook, fruitName is the current state. It holds the value the user types into the input field.
  // setFruitName is the function used to update the fruitName state. 
  // useState("") initializes the state to an empty string. 

  // Declare state: fruitName holds the value of the current state.
  // setFruitName is the function that updates the fruitName state with the value inputted by the user.
  // useState("") initializes the state to an empty string.
  const [fruitName, setFruitName] = useState("")

  // handleSubmit will be called when the form is submitted in the onSubmit event in <form>.
  // event.preventDefault() prevents the default behavior, in this case reloading the page.
  // if (fruitName)  checks if the user has entered a value.
  // addFruit() is the function that will be passed as a prop. fruitname is passed to it.
  // setFruitName clears the input field by resetting state to an empty string.
  const handleSubmit = (event) => {
    event.preventDefault();
    if (fruitName) {
      addFruit(fruitname);
      setFruitName("");
    }
  };

  return (
    // <form> listens for the onSubmit event.
    <form onSubmit={handleSubmit}>
    // value is set equal to the state value fruitName.
    // When the user types into the input field, the onChange event is triggered.
    // The event handler arrow function that OnChange is set equal to recieves the event object (e)
    // e.target.value accesses and captures the current text entered into the input field.
    // The state updater setFruitName stores the new value in the state variable fruitName
      <input
        type ="text"
        value ={fruitName}
        onChange = {(e) => setFruitName(e.target.value)}
        placeholder="Enter fruit name"
      />
      <button type="submit">Add Fruit</button>
    </form>
    );
  };

export default AddFruitForm;
