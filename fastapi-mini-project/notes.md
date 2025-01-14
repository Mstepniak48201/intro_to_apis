# Introduction

## What is an API?

- Application Programming Interface
  - One software requests data from another, and receives a response.

- Example: A user checks the weather on their phone. The weather app sends out a request to the weather database, and returns that data to the user.


## CRUD

- Most APIs interact with data through four principle methods:
  - Create
  - Read 
  - Update
  - Delete

- Create: done through the Post method. 
- Read: done with the Get method.
- Update: Put (change existing item)
- Delete: Delete method.


## Request and Response

- When an API is used, it makes a request to a server.
  - The request asks the server for data or an action.
  
- The server processes the request and sends back a response.
  - The response will tell the user if the request was successful with a status code.
  

## FastAPI

[ ] Install packages
  - pip3 install fastapi
  - pip3 install fastapi uvicorn pydantic


## Discussion of FastAPI, Uvicorn, the API and the split functionality of the web server and the application server.

* Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server. Most of the descriptions of the server/client request/response process display something like this:

A client at a restaurant requests a menu item from their server, who then communicates that request to the kitchen. When the item is ready, the server brings it to the client. The kitchen, in this analogy is the database.

A common diagram:
```
           ->REQUEST->
 _____       _____       _____
|     | --> |     | --> |     |
| App |     | API |     | DB  |
|_____| <-- |_____| <-- |_____|
            
           <-RESPONSE<-
```

It's a little more complicated than that though. In this case, the API will be split into two parts: the web server (Uvicorn) and the application server (the API). Keeping with the restaurant metaphor, here is a more detailed breakdown:

1. The Browser or App (Client):
  - A Customer who comes to a restaurant

2. Uvicorn (Web Server)
  - Wait staff:
    - Takes customer Order (Request)
    - Passes Order to the kitchen
  
  - Uvicorn (Web Server) handles communication between the Client and the API Server.
  - The Web Server ensures that the Request reaches the correct place and delivers the Response back.

3. The API Server:
  - Kitchen:
    - Checks the Pantry (Database) for Ingredients (Data Queries)
    - Cooks the Ingredients (Logic and Processing)
    - Plates the Dish (Response)
  
    - The API Server is where the Request is Processed.
      - Database interaction
      - Preparing the Response

4. Uvicorn (Web Server)
  - Wait staff:
    -Delivers the Dish (Response) to the Customer (Client)

  - The Web Server delivers the Response back to the Client.

## Running FastAPI

```
main.py

from fastapi import FastAPI

# Get instance of FastAPI.
app = FastAPI()

# Set up basic root.
# We can send a get request to this URL.
@app.get("/")

# Upon the get request, this function will execute.
# FastAPI will automatically convert the Dict into JSON.
def read():
  return {"hello": "world"}

if __name__ == "__main__":
  # Import uvicorn, a simple web server.
  import uvicorn

  # 0.0.0.0 means we are running on our local IP address.
  # local host 8000
  uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run:
python3 main.py

The Terminal should give the following messages:

INFO:     Started server process [594393]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http:#0.0.0.0:8000 (Press CTRL+C to quit)

In the browser, enter the address: http:#localhost:8000

The browser sends a request to the API, and hello: "world" should display on the screen.

- Now, got to localhost:8000/docs Or localhost:8000/redoc
  - Documentation for the API will be automatically generated.
  - docs and redoc are two different versions.


## Pydantic Models | Get | Post

We want the API to be able to:
- Create tasks
- Delete tasks 
- Update tasks

- Create an empty list for tasks.


```
main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

# Create class Task that inherits from BaseModel
class Task(BaseModel):
  # Create fields with types.
  # UUID = A unique identifier.
  id: Optional[UUID] = None
  title: str
  description: Optional[str] = None
  completed: bool = False

# Empty list for tasks
# This would be a real database for a working API.
tasts = []

# Any data that is given to the API that is valid will be wrapped in the Task object, and given a unique ID, and appended to the list.

# URL we go to to create tasks.
# Tell FastAPI that we want to use the Task Pydantic model to encode the JSON that will be returned from this root.
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
  # Create new unique identifier.
  task.id = uuid4()
  tasks.append(task)
  return task

@app.get("/tasks/", response_model=List[Task])
# Change from read to read_tasks
# Pass the List of Tasks as the response_model arg.
# The return value of tasks is a List.
def read_tasks():
  return tasks

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run:
python3 main.py

- Now when we go to localhost:8000/docs we see that under default, there are  both Get and Post fields we can click into.

- Click into Post -> Try it out -> and: delete the id number, add a title of "hello, world," and a description of "testing."

- Click Execute: The server response code should be 200, a new unique id should have been added, as well as the "hello, world," and "testing" entries.

- Try sending a Post with an empty response. We should get response 422: Unprocessable Entity.


## Path Parameters | Read based on dynamic parameter | Update

```
main.py

# Import HTTPException for for task in tasks statement.
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Task(BaseModel):
  id: Optional[UUID] = None
  title: str
  description: Optional[str] = None
  completed: bool = False

tasts = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
  task.id = uuid4()
  tasks.append(task)
  return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
  return tasks

# Add the task_id, a dynamic path parameter
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
  for task in tasks:
    if task.id == task_id:
      return task
  
  # Raise HTTPException imported from FastAPI.
  raise HTTPException(status_code=404, detail="Task not found")

# Update task list.
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
  for idx, task in enumerate(tasks):
    if task.id == task_id:
      updated_task = task.copy(update=task_update.dict(exclude_unset=True))
      tasks[idx] = updated_task
      return updated_task
  raise HTTPException(status_code=404, detail="Task not found")

# Delete task.
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
  for idx, task in enumerate(tasks):
    if task.id == task_id:
      return tasks.pop(idx)
  raise HTTPException(status_code=404, detail="Task not found") 
  

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run:
python3 main.py

- Now when we go to localhost:8000/docs we see that under default, we can read all tasks, create a new task, read a specific task, update a task (for instance, completed: true), or delete a task.







