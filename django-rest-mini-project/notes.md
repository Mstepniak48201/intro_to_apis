Django REST API mini project



## Setup

- mkdir api

- cd api

- Make requirements.txt

```
requirements.txt

django
djangorestframework
environs
```

- Set up Python Virtual Enviroment: Run:
python3 -m venv .venv

    - To activate: Run:
    source .venv/bin/activate

    - To deactivate: Run:
    deactivate

- Install dependencies: Run:
pip3 install -r requirements.txt

- Create new Django project: Run:
django-admin startproject mysite
  
// If the above command doesn't work, try:
python3 -m django startproject mysite

// This should create a new directory called "mysite."
// This is where we will write the API.
// The current directory structure should look like this:
api
- mysite
    - mysite
    - manage.py
- requirements.txt
- .venv

cd mysite 

- Create app: Run:
// Notice within the mysite directory, there is a file manage.py. This will help us create the app.
// The command startapp in manage.py takes a name arg. We will name the app "api."
python3 manage.py startapp api

// A new directory called api should be created within mysite.
// Project structure should look like this:

```
api
  - mysite
    - api
    - mysite
    - manage.py
- requirements.txt
- .venv
```


## Overview of Django Request-Response Workflow

Before beginning, here is a step-by-step, high-level description of the flow of a request through Django API.

1. The client sends an HTTP request. The request reaches urls.py in the main project directory (in this case mysite/mysite/urls.py), where Django's URL dispatcher looks for a match.

2. mysite/mysite/urls.py forwards the request to the app-specific routing in api/urls.py, where it matches with a corresponding view. api/urls.py sends the request to the appropriate view in views.py.

3. The view handles the request logic. If the request requires database interaction, the view calls the ORM.

4. The ORM (defined in models.py) translates the Python-based model queries into SQL commands to interact with the database. When the database responds, the ORM converts the results into Python objects (model instances).o

5. Data returned by the ORM is passed to the serializer, which converts the Python objects (model instances) into a client friendly format, in this case JSON.

6. The view packages the serialized data into an HTTP response. The response is sent back to the client for use in the application.



## Connecting the app with the Django project

cd mysite

Current working directory: api/mysite/mysite

open settings.py -> scroll to INSTALLED APPS = []
  - Add our app to the list of installed apps.
  - The app should be called "api" so we just add "api" to the list.
  - Additionally, we will add the Django REST framework to the installed apps list.
    - Add `"rest_framework"` to the list.



## Building the model that our data will interact with

cd api

current working directory: api/mysite/api

open models.py

Django uses ORM: Object Relational Mapping.

ORM maps a Python Object to an Instance of a Database. This allows us to use multiple types of databases, and Django handles all of the low level commands that create, update and retrieve data. The ORM is a higher level wrapper.

```
from django.db import models

# Create your models here.

# Inheriting from Model gives us the functionality of a table from a SQL database.
class BlogPost(models.Model):
  # Define the model's columns/fields, the type of information it will store.
  title = models.CharField(max_length=100)
  content = models.TextField()
  published_date = models.DateTimeField(auto_add_now=True)
  
  # So we can print() and see the title of the object.
  def __str__(self):
    return self.title 
```


## Defining the Serializer

For now, we will treat the Serializer as a black box that converts our data model into JSON. Further study will focus on customizing and extending it. Here, it will take the model that we just defined, and convert it into JSON compatiable data that the API can interact with.

This will use the Meta class, which is common to Django and Django Rest Framework. It is used to define metadata for a parent class.

- "Meta" is not a reserved word for this class, but it is convention and the Django framework is programmed to look for a class named Meta.

- The Meta class is where we specify additional configuration for the parent class

Current working directory: api/mysite/api

vim serializers.py

```

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    # Fields specified here will be serialized and  returned in the API.
    # id is automatically created in the model.
    fields = ["id", "title", "content", "published_date"]
```


## Creating Views

A view is a function or class that takes a web request and returns a response such as an HTML page, JSON, or error.

A view is where the logic for handling requests and returning responses is defined. Views take user requests and decide what data to fetch, how to format it, and what to send back. In Django REST Framework, views work with serializers to format data, and with models to retrieve data. Views are the brain of the API that connects requests to the correct data and ensures it is in the correct format when returned.

