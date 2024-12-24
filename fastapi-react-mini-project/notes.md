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
  allow_methods=[*],
  allow_headers=[*],)

# In-memory database. This data will not persist when the app is shut down.
memory_db = {"fruits": []}





  


```












