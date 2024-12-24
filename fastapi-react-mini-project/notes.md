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


## Project Structure

- Create directory in which two separate projects will live: The React frontend and the FastAPI backend.

- In the root directory, create a directory named "backend":

  project
    backend

- cd into backend.

### Virtual Environment

A virtual environment is an isolated environment for Python projects. it ensures that the Pyton libraries and tools installed for a single project won't conflict with those of other project's or a user's global Python environment.

- For example: suppose there are two projects, and each uses a different version of FastAPI. The virtual environment allows each project to have its specific version of FastAPI without conflict.

- Create the Python virtual environment to isolate the dependencies for this project:
Run:
python -m venv venv

- 

Bash:
cd backend
python -m venv venv