We are going to import generics from `rest_framework`, which will give us the "generic view," which is a pre-built class that handles a lot of typical API tasks, such as listing, retrieving, creating, updating, deleting. 

Create a view that utilizes the model and the serializer.

Current working directory: api/mysite/api

Open views.py

```
from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer 

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
  # Get all BlogPost objects that exist using the ORM.
  queryset = BlogPost.objects.all()

  # Specify which serializer we want to use.
  serializer_class = BlogPostSerializer 
```

Once this view is connected to a URL, the generics.ListCreateAPIView generic will allow us to get all existing blog posts and create new posts.o



## Specify a URL or route

Working directory: api/mysite/api

Make a new file named urls.py.


### Two-step routing system:

Within mysite/mysite, there is another file named urls.py. In mysite/mysite/urls.py, is the following boilerplate pattern:

```
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Within this file is the ability to forward URLs to different apps. Django will always look here first, and look for a specific pattern. In this case the pattern is "admin/". Any remainder in the URL after "admin/" will be forwarded to a different app, in this case admin.site.urls.


### Explanation of urlpatterns

urlpatterns is a list of route patterns that Django uses to determine the handling of incoming HTTP requests:

- When a request comes in, Django compares the URL path of the request and matches it against the patterns defined in urlpatterns.
- If it is found, Django uses the associated view to process the request and return the response.
- If not found, Django raises a 404 Not Found error.

In this case, the item in the list is a path() function, but it could also be a `re_path()` or url() function.
- path() defines:
    1. Route: a URL pattern to match
    2. View: the function or class that will handle the request
    3. Name (optional): a name for the route, used for reverse URL lookups.

In the boilerplate code:
    1. Route: 'admin/'
    2. View: admin.site.urls


### Forwarding to the api app

Working directory/file: mysite/mysite/urls.py

We want to take ANY URL, and forward it to the api app.
 
We are going to remove the import line `from django.contrib import admin` up top, and change the boilerplate function to:

```
urlpatterns = [

    # Change the path to an empty path.
    # Use the include() function
    path("", include("api.urls")),
]
```


### Explanation of include() as used in path()

- The empty string "" as the first argument to path(): matches the root URL of the project. Any request to the base URL ("http://mydomain.com/") will match this pattern.

- include("api.urls") tells Django to look for the URL

include("api.urls") tells Django to look for the URL patterns defined in api/urls.py. This means any request to the root URL (in this case, http://yourdomain.com/) will be handled by the URL patterns inside api/urls.py.

Project structure as of now:

api
- mysite
    - api
        - migrations
        - __init__.py
        - admin.py
        - apps.py
        - models.py
        - serializers.py
        - tests.py
        - urls.py
        -views.py
    - mysite
        - __init__.py
        - asgi.py
        - settings.py
        - urls.py
        - wsgi.py
    - manage.py
- requirements.txt
- .venv


## Pointing the request to a view

Working directory/file: api/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/create/", views.BlogPostListCreate.as_view(), name="blogpost-view-create")
]
```

Here, Django defines patterns for the api app. A request to /blogposts/create/ is routed to the BlogListCreate view, which handles the dispaly of a list of blog posts, or creating a new one.



## Database Migration

Any time we make a new model, or changes to a model, we apply a Database Migration.

- This uses the Django ORM to automatically create the correct SQL table, or otherwise execute actions in the database.

- Apply a database migration from the terminal:

Run:
cd mysite (main project directory)
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

- `makemigrations` will make the files that specify what migrations need to be applied. In this case, it will - Create model BlogPost
- `migrate` will create the tables in the SQL database. We should see this in the mysite directory as db.sqlite3.
- `runserver` will start running the API.

After running runserver, it will show a URL: http://127.0.0.1:8000/
- When we go to it in the browser, there is an error. This is because we need to go to http://127.0.0.1:8000/blogposts/
- When we enter the correct URL, the Blog Post List Create page should display in the browser. We should be able to interact with it by adding test title and content. The info we enter should display as a JSON.
- After verifying that the API is functioning, shut down the server.



