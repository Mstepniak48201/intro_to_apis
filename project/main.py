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
