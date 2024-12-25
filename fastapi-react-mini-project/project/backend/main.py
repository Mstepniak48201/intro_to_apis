import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Define data models: automatically validate data coming in, and format data going out based on Pydantic models.
class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

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
@app.get("/fruits", response_model=Fruits)
def get_fruits():
    # Return an instance of the Fruits class.
    return Fruits(fruits=memory_db["fruits"])

# Take input from user, create new data.
@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
