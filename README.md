# Intro To APIs

## Overview

These are three projects that I did from the Tech With Tim Youtube channel. While much of the material in the notes.md file for each project is directly from the tutorials, I have documented my process as I work through new concepts, and have added a good deal of additional detailed information based on my individual research and work.

There will be sections for all three projects, each of which will include:
- A link to the relevant Tech With Tim video and GitHub pages.
- A brief description
- How to use the API


## FastAPI Mini-project

### Links to Tech with Tim video and GitHub
`YouTube: https://www.youtube.com/watch?v=lWsGhG6N_1E`
`GitHub: https://github.com/techwithtim/Fast-API-CRUD-App/tree/main`


### Description

notes.md begins with a brief overview of what an API is, and then goes much more in depth exploring how an API works using a restaurant as a metaphor. 

In the video, Tim begins the discussion and uses a restaurant as a metaphor for an API. But his explanation left me with lots of questions. Having nearly two decades of experience in the restaurant industry I decided this would be a good context through which to explore more complex questions of "how" and API functions.

I decided to pursue Tim's restaurant analogy and flesh it out with my own original research.

I begin with a discussion, using the restaurant metaphor, of an API in the abstract, and then apply those concepts to the "hello, world" API from the tutorial. I include discussions of the separate functionalities of the web server and the application (API) server, as well as breakdowns of program-specific elements like the Uvicorn web server, and FastAPI HTML request methods.

In the "hello, world!" breakdown, I give specific breakdowns of the code, and then run through the process of what happens when the client sends a request to the server. I pair a plain-spoken yet technical explanation side-by-side with the restaurant metaphor.

Following the tutorial, I build out a task list app that has methods to Post, GET, GET a specific task, PUT to update, and DELETE. There are notes on the process in Python comments and markdown.


### How to Use

```
cd into the repo
pip install -r requirements.txt
python3 main.py
```
From the printout, copy the address http://0.0.0.0:8000 and go to http://0.0.0.0:8000/docs in a browser.

This will open the automatically-generated API documentation provided by FastAPI. For each method created, there is the option to "try it out," Create a few tasks. Using "Read Task" will display all tasks that have been created. 

Because the API is not connected to a database, the data created will not persist.



## FastAPI React Mini-project

### Links to Tech with Tim video and GitHub
`YouTube: https://www.youtube.com/watch?v=aSdVU9-SxH4`
`GitHub: https://github.com/techwithtim/FastAPI-React-Integration/blob/main/notes.md`


### Description