## More Complex Views

Working directory/file: api/views.py

- Create a route that allows us to delete individual blog posts.

```
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Copy the queryset and serilizer.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # pk stands for "primary key," which is the id of the blogpost
    # This allows us to access an individual post.
    lookup_field = "pk"
```


Working directory/file: api/views.py

- Now we make a url that maps to the view we created.

Add a new path() to the urlpatterns [] list, separated by a comma.

```
urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name = "blogpost-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name = "update")
]
```

Run python3 manage.py runserver to start the server back up.

- Add /blogposts/1 (or /blogposts/1/) to the URL in the browser, and the options: Delete, Options, and Get should be available. We can test the Update by changing "title" to "revised title" and "test content" to "test content update." Pressing Put should update the JSON display of the blogpost.



## Overriding views

Working directory/file: api/views.py

Generic views from django are useful, but suppose we want something more custom? We override them. The following allows us to delete all blog posts.

Inside of the BlogPostListCreate class, define a new function:

```
# Modify imports
from rest_framework import genreics, status
from rest_framework.response import Response

class BlogPostListDelete(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

When we run the server, there should be a red DELETE button available. When we press it, it should delete all of the blog posts we have created, and return "HTTP 204 NO CONTENT."


## Custom Views

Working directory/file: api/views.py

Suppose we don't want to use the generics, and we want to use our own routes. We import APIView from `rest_framework.views` and pass it as an arg to the class so that our class inherits from APIView.

Then we can write different methods based on which method we want to use (i.e. get, post, delete, put, patch), 

```
# Modify imports
from rest_framework.views import APIView

