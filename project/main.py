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
tasks = []

# Any data that is given to the API that is valid will be wrapped in the Task object, and given a unique ID, and appended to the list.

# URL we go to to create tasks.
# Tell FastAPI that we want to use the Task Pydantic model to encode the JSON that will be returned from this root.
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    print(f"Received task: {task}")
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
