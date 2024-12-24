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














