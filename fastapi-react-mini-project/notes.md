# FastAPI and React mini-project

# Frontend and Backend

React Frontend -> Request -> FastAPI Backend
      ⭡                           ⭣
       ⭠ ⭠ ⭠ ⭠ ⭠  Result ⭠ ⭠ ⭠ ⭠ ⭠

FastAPI Backend handles:
- Sensitive data
- Storing in database
- Authentication
- Authorization


## Project Setup

- Create directory in which two separate projects will live: The React frontend and the FastAPI backend.

- In the root directory, create a directory named "backend":

  project
    backend

- cd into backend.

### Virtual Environment
A virtual environment is an isolated environment for Python projects. it ensures that the Pyton libraries and tools installed for a single project won't conflict with those of other project's or a user's global Python environment.

- For example: suppose there are two projects, and each uses a different version of FastAPI. The virtual environment allows each project to have its specific version of FastAPI without conflict. The virtual environment isolates the dependencies of each project.

* Creating the Python Virtual Environment:
Run:
python -m venv venv

* Activating the Python Virtual Environment:
Run:
source ./venv/bin/activate

The command to activate the virtual environmnent will need to be run if the user is away from the computer for a while, or is assigning the project to a server.

While the virtual environment is active, we are working in an isolated Python environment. Packages installed will be stored in the venv directory. The Python interpreter will use the virtual environment, and running python or pip will use the isolated virtual environment versions.

When done, run deactivate to exit the virtual environment.
```
Bash:
cd backend

# Create Virtual Environment
python -m venv venv

# Activate Virtual Environment
source ./venv/bin/activate

# Deactivate Virtual Environment
deactivate
```

### Requirements
From within the backend directory, create a new file, requirements.txt

Enter the project dependencies, one per line:

fastapi
uvicorn
pydantic


### Install Dependencies
With the virtual environment activated,
Run:
pip install -r ./requirements.txt


## FastAPI Python Setup

From within backend, create main.py

### What is CORS?
CORS: Cross Origin Resource Sharing. A security feature of browsers that determines wheter a website hosted on one domain (for example: frontend.com) can access resources hosted on another domain (for example: backend.com).

CORS errors happen when:
- A web browser detects that a client (such as a React app on localhost:3000) is trying to access resources from another origin, such as localhost:8000.

- The server hosting the API does not explicitly allow the origin making the request.

### FastAPI CORSMiddleware
Suppose that the frontend is running on localhost:3000, and the backend API is running on localhost:8000. Without CORS configuration, the browser sees these as different origins and blocks the requests for security reasons. CORSMiddleware allows us to configure and allow this behavior.


## Writing main.py

```
# Uvicorn: server
import uvicorn

# FastAPI: Python web framework 
from fastapi import FastAPI

# CORSMiddleware: A tool to configure and allow CORS on the app.
# Ensures that browsers can make requests from specific origins to the API.
from fastapi.middleware.cors import CORSMiddleware

# Pydantic: library for data validation and settings management.
from pydantic import BaseModel

# typing: typing library.
from typing import List

# Define data models: automatically validate data coming in, and format data going out based on Pydantic models.
class Fruit(BaseModel):
  name: str

class Fruits(BaseModel):
  fruits: List[Fruit]

# Get reference to FastAPI.
app = FastAPI()

# Create list of origins that are allowed to access the API (in this case, the React app running locally).
origins = ["http://localhost:3000"]

# Enable and configure CORSMiddleware
# If we wanted to block a method, such as Put or Delete, this would be the place.
# Now that we've configured this, we can send a request from the frontend to the backend.
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],)

# In-memory database. This data will not persist when the app is shut down.
memory_db = {"fruits": []}

# @app.get defines the HTTP Get route
# /fruits is the path the API request will hit, and we are defining that URL endpoing here, inside the decorator parameters.
# response_model specifies the expected structure of the response the route will return.
# When FastAPI receives a request for /fruits, it will ensure that the return value from the function is formatted according to the fruits model.
# So: When the API request hits the /fruits endpoint with a get request, the decorator will determine that the response model should be Fruits.
# FastAPI will automatically convert the response into JSON.
@app.get(path: "/fruits", response_model=Fruits)
  # Return an instance of the Fruits class.
  return Fruits(fruits=memory_db["fruits"])

# Take input from user, create new data.
@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
  memory_db["fruits"].append(fruit)
  return fruit

if __name__=="__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
```


## Create the Frontend

Go to the project root.

Run:
npm create vite@latest frontend --template react
- select React
- select JavaScript

cd into frontend

Run:
npm install
npm install axios

There may be some conflicts between node version. If needed, update node:
```
Run:

# Check node version
node -v

# Install most reacent long term support version
nvm install --lts
```

Navigate to src -> Make a new directory named "components."

In src -> make a new file named api.js

```
api.js

// Axios definition for calling the api
import axios from 'axios';

// Create an oinstance of axios with the base URL
// If we ever want to point the frontend to a different backend, we only need to change the URL here.
const api: AxiosInstance = axios.create({
  baseURL: "http://localhost:8000"
});

// Export the Axios instance.
export default api;
```

Navigate to src/components -> make new file named AddFruitForm.jsx

```
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
```

Make a new file named Fruits.jsx

* Flow:
1. Mount (first render):
  - useEffect triggers -> fetchFruits is called -> setFruits (useState()) is called, setting fruits to
  the current list of fruits from the server (empty right now)

2. User enters a new fruit into AddFruitForm:
  - addFruit is called, and addFruit sends POST request to the server with the new fruit's name.
  - After the server updates, fetchFruits is called, fetching the updated list to keep the UI in sync.

3. Axios POST request explaination:
  - When addFruit is called, fruitName is passed as a prop. 
  - The actual POST request is made by a method from the axios library.
  - We have our instance of axios, named "api" imported at the top.
  - api.post() takes two args: a path and a payload (key-value pair), in this case, api.post("/fruits", name: fruitName)

4. Re-Rendering:
  - Each time the fruits state is updated, the component re-renders with the new data.

* Summary:
On mount, fetchFruits is called from within useEffect(), which is called as a best practice to syncronize the data. The useEffect() call has a dependency array [] at the end, and this signals to the browser that this is the only time that THIS useEffect() will be called. From there on, fetchFruits will be called from within addFruit, which will be called when new data is entered into the AddFruitForm.

```
import React, {useEffect, useState} from "react";
import AddFruitForm from "./AddFruitForm";
import api from "../api";

// Declare functional component FruitList
const FruitList = () => {
  // useState() initilaizes fruits as an empty array.
  const [fruits, setFruits] = useState([]);

  // async keyword signals that the function contains asynchronous code an await statements. 
  const fetchFruits = async () => {
    try {
      // await: pauses the code until promise is resolved.
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
      <AddFruitform addFruit={addFruit} />
    </div>
  );
};

export default FruitList;
```














