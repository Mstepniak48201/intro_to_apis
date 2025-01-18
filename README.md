# Intro To APIs

## Overview

These are three projects that I did from the Tech With Tim Youtube channel. While much of the material in the notes.md file for each project is directly from the tutorials, I have documented my process as I work through new concepts, and have added a good deal of additional detailed information based on my individual research and work.

There will be sections for all three projects, each of which will include:
- A link to the relevant Tech With Tim video and GitHub pages.
- A brief description
- How to use the API


## FastAPI Mini-project

### Links to Tech with Tim video and GitHub
YouTube: https://www.youtube.com/watch?v=lWsGhG6N_1E<br>
GitHub: https://github.com/techwithtim/Fast-API-CRUD-App/tree/main<br>


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
YouTube: https://www.youtube.com/watch?v=aSdVU9-SxH4<br>
GitHub: https://github.com/techwithtim/FastAPI-React-Integration/blob/main/notes.md<br>


### Description

notes.md begins by setting up the project structure and the dev environment. This project has a frontend and a backend, so those directories get set up.

The tutorial also covers setting up a Python Virtual Environment (venv), as well as writing the requirements file and installing the backend and frontend dependencies. 

There is a brief discussion on CORS, what it is, and why we are using FastAPI CORS Middleware, 

As I follow the tutorial, I give comments and explanations in both main.py and api.js, followed by a brief walk through of the flow when a user makes a POST request in the React frontend.


### How to Use

Before cloning the repo, instal the lates Long-Term Support version of Node.js:
```
nvm install --lts
```

* Create the Python Virtual Environment
```
cd fastapi-react-mini-project/project/backend
python3 -m venv venv
```

* Activate/Deactivate venv
```
source ./venv/bin/activate
deactivate
```

* Install dependencies
- With the venv activated:
```
pip install -r ./requirements.txt
```

* Install React dependencies/Run Server
```
cd fastapi-react-mini-project/project/frontend
npm install
npm run dev
```


## Django REST API Mini-project

### Links to Tech with Tim video and GitHub
https://www.youtube.com/watch?v=t-uAgI-AUxc<br>
https://github.com/techwithtim/django-rest-api<br>


### Description

notes.md describes the setup of the project and the dev environment. 

The two preceding projects had a single file, main.py, as the brains of the API. Here, things are different, beginning with how a request is routed. While the tutorial shows *how* to use Django, it doesn't always take the time to explain *what* is going on. Feeling a bit lost, I did some research and worked through the Django Request-Response Workflow.

Following the tutorial, we then:
- Build an ORM (Object Relational Mapping) model for data to interact with
- Define the Serializer, which takes the model and converts it into JSON-compatible data the API can interact with
- Create Views - the function/class that takes a request and returns a response

The tutorial then briefly discusses the two-step routing system, but again the focus was on "here's what you need to do to get the API up and running," and I felt it was worthwhile to understand a bit bet

The tutorial, with a focus on what is needed to get the API up and running, touches on the two step routing system, but I felt it would be worthwhile to understand a bit more, so I have included a discussion on:
- urlpatterns[]
- path()
- include() as used in path()

Following the tutorial, and supplemented by my own notes, the project is finished with:
- More complex views
- Overriding views
- Custom views

* Deployment Section

I have left my notes on deployment intact, but chose to not go through the process, because the software used in the tutorial, Acorn, is now migrated and rebranded to Obot. I have never done a deployment before, and I decided that trying to do so while refactoring my code within a framework that I have only begun to understand is not the best learning environment. That said, I think that the process of writing the code out in notes.md and describing the process will aid me in future projects.


### How to use

* Create the Python Virtual Environment
```
cd django-rest-mini-project/project/api
python3 -m venv .venv
source .venv/bin/activate
```

* Install dependencies: Run:
pip3 install -r requirements.txt


- Manage migrations and start server:
```
cd mysite (main project directory)
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

- Navigate:
Copy the address from the printout: http://127.0.0.1:8000/ and paste it into the browser.

To navigate to the various views, go to:

```
http://127.0.0.1:8000/blogposts/create/
http://127.0.0.1:8000/blogposts/blogposts/
http://127.0.0.1:8000/blogposts/<int>/ (add ID number of a desired blogpost, view expects an integer)
```

These views can be used to GET, POST and DELETE blogposts.