# New class:
class BlogPostList(APIView):
  def get(self, request, format=None):
    # Get title, if no title, title = "".
    title = request.query_params.get("title", "")

    if title:
      # Filter the queryset based on title
      blog_posts = BlogPost.objects.filter(title_icontains=title)
    else:
      # If no title, return all blog posts
      blog_posts = BlogPost.objects.all()

    serializer = BlogPostSerializer(blog_posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

```

If we want to connect this, add:

`views.BlogPostList.as_view()`

to urlpatterns.


## Deployment


### Acorn

Acorn is free and open source software that allows us to create an Acorn file, which specifies the entire app, and describes how it should be deployed. 

We use the Acorn file to build an Acorn Image, which is similar to a Docker image.

We can then publish that image and use it to deploy as many instances of our app as we want.

This allows us to share the app with others by giving them the Acorn Image.


### Steps

1. Create Docker File.

The Docker file specifies How We Run the application, while the Acorn File specifies the services and additional configuration needed when we deploy.

working directory: api (main project directory)

Run:
mv requirements.txt mysite
cd mysite

requirements.txt should now be in api/mysite. We need it there for the next steps.

Working directory: api/mysite

- Create new file named Dockerfile
  - Specifiy the syntax.
  - Specify the image we build from.
  - Expose port 8000, where our server will run.
  - Specify working directory.
  - Install dependencies.
  - Copy requirements.txt
  - Use pip command to install requirements.txt
  - Copy contents off the working directory.
  - Specify the entry point and the command we will use to run the server.

```
# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
EXPOSE 8000
WORKDIR /app
# Install system dependencies
RUN apk update
RUN apk add \
    pkgconfig \
    gcc \
    musl-dev \
    bash \
    mariadb-dev

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install --no-chace-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . /app
# Run server
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
```


2. Create the Acorn file

The Dockerfile literally explains how the application is run.

Now that we have instructions on how to run the app, we need instructions on how to deploy it. We need to:
  - Set up the database
  - Do database migrations
  - etc.

working directory: api/mysite

Create a new file: db-script.sh

This script will be used whenever the app runs, so that we migrate the database. Automatically apply changes to the database, and make sure the correct tables exist when we run a new deployment.

```
#! /bin/bash

sleep 10
python3 manage.py makemigrations
python3 manage.py migrate
```

Run:
cd api

Working directory: api (main project directory)

- Create a new file named Acornfile
  - The Acornfile specifies everything we need to deploy the app.
  - services, jobs, containers, images.
  - We start with our args: djangodbname: "djangodb"
    - We will use this name when we create the database with a service.

  - services: We could use many databases, MongoDB, Postgres, etc.
    - We will be using MariaDB
    - We use an image to create a database.
    - We pass the arg djangodbname, which we defined in args, to the service.

  - The jobs will initialize the database with dbinit.
    - dbinit will build from images.app.containerBuild, which we define at 
    the bottom of the file.
    - The environment is specified by environment variables that we are
    declaring, and come from the service.
    - Specify that the database is what is consumed.
    - Specify the entry point "/bin/bash"
    - Specify the command that makes the database script executable, then
    executes the database script, applying the migrations to the new 
    database.

  - The job sets everything up.

  - The container runs the app.
    - build the image specified at the bottom of the file.
    - Determine which port we publish on.
    - depend on the job (dbinit).
    - consume the database.

    - Check if in dev mode.
    
    - Specify environment variables.

  - images: specify the container

```
args: {
	djangodbname: "djangodb"
}

services: db: {
	image: "ghcr.io/acorn-io/mariadb:v10.11.5-1"
	serviceArgs: {
		dbName: args.djangodbname
	}
}

jobs: {
	dbinit: {
		build: images.app.containerBuild
		env: {
			MARIADB_USER:          "@{service.db.secrets.admin.username}"
			MARIADB_ROOT_PASSWORD: "@{service.db.secrets.admin.password}"
			MARIADB_HOST:          "@{service.db.address}"
			MARIADB_PORT:          "@{service.db.port.3306}"
			MARIADB_DATABASE:      "@{service.db.data.dbName}"
		}
		consumes: ["db"]
		entrypoint: "/bin/bash"
		command:    "-c 'chmod +x ./db-script.sh && ./db-script.sh'"
	}
}

containers: web: {
	build: images.app.containerBuild
	ports: publish: "8000:8000/http"
	dependsOn: ["dbinit"]
	consumes: ["db"]

	if args.dev {dirs: "/app": "./mysite"}

	env: {
		MARIADB_USER:          "@{service.db.secrets.admin.username}"
		MARIADB_ROOT_PASSWORD: "@{service.db.secrets.admin.password}"
		MARIADB_HOST:          "@{service.db.address}"
		MARIADB_PORT:          "@{service.db.port.3306}"
		MARIADB_DATABASE:      "@{service.db.data.dbName}"
	}
}

images: app: containerBuild: {
	context:    "./mysite"
	dockerfile: "./mysite/Dockerfile"
}
```

3. Adjustments

- Add mysqlclient package to requirements.

Working directory/file: api/mysite/requirements.txt

```
django
djangorestframework
environs
mysqlclient
```

- Adjust settings so app works in a deployed environment, not just on a local machine.

Working directory/file: api/mysite/mysite/settings.py

```
# Change ALLOWED_HOSTS to *, for "any host," i.e. the Acorn Host.
ALLOWED_HOSTS = ["*"]

# Create trusted origins variable under ALLOWED_HOSTS.
# Allow all Acorn origins, avoid CSRF issues.
CSRF_TRUSTED_ORIGINS = ["http://*.on-acorn.io", "https://*.on-acorn.io"]
```

- import os into settings so we can access environment variables.

- Change database configuration so the app uses the database that is created by the Acorn File for our deployment.

Working directory/file: api/mysite/mysite/settings.py

```
# Import os.
from pathlib import Path
import os
```

```
# Change database config.
DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": os.getenv("MARIADB_DATABASE"),
    "USER": os.getenv("MARIADB_USER"),
    "PASSWORD": os.getenv("MARIADB_ROOT_PASSWORD"),
    "HOST": os.getenv("MARIADB_HOST"),
    "PORT": os.getenv("MARIADB_PORT", 3306)
  }
}
```

The Acorn file will spin up a database, and we need to use the environment variables that allow us to connect to that database.


### Run the Acorn File/Build the Acorn Image

- Install the Acorn CLI
  - mac)S brew install acorn-io/cli/acorn
  - Linux: curl https://get.acorn.io | sh

Working directory: api/mysite

Run:
curl https://get.acorn.io | sh

The Acorn CLI should now be installed.

Run:
acorn login

34:24

















