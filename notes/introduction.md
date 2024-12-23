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
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

In the browser, enter the address: http://localhost:8000

The browser sends a request to the API, and hello: "world" should display on the screen.

- Now, got to localhost:8000/docs Or localhost:8000/redoc
  - Documentation for the API will be automatically generated.
  - docs and redoc are two different versions.




