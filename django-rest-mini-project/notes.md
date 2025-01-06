#Django REST API mini project



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

```\
from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create")
]
```














